#!/usr/bin/python

# This program will automatize the gathering of temperature data and feed the
# turtles once a day. It will work with the mongodb, where it will record all
# its activities.

# Step 1: feed once a day
import threading
import time

class feedThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.threadID = 1
        self.name = "feedThread"
    def run(self):
        print "Starting " + self.name
	print "Feeding now ..."
        feed_now()
        print "Logging the feeding in the database ..."
	log_now()
        print "Exiting " + self.name

def feed_now():
	print "Feed_now()"

def log_now():
	now = time.strftime("%Y-%m-%d %H:%M:%S")
	print now

# Create threads
thread1 = feedThread()

# Start threads
thread1.start()

print "Exiting Main Thread"
