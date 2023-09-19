from asyncio import sleep as asleep
from asyncio.subprocess import create_subprocess_exec, PIPE

def usage(l):
    if ("gpu" in l) or ("Idx" in l):
        return 0,0,0,0,0,0
    _, pwr, tgpu, _, clkm, clks = l.split()
    vram_used = 0
    vram = 1 
    return vram, vram_used, int(tgpu), int(clkm), int(clks), pwr

async def co(MTAB={}):
    try: 
        h = await create_subprocess_exec("nvidia-smi", "dmon", "-d", "2", "-s", "pc", stdout=PIPE)
    except Exception as e:
        print('#nvgpu, error', e)
        while True:
            await asleep(1)
    while True:
        l = (await h.stdout.readline()).decode("utf-8")
        if not l:
            await asleep(1)
            continue
        vram, vram_used, tgpu, gmf, gsf, pwr = usage(l)
        # print('#nvgpu:', vram, tgpu, pwr)
        if vram:
            MTAB['gpu_id'] = "nv"
            MTAB['nv:gpu_mem'] = vram / 1000000
            MTAB['nv:gpu_mem_used'] = vram_used / 1000000
            MTAB['nv:gpu_mem_used_pc'] = vram_used * 100 / vram
            MTAB['nv:gpu_temp'] = tgpu
            MTAB['nv:gpu_mclk'] = gmf
            MTAB['nv:gpu_sclk'] = gsf
            MTAB['nv:gpu_pwr'] = pwr
        await asleep(1)
