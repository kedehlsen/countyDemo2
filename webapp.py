from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
import random
app = Flask(__name__)

@app.route("/")
def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        state= request.args
    return render_template('countyDemo.html', options=get_state_options(counties), fact=get_interesting_fact(state,counties))

@app.route("/fact")
def facts():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        state= request.args
    return render_template('countyDemo.html', options=get_state_options(counties), fact="hullo")



def get_state_options(counties):
    listOfStates = []
    options = ""
    for data in counties:
        if data['State'] not in listOfStates:
            listOfStates.append(data['State'])
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options


def get_interesting_fact(state,counties):
    states={}
    for data in counties:
        if data['State'] not in states:
            states[data['State']] = 1
        else:
            states[data['State']] += 1
    return state + " has " + str(states[state]) + " counties."
    
  

if __name__=="__main__":
  app.run(debug=False, port=54321)
