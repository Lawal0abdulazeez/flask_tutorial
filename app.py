from flask import Flask, redirect, url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to My Youtube Channel..."

@app.route('/members')
def members():
    return "Oh My Members"

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the mark is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the mark is "+str(score)

@app.route('/results/<int:mark>')
def results(mark):
    result=''
    if mark<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=mark))

if __name__=='__main__':
    app.run(debug=True)