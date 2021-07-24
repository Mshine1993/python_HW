class Stationary:

    def __init__(self, title="Канцелярская принадлежность"):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Запуск отрисовки ручкой')


class Pencil(Stationary):
    def draw(self):
        print(f'Запуск отрисовки карандашом')


class Handle(Stationary):
    def draw(self):
        print(f'Запуск отрисовки маркером')


stat = Stationary()
stat.draw()

pen = Pen()
pencil = Pencil()
han = Handle()

pen.draw()
pencil.draw()
han.draw()
