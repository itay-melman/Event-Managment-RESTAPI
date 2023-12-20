from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def scheduled_job():
    print(f"Scheduler job ran at {datetime.now()}")

scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_job, trigger='interval', seconds=30)
scheduler.start()
