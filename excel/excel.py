# -*- coding: utf-8 -*-
import os
import os.path
import datetime
import xlwt
import xlrd
from xlutils.copy import copy

scriptPath = os.path.realpath(__file__)
dirName = os.path.dirname(scriptPath)
currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
fileDate = datetime.datetime.now().strftime('%Y%m%d')

TEMPLATE = dirName+"/template.xls"
REPORT = dirName+"/"+fileDate+".xls"



tempWB = xlrd.open_workbook(TEMPLATE, formatting_info=True)
newWB = copy(tempWB)
newWS = newWB.get_sheet(0)

for i in xrange(1, 8):
    newWS.write(i, 2, u'正常')
newWS.write(12, 1, currentTime)
newWB.save(REPORT)

