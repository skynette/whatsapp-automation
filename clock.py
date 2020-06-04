from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from send_message import main



sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(main, 'interval', seconds=2)

sched.start()
