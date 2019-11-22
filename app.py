from flask import Flask
from sample_classes.data import Data
app = Flask(__name__)


@app.route('/')
def full_name():
    full_name = Data('Pedro', 'Martinez').get_full_name()
    return {"full_name": full_name}

if __name__ == '__main__':
    app.run()