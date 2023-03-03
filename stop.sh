#!/bin/bash

ps aux | grep -e main.py -e chromedriver -e chromium-browse | grep -v grep | awk '{ print "kill -9", $2 }' | sh