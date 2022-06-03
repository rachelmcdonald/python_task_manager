from flask import render_template
from app import app
from models.todo_list import tasks

@app.route('/tasks')
def index():
    return render_template('index.html', title='Home', tasks=tasks)

@app.route('/tasks/all_tasks')
def all_tasks():
    return render_template('all_tasks.html', task=tasks)

@app.route('/tasks/<index>')
def single_task(index):
    chosen_task = tasks[int(index)]
    return render_template('task.html', task=chosen_task)