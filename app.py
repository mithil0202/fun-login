from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=False)