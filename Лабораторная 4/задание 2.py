def get_count_char(main_str):
    dictionary = {}
    for letter in main_str:
        if letter.isalpha():
            letter = letter.lower()
            if dictionary.get(letter):
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
    return dictionary

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

def second(dictionary,main_str):
    dictionary2 = {}
    mainlen = sum(dictionary.values())
    for letter, counts in dictionary.items():
        dictionary2[letter] = counts/mainlen * 100
    return dictionary2

print(get_count_char(main_str))