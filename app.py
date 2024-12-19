from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "secret_key"  # Nécessaire pour les flash messages

# Connexion à la base de données MongoDB
try:
    client = MongoClient("mongodb://db:27017/")
    db = client.todolist
    tasks_collection = db.tasks
except Exception as e:
    print(f"Erreur de connexion à MongoDB : {e}")
    exit(1)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks_collection.insert_one({"task": task})
            flash("Tâche ajoutée avec succès !", "success")
        else:
            flash("Veuillez entrer une tâche.", "error")
        return redirect(url_for("index"))

    tasks = tasks_collection.find()
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<task_id>")
def delete(task_id):
    try:
        tasks_collection.delete_one({"_id": ObjectId(task_id)})
        flash("Tâche supprimée avec succès !", "success")
    except Exception as e:
        flash(f"Erreur lors de la suppression : {e}", "error")
    return redirect(url_for("index"))

@app.route("/edit/<task_id>", methods=["GET", "POST"])
def edit(task_id):
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if not task:
        flash("Tâche introuvable.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        new_task = request.form.get("task")
        if new_task:
            tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": {"task": new_task}})
            flash("Tâche modifiée avec succès !", "success")
        else:
            flash("Veuillez entrer une tâche valide.", "error")
        return redirect(url_for("index"))

    return render_template("edit.html", task=task["task"], task_id=task_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
