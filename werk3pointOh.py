from flask import Flask, render_template
import utils

app = Flask(__name__)


#root
@app.route("/")
def hola():
    return "how do you solve a problem like Olivia?"

#occutable
@app.route("/occupations")

def helpMeFindAJob():
    return render_template('jobs.html', job= utils/occupations.giveMeAJob(utils/occupations.giveMeADict()),
                           dict = utils/occupations.giveMeADict())


if __name__ == '__main__':
    app.debug = True
    app.run()
