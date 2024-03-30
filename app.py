# import the Flask 
from flask import Flask
from mushroom.logger import logging

# create the application object
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info('A request was made to the home page')
    return 'This is My New Application,Name - Mushroom Classification'

if __name__ == '__main__':
    app.run(debug=True,port=5001)