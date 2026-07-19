from models.person import Person

# Represents a user who can own multiple project
class User(Person):
    
# Initialize anew user with a name , email and empty project list
    def __init__(self, name, email):
         
        super().__init__(name, email)
        self.projects = []
# Add a project to the user's project list
    def add_project(self, project):
        
        self.projects.append(project)
# Remove a project from the user's project list
    def remove_project(self, project):
        
        if project in self.projects:
            self.projects.remove(project)
# Return all projects owed by the user
    def list_projects(self):
        
        return self.projects
# Convert the user object into a dictionary for JSON storage
    def to_dict(self):
        
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [project.title for project in self.projects]
        }
# Return a readable string representation of the user
    def __str__(self):
        
        return f"[{self.id}] {self.name} ({self.email}) - {len(self.projects)} project(s)"