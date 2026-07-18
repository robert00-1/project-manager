# Project Manager CLI

A command-line application built with Python that allows administrators to manage users, projects, and tasks.

## Features

- Add users
- List users
- Add projects
- List projects
- Add tasks
- List tasks
- Mark tasks as completed
- Store data using JSON files
- Object-oriented design with inheritance
- Automated testing using pytest



## Technologies

- Python 3.12
- argparse
- rich
- pytest
- JSON

## Installation

Clone the repository:


git clone 


Move into the project:


cd project_manager


Create a virtual environment:


python -m venv venv

source venv/bin/activate

venv\Scripts\activate


Install dependencies:


pip install -r requirements.txt




## Running the CLI

### Add a user


python main.py add-user --name "Alex" --email "alex@gmail.com"


### List users

python main.py list-users

### Add a project

```bash
python main.py add-project \
--user "Alex" \
--title "CLI Tool" \
--description "Python CLI Assignment" \
--due-date "2026-08-30"
```

### List projects


python main.py list-projects


### Add a task


python main.py add-task \
--project "CLI Tool" \
--title "Build Models" \
--assigned-to "Alex"


### List tasks


python main.py list-tasks


### Complete a task


python main.py complete-task --title "Build Models"


## Running Tests


python -m pytest
```



## Project Structure

```
project_manager/
│
├── data/
├── models/
├── tests/
├── utils/
├── main.py
├── requirements.txt
└── README.md




## Known Issues

- Data is stored locally in JSON files.
- Project and task lookups use names rather than unique IDs.
- No delete commands have been implemented.



## Author

Robert Mmasi 