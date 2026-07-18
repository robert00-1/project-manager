from models.task import Task

def test_task_creation():
    task = Task("Build CLI", "Alex")

    assert task.title == "Build CLI"
    assert task.status == "Pending"

def test_mark_complete():
    task = Task("Build CLI", "Alex")

    task.mark_complete()

    assert task.status == "Completed"