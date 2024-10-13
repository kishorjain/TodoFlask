from datetime import datetime

from werkzeug.utils import redirect

from application import app
from application import db
from flask import render_template, flash, request, url_for
from .forms import TodoForm
from flask.templating import render_template_string
from datetime import datetime
from bson import ObjectId


@app.route("/")
def getTodo():
    todos = []
    for todo in db.todo_list.find():
        todo["id"] = str(todo["_id"])
        todo["created"] = todo["completedTime"]
        todos.append(todo)
    return render_template("todoview.html", todo=todos)


@app.route("/add_task", methods=["POST", "GET"])
def add_task():
    if request.method == "POST":
        form = TodoForm(request.form)
        todoName = form.name.data
        todoNote = form.note.data
        completed = form.completed.data
        db.todo_list.insert_one({
            "name": todoName,
            "note": todoNote,
            "completed": completed,
            "completedTime": datetime.now()
        })
        flash("Todo successfully added","success")
        return redirect("/")
    else:
        form = TodoForm()
        return render_template("addTodoView.html", form=form)


@app.route("/updateTask/<id>", methods=["POST", "GET"])
def updateTask(id):
    if request.method == "POST":
        form = TodoForm(request.form)
        todoName = form.name.data
        todoNote = form.note.data
        completed = form.completed.data
        db.todo_list.find_one_and_update({"_id": ObjectId(id)},{"$set":{
            "name":todoName,
            "note": todoNote,
            "completed": completed,
            "completedTime": datetime.now()
        }})
        flash("Todo successfully updated", "success")
        return redirect("/")
    else:
        form = TodoForm()
        todo = db.todo_list.find_one_or_404({"_id": ObjectId(id)})
        print(todo)
        form.name.data = todo.get("name", None)
        form.note.data = todo.get("note", None)
        form.completed.data = todo.get("completed", None)

    return render_template("addTodoView.html", form=form)

@app.route("/deleteTask/<id>")
def deletTask(id):
    todo = db.todo_list.find_one_and_delete({"_id": ObjectId(id)})
    flash("Todo successfully deleted", "success")
    return redirect("/")
