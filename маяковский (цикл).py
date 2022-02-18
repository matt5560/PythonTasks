line = ("И волны клянутся всеводному Цику  оружие бурь до победы не класть.")

text = (line.split(" "))

for i in range (len(text)):
    if text[i] != " ":
        print(text[i])
