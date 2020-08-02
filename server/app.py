from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import pytz

# configuration
DEBUG = True


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/local-time-in-timezone', methods=['GET'])
def get_local_time():    
    utcmoment_naive = datetime.utcnow()
    utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
    local_format = '%H:%M:%S'

    selected = request.args.get('selectedTimezone')
    local_datetime = utcmoment.astimezone(pytz.timezone(selected))

    return jsonify({
        'timezone': local_datetime.strftime(local_format)
    })


if __name__ == '__main__':
    app.run()