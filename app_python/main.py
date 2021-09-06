from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def hello_world():
    tz_moscow = pytz.timezone('Europe/Moscow')
    datetime_moscow = datetime.now(tz_moscow)
    moscow_time = datetime_moscow.strftime("%H:%M:%S")
    return f"<p> MOSCOW TIME: {moscow_time}<p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
