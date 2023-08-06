import unicodedata

up = chr(8593)
dw = chr(8595)
no = chr(1509)
atom = chr(1431)
th = chr(1002)

glyps = {
    'cpu': atom + 'c',
    'gpu': atom + 'g',
    'mem': chr(1234),
    'eth': chr(1329),
    'wifi': chr(128246),
    'net': chr(128423),
    'net_disabled': chr(128423) + no,
    'disc': chr(1213),
    'clock': chr(962),
    'bat': chr(128267),
    'bat_charging': chr(128267) + up,
    'bat_discharging': chr(128267) + dw,
    'AC': chr(128268),
    'snd': chr(128266),
    'snd_mute': chr(128263),
    'audio': chr(128266),
    'audio_mute': chr(128263),
    'cpu_temp': th,
}
ascii = {
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
    'bat': 'Bat ',
    'bat_charging': 'B(+) ',
    'bat_discharging': 'B(-) ',
    'AC': 'P(+-)',
    'snd': 'Snd',
    'snd_mute': 'Snd?',
    'audio': 'Snd',
    'audio_mute': 'Snd?',
    'cpu_temp': 'Th ',
}
