import subprocess
import re

reps = re.compile("(\w+)\s+(\w+)\s+(\d+.\d+)\s+(\d+.\d+)\s+([\w\s\-]+)")
def usage():
    t=[]
    result = subprocess.check_output(["ps", "-Ao", "user,pid,pcpu,pmem,comm", "--sort=-pcpu"]).decode('utf-8').split('\n')[:6]
    print(result[1:])
    for line in result[1:]:
        user,pid,pcpu,pmem,comm=reps.match(line).groups()
        r={}
        r['user']=user
        r['comm']=comm
        r['pid'] =pid
        r['pcpu']=pcpu
        r['pmem']=pmem
        t.append(r)
    return t

def co_usage(MTAB={}):
    while True:
        m=ps_top()
        for i,p in enumerate(m):
            MTAB[f'p{i+1}_pid'] = p['pid']
            MTAB[f'p{i+1}_pcpu'] = p['pcpu']
            MTAB[f'p{i+1}_pmem'] = p['pmem']
            MTAB[f'p{i+1}_name'] = p['comm']
        yield
