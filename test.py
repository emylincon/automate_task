import schedule
import time


def hello():
    print("hello")


def hi():
    print("hi")


def mixed():
    g = [hello, hi]
    for i in g:
        i()
        print('__--__')


schedule.every().thursday.at("19:02").do(mixed)

while True:
    print('Listening...')
    schedule.run_pending()
    time.sleep(50)
