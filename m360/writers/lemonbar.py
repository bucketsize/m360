import os
import io
from time import strftime
from m360.config.sym import ascii as sym
from m360.config.formats import formatvalue 

def fmtab(mtab: {}, key: str) -> str:
    if key in mtab:
        return formatvalue(key, mtab[key])
    return "?"

def fsym(s, k):
    if k in s:
        return s[k]
    return k+"_?"

def statusline(mtab: {}) -> str:
    return "%%{l} %s%s %%{c}...%%{r} %s%s %s%s | %s%s | %s%s | %s%s | %s%s | %s%s\n" % (
        sym["clock"],
        strftime("%a %b %d, %Y | %H:%M:%S"),
        sym["cpu"],
        fmtab(mtab, "cpu"),
        sym["cpu_temp"],
        fmtab(mtab, "cpu_temp"),
        fsym(sym, "gpu_"+fmtab(mtab, "gpu_id")),
        fmtab(mtab, "gpu"),
        sym["mem"],
        fmtab(mtab, "mem"),
        sym["audio"],
        fmtab(mtab, "audio"),
        sym["net"],
        fmtab(mtab, "net_gateway"),
        fsym(sym, "bat_"+fmtab(mtab, "battery_status").lower()),
        fmtab(mtab, "battery"),
    )

def co_usage(mtab: {}):
    user = os.getenv("USER")
    with io.open("/tmp/m360.lemonbar.out." + user, "w") as hout:
        while True:
            hout.write(statusline(mtab))
            yield
