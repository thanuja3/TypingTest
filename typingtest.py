"""Typing Test""" 

from time import time

print('press enter to start typing')
print('Also can use enter to go to the next line')
print('press enter twice to exit the typing test')

input('-------------')


start = time()

text =[]
while True:
    line = input()
    if not line:
        break
    text.append(line)

end = time()

print('------------')

time_taken = (end-start) /60
char_count = sum(len(item) for item in text)
words_count = char_count /4

wpm = round(words_count/time_taken)
print(f'Average wordperminute is {wpm}')
