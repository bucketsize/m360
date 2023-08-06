import subprocess


Alerts_Config = {
	cpu : Alert(compare = ">",
		trigger = 59,
		count = 0,
		highmark = 10
    ),
    mem : Alert(
		compare = ">",
		trigger = 79,
		count = 0,
		highmark = 10
    ),
    cpu_temp : Alert(
		compare = ">",
		trigger = 79,
		count = 0,
		highmark = 5
    ),
    battery : Alert(
		compare = "<",
		trigger = 10,
		count = 0,
		highmark = 5
    )
}

Alerts_Compare = {
	">"  : "is running high!",
	">=" : "is running somewhat high!",
	"<"  : "is running low!",
	"<=" : "is running somewhat low",
	"==" : "is",
	"!=" : "is not as expected!",
}

class Alert:
    def __init__(self, compare='', trigger=0, count=0, highmark=0):
        self.compare = compare
        self.trigger = trigger
        self.count = count
        self.highmark = highmark

    def __compare(self, p, a):
        c, b = self.compare, self.trigger
        if (c == ">"  and a >  b) or (c == ">=" and a >= b) or (c == "<"  and a <  b) or (c == "<=" and a <= b) or (c == "==" and a == b) or (c == "!=" and a != b):
            return true
        else:
            return false
	
    def __alert(self, p, pc):
        print("Al.alert: ", p, pc, Alerts_Compare[self.compare])
        subprocess.Popen(['notify-send', '-u', 'critical', '-c', 'system'
            , p
            , Alerts_Compare[self.compare]
            , pc
        ], stdout=subprocess.PIPE)

    def check(self, p, pc):
        print("Al.check:", p, pc)
        if self.__compare(p, pc):
            print("Al.check, trigger:", p, pc)
            if self.count > self.highmark:
                self.__alert(p, pc)
                self.highmark = self.highmark * 2 # exponential backoff
            
            self.count = self.count + 1
            return true
        else:
            self.count = 0
            return false
