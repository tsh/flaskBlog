from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/user/<name>')
def user(name):
    return '<h2>hello, {0}</h2>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)