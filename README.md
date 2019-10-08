# flask-redis-example

Simple redis queue example using flask and yarqueue. Post data to flask to insert the data into the queue and consume the data a seperate process. 

# Install

Clone the repo.

Setup a [redis](https://redis.io/) server or run **redis_run.bash** to install a local one.

```console
$ ./redis_run.bash
```

It is recommend to run this project in a virtualenv.

```console
$ python3 -m virtualenv ENV
$ source ENV/bin/activate
```

Install the dependencies.

```console
$ pip install -r requirements.txt 
```

# Running

Start flask.

```console
$ export FLASK_APP=example.app:app
$ flask run
```
Start the redis consumer.

```console
$ python -m example consume
```

Test using a curl command.

```console
$ curl -X POST -d @test.txt http://localhost:5000/submit --header "Content-Type: text/plain"
```

Check the conumer for the output.

```console
$ python -m example consume
INFO:example.consumer:waiting...
INFO:example.consumer:Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```
