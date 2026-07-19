from models.person import Person


class User(Person):
    """Represents a user who can own multiple projects."""

    def __init__(self, name, email):
        """Initialize a new user with a name, email, and empty project list."""
        super().__init__(name, email)
        self.projects = []

    def add_project(self, project):
        """Add a project to the user's project list."""
        self.projects.append(project)

    def remove_project(self, project):
        """Remove a project from the user's project list."""
        if project in self.projects:
            self.projects.remove(project)

    def list_projects(self):
        """Return all projects owned by the user."""
        return self.projects

    def to_dict(self):
        """Convert the user object into a dictionary for JSON storage."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [project.title for project in self.projects]
        }

    def __str__(self):
        """Return a readable string representation of the user."""
        return f"[{self.id}] {self.name} ({self.email}) - {len(self.projects)} project(s)"