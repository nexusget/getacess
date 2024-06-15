from flask import Flask, request
import os

app = Flask(__name__)
password = "none"

@app.route('/')
def index():
    return '''
    <form action="/send_message" method="post">
        <input type="password" name="password" placeholder="Enter password">
        <input type="text" name="message" placeholder="Enter your message">
        <input type="submit" value="Send">
    </form>
    '''

@app.route('/send_message', methods=['POST'])
def send_message():
    entered_password = request.form['password']
    message = request.form['message']
    if entered_password == password:
        powershell_command = f'powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show(\'{message}\')"'
        os.system(powershell_command)
        return f'Message "{message}" sent!'
    else:
        return "Invalid password!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
