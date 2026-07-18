import pytest
from models.person import Person


def test_person_creation():
    person = Person("Alex", "alex@gmail.com")

    assert person.name == "Alex"
    assert person.email == "alex@gmail.com"


def test_empty_name():
    with pytest.raises(ValueError):
        Person("", "alex@gmail.com")


def test_invalid_email():
    with pytest.raises(ValueError):
        Person("Alex", "alexgmail.com")