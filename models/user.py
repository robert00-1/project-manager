from models.person import Person


class User(Person):
    """Represents a user who can own multiple projects."""

    def __init__(self, name, email):
        super().__init__(name, email)
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def remove_project(self, project):
        if project in self.projects:
            self.projects.remove(project)

    def list_projects(self):
        return self.projects

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [project.title for project in self.projects]
        }

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.email}) - {len(self.projects)} project(s)"