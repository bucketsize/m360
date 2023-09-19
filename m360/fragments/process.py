from subprocess import check_output
from re import compile
from asyncio import sleep as asleep

reps = compile("(\w+)\s+(\w+)\s+(\d+.\d+)\s+(\d+.\d+)\s+([\w\s\-]+)")
def usage():
    t=[]
    result = check_output(["ps", "-Ao", "user,pid,pcpu,pmem,comm", "--sort=-pcpu"]).decode('utf-8').split('\n')[:6]
    # print(result[1:])
    for line in result[1:5]:
        m = reps.match(line)
        if m == None or m.groups() == None:
            continue 
        user,pid,pcpu,pmem,comm=m.groups()
        r={}
        r['user']=user
        r['comm']=comm
        r['pid'] =pid
        r['pcpu']=pcpu
        r['pmem']=pmem
        t.append(r)
    return t

async def co(MTAB={}):
    while True:
        m=usage()
        for i,p in enumerate(m):
            MTAB[f'{i}:pid'] = p['pid']
            MTAB[f'{i}:pcpu'] = p['pcpu']
            MTAB[f'{i}:pmem'] = p['pmem']
            MTAB[f'{i}:name'] = p['comm']
        await asleep(1)
