from flask import Flask, request
import celery_tasks.tasks as tasks
import json

app = Flask(__name__)


@app.get("/hello")
def hello():
    return {"abc": "abc"}


@app.get("/add")
def add():
    task = tasks.add.delay(1, 2)
    return {"result": task.get()}


@app.get("/mul")
def mul():
    task = tasks.mul.delay(2, 3)
    return {"result": task.get()}


@app.get("/xsum")
def xsum():
    task = tasks.xsum.delay([2, 3, 4, 5])
    return {"result": task.get()}
