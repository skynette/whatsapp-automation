from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from send_message import send



sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send, 'interval', seconds=2)

sched.start()
