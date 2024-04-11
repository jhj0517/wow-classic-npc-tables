from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from tqdm import tqdm

import requests
from urllib.parse import urlparse, unquote

BASE_URL = "https://www.wowhead.com/classic/"
OTHER_LANGS = ["de", "cn", "es", "ko", "pt", "ru", "fr"]


class Scraper:
    def __init__(self):
        self.driver = None

    def start(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def scrape_npc_name_with_selenium(self, url: str):
        self.driver.get(url)
        # wait until content is loaded
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "heading-size-1"))
        )

        text = element.text.split('\n')[0]
        return text

    @staticmethod
    def scrape_npc_name_with_request(url: str):
        response = requests.get(url, allow_redirects=True)

        parsed_url = urlparse(response.url)
        path = unquote(parsed_url.path)

        parts = path.split('/')
        npc_name = parts[-1]

        npc_name.replace('-', ' ')
        return npc_name.replace('-', ' ')

    def quit(self):
        self.driver.quit()

    @staticmethod
    def table_to_dict():
        english_table = "./../NPCs/id_to_npc_classic_en.lua"
        npc_dict = {}

        with open(english_table, 'r') as file:
            content = file.read()

        content = content.split('=', 1)[1].strip()
        content = content.strip("{}")

        items = content.split(",")
        for item in items:
            item = item.strip()
            key, value = item.split("=")
            key = key.strip("[] ")
            value = value.strip('" ')
            npc_dict[int(key)] = value
        return npc_dict


if __name__ == "__main__":
    scraper = Scraper()
    scraper.start()

    en_table = scraper.table_to_dict()

    # scrape per language
    for lang in OTHER_LANGS:
        locale_url = BASE_URL + lang + "/"

        localized_dict = {}
        for id, name in tqdm(en_table.items(), desc="Scraping..."):
            npc_url = locale_url + f"npc={id}"
            localized_name = scraper.scrape_npc_name_with_request(npc_url)
            localized_dict[id] = localized_name
            print(f"{id}: {name} => {localized_name}")

        with open(f"./id_to_npc_{lang}.json", 'w') as json_file:
            json.dump(localized_dict, json_file)

    scraper.quit()
