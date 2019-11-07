from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        
def render_main():
    return render_template('countydemographics.html')


def get_state_options(counties):
    listOfStates = []
    for data in counties:
        if data['State'] not in listOfStates:
            listOfStates.append(data['State'])
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options

  

if __name__=="__main__":
  app.run(debug=False, port=54321)
