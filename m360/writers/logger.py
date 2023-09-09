import os
import io
from time import strftime
from m360.config.sym import ascii as sym
from m360.config.formats import formatvalue 

def co_usage(mtab: {}):
    user = os.getenv("USER")
    sk = list(mtab.keys())
    sk.sort()
    with io.open("/var/tmp/m360.csv.out." + user, "w") as hout:
        while True:
            hout.write("{")
            for k in sk:
                hout.write(f"{k}={mtab[k]},")
            hout.write("}\n")
            hout.flush()
            yield
