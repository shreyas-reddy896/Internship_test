from flask import Flask, redirect, url_for
import os
import getpass
import time
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('htop'))  # Redirect to /htop

@app.route('/htop')
def htop():
   
    name = "Shreyas H Reddy" 

    username = os.environ.get('USER') or os.environ.get('USERNAME') or getpass.getuser()
    
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    try:
        output = subprocess.check_output(['top', '-b', '-n', '1'], universal_newlines=True)
    except Exception as e:
        output = f"Error executing command: {e}"

    return f'<pre>Name: {name}\nUsername: {username}\nServer Time: {server_time}\n\nTop output:\n{output}</pre>'

if __name__ == '__main__':
    app.run(debug=True)


