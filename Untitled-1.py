class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        self.full = full
        return (f'Размер птицы {self.name} — {self.size}.')


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    def describe(self, full=False):
        self.full = full
        if self.full is True:
            return (f'Попугай {self.name} — заметная птица, '
                    f' окрас её перьев —{self.color}, а размер —'
                    f' {self.size}.'
                    f' Интересный факт: попугаи чувствуют ритм, '
                    f'а вовсе не бездумно двигаются под музыку. '
                    f'Если сменить композицию, то и темп движений'
                    f'птицы изменится.')
        else:
            return (super().describe())


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full=True):
        self.full = full
        if self.full is True:
            return (f'Размер пингвина {self.name} из рода '
                    f'{self.genus} — {self.size}. Интересный факт: '
                    f'однажды группа геологов-'
                    f'разведчиков похитила пингвинье яйцо, и их принялась'
                    f' преследовать вся стая, не пытаясь, '
                    f'впрочем, при этом нападать. Посовещавшись,'
                    f' похитители вернули птицам яйцо, и те отстали.')
        else:
            return (super().describe())


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

print(kesha.describe())
print(kowalski.describe())
