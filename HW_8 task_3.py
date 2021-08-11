class Error:
    def __init__(self, *args):
        self.my_list = []

    @property
    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter(для выхода введите stop, затем нажмите n) - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')

            except:
                print(f"Недопустимое значение")
                y_or_n = input(f'Попробовать еще раз? Y/N(для выхода введите n) ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input)
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Текущий список - {self.my_list} \nВы вышли'
                else:
                    return f'Все сломалось'


try_except = Error(1)
print(try_except.my_input)
