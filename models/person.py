#Base class for all people in the system
class Person:
    

    id_counter = 1
# Initilize a new person with a unique ID, name and email
    def __init__(self, name, email):
        
        
        self.id = Person.id_counter
        Person.id_counter += 1

        self.name = name
        self.email = email
# return the person's name
    @property
    def name(self):
        
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")

        self._name = value

    @property
    def email(self):
        return self._email
# Set the person's name after validating it is not empty
    @email.setter
    def email(self, value):
        
        if "@" not in value:
            raise ValueError("Invalid email address.")

        self._email = value
# Convert the person object into a dictionary for JSON storage
    def to_dict(self):
        
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
# Create a person object from a dictionary
    @classmethod
    def from_dict(cls, data):
        
        person = cls(data["name"], data["email"])
        person.id = data["id"]

        if person.id >= cls.id_counter:
            cls.id_counter = person.id + 1

        return person

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.email})"