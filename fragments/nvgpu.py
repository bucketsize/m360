import subprocess

def usage(l):
    if ("gpu" in l) or ("Idx" in l):
        return 0,0,0,0,0,0
    _, pwr, tgpu, _, clkm, clks = l.split()
    vram_used = 0
    vram = 1 
    return vram, vram_used, int(tgpu), int(clkm), int(clks), pwr

def co_usage(MTAB={}):
    try: 
        h = subprocess.Popen(["nvidia-smi", "dmon", "-d", "2", "-s", "pc"], stdout=subprocess.PIPE)
    except:
        yield
    while True:
        l = h.stdout.readline().decode("utf-8")
        if not l:
            return
        vram, vram_used, tgpu, gmf, gsf, pwr = usage(l)
        if vram:
            MTAB['gpu_id'] = "nv"
            MTAB['nv:gpu_mem'] = vram / 1000000
            MTAB['nv:gpu_mem_used'] = vram_used / 1000000
            MTAB['nv:gpu_mem_used_pc'] = vram_used * 100 / vram
            MTAB['nv:gpu_temp'] = tgpu
            MTAB['nv:gpu_temp'] = tgpu
            MTAB['nv:gpu_mclk'] = gmf
            MTAB['nv:gpu_sclk'] = gsf
            MTAB['nv:gpu_pwr'] = pwr
        yield
