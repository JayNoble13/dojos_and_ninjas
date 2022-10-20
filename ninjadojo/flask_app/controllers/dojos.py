from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo


@app.route('/')
def reroute():
    return redirect('/dojo')

@app.route('/dojo')
def dojopg():
    dojos=Dojo.get_all()
    return render_template("adddojo.html", all_dojos=dojos)

@app.route('/adddojo',  methods=['POST'])
def adddojo():
    Dojo.create(request.form)
    return redirect('/dojo')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data={
        "id":id
    }
    return render_template("dashboard.html", dojo=Dojo.ninjas_with_dojos(data))