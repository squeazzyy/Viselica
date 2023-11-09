word_to_guess = input("Введите слово: ")
print("\n" * 40)
unsuccessful = 0
body_parts = [
    '',
    '/',
    '/\\',
    '''|
/\\
                    ''',
    '''|
|
/\\
                    ''',
    '''|
|
|
/\\
                    ''',
    '''----
|
|
|
/\\
                    ''',
    '''----
|  o
|
|
/\\
                    ''',
    '''----
|  o
|  0
|
/\\
                    ''',
    '''----
|  o
|  0
|  0
/\\
                    '''
]
while True:
    user_word = input("Слово: ")
    if user_word != word_to_guess:
        unsuccessful += 1
    elif user_word == word_to_guess:
        print("Вы выиграли!\nИгра окончена!")
        break

    if unsuccessful < len(body_parts):
        body = body_parts[unsuccessful]
    else:
        print("Вы проиграли!\nИгра окончена!")
        break

    print(body)