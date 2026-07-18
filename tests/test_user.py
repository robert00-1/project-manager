from models.user import User
from models.project import Project


def test_add_project():
    user = User("Alex", "alex@gmail.com")

    project = Project(
        "CLI Tool",
        "Assigment",
        "2026-08-30"
    )

    user.add_project(project)

    assert len(user.projects) == 1