import niquests
import asyncio

async def main() -> None:
    r = await niquests.aget('https://one.one.one.one', stream=True)
    print(r) 
    
    payload = await r.text
    print(payload)
    
    
    r = await niquests.aget('https://one.one.one.one')
    print(r)
    
    payload = r.text
    print(payload)

asyncio.run(main())