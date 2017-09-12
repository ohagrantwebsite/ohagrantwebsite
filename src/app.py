from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listings')
def listings():
    return render_template('listings.html')

@app.route('/qa')
def qa():
    return render_template('qa.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run()
