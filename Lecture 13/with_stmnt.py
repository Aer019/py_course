
import os
os.getcwd()

fstream = open('my_first_txt_file.txt', 'w')

try:
    fstream.write('1 Привет мир!\n')
    fstream.write('2 Привет мир!\n')
    fstream.write('3 Привет мир!\n')
    fstream.write('4 Привет мир!\n')
    fstream.write('5 Привет мир!\n')
    fstream.write('6 Привет мир!\n')
except:
    print('up')
finally:
    fstream.close()


with open('my_second_txt_file.txt', 'w') as fstream:
    fstream.write('1 Привет мир!\n')
    fstream.write('2 Привет мир!\n')
    fstream.write('3 Привет мир!\n')
    fstream.write('4 Привет мир!\n')
    fstream.write('5 Привет мир!\n')
    fstream.write('6 Привет мир!\n')
    