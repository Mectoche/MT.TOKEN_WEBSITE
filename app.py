from flask import Flask, request, render_template, redirect, url_for, session, abort
import os

app = Flask(__name__)
app.secret_key = '91ee8c748112b888b708934dbbe6dcd4b79f8c0a66d325aa'
TOKEN = r'C:\Users\Samuel\Desktop\MectocheToken\TOKEN\Debug\token.txt'

def read_token():
    if os.path.exists(TOKEN):
        with open(TOKEN, 'r') as file:
            return file.read().strip()
    return None

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        token_input = request.form.get('token')
        if token_input == read_token():
            session['logged_in'] = True
            return redirect(url_for('protected'))
        else:
            return render_template('login.html', error='Token inválido.')
    return render_template('login.html')

@app.route('/protected')
def protected():
    if not session.get('logged_in'):
        abort(403)
    return render_template('protected.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
