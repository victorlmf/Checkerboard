from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def board1():
    return render_template('index.html', xNum=8, yNum=8, colorOne="red", colorTwo="blue")

@app.route('/<int:num>')
def board2(num):
    return render_template('index.html', xNum=8, yNum=num, colorOne="red", colorTwo="blue")

@app.route('/<int:num1>/<int:num2>')
def board3(num1,num2):
    return render_template('index.html', xNum=num1, yNum=num2, colorOne="red", colorTwo="blue")

@app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def board4(num1,num2,color1,color2):
    return render_template('index.html', xNum=num1, yNum=num2, colorOne=color1, colorTwo=color2)

if __name__=="__main__":
    app.run(debug=True)