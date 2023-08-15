import string

Formats = {
    "time": "%s",
    "cpu": "%3.0f",
    "cpu_level": "%.0f",
    "cpu_temp": "%3.0f",
    "cpu_freq": "%4.0f",
    "mem": "%3.0f",
    "mem_level": "%.0f",
    "snd_live": "%s",
    "vol": "%3.0f",
    "vol_level": "%.0f",
    "gpu_id": "%s",
    "gpu_mem": "%4f",
    "gpu_mem_used": "%4f",
    "gpu_mem_used_pc": "%3.0f",
    "gpu_temp": "%d",
    "gpu_sclk": "%4d",
    "gpu_mclk": "%4d",
    "net_gateway": "%s",
    "net_device": "%s",
    "net_proto": "%s",
    "net_tx": "%f",
    "net_rx": "%f",
    "net_ts": "%4.0f",
    "net_rs": "%4.0f",
    "p_pid": "%s",
    "p_pcpu": "%s",
    "p_pmem": "%s",
    "p_name": "%s",
    "cpu_volt": "%s",
    "cpu_fan": "%s",
    "discio": "%d",
    "discio_r": "%d",
    "discio_w": "%d",
    "fs_free": "%s",
    "battery_status": "%s",
    "battery": "%d",
    "weather_temperature": "%.1f",
    "weather_humidity": "%.1f",
    "weather_summary": "%s",
    "ps_sink": "%s",
    "Tdie": "%3.0f",
    "Core_0": "%3.0f",
    "Core_1": "%3.0f",
    "Core_2": "%3.0f",
    "Core_3": "%3.0f",
    "Package_id_0": "%3.0f",
    "thermal_zone0": "%3.0f"
}

def formatvalue(k: str, v) -> str:
    if not v:
        return "%s=?" % k
    f = Formats.get(k)
    if not f:
        fk = k.split(":")[-1]
        f = Formats.get(fk)
    if not f:
        return "__f:%s=%s" % (k, v)
    return f % v
