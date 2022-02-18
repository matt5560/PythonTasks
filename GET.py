import re

line = input()
link = "https://yandex.ru/images/search?text=КОТЁКИ&source=images_drawing"

print("looking for '%s' '%s' " % (line, link), end='')

print (re.search('text=([а-яёЁ А-Я]+)\W?\s?', link)[1])

