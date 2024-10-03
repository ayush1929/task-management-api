
# Task Management API

This project is a **Task Management API** built using **Flask** and **SQLite**. It allows users to manage tasks by creating, updating, deleting, and viewing them with specific due dates and times. The API is integrated with a user-friendly web interface built with **HTML**, **Bootstrap**, and **JavaScript**.

## Features

- **Task Management**: Create, view, edit, and delete tasks.
- **Due Date and Time Selection**: Users can assign tasks specific due dates and select times.
- **Persistent Database**: All tasks are stored in an **SQLite** database and persist across sessions.
- **Responsive Web Interface**: The frontend is built using **Bootstrap** for a professional and responsive design.
- **API Integration**: Interact with the system via a simple REST API.

## Installation

### Prerequisites

- **Python 3.10** or higher
- **Flask** and **Flask-SQLAlchemy**

### Steps to Install Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ayush1929/task-management-api.git
   ```

2. **Navigate into the project directory:**

   ```bash
   cd task-management-api
   ```

3. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   - For Windows:
     ```bash
     venv\Scripts\activate
     ```

   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Flask app:**

   ```bash
   python app.py
   ```

7. **Access the app:**

   Open your browser and go to `http://127.0.0.1:5000` to start managing tasks.

## Usage

Once the server is running, you can:

- **Add a Task**: Use the form to create tasks with a title, description, due date, and time.
- **View Tasks**: All tasks will be displayed in a responsive task list with due dates and times.
- **Edit Tasks**: Click "Edit" to modify any task’s details. The form will auto-fill with existing task data for easy updates.
- **Delete Tasks**: Click "Delete" to remove a task when it is no longer needed.

## API Endpoints

- **GET /tasks**: Retrieve all tasks.
  
  Example request:
  ```bash
  curl http://127.0.0.1:5000/tasks
  ```

- **POST /tasks**: Create a new task.
  
  Example request:
  ```bash
  curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title": "New Task", "description": "Complete by Friday", "due_date": "2024-10-07", "time_of_day": "09:00 AM"}'
  ```

- **PUT /tasks/<id>**: Update an existing task by ID.
  
  Example request:
  ```bash
  curl -X PUT http://127.0.0.1:5000/tasks/1 -H "Content-Type: application/json" -d '{"title": "Updated Task", "description": "Updated description", "due_date": "2024-10-08", "time_of_day": "02:00 PM"}'
  ```

- **DELETE /tasks/<id>**: Delete a task by ID.
  
  Example request:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/tasks/1
  ```
## Web Interface for Efficient User Interaction

In addition to the API functionality, this project includes a **responsive web interface** designed to provide a user-friendly experience. The interface allows users to manage tasks visually through an intuitive form and task list, making it more efficient than interacting solely through API calls.

### Key Features of the Web Interface:
- **Task Creation**: Users can easily add new tasks with a form that includes fields for the title, description, due date, and specific time.
- **Task Viewing**: All tasks are displayed in a responsive list, with the due date and time clearly visible.
- **Task Editing**: Users can edit existing tasks directly from the interface. The form is auto-filled with the task's current data for easy modifications.
- **Task Deletion**: Tasks can be quickly deleted with a simple button click, ensuring that outdated or unnecessary tasks are removed without hassle.
- **Responsive Design**: The interface is built using **Bootstrap**, ensuring that it works well on both desktop and mobile devices.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

