from flask import Flask,send_file
app=Flask(__name__)
@app.route('/')
def dashboard():
 return send_file('dashboard.html')
