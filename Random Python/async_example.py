import asyncio
import time

class MyClass:
    def __init__(self):
        self.name = "test class"

    @staticmethod
    async def async_method():
        print('SLEEP! async')
        await asyncio.sleep(1)

    @staticmethod
    def non_async_method():
        print('SLEEP! Sync')
        time.sleep(1)


async def main():
    coroutines = [MyClass.async_method() for _ in range(10)]
    await asyncio.gather(*coroutines)
    [MyClass.non_async_method() for _ in range(10)]

if __name__ == "__main__":
    asyncio.run(main())
