from flask import Flask, render_template, session, redirect
app = Flask (__name__)
app.secret_key="this is my secret key"

@app.route('/')
def index():
    if "visit" not in session:
        session['visit'] = 0
    else:
        session['visit'] +=1
    return render_template('index.html')

@app.route('/increase')
def increase():
    session['visit'] += 1
    return redirect('/')

@app.route('/destroy_session')
def reset():
    # session['visit'] = 0 reassigns value to zero
    # session.clear() #clears all keys
    session.pop('visit') #clears specific key
    return redirect('/')

@app.route('/plus_two')
def plus_two():
    session['visit'] +=1 #adds 2 because of the redirect also adds 1 in the else statement
    return redirect('/')



@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again. "

if __name__=="__main__":
    app.run(debug=True) 