# -- https://unicode.org/emoji/charts/full-emoji-list.html
# -- https://www.fontspace.com/unicode/analyzer

up = chr(8593)
dw = chr(8595)
no = chr(1509)
atom = chr(1431)
th = chr(1002)
return {
    'glyps': {
        'cpu': atom + 'c',
        'gpu': atom + 'g',
        'mem': chr(1234),
        'eth': chr(1329),
        'wifi': chr(128246),
        'net': chr(128423),
        'net_disabled': chr(128423) + no,
        'disc': chr(1213),
        'clock': chr(962),
        'battery': chr(128267),
        'battery_charging': chr(128267) + up,
        'battery_discharging': chr(128267) + dw,
        'AC': chr(128268),
        'snd': chr(128266),
        'snd_mute': chr(128263),
        'temperature': th,
    },
    'ascii': {
        'cpu': 'Cpu',
        'gpu': 'Gpu',
        'gpu_nv': 'Nv',
        'gpu_amd': 'Amd',
        'mem': 'Mem',
        'eth': 'Enp ',
        'wln': 'Wlp ',
        'net': 'Net ',
        'net_disabled': 'Net?',
        'disc': 'Df',
        'clock': '',
        'battery': 'Bat ',
        'battery_charging': 'B(+) ',
        'battery_discharging': 'B(-) ',
        'AC': 'P(+-)',
        'snd': 'Snd',
        'snd_mute': 'Snd?',
        'temperature': 'Th ',
    },
}
