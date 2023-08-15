from os.path import exists as path_exists

hwmons = {}
# intel i5 / amd ryzen 2200 g
for i in range(0, 127):
    hwmfd = f"/sys/class/hwmon/hwmon{i}/name"
    if path_exists(hwmfd):
        print(f"cpu_temp, checking {hwmfd}")
        with open(hwmfd, "r") as f:
            print(f.read())
        for j in range(0, 127):
            tempfd = f"/sys/class/hwmon/hwmon{i}/temp{j}_label"
            if path_exists(tempfd):
                with open(tempfd, "r") as f:
                    templb = f.read()
                hwmons[templb] = f"/sys/class/hwmon/hwmon{i}/temp{j}_input"

# pi 4
if path_exists("/sys/class/thermal/thermal_zone0/temp"):
    hwmons["thermal_zone0"] = "/sys/class/thermal/thermal_zone0/temp"

def usage():
    ts = {}
    for i, v in hwmons.items():
        h = open(v, "r")
        if h:
            result = h.readline()
            ts[i.strip()] = int(result)
            h.close()

    # ryzen 2 2200g
    if "Tdie" in ts:
        return ts['Tdie'] / 1000
    
    # intel
    if "Core 0" in ts:
        return ts['Core 0'] / 1000
    
    # pi 4
    if "thermal_zone0" in ts:
        return ts['thermal_zone0'] / 1000


def co_usage(MTAB={}):
    while True:
        MTAB['cpu_temp'] = usage()
        yield
