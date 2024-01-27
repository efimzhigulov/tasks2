import asyncio
import aiohttp
import time

async def call_url(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                st_time = time.time()
                html = await response.text()
                print(f"-----\nStatus of '{url}' request:", response.status,
                      f"\nBody: {html[:15]}...")
                et_time = st_time - time.time()
                print(f"Ping time: {et_time}")
                #await asyncio.sleep(3)
        except:
            print(f"\nWrong '{url}' response status")

async def main():
    st_time = time.time()
    await asyncio.gather(call_url('http://www.python.org',),
                         call_url('https://www.youtube.com/'),
                         call_url('http://www.yandex.ru'),
                         call_url('http://www.google.com'),
                         call_url('htp://www.python.org',),
                         call_url('https://pythonru.com/osnovy/python-asyncio,'))
    et_time = st_time - time.time()
    print(f"-----\nОбщее время работы: {et_time} ")
asyncio.run(main())
