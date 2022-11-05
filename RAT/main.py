from colorama import init # модуль позволяющий выводить красивый текст
init(autoreset=True) # подключаем его и задаём параметр, чтобы именно выделенный текст выводился в цвете
from colorama import Fore, Back, Style # комманды этого модуля
import commands # импортировали наши команды

# создаём функцию и засовываем туда наши комманды
def main():

    com = ['move_right', 'move_left', 'click'] # список с функциями для дальнейшей выборки
    v1 = ','.join(com)# делаем маску для вывода
    # если не сделаем маску вывод получится: ['move_right', 'move_left', 'click']
    requests_1 = input(f'Комманды:{v1}, ваша комманда:')
    # используем try expect, для обработки ошибок(если будут)
    try:
        # стандартные условия выборки
        if requests_1 == 'move_right':
          commands.Mouse.move_right(3)

        if requests_1 == 'move_left':
           commands.Mouse.move_left(3)

        if requests_1 == 'click':
           commands.Mouse.click(3,3)
        # если запрос не похожь на все то выводим ошубку
        if requests_1 not in com:
               print(Fore.RED + 'COMMAND IS DIFFERENT')
    # есди что то пошло не так
    except:
        print(Fore.RED + 'ERROR')
        
# запуск 
if __name__ == "__main__":
    while True:
        main()







