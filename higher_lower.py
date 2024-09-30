from flask import Flask
import random

app1=Flask(__name__)

num=random.randint(1,10)

@app1.route("/")
def homepage():
    return ('<h1>Guess a number between 1 and 9</h1>'
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDY3dzJyMHp1c2xscWh5bHd3a25hcGJ4cmFvdmkwM3F0NG1menptaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/4pqm16XH2rQopZrdFU/giphy.gif" width=200 height=200>')

@app1.route("/<int:number>")
def checking(number):
    if number>num:
        return ('<h1> TOO HIGH </h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.g" width=200 height=200>')
    if number<num:
        return ('<h1> TOO LOW </h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200 height=200>')
    if number==num:
        return ('<h1> YOU FOUND ME </h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200 height=200>')

if __name__=="__main__":
    app1.run(debug=True)