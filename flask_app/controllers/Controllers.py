from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.Model import Model

@app.route('/')
def index():
    return render_template('index.html')