import json
from tqdm import tqdm

import requests
from urllib.parse import urlparse, unquote

BASE_URL = "https://www.wowhead.com/classic/"
OTHER_LANGS = ["de", "cn", "es", "ko", "pt", "ru", "fr"]


class Scraper:
    @staticmethod
    def scrape_npc_name(url: str):
        response = requests.get(url, allow_redirects=True)

        parsed_url = urlparse(response.url)
        path = unquote(parsed_url.path)
        parts = path.split('/')

        npc_name = parts[-1]
        npc_name = npc_name.replace('-', ' ')
        return npc_name

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

    en_table = scraper.table_to_dict()

    # scrape per language
    for lang in OTHER_LANGS:
        locale_url = BASE_URL + lang + "/"

        localized_dict = {}
        for id, name in tqdm(en_table.items(), desc="Scraping..."):
            npc_url = locale_url + f"npc={id}"
            localized_name = scraper.scrape_npc_name(npc_url)
            localized_dict[id] = localized_name

        with open(f"./id_to_npc_{lang}.json", 'w') as json_file:
            json.dump(localized_dict, json_file)
            print(f"./id_to_npc_{lang}.json file is done!")
