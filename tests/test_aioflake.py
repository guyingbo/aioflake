import asyncio
import aioflake


def test_flake():
    flake = aioflake.Flake()
    loop = asyncio.get_event_loop()

    async def go():
        last_id = 0
        for i in range(1000000):
            ident = await flake.next()
            assert ident > last_id
            last_id = ident
            assert len(aioflake.hex(ident)) == 32
            assert len(aioflake.urlsafe(ident)) == 24
            aioflake.ctime(ident)
            assert len(await flake.next_hex()) == 32
            assert len(await flake.next_urlsafe()) == 24
    loop.run_until_complete(go())
