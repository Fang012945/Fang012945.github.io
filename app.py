import flask
from flask import Flask,request, redirect
import csv
app=Flask(__name__)

@app.route("/")
def home_page():
    return flask.render_template('index.html')

@app.route("/<string:page_name>")
def page(page_name):
    return flask.render_template(page_name)

def database_writer(data):
    name=data['name'].replace(',',' ')
    emailaddress=data['emailaddress']
    Date=data['Date']
    pet=data['pet']
    message=data['Message'].replace(',',' ')
    with open(r'.\database.csv','a',newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([name,emailaddress,Date,pet,message])

@app.route("/send_form", methods=['GET', 'POST'])
def send_form():
    if request.method=='POST':
        data=request.form.to_dict()
        print(data)
        database_writer(data)
        return redirect('/thanks.html')