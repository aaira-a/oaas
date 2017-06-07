import time

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/okay', methods=['POST'])
def okay():
    count = 1
    sleep = 0

    try:
        inputs = request.get_json()
        if 'count' in inputs:
            count = inputs['count']

        if 'sleep':
            sleep = inputs['sleep']

    except:
        pass

    time.sleep(sleep)

    return ('okay ' * count)


if __name__ == '__main__':
    app.run()
