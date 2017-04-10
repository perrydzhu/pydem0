from celery import Celery

app = Celery("task", broker='redis://192.168.86.86:6379/9', backend='redis://192.168.86.86:6379/10')


@app.task
def add(x, y):
    return x + y
