# TODO App using Flask - README 📝

- 🍴 ![GitHub forks](https://img.shields.io/github/forks/Akash-nath29/TODO_FLASK?style=social)
⭐️ ![GitHub stars](https://img.shields.io/github/stars/Akash-nath29/TODO_FLASK?style=social)
👁️‍🗨️ ![GitHub watchers](https://img.shields.io/github/watchers/Akash-nath29/TODO_FLASK?style=social)
- 📦 ![GitHub repo size](https://img.shields.io/github/repo-size/Akash-nath29/TODO_FLASK)
🐞 ![GitHub issues](https://img.shields.io/github/issues/Akash-nath29/TODO_FLASK)
🚀 ![GitHub pull requests](https://img.shields.io/github/issues-pr/Akash-nath29/TODO_FLASK)
- 📜 ![GitHub license](https://img.shields.io/github/license/Akash-nath29/TODO_FLASK)

Welcome to the TODO App developed using Flask! This application provides a convenient way to manage your tasks. You can add tasks along with their names and descriptions, which will be stored in a database for efficient tracking.

## Table of Contents 📑

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation 🛠️

Get started with the TODO App locally by following these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Akash-nath29/TODO_FLASK.git
   cd TODO_FLASK
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   or, for cmd
   ```bash
   venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Run the application:
   ```bash
   flask run
   ```

Access the application through your web browser at `http://127.0.0.1:80`.

## Usage 🚀

Interact with the application through a user-friendly web interface:

- ✅ **Add a Task:** Click the "Add Task" button and provide the task name and description. Click "Submit" to store the task in the database.

- 📋 **View Tasks:** The main page lists all tasks. You can view task details.


- 🗑️ **Delete Task:** Remove a task by clicking the "Delete" button next to it.

## Contributing 👥

Contributions are welcome! To contribute:

1. Fork the repository and create a new branch for your feature/fix.

2. Make changes, commit them, and push to your forked repository.

3. Create a pull request to the main project repository.

4. Your contribution will be reviewed and merged upon approval.

## License 📜

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the terms of the license.

---

Thanks for using the TODO App! If you have questions or encounter issues, please open an issue on the [GitHub repository](https://github.com/Akash-nath29/TODO_FLASK/issues). Keep on track with your tasks! 📝