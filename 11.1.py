'''
Дан текстовий файл f. Отримати копію цього файлу.
'''
import shutil

f = open('f.txt', 'tw', encoding='utf-8')  # стоврення файлу
f.close()

shutil.copy('f.txt', r'C:\Users\Danya\Desktop')  # копія файлу(сам файл, дерикторфя куди копіювати)
