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
@app.route('/ping', methods=['GET'])
def ping_pong():    
    utcmoment_naive = datetime.utcnow()
    utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
    localFormat = "%H:%M:%S"

    selected = request.args.get('selectedZone')
    localDatetime = utcmoment.astimezone(pytz.timezone(selected))

    return jsonify({
        'timezone': localDatetime.strftime(localFormat)
        # 'timezone': request.args.get('selectedZone')
    })


if __name__ == '__main__':
    app.run()