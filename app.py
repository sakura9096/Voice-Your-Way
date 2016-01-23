from flask import Flask, render_template, json, request, redirect, session
import sqlite3
import houndify

app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'

# global variable
msg = ""

# home page
@app.route('/')
def main():
    return render_template('index.html')

# show sign up page
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

# sign up page, POST method
@app.route('/signUp', methods=['POST'])
def signUp():
    conn = sqlite3.connect('user.sqlite', timeout=1, check_same_thread=False)
    cur = conn.cursor()

	# create some tables
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS User (
	    name TEXT NOT NULL PRIMARY KEY,
	    email TEXT,
	    password TEXT
    );
    ''')

    # extract values from user submission
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

	# check if user name already exists
    cur.execute('SELECT COUNT(*) FROM User WHERE name = ? ', (_name, ))
    exist_name = int(cur.fetchone()[0])

    if exist_name == 0:
        cur.execute('''INSERT INTO User ( name, email, password ) 
            VALUES ( ?, ?, ? )''', ( _name, _email, _password ) )

        conn.commit()

        cur.close() 
        conn.close()

        session['user'] = _name
        
    return redirect('/showSignUp')

# sign in page
@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')

# validate login
@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    conn = sqlite3.connect('user.sqlite', timeout=1, check_same_thread=False)
    cur = conn.cursor()

    # extract values from user submission
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

	# check if user info match
    cur.execute('SELECT name, email, password FROM User WHERE name = ? ', (_name, ))
    data = cur.fetchone()

    if _email != data[1] or _password != data[2]:
    	return render_template('error.html', error='Wrong Info')
    
    session['user'] = data[0]
    return redirect('/userHome')

# user home
@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html', error='Unauthorized Access')

# user log out
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# prompt for user input audio
@app.route('/inputAudio')
def inputAudio():
    return render_template('inputAudio.html')

# show audio context page
@app.route('/showAudioContext', methods=['POST'])
def showAudioContext():
    # extract values from user submission
    audio = request.form['inputName']
    msg = houndify.run(audio)
    return render_template('showAudioContext.html', audio_msg=msg, text="https://twitter.com/intent/tweet?text=%s" % msg)


# run program
if __name__ == "__main__":
    app.run(debug=True)
