from flask import Flask,render_template, request
import parser_to_json

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

@app.route('/loadtable', methods=['get'])
def loadtable():
    page = None
    per_page = None
    try:
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
    except ValueError:
        page = 1
        per_page = 10
    req = request.query_string
    filename = "OHA Test Data Grant_2013_2014_2015_2016_Table.xlsx"
    dataframe = parser_to_json.parse_excel(filename, req, page, per_page)
    return dataframe



if __name__ == '__main__':
    app.run()
