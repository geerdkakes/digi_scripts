#!/usr/bin/env bash
echo "timestamp,rsrp,rssi"

PASSWORD="thisissecret"

while true; do
sshpass -p ${PASSWORD} ssh admin@192.168.1.1 "cli -c \"show modem name wwan1\"" | ./filter_signal_strength.py
sleep 0.2
done
