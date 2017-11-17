import asyncio
import aioflake


def test_flake():
    flake = aioflake.Flake()
    loop = asyncio.get_event_loop()

    async def go():
        last_id = 0
        for i in range(1_000_000):
            ident = await flake.next()
            assert ident > last_id
            last_id = ident
            aioflake.hex(ident)
            aioflake.ctime(ident)
    loop.run_until_complete(go())
