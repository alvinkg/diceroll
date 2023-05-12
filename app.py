from flask import Flask
from example_blueprint import example_blueprint


app = Flask(__name__)

app.register_blueprint(example_blueprint)#, url_prefix='/blueprint'

@app.route('/')
def index():
    return 'Hello World'

# @example_blueprint.route('/')
# def index():
#     return 'What a great idea'


if __name__ == "__main__":
    app.run(debug=True)
