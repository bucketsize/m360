from re import search

def usage():
    try:
        with open('/sys/class/drm/card0/device/mem_info_vram_used', 'r') as f:
            vram_used = int(f.read())
        with open('/sys/class/drm/card0/device/mem_info_vram_total', 'r') as f:
            vram = int(f.read())
    except: 
        vram_used = 0 
        vram = 0 
    tgpu = 0
    clkm = 0
    clks = 0
    try:
        with open('/sys/kernel/debug/dri/0/amdgpu_pm_info', 'r') as f:
            result = f.read()
    except:
        result = None 
    if result is not None:
        tgpu = int(search(r'GPU Temperature: (\d+) C', result).group(1))
        clkm = int(search(r'\s+(\d+) MHz\s+\ZMCLK', result).group(1))
        clks = int(search(r'\s+(\d+) MHz\s+\ZSCLK', result).group(1))
    return vram, vram_used, tgpu, clkm, clks

def co_usage(MTAB={}):
    while True:
        vram, vram_used, tgpu, gmf, gsf = usage()
        if vram:
            MTAB['gpu_id'] = "amd"
            MTAB['amd:gpu_mem'] = vram / 1000000
            MTAB['amd:gpu_mem_used'] = vram_used / 1000000
            MTAB['amd:gpu_mem_used_pc'] = vram_used * 100 / vram
            MTAB['amd:gpu_temp'] = tgpu
            MTAB['amd:gpu_temp'] = tgpu
            MTAB['amd:gpu_mclk'] = gmf
            MTAB['amd:gpu_sclk'] = gsf
        yield
