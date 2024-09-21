import aiohttp
import asyncio

class DeeplAPI:
    def __init__(self, api_key) -> None:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        self.key = api_key
        self.URL = 'https://api-free.deepl.com/v2/translate'

    async def translate(self, text, traget_language):
        params = {"text": text, "target_lang": traget_language}
        headers = {"Authorization": f" DeepL-Auth-Key {self.key}"}

        async with aiohttp.ClientSession() as session:
            async with session.post(self.URL, headers=headers, data=params) as resp:
                response = await resp.json()
                return response['translations'][0]['text']

