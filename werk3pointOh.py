from flask import Flask, render_template
import occupations

app = Flask(__name__)


#root
@app.route("/")
def hola():
    return "how do you solve a problem like Olivia?"

job = ""
dict = {}
#occutable
@app.route("/occupations")

def helpMeFindAJob():
    return render_template('jobs.html', job=occupations.giveMeAJob(occupations.giveMeADict()),
                           dict=occupations.giveMeADict())


if __name__ == '__main__':
    app.debug = True
    app.run()
