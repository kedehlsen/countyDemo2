from flask import Flask, request, Markup, render_template, Flash, Markup
import os
import json
app = Flash(__name__)

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)

@app.route("/")
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
