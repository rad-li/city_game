# Игра в города
В этой игре человек и компьютер по очереди называют реально существующий город, название которого начинается на ту букву, которой оканчивается название предыдущего участника. Игра продолжается пока у компьютера или игрока не закончатся варианты. Первым начинает комьютер со случайно выбранного города.

### Запуск
Скачайте все фалы и запустите файл main.py
```
python main.py
```

### Функционал
Чтобы не было повторов, список названных городов сохраняется в кэше до конца игры.

Список городов хранится в файле cities.txt. Можно заменить своим файлом с другим списком городов или списком чего-нибудь другого, например, имен известных людей.

Чтобы закончить игру, введите слово стоп вместо названия города.

### Планы
- [ ] добавить ограничение по времени ответа,
- [ ] озвучивание ответов компьтера,
- [ ] распознавание речи игрока
