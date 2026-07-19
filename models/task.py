class Task:
    

    id_counter = 1
# Initialize a new task with a unique ID, title, assignee and status
    def __init__(self, title, assigned_to, status="Pending"):
         
        self.id = Task.id_counter
        Task.id_counter += 1

        self.title = title
        self.assigned_to = assigned_to
        self.status = status
# Return the task title
    @property
    def title(self):
        
        return self._title
# Set the task title after validating it isnot empty
    @title.setter
    def title(self, value):
        
        if not value.strip():
            raise ValueError("Task title cannot be empty.")

        self._title = value
# Return the current task status
    @property
    def status(self):
        
        return self._status
# Set the task status after validating the allowed value
    @status.setter
    def status(self, value):
        
        allowed = ["Pending", "In Progress", "Completed"]

        if value not in allowed:
            raise ValueError(
                "Status must be 'Pending', 'In Progress', or 'Completed'."
            )

        self._status = value
# Mark the task as completed
    def mark_complete(self):
        
        self.status = "Completed"
# Convert the task object into a dictionary for JSON storage
    def to_dict(self):
        
        return {
            "id": self.id,
            "title": self.title,
            "assigned_to": self.assigned_to,
            "status": self.status
        }
# Create a task object from a dictioonary
    @classmethod
    def from_dict(cls, data):
        
        task = cls(
            data["title"],
            data["assigned_to"],
            data["status"]
        )

        task.id = data["id"]

        if task.id >= cls.id_counter:
            cls.id_counter = task.id + 1

        return task
# Return a readable string representation of the task
    def __str__(self):
        
        return (
            f"[{self.id}] {self.title} - "
            f"{self.status} (Assigned to: {self.assigned_to})"
        )