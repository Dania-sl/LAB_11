'''
Дани два текстових файли f і g з однаковою кількістю рядків. Визначити чи
співпадають рядки двох файлів. Якщо ні, то отримати номер першого рядка, в якому ці
файли відрізняютсья один від одного.
'''
f = open('f.txt', 'w', encoding='utf-8')  # відкриття (створення файлу) f в режимі запису
g = open('g.txt', 'w', encoding='utf-8')  # відкриття (створення файлу) g в режимі запису
f.write(
    'Python can be easy to pick up whether you re a first time \nprogrammer or you re experienced with other languages. \nThe following pages are a useful first step to \nget on your way writing programs with Python!')
# заповнення файлу f
g.write(
    'Python can be easy to pick up whether you re a first time \nprogrammer or you re experienced with other languages. \nget on your way writing programs with Python! \nThe following pages are a useful first step to ')
# заповнення файлу g
f.close()
g.close()
f = open('f.txt', encoding='utf-8')  # відкриття файлу f в режичі читання
g = open('g.txt', encoding='utf-8')  # відкриття файлу g в режичі читання
c = 2  # задання зміної для підрахунку рядку в якому вірізняється перший рядок
x = True  # залання зміної для відображення подібності файлів
for row_f in f:  # перебірп ярдків файлу f
    for row_g in g:  # перебір рядків файлу g
        if row_f == row_g:  # порівняння рядків з файлів
            c += 1
        else:
            x = False  # якщо  рядки відрізняються то змінна змінюж своє значення
            break
if c > 2:
    print(c)
print(x)
