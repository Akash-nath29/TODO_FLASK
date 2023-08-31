import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'MLXH243rjBDIBibiBIbibIUBImmfrdTWS7FDhdwYF56wPj8'

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String(100), nullable=False)
    taskDescription = db.Column(db.Text(500), nullable=True)
    
    def __init__(self, taskName, taskDescription):
        self.taskName = taskName
        self.taskDescription = taskDescription
        
    def __repr__(self):
        return '<User %r>' % self.username
        
@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@app.route("/addTask")
def addTask():
    return render_template("createTask.html")

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        taskName = request.form.get("taskName")
        taskDescription = request.form.get("taskDescription")
        newTask = Task(taskName, taskDescription)
        db.session.add(newTask)
        db.session.commit()
    return redirect("/")

@app.route("/<int:id>/delete")
def delete(id):
    task_to_delete = Task.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="80")