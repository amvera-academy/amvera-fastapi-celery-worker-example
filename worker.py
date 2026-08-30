import os
import time

from celery import Celery


REDIS_URL = os.environ["REDIS_URL"]
app = Celery("worker", broker=REDIS_URL, backend=REDIS_URL)


@app.task(name="process_text")
def process_text(text):
    time.sleep(2)
    return {"original": text, "result": text.upper()}

