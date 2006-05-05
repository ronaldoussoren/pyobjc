#!/usr/bin/python
"""
Shows of how to fetch events using notify_check.
"""
import notify
import time

token = notify.notify_register_check("org.python.randomevent")
while 1:
    print notify.notify_check(token)
    time.sleep(5)
