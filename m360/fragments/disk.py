from os import walk
from os.path import join
from re import search, findall
from asyncio import sleep as asleep

discstat_files = []
for root, _, files in walk("/sys/devices"):
    for file in files:
        if file == "stat":
            ds = root.split("/")
            if ds[-1].startswith(ds[-2]):
                continue
            print(f"disk stat |{root}|{file}|")
            discstat_files.append(join(root, file))

def usage():
    du = []
    for f in discstat_files:
        try:
            with open(f, "r") as handle:
                result = handle.readline()
                label = search(r"/.+/(\w+)/stat", f).group(1)
                v = [int(d) for d in findall(r"\d+", result)]
                du.append((label, v[0], v[4])) # -> {sda, rb, wb}
        except:
            pass
    return du

async def co(MTAB={}):
    while True:
        du = usage()
        for dui in du:
            l, r, w = dui
            MTAB[l+':discio_r'] = r // 1000
            MTAB[l+':discio_w'] = w // 1000
            MTAB[l+':discio'] = (r+w) // 1000
        await asleep(1)

