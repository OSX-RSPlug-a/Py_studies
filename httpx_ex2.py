import asyncio
import httpx


async def fetch_url(url):
    """An asynchronous function to fetch a single URL."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return f"{url}: Status {response.status_code}"



async def main():

    urls = [
        'https://api.github.com',
#        'https://api.pypi.org',
#        'https://api.example.com'
    ]

    tasks = [fetch_url(url) for url in urls]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)



if __name__ == "__main__":
    asyncio.run(main())

