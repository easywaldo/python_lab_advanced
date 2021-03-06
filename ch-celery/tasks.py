from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//', 
            #  backend = 'db+sqlite:///db.sqlite')
            backend='redis://localhost')

@app.task
def add(x, y):
    return x + y