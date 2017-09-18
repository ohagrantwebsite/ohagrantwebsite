from flask import Flask,render_template, request
import json
import parser_to_json
import os
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

@app.route('/loadtable', methods=['post'])
def loadtable():
    req = request.get_json()
    page = req['page']
    per_page = req['per_page']
    filters = req['filters']
    filename = "OHA Test Data Grant_2013_2014_2015_2016_Table.xlsx"
    dataframe = parser_to_json.parse_excel(filename, filters, page, per_page)
    return dataframe

@app.route('/loadsearch', methods=['get'])
def loadsearch():
    filename = "OHA Test Data Grant_2013_2014_2015_2016_Table.xlsx"
    return parser_to_json.get_dropdowns(filename)

@app.route('/loadchart', methods=['post'])
def loadchart():
    req = request.get_json()
    indices = req['indices']
    axis = req['axis']
    mode = req['mode']
    filename = "OHA Test Data Grant_2013_2014_2015_2016_Table.xlsx"
    return parser_to_json.get_chart(filename, axis, indices, mode)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port)
