import logging

import redis
import yarqueue

from flask import Flask, request


app = Flask(__name__)

app.logger.setLevel(logging.INFO)  # pylint: disable=no-member

queue = yarqueue.Queue(
    name="example",
    redis=redis.Redis()
)


@app.route('/', methods=["GET"])
def home():
    return "Hello\n"


@app.route('/submit', methods=["POST"])
def submit():
    data = request.data.decode("utf-8")
    app.logger.info(data)  # pylint: disable=no-member
    queue.put(data)
    return "Success\n"
