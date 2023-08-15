#!/usr/bin/env python

import os
import asyncio
from m360.config.formats import formatvalue 
from m360.fragments import (
    cpu,
    cpu_temp, 
    cpu_freq,
    mem, 
    battery, 
    disk, 
    net, 
    nvgpu,
    amdgpu,
    process
)
from m360.writers import lemonbar

EPOC = 1
MTAB = {}

gs = [
    cpu.co_usage(MTAB),
    cpu_temp.co_usage(MTAB),
    cpu_freq.co_usage(MTAB),
    mem.co_usage(MTAB),
    battery.co_usage(MTAB),
    disk.co_usage(MTAB),
    net.co_usage(MTAB),
    nvgpu.co_usage(MTAB),
    amdgpu.co_usage(MTAB),
    process.co_usage(MTAB),

    # writers
    lemonbar.co_usage(MTAB),
]

async def runloop():
    while True:
        print("\n==")
        for g in gs:
            next(g)
        for k, v in MTAB.items():
            print(k, formatvalue(k, v))
        await asyncio.sleep(EPOC)

def main():
    asyncio.run(runloop())
    print("daemon exited ... ")
