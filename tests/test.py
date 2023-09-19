import m360
from m360.fragments import cpu
from m360.fragments import cpu_freq
from m360.fragments import cpu_temp
from m360.fragments import mem
from m360.fragments import disk
from m360.fragments import net
from m360.fragments import battery
from m360.fragments import process
from m360.fragments import pulseaudio

from m360.control import main

# print("cpu", cpu.usage())
# print("cpu_freq", cpu_freq.usage())
# print("cpu_temp", cpu_temp.usage())
# print("mem", mem.usage())
# print("disk", disk.usage())
# print("net", net.usage())
# print("battery", battery.usage())
# print("process", process.usage())
# print("pulseaudio", pulseaudio.usage())

main()
