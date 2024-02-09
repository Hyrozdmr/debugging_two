from lib.todo_list import *
from lib.todo import *

"""
Initially, if There are no todo
"""
def test_if_there_are_no_tasks():
    todo_list = TodoList()
    assert todo_list.incomplete() == []
 
"""
When we add a todo
It is reflected in the list of todo

"""
def test_add_todo_reflected_in_todos():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    todo_list.add(task1)
    assert todo_list.incomplete() == [task1]

"""
When we add multiple task 
They are all reflected in the list of todo

"""
def test_add_multiple_todo_reflected_in_todos():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task2 = Todo("Finish challenge")
    task3 = Todo("Watch the football game")
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    assert todo_list.incomplete() == [task1, task2, task3]

"""
When we add multiple todo 
And  two as completed
It disappers from the list of todo
"""
def test_todo_copmlete():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task2 = Todo("Finish challenge")
    task3 = Todo("Watch the football game")
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    task2.mark_complete()
    task3.mark_complete()
    assert todo_list.complete() == [task2, task3]
    
    





