from datetime import datetime
from events.models import Event

from apscheduler.schedulers.background import BackgroundScheduler
from emailscheduler import email_api

def start():
    scheduler = BackgroundScheduler()
    events = Event.objects.all()
    for event in events:
        subject = f"UpgradTodo EVENT REMINDER for {event.title} in 5 minutes"
        message = f"{event.title} \n ------------- \n At {event.time} \n {event.description}"
        email = [f"{event.email}"]
        scheduler.add_job(email_api.send_notification(subject, message, email), 'date', run_date=event.time.replace(tzinfo=None), timezone=event.time.tzinfo)
    scheduler.start()
