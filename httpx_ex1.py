import httpx
import asyncio


async def fetch_url(client, url):
    response = await client.get(url)
    return response.status_code



async def main():

    limits = httpx.Limits(max_connections=20)
    
    async with httpx.AsyncClient(limits=limits) as client:
        urls = ['http://example.com/' for _ in range(100)] 
        tasks = [fetch_url(client, url) for url in urls]
        results = await asyncio.gather(*tasks)
    print(results)



if __name__ == "__main__":
    asyncio.run(main())
