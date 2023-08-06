#!/usr/bin/env python

import os
import asyncio
from m360.config.formats import formatvalue 
from m360.fragments import cpu
from m360.fragments import cpu_temp 
from m360.fragments import cpu_freq 
from m360.fragments import mem 
from m360.fragments import battery 
from m360.fragments import disk 
from m360.fragments import net 
from m360.fragments import nvgpu 

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

    # writers
    lemonbar.co_usage(MTAB),
]

async def runloop():
    while True:
        for g in gs:
            next(g)
        for k, v in MTAB.items():
            print(k, formatvalue(k, v))
        await asyncio.sleep(EPOC)

def main():
    asyncio.run(runloop())
    print("daemon exited ... ")
