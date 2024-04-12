import json
import asyncio
import aiohttp
from aiohttp import ClientTimeout
from tqdm.asyncio import tqdm_asyncio
from urllib.parse import urlparse, unquote

BASE_URL = "https://www.wowhead.com/classic/"
OTHER_LANGS = ["de", "cn", "es", "ko", "pt", "ru", "fr"]


class Scraper:
    def __init__(self):
        self.client = None
        self.max_sessions = 100
        self.semaphore = asyncio.Semaphore(self.max_sessions)
        self.timeout_for_session = ClientTimeout(total=10)

    async def start(self):
        connector = aiohttp.TCPConnector(limit=self.max_sessions)
        self.client = await aiohttp.ClientSession(connector=connector).__aenter__()

    async def scrape_npc_name(self, url):
        async with self.semaphore:
            try:
                async with self.client.get(url, timeout=self.timeout_for_session) as response:
                    if response.status == 200:
                        parsed_url = urlparse(response.url.name)
                        path = unquote(parsed_url.path)
                        parts = path.split('/')
                        npc_name = parts[-1].replace('-', ' ')
                        return npc_name
                    else:
                        print(f"Non-200 status code: {response.status} URL: {url}")
                        return ""
            except asyncio.TimeoutError:
                print(f"Timed out : {url}")
                return ""
            except Exception as e:
                print(f"Error occurred: {str(e)} URL: {url}")
                return ""

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

    async def close(self):
        if self.client:
            await self.client.close()
            self.client = None


async def main():
    scraper = Scraper()
    await scraper.start()

    en_table = scraper.table_to_dict()

    # scrape per language
    for lang in OTHER_LANGS:
        locale_url = BASE_URL + lang + "/"
        localized_dict = {}

        tasks = []
        for id, name in en_table.items():
            npc_url = locale_url + f"npc={id}"
            task = asyncio.create_task(scraper.scrape_npc_name(npc_url))
            tasks.append(task)

        results = await tqdm_asyncio.gather(*tasks)

        for (id, name), localized_name in zip(en_table.items(), results):
            localized_dict[id] = localized_name

        with open(f"./id_to_npc_{lang}.json", 'w', encoding="utf-8") as json_file:
            json.dump(localized_dict, json_file, ensure_ascii=False)
            print(f"./id_to_npc_{lang}.json file is done!")

    await scraper.close()


if __name__ == "__main__":
    asyncio.run(main())
