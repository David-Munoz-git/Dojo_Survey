from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "k564lsadifuhaw9puoefja268nkjdf73u4y"

#render form

@app.route('/')
def form():
  return render_template('index.html')

#processed form


@app.route('/process', methods=['POST'])

def prossedForm():
  print(request.form['Name'])
  print(request.form['state'])
  print(request.form['Language'])
  print(request.form['Comments'])
  session['session_name'] = request.form['Name']
  session['session_state'] = request.form['state']
  session['session_Language'] = request.form['Language']
  session['session_Comments'] = request.form['Comments']
  return redirect('/result')

@app.route('/result')
def postForm():
  if "session_name" in session:
    print(session['session_name'])
  return render_template('index2.html',name = session['session_name'], location = session['session_state'], language = session['session_Language'], comments = session['session_Comments'])

@app.route('/goback', methods =['POST'])
def goBack():
  return redirect('/')

if __name__=="__main__":
  app.run(debug=True)