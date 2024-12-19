from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Liste pour stocker les tâches
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Ajouter une nouvelle tâche
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect(url_for("index"))
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:task_id>")
def delete(task_id):
    # Supprimer une tâche
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    # Modifier une tâche
    if 0 <= task_id < len(tasks):
        if request.method == "POST":
            new_task = request.form.get("task")
            if new_task:
                tasks[task_id] = new_task  # Mettre à jour la tâche
            return redirect(url_for("index"))
        return render_template("edit.html", task=tasks[task_id], task_id=task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
