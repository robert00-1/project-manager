from models.task import Task

# Represents a project that contains multiple tasks
class Project:
    

    id_counter = 1
# Initialize a new project with a unique ID, title, description and due date
    def __init__(self, title, description, due_date):
        
        self.id = Project.id_counter
        Project.id_counter += 1

        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []
# Return the project title
    @property
    def title(self):
    
        return self._title
# Set the project title after validating it is not empty
    @title.setter
    def title(self, value):
        
        if not value.strip():
            raise ValueError("Project title cannot be empty.")

        self._title = value
# Add a task from the project
    def add_task(self, task):
        
        self.tasks.append(task)
# Remove a task from the project
    def remove_task(self, task):
        
        if task in self.tasks:
            self.tasks.remove(task)
# Return all tasks belonging to the project
    def list_tasks(self):
        
        return self.tasks

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True

        return False

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(
            data["title"],
            data["description"],
            data["due_date"]
        )

        project.id = data["id"]

        if project.id >= cls.id_counter:
            cls.id_counter = project.id + 1

        for task_data in data["tasks"]:
            project.tasks.append(Task.from_dict(task_data))

        return project

    def __str__(self):
        return (
            f"[{self.id}] {self.title} "
            f"(Due: {self.due_date}) - "
            f"{len(self.tasks)} task(s)"
        )