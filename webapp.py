from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
import random
app = Flask(__name__)

@app.route("/")
def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('countyDemo.html', options=get_state_options(counties))

@app.route("/fact")
def facts():
    toReturn = ""
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        state= request.args["state"]
        value = random.randint(0,2)
        if value < 1:
            toReturn = render_template('countyDemo.html', options=get_state_options(counties), fact=get_interesting_fact(state,counties))
        else:
            toReturn = render_template('countyDemo.html', options=get_state_options(counties), fact=get_interesting_fact2(state,counties))
    return toReturn



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
    returnVal= ""
    for data in counties:
        if data['State'] not in states:
            states[data['State']] = 1
        else:
            states[data['State']] += 1
    if states[state] > 1:
        returnVal= state + " has " + str(states[state]) + " counties."
    else:
        returnVal= state + " has " + str(states[state]) + " county."
    return returnVal

def get_interesting_fact2(state,counties):
    states={}
    returnVal= ""
    for data in counties:
        if data['State'] not in states:
            states[data['State']] = data['Population']['2014 Population']
        else:
            states[data['State']] += data['Population']['2014 Population']
    
    returnVal= state + " has " + str(states[state]) + " people in its population as of 2014."
    
    return returnVal

if __name__=="__main__":
  app.run(debug=True, port=54321)
