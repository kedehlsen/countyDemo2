from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flash(__name__)

if __name__=="__main__":
  app.run(debug=False, port=54321)
