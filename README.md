
# Task Management API

This project is a **Task Management API** built using **Flask** and **SQLite**. It allows users to manage tasks by creating, updating, deleting, and viewing them with specific due dates and times. The API is integrated with a simple, user-friendly web interface built with **HTML**, **Bootstrap**, and **JavaScript**.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Tracking Repository Activity](#tracking-repository-activity)

## Features

- **Task Management**: Create, view, edit, and delete tasks.
- **Date and Time Selection**: Users can set a specific due date and time for tasks.
- **Database Persistence**: All tasks are stored in a persistent SQLite database.
- **User-Friendly Web Interface**: Built with Bootstrap for a professional and clean user experience.
- **Specific Time Selection**: Optimized time selection (e.g., 09:00 AM, 01:00 PM) instead of minute-by-minute scrolling.

## Installation

### Prerequisites

- Python 3.10 or higher
- Flask and Flask-SQLAlchemy installed (these can be installed via `requirements.txt`)

### Steps to Install Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/task-management-api.git
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

   Open your web browser and go to `http://127.0.0.1:5000` to use the task management interface.

## Usage

Once the server is running, you can:

- Add new tasks with a title, description, due date, and specific time (e.g., 09:00 AM, 01:00 PM).
- View your task list with all due dates and times.
- Edit tasks directly from the task list.
- Delete tasks when they are no longer required.

### API Endpoints

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

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Please make sure your changes are well-documented and tested.

### How to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push your branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Tracking Repository Activity

### GitHub Insights

You can monitor repository activity directly on GitHub, including:

- **Forks**: How many users have forked your project.
- **Stars**: How many users have starred your repository.
- **Contributors**: See who has contributed to the project.

### GitHub Clones and Traffic

To track how many times your repository has been cloned or how many visitors you've had, you can check the **traffic insights** of your repository on GitHub:

1. Go to the main page of the repository.
2. Click on the **"Insights"** tab.
3. In the left menu, click on **"Traffic"**.

Here, you'll see:

- **Total Clones**: How many times your repository has been cloned.
- **Unique Cloners**: How many unique users cloned the repository.
- **Total Views**: How many times your repository has been visited.

### Adding a Clone Tracker Badge

You can add a **GitHub clone tracker badge** to your `README.md` to track clone count using services like [Shields.io](https://shields.io/).

Example:

```markdown
![GitHub clones](https://img.shields.io/badge/dynamic/json?color=blue&label=Clones&query=clones_count&url=https://api.github.com/repos/ayush1929/task-management-api/traffic/clones)
```

Simply replace `youruser` with your GitHub username and repository name.

---

### Contact

For any questions or feedback, feel free to open an issue or contact me at **patelayush1929@gmail.com**.

