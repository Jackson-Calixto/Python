




from flask import Flask, render_template
app = Flask(__name__)

@app.route("/myflaskapp/<username>/<int:marks>")
def myflaskapp(username, marks):
    return render_template('myflaskapp.html', name = username, grade = marks)

@app.route("/myflaskapp/scores")
def scores():
    scorelist = {'Gina':75, 'Ben':55, 'Jane':59}
    return render_template('scores.html', scores =  scorelist)

if __name__ == "__main__":
    app.run(port = 8010)
