import time
import random
from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def default(name):
    time.sleep(random.randint(1, 5))
    return "hi, {}".format(name)

if __name__ == '__main__':
    app.run()



