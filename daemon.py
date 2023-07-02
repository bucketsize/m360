import os
import asyncio
import fragments.cpu as cpu
import fragments.cpu_temp as cpu_temp 
import fragments.cpu_freq as cpu_freq 
import fragments.mem as mem
import fragments.battery as bat
import fragments.disk as dsk 
import fragments.net as net 
import fragments.nvgpu as nvgpu  
import config.formats as f 

EPOC = 1
MTAB = {}

gs = [
    cpu.co_usage(MTAB),
    cpu_temp.co_usage(MTAB),
    cpu_freq.co_usage(MTAB),
    mem.co_usage(MTAB),
    bat.co_usage(MTAB),
    dsk.co_usage(MTAB),
    net.co_usage(MTAB),
    nvgpu.co_usage(MTAB),
]

async def main():
    while True:
        for g in gs:
            next(g)
        for k, v in MTAB.items():
            print(k, f.formatvalue(k, v))
        await asyncio.sleep(EPOC)

asyncio.run(main())
print("daemon exited ... ")
