# import the Flask 
from flask import Flask

# create the application object
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'This is My New Application,Name - Mushroom Classification'

if __name__ == '__main__':
    app.run(debug=True)