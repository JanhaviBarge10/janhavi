from flask import Flask, render_template
from redis import Redis 

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.rout('/')
def index():
    redis.incr('hits')
    count = redis.get('hits').decode('utf-8')
    return render_template('index.html', count=count)

if__name__ == '__main__':
app.run(debug=True, host='0.0.0.0')
        