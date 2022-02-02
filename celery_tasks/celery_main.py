import os
from celery import Celery


app = Celery('tasks',
             broker=os.environ['BROKER_URL'],
             include=['celery_tasks.tasks'],
             backend=os.environ['BROKER_URL'],
             )

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
