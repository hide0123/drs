#!/bin/bash

rm -f drs.log
$1 python3 -u main.py > drs.log 2>&1 &
