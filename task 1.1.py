# Есть строка с перечислением песен
# my_favorite_songsmy_favorite_songs  ='Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'


# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
my_favorite_songs = "Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Solvation"
print(len(my_favorite_songs))
print(my_favorite_songs[0:14], my_favorite_songs[63::], my_favorite_songs[15:30], my_favorite_songs[50:62])