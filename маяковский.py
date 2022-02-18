import re

line = ("И волны клянутся всеводному Цику  оружие бурь до победы не класть.")
sub = re.sub(r'\s+', '\n', line)
print(sub)
