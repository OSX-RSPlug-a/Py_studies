import aiohttp
import asyncio


async def fetch_url_with_limit(session, url, semaphore):
    async with semaphore:
        async with session.get(url) as response:
            return response.status



async def main():

    semaphore = asyncio.Semaphore(20)

    async with aiohttp.ClientSession() as session:
        urls = ['http://example.com/' for _ in range(100)] # list of many URLs
        tasks = [fetch_url_with_limit(session, url, semaphore) for url in urls]
        results = await asyncio.gather(*tasks)
    print(results)



if __name__ == "__main__":
    asyncio.run(main())
