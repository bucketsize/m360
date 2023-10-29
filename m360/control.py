#!/usr/bin/env python3

import os
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
    process,
    pulseaudio
)
from m360.writers import lemonbar, swaybar, logger, udp
import asyncio

async def entry_point():
    MTAB = {}
    await asyncio.gather(
        cpu.co(MTAB),
        cpu_temp.co(MTAB),
        cpu_freq.co(MTAB),
        mem.co(MTAB),
        battery.co(MTAB),
        disk.co(MTAB),
        net.co(MTAB),
        nvgpu.co(MTAB),
        amdgpu.co(MTAB),
        process.co(MTAB),
        pulseaudio.co(MTAB),

        # writers
        lemonbar.co(MTAB),
        swaybar.co(MTAB),
        logger.co(MTAB),
        udp.co(MTAB),
    )

def main(epoc=1):
    asyncio.run(entry_point())
    print("daemon exited ... ")
