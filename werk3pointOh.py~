from flask import Flask, render_template
import csv
import random


app = Flask(__name__)
@app.route('/occupations')
d = {}
randoJob = ""



# init a dictionary of occupations, send it to template
with open('occupations.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if (row[0] != "Job Class" and row[0] != "Total"):
            d[row[0]] = row[1]


li = []

for x in d.keys():
        for i in range( int(float(d[x]) * 10)):
                li.append(x)



randoJob = random.choice(li)




def helpMeFindAJob():
    return render_template('jobs.html', dict = d, job = randoJob)





if __name__ == '__main__':
    app.debug = True
    app.run()
