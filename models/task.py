class Task:
    """Represents a task in a project."""

    id_counter = 1

    def __init__(self, title, assigned_to, status="Pending"):
        self.id = Task.id_counter
        Task.id_counter += 1

        self.title = title
        self.assigned_to = assigned_to
        self.status = status

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Task title cannot be empty.")

        self._title = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed = ["Pending", "In Progress", "Completed"]

        if value not in allowed:
            raise ValueError(
                "Status must be 'Pending', 'In Progress', or 'Completed'."
            )

        self._status = value

    def mark_complete(self):
        self.status = "Completed"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "assigned_to": self.assigned_to,
            "status": self.status
        }

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

    def __str__(self):
        return (
            f"[{self.id}] {self.title} - "
            f"{self.status} (Assigned to: {self.assigned_to})"
        )