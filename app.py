# import the Flask 
import sys
from flask import Flask
from mushroom.logger import logging
from mushroom.exception import MushroomException

# create the application object
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing custom Exception")
    except Exception as e:
        mushroom = MushroomException(e,sys)
        logging.info(mushroom.error_message)
        logging.info('A request was made to the home page')
    return 'This is My New Application,Name - Mushroom Classification'

if __name__ == '__main__':
    app.run(debug=True,port=5001)