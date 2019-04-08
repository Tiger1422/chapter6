# -*- coding: utf-8 -*-

import smbus
import time
import datetime  #課題2用
import json  #課題2

log={}

i2c = smbus.SMBus(1)
address = 0x48
json_file = open('result.json', 'w')  #課題2用

for i in range(10):
    block = i2c.read_i2c_block_data(address, 0x00, 12)
    temp = (block[0] << 8 | block[1]) >> 3
    if(temp >= 4096):
        temp -= 8192
    print(datetime.datetime.now())
    log["id"+str(i)]={}
    log["id"+str(i)]["time"]=str(datetime.datetime.now())
    print("Temperature:%6.2f" % (temp / 16.0))
    log["id"+str(i)]["temp"]=str(temp)
time.sleep(1)



json.dump(log, json_file)

json_file.close()
