import os
import time
import uuid
import base64
import asyncio
# Tue, 21 Mar 2006 20:50:14.000 GMT
__version__ = '0.1.2'
twepoch = 1142974214000
total_bits = 128
timestamp_bits = 41
mac_bits = 48
pid_bits = 16
seq_bits = 23
max_seq = -1 ^ (-1 << seq_bits)
timestamp_shift = total_bits - timestamp_bits
mac_shift = total_bits - timestamp_bits - mac_bits
pid_shift = mac_shift - pid_bits


class Flake:
    def __init__(self):
        self.mac_val = uuid.getnode() << mac_shift
        self.pid_val = os.getpid() << pid_shift
        self.last_timestamp = 0
        self.seq = 0

    async def next(self):
        timestamp = int(time.time() * 1000) - twepoch
        timestamp_val = timestamp << timestamp_shift
        if timestamp > self.last_timestamp:
            self.seq = 0
            val = timestamp_val | self.mac_val | self.pid_val
            self.last_timestamp = timestamp
            return val
        elif timestamp == self.last_timestamp:
            if self.seq <= max_seq:
                self.seq += 1
                val = timestamp_val | self.mac_val | self.pid_val | self.seq
                return val
            else:
                self.seq = 0
                await asyncio.sleep(0.001)
                return await self.next()
        else:
            await asyncio.sleep((self.last_timestamp-timestamp)/1000)
            return await self.next()

    async def next_urlsafe(self):
        return urlsafe(await self.next())

    async def next_hex(self):
        return hex(await self.next())


def hex(ident: int):
    assert ident > 0, 'must > 0'
    return ident.to_bytes(16, 'big').hex()


def urlsafe(ident: int):
    assert ident > 0, 'must > 0'
    return base64.urlsafe_b64encode(ident.to_bytes(16, 'big'))


def timestamp(ident: int):
    return ((ident >> timestamp_shift) + twepoch) // 1000


def ctime(ident: int):
    return time.ctime(timestamp(ident))
