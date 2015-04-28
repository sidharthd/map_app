# Serves the HTML file containing the JavaScript to render the map.

from flask import Flask, render_template, url_for
from pandas import read_csv
import json

app = Flask(__name__)

@app.route('/map/')
def show_map():
    return render_template('map.html')


'''
@app.route('/get_data/')
def get_data():
#    csv_file = url_for('static', filename='air_quality_2011_states.csv')
    csv_data = read_csv('static/air_quality_2011_states.csv')

    json_data = {}
    for i, state in enumerate(csv_data['State']):
        json_data[state] = [k for k in [csv_data['SO2 Annual average'][i], csv_data['SO2 Std. Dev.'][i], csv_data['NO2 Annual average'][i], csv_data['NO2 Std. Dev.'][i], csv_data['PM10 Annual average'][i], csv_data['PM10 Std. Dev.'][i]]]
    return json.dumps(json_data)
'''


if __name__ == '__main__':
    app.run()
