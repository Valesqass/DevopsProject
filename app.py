from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à la base de données MongoDB
client = MongoClient("mongodb://db:27017/")
db = client.todolist
tasks_collection = db.tasks



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Ajouter une nouvelle tâche
        task = request.form.get("task")
        if task:
            tasks_collection.insert_one({"task": task})
        return redirect(url_for("index"))

    tasks = tasks_collection.find()
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<task_id>")
def delete(task_id):
    # Supprimer une tâche
    tasks_collection.delete_one({"_id": ObjectId(task_id)})
    return redirect(url_for("index"))

@app.route("/edit/<task_id>", methods=["GET", "POST"])
def edit(task_id):
    # Modifier une tâche
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if request.method == "POST":
        new_task = request.form.get("task")
        if new_task:
            tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": {"task": new_task}})
        return redirect(url_for("index"))

    return render_template("edit.html", task=task["task"], task_id=task_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)