from __future__ import unicode_literals
from celery import shared_task
from grab import Grab
import logging

logger = logging.getLogger('grab')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

grab = Grab()


@shared_task()
def register_users(input_data):
    urlLogin = 'http://news.ycombinator.com/login'
    grab.setup(timeout=20, connect_timeout=20)
    grab.go(urlLogin, log_file='login.html')
    grab.doc.set_input('acct', 'denisoed')
    grab.doc.set_input('pw', 'gorod312')
    grab.doc.submit()
    if grab.response.code == 200:
        send_data(input_data, urlLogin)
    else:
        print('Error!')


def send_data(input_data, urlLogin):
    urlSubmit = 'http://news.ycombinator.com/submit'
    grab.go(urlSubmit, log_file='submit.html')
    grab.doc.set_input('url', input_data['url'])
    grab.doc.set_input('title', input_data['title'])
    # grab.doc.set_input('description', input_data['description'])
    grab.doc.submit()


def handler_errors(error):
    print(error)






