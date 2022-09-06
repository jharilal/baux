from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)