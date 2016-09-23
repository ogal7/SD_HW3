from flask import Flask, render_template
import csv
import random

app = Flask(__name__)


#root
@app.route("/")
def hola():
    return "how do you solve a problem like Olivia?"

job = ""
dict = {}
@app.route("/occupations")

def helpMeFindAJob():
    return render_template('jobs.html', job=ArandoJob(di()), dict=di())

def di():
    with open('occupations.csv') as csvfile:
        reader = csv.reader(csvfile)
        d = {}
        for row in reader:
            if (row[0] != "Job Class" and row[0] != "Total"):
                d[row[0]] = row[1]
        return d


def ArandoJob(d):
    li = []
    for x in d.keys():
        for i in range( int(float(d[x]) * 10)):
                li.append(x)                                                         
    randoJob = random.choice(li)
    return randoJob




if __name__ == '__main__':
    app.debug = True
    app.run()
