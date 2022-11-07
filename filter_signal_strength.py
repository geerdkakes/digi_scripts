#!/usr/bin/env python3

import re
import sys
import os
import time;

rsrp_str=""
rssi_str=""

for line in sys.stdin:
    rssi = re.findall(r'RSSI\s*:\s*[a-zA-Z]*\s*\(([0-9.\-dBm\s]*)\)', line)
    rsrp = re.findall(r'Signal\sStrength\s*:\s*[a-zA-Z]*\s\(([0-9.\-dBm\s]*)\)', line)
    if len(rssi) > 0:
        rssi_str = rssi[0]
    if len(rsrp) > 0:
        rsrp_str = rsrp[0]
ts = time.time()
print(str(ts) + "," +  rsrp_str + "," + rssi_str)
