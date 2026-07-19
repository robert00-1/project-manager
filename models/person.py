class Person:
    """Base class for all people in the system."""

    id_counter = 1

    def __init__(self, name, email):
        """Initialize a new person with a unique ID, name and email."""
        
        self.id = Person.id_counter
        Person.id_counter += 1

        self.name = name
        self.email = email

    @property
    def name(self):
        """Return the person's name."""
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")

        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        """Set the person's nae after validating it is not empty."""
        if "@" not in value:
            raise ValueError("Invalid email address.")

        self._email = value

    def to_dict(self):
        """Convert the person object into a dictionary for JSON storage."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        """Create a person object from a dictionary"""
        person = cls(data["name"], data["email"])
        person.id = data["id"]

        if person.id >= cls.id_counter:
            cls.id_counter = person.id + 1

        return person

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.email})"