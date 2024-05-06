from queue import Queue
from typing import List

from openagi.tasks.task import Task


class TaskLists:
    def __init__(self) -> None:
        self.tasks = Queue()
        self.completed_tasks = Queue()

    def add_task(self, task: Task) -> None:
        """Adds a Task instance to the queue."""
        self.tasks.put(task)

    def add_tasks(self, tasks: List[Task]):
        for task in tasks:
            self.add_task(task)

    def get_tasks(self):
        return self.tasks

    def get_next_unprocessed_task(self) -> Task:
        """Retrieves the next unprocessed task from the queue."""
        if not self.tasks.empty():
            return self.tasks.get_nowait()
        return None

    @property
    def all_tasks_completed(self) -> bool:
        """Checks if all tasks in the queue have been processed."""
        return self.tasks.empty()

    def add_completed_tasks(self, task: Task):
        self.completed_tasks.put(task)
