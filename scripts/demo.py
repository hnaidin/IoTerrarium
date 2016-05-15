from apscheduler.schedulers.blocking import BlockingScheduler
import logging
import time
#import TemperatureGetter
import TurtleFeeder
from pymongo import MongoClient

logging.basicConfig()

sched = BlockingScheduler()

#@sched.scheduled_job('interval', seconds=30)
#def timed_job():
#    now = time.strftime("%Y-%m-%d %H:%M:%S")
#    print('Get the temperature every 30 minutes. Time = %s '%now)
    # Get temperature from sensor
#    t = TemperatureGetter()
#    temp = t.getTemp()
    # Add data to db
#    client = MongoClient()
#    db = client.passport_local_mongoose_express4
#    result = db.temperatures.insert_one(
#        {
#    	    "temperature": temp,
#	    "time": now
#	})
@sched.scheduled_job('interval', seconds=20)
def timed_job():
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    print('Feed the turtles everyday at 08 am. Time = %s '%now)
    # Feed the monsters
    t = TurtleFeeder()
    t.feed()


@sched.scheduled_job('cron', day_of_week='mon-sat', hour=8)
def scheduled_job():
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    print('Feed the turtles everyday at 08 am. Time = %s '%now)
    # Feed the monsters
    t = TurtleFeeder()
    t.feed()
    # Add data to db
#    client = MongoClient()
#    db = client.passport_local_mongoose_express4
#    result = db.feeds.insert_one(
#        {
#            "time": now
#        })


sched.start()

