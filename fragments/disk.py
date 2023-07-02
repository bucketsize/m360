import os
import re
import subprocess

discstat_files = []
for root, _, files in os.walk("/sys/devices"):
    for file in files:
        if file == "stat":
            ds = root.split("/")
            if ds[-1].startswith(ds[-2]):
                continue
            print(f"disk stat |{root}|{file}|")
            discstat_files.append(os.path.join(root, file))

def usage():
    du = []
    for f in discstat_files:
        try:
            with open(f, "r") as handle:
                result = handle.readline()
                label = re.search(r"/.+/(\w+)/stat", f).group(1)
                v = [int(d) for d in re.findall(r"\d+", result)]
                du.append((label, v[0], v[4])) # -> {sda, rb, wb}
        except:
            pass
    return du

def co_usage(MTAB={}):
    while True:
        du = usage()
        for dui in du:
            l, r, w = dui
            MTAB[l+':discio_r'] = r // 1000
            MTAB[l+':discio_w'] = w // 1000
            MTAB[l+':discio'] = (r+w) // 1000
        yield

