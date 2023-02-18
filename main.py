from flask import Flask, redirect, url_for, render_template,  request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index2.html')



@app.route('/success/<int:score>')
def success(score):
    res='pass'
    return render_template('result.html', result=res)

@app.route('/fail/<int:score>')
def fail(score):
    res='fail'
    return render_template('result.html',  result=res)

@app.route('/results/<int:mark>')
def results(mark):
    result=''
    if mark<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=mark))


@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data=float(request.form['data'])
        total_score=(science+maths+c+data)/4
    res=''
    if total_score>50:
        res='success'
    else:
        res='fail'
    return redirect(url_for(res, score=total_score))



    





if __name__=='__main__':
    app.run(debug=True)