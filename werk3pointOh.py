from flask import Flask, render_template
import csv
import random

app = Flask(__name__)


#root
@app.route("/")
def hola():
    return "how do you solve a problem like Olivia?"

@app.route("/occupations")

def helpMeFindAJob():
    return render_template('jobs.html', dict = di(), job = ArandoJob())


with open('occupations.csv') as csvfile:
    reader = csv.reader(csvfile)
    d = {}
    for row in reader:
        if (row[0] != "Job Class" and row[0] != "Total"):
            d[row[0]] = row[1]

##For probabilities
li = []

for x in d.keys():
        for i in range( int(float(d[x]) * 10)):
                li.append(x)
#pick a random job to print at the bottom of the table
randoJob = random.choice(li)

#testing template
#def helpMeFindAJob():
 #   return render_template('jobs.html', dict = d, job = randoJob)

def ArandoJob():
    return randoJob

def di():
    return d


if __name__ == '__main__':
    app.debug = True
    app.run()
