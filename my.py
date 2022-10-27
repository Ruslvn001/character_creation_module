from datetime import datetime as dt 
# Импортируйте datetime. 
import time
# Импортируйте time.

class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        # Допишите два свойства класса.
        self.start_time = None
        self.end_time = None

    def accept_quest(self):
        self.start_time = dt.now()

        if self.end_time is not None:
            return f'Начало "{self.name}" положено.'
        else:
            return 'С этим испытанием вы уже справились.'

    def pass_quest(self):
        self.end_time = dt.now()

        if self.start_time is None:
            return 'Нельзя завершить то, что не имеет начала!'
        else:

            completion_time = self.end_time - self.start_time
            self.end_time = None
            return f'Квест "{self.name}" окончен. '\
                   f'Время выполнения квеста: {completion_time}'


    def __str__(self):
        if self.start_time is not None and self.end_time is not None:
            return (f'Цель квеста {self.name} - {self.goal}. Квест завершён.')
        if self.start_time is not None and self.end_time is None:
            return (f'Цель квеста {self.name} - {self.goal}. Квест выполняется.')
        

    # Напишите методы приема и сдачи квеста.


quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельнки'
quest_description = """
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельнки"""

new_quest = Quest(quest_name, quest_description, quest_goal)

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())

print(new_quest)