# -*- coding: utf-8 -*-

from controller import Controller
from model import Todo

controller = Controller()

title = raw_input('Inngresar tarea: ')
todo = Todo(title, completed = False)

controller.add_taks(todo)

print('Lista de tareas: ')
print(controller.list_taks())

