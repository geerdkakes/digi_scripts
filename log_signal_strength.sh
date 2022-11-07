#!/usr/bin/env bash
echo "timestamp,rsrp,rssi"

PASSWORD="thisissecret"

while true; do
sshpass -p ${PASSWORD} ssh admin@192.168.1.1 "cli -c \"show modem name wwan1\"" | ./digi_modem.py
sleep 0.2
done
