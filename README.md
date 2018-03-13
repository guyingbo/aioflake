# aioflake

[![Build Status](https://travis-ci.org/guyingbo/aioflake.svg?branch=master)](https://travis-ci.org/guyingbo/aioflake)
[![Python Version](https://img.shields.io/pypi/pyversions/aioflake.svg)](https://pypi.python.org/pypi/aioflake)
[![Version](https://img.shields.io/pypi/v/aioflake.svg)](https://pypi.python.org/pypi/aioflake)
[![Format](https://img.shields.io/pypi/format/aioflake.svg)](https://pypi.python.org/pypi/aioflake)
[![License](https://img.shields.io/pypi/l/aioflake.svg)](https://pypi.python.org/pypi/aioflake)

Unique id generator inspired by twitter's snowflake.

## Usage

```python
import asyncio
import aioflake


async def go():
    flake = aioflake.Flake()
    ident = await flake.next()
    print(ident)
    idstr = aiflake.urlsafe(ident)
    print(idstr)


loop = asyncio.get_event_loop()
loop.run_until_complete(go())
loop.close()
```
