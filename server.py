from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def index():
    return ("<h1>Guess a number between 0 and 9</h1> "
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />")

@app.route("/<int:number>")
def guess(number):
    n = random.randint(1, 9)
    html = ""
    if number < n:
        html = ("<h1 style='color: red'>To low, try again!</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />")
    elif number > n:
        html = ("<h1 style='color: purple'>To high, try again!</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />")
    else:
        html = ("<h1 style='color: green'>You found me</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />")


    return html



if __name__ == '__main__':
    app.run()