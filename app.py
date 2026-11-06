from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'lana=linda-perfeita-maravilhosa'

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':  
    app.run(debug=True, port=5001)