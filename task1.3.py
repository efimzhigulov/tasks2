import asyncio


async def two():
    print("Start two")
    await asyncio.sleep(2)
    print("End two")


async def four():
    print("Start four")
    await asyncio.sleep(4)
    print("End four")

async def six():
    print("Start six")
    await asyncio.sleep(6)
    print("End six")


async def main():
    await asyncio.gather(two(), four(), six())


asyncio.run(main())


