""" Игра в города """
import random  # импортируем необходимые модули


city_cache = []  # список для записи названных городов, чтобы не было повторов
exclude_char = {"ь", "ъ", "ы"}  # эти буквы будем исключать из последней буквы города
city_list = []  # список известных городов


# окрываем файл с названиями городов и заносим их в список
with open('cities.txt', 'r') as f:
    for line in f:
        city_list.append(line.strip().lower())


def normalize(city_name):
    """ Функция удаляет лишние пробелы, переводит слово в нижний регистр и меняет ё на е """
    return city_name.strip().lower().replace('ё', 'е')


def get_last_letter(city_name):
    """ Функция выбирает последний символ из названия города """
    if city_name != 0:

        # Если символ в списке исключения, выбираем предпоследнюю букву
        s_end = city_name[-2] if city_name[-1] in exclude_char else city_name[-1]
        return s_end

    else:
        return False


def get_first_letter(city_name, prev_city):
    """ Функция выбирает первый символ из названия города и сравнивает с последним символом предыдущего города """

    s_start = city_name[0]  # Определяем первый символ

    # Сравниваем с последним симовлом предыдущего города
    if s_start == get_last_letter(prev_city):
        return True

    else:
        print("Не верно. Назовите город на букву", get_last_letter(prev_city))
        return False


def is_valid(city_name, prev_city):
    last_letter = get_last_letter(city_name)

    if get_first_letter(city_name, prev_city):
        if city_name not in city_list:
            print("Такого города нет")
            return False

        elif city_name in city_cache:
            print("Такой город уже был")
            return False

        elif len(city_cache) != 0 and last_letter != city_cache[-1][-1].lower() not in city_cache:
            city_cache.append(city_name)
            return True


def next_city(human, city_cache):
    filtered_list = [item for item in city_list if item.startswith(get_last_letter(human)) and item not in city_cache]

    if len(filtered_list) == 0:
        return False
    else:
        computer = random.choice(filtered_list)
        return computer


# первый город называет компьютер
computer = normalize(random.choice(city_list))

# заносим город в кеш
city_cache.append(computer)

# начниаем игру с привествия и компьютер делает ход
print("Играем в города. Что бы закончить игру скажите стоп. Я начинаю:", computer.title())

game_over = False


while not game_over:
    correct = True

    while correct is True and game_over is False:

        # игрок вводит название города
        human = normalize(input("Вам на " + get_last_letter(computer) + ": "))

        if human == "стоп":
            game_over = True
            correct = True

        elif is_valid(human, computer):
            correct = True
            del computer
            computer = next_city(human, city_cache)

            if computer:
                city_cache.append(computer)
                print(computer.title())
            else:
                print('Я больше не знаю городов на букву "' +
                      get_last_letter(human) + '". Сдаюсь, вы победили!')
                game_over = True

if game_over:
    if human == "стоп":
        print("Победил компьютер")
    else:
        print("Победил игрок")
    exit(0)
