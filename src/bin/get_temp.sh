#!/bin/bash
for t in $(ls /sys/bus/w1/devices/ | grep 28-); do echo -n "$(date '+%F %T'),${t},"; cat /sys/bus/w1/devices/${t}/w1_slave  | grep t= | sed 's/^.*t=//g' | for temp in $(cat); do echo "scale=3; ${temp}/1000" | bc ;done; done
