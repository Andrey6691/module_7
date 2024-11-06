def custom_write(file_name, strings):
    file_string = open(file_name, 'w', encoding = 'utf-8')
    strings_positions = {}
    for index, string in enumerate(strings):
        n = file_string.tell()
        strings_positions[(index+1, n)] = string
        file_string.write(f'{string}\n')
    file_string.close()
    return strings_positions

info = ['Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)