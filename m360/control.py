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
    pulseaudio,
    div
)
from m360.writers import lemonbar, swaybar, logger, udp
import asyncio

async def entry_point():
    cors = [div, cpu, cpu_temp, cpu_freq,mem,disk,battery,net,amdgpu,nvgpu,process,pulseaudio,lemonbar,logger,udp]
    MTAB = {}
    cots = map(lambda x: asyncio.create_task(x.co(MTAB)), cors)
    for ts in list(cots):
        try:
            await ts 
        except Exception as e:
            print("EE", ts, e)

def main(epoc=1):
    asyncio.run(entry_point())
    print("daemon exited ... ")
