from flask import Flask, render_template

app = Flask(__name__)

@app.route('/greet')
def greet():
    hour = 14 
    name = 'Sardor'
    return render_template('greet.html', hour=hour, name=name)

if __name__  == '__main__':
    app.run(debug=True)
