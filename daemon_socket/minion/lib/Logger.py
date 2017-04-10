import sys
from time import strftime,gmtime

class Logger:
    def log(self,level,msg):
        timestamp = strftime("[%Y-%m-%d %H:%M:%S]", gmtime())
        level = "[%s]" % level
        sys.stdout.write("{0}{1:<10}: {2}\n".format(timestamp,level,msg))
