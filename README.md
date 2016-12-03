# cristoreferendum
Weekly Cristo Elections

## Depenencies

- python3
- virtualenv for python 3

OR

- python3
- django 1.10

## VirtualEnv install instructions
<pre>
$ virtualenv3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
</pre>

## Generate secret key
<pre>
$ python -c 'from django.utils.crypto import get_random_string; chars = "abcdefghijklmnopqrstuvwxyz0123456789%^&*(-_=+)"; print(get_random_string(50, chars), end="")' > secret_key.txt
</pre>

## Run in Development
If using virtualenv, remember to activate it first.
If is the first run, or the models have been updated, remember to `migrate` first.
<pre>
$ export SECRET_KEY=`cat secret_key.txt`
$ python manage runserver
</pre>

## Run in production
This configuration assumes that you are going to run in HTTPS. If not, please modify the settings.py before running it. If you forget before opening the browser, you could run in some troubles.
<pre>
$ SECRET_KEY=`cat secret_key.txt` \
  PRODUCTION=1 \
  gunicorn cristoreferendum.wsgi --workers 8 -b :8080
</pre>

### Production with docker
Assumptions from before don't change
<pre>
$ docker build -t cristo .
$ docker run --env SECRET_KEY=`cat secret_key.txt` --name cristo-instance cristo
</pre>

