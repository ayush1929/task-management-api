from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)  # Use DateTime for the due date
    time_of_day = db.Column(db.String(20), nullable=True)  # Morning, Afternoon, Evening

# Create the database inside the application context
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

# Create Task
@app.route('/tasks', methods=['POST'])
def create_task():
    task_data = request.json
    due_date_str = task_data.get('due_date', None)

    # Convert string due_date to datetime object
    if due_date_str:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
    else:
        due_date = None

    new_task = Task(
    title=task_data['title'],
    description=task_data['description'],
    due_date=due_date,
    time_of_day=task_data.get('time_of_day', '09:00 AM')  # Default to '09:00 AM' if not provided
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created'}), 201

# Read All Tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'due_date': task.due_date.strftime('%Y-%m-%d') if task.due_date else None,
        'time_of_day': task.time_of_day
    } for task in tasks]
    return jsonify(task_list), 200

# Update Task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    task_data = request.json
    due_date_str = task_data.get('due_date', None)

    # Convert string due_date to datetime object
    if due_date_str:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
    else:
        due_date = None

    task.title = task_data['title']
    task.description = task_data['description']
    task.due_date = due_date
    task.time_of_day = task_data.get('time_of_day', '09:00 AM')
    db.session.commit()

    return jsonify({'message': 'Task updated'}), 200

# Delete Task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
