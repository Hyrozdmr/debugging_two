from lib.todo import *

"""
Initially test todo
"""
def test_Initially_todo():
    todo = Todo("")
    assert todo.task == ""


def test_mark_complete_todo():
    todo = Todo("Complete Task")
    todo.mark_complete()
    assert todo.complete 