from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninja')
def ninjapg():
    return render_template("addninja.html", dojos=Dojo.get_all())


@app.route('/addninja',  methods=['POST'])
def addninja():
    Ninja.create(request.form)
    return redirect('/')