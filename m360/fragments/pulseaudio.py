from subprocess import check_output
from re import search, findall
from asyncio import sleep as asleep

def usage():
    na, s, v, st = [], [], [], []
    output = check_output("pactl list sinks 2>&1", shell=True).decode()
    for line in output.split('\n'):
        n = search('Name: (.+)', line)
        if n:
            na.append(n.group(1))
        i = search('Sink #(\w+)', line)
        if i:
            s.append(i.group(1))
        j = search('State: (\w+)', line)
        if j:
            st.append(j.group(1))
        k = search('Volume: f.*', line)
        if k:
            vol = 0
            for iv in findall('/\s+(\d+)', k.group(0)):
                vol += int(iv)
            vol /= 2
            v.append(vol)
    return {'names': na, 'sinks': s, 'vols': v, 'states': st}

async def co(MTAB={}):
    while True:
        r = usage()
        n, s, v, st = r['names'], r['sinks'], r['vols'], r['states'] 
        for i, sink in enumerate(s):
            MTAB[sink+':vol'] = v[i]
            MTAB[sink+':vol_level'] = v[i]*0.05
            MTAB[sink+':snd_live'] = st[i]
            if st[i] == "RUNNING":
                MTAB['vol'] = v[i]
                MTAB['vol_level'] = v[i]*0.05
                MTAB['snd_live'] = st[i]
                MTAB['pa_sink'] = sink
        await asleep(1)
