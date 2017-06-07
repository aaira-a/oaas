import time

from flask import jsonify, Flask, request

app = Flask(__name__)


@app.route('/okay', methods=['POST'])
def okay():
    count = 1
    sleep = 0

    try:
        inputs = request.get_json()
        if 'count' in inputs:
            count = inputs['count']

        if 'sleep' in inputs:
            sleep = inputs['sleep']

    except:
        pass

    time.sleep(sleep)

    return jsonify({'message': ('okay ' * count).strip()})


if __name__ == '__main__':
    app.run()
