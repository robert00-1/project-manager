from models.project import Project
from models.task import Task

def test_add_task():
    project = Project(
        "CLI Tool",
        "Python Assignment",
        "2026-08-30"
    )

    task = Task("Build Models", "Alex")

    project.add_task(task)

    assert len(project.tasks) == 1