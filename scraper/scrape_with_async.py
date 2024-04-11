import json
import asyncio
import aiohttp
from tqdm.asyncio import tqdm_asyncio
from urllib.parse import urlparse, unquote

BASE_URL = "https://www.wowhead.com/classic/"
# OTHER_LANGS = ["de", "cn", "es", "ko", "pt", "ru", "fr"]
OTHER_LANGS = ["ko"]

class Scraper:
    def __init__(self):
        self.session = None
        self.max_sessions = 100
        self.semaphore = asyncio.Semaphore(self.max_sessions)

    async def start(self):
        self.session = await aiohttp.ClientSession().__aenter__()

    async def scrape_npc_name(self, url):
        async with self.semaphore:
            response = await self.session.get(url, allow_redirects=True)
            parsed_url = urlparse(response.url.name)
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

    async def close(self):
        if self.session is not None:
            await self.session.__aexit__(None, None, None)


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

        with open(f"./id_to_npc_{lang}.json", 'w') as json_file:
            json.dump(localized_dict, json_file)
            print(f"./id_to_npc_{lang}.json file is done!")

    await scraper.close()

if __name__ == "__main__":
    asyncio.run(main())

