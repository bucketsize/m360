
def mtab(k):
    if k not in MTAB:
        return " ?"
    return fmt.formatvalue(k, MTAB[k])

def translate():
    return {
        'bat': (lambda: {'sym': sym['battery_charging'], 'val': mtab('battery')})() if MTAB['battery_status'] == 'Full' or MTAB['battery_status'] == 'Charging' else {'sym': sym['battery_discharging'], 'val': mtab('battery')} if MTAB['battery_status'] == 'Discharging' else {'sym': sym['AC'], 'val': ''},
        'audio': (lambda: {'sym': sym['snd_mute'], 'val': ''})() if MTAB['vol'] is None or mtab('vol') < 1 else {'sym': sym['snd'], 'val': mtab('vol')},
        'net': (lambda: {'sym': sym['net_disabled'], 'val': ''})() if MTAB['net_gateway'] == '?' else {'sym': sym['wln'], 'val': mtab('net_gateway')} if MTAB['net_device'].startswith('wl') else {'sym': sym['eth'], 'val': mtab('net_gateway')} if MTAB['net_device'].startswith('en') else {'sym': sym['net'], 'val': mtab('net_gateway')},
        'mem': {'sym': sym['mem'], 'val': mtab('mem')},
        'cpu': {'sym': sym['cpu'], 'val': mtab('cpu')},
        'cpu_temp': {'sym': sym['temperature'], 'val': mtab('cpu_temp')},
        'gpu': {'sym': sym['gpu_' + MTAB['gpu_id']] if MTAB['gpu_id'] is not None else sym['gpu_Gpu'], 'temp': mtab(MTAB['gpu_id'] + ':gpu_temp'), 'speed': mtab(MTAB['gpu_id'] + ':gpu_sclk')}
    }
   
