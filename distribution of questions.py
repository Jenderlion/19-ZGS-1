import sys
import unicodedata


def generate(last_names_dict: dict, prepared_questions_list: dict, reserv: int = 4) -> str:
    _names = []
    _generated_questions = {}
    for name in last_names_dict:
        if last_names_dict[name]:
            _names.append(name)
    _numbers = set([i for i in prepared_questions_list.keys()])
    min_q = int((len(_numbers) - reserv) / len(_names))
    for name in _names:
        _names_numbers = []
        for _ in range(min_q):
            _names_numbers.append(_numbers.pop())
        _generated_questions[name] = _names_numbers

    to_add = len(_numbers) - reserv
    _names = set(_names)
    while to_add != 0:

        _cur_name = _names.pop()
        _generated_questions[_cur_name].append(_numbers.pop())

        to_add -= 1

    if reserv:
        _generated_questions['В резерве'] = [i for i in _numbers]

    for name, numbers in _generated_questions.items():
        _generated_questions[name] = sorted([int(i) for i in numbers])
        normalized_questions = []
        for num in _generated_questions[name]:
            normalized_questions.append(f'{num}. {prepared_questions_list[str(num)]}')
        _generated_questions[name] = normalized_questions

    strings = []
    for name, questions_list in _generated_questions.items():
        _string = [f'{name}:', ]
        [_string.append(question) for question in questions_list]
        strings.append('\n'.join(_string))
    _return = '\n\n'.join(strings)
    return _return


def get_names_dict() -> dict:
    _dict = {
        'Богдевич': False,
        'Борисевич': False,
        'Владыко': True,
        'Глушакова': False,
        'Горбатюк': True,
        'Захарова': False,
        'Климашевская': False,
        'Козловская': True,
        'Кононович': True,
        'Луговская': True,
        'Мельник': False,
        'Мишук': True,
        'Мурашко': False,
        'Нехай': False,
        'Овсянников': True,
        'Павлович': True,
        'Рабцевич': True,
        'Роговенко': True,
        'Русакова': True,
        'Русович': True,
        'Самолазов': False,
        'Сельвеструк': False,
        'Соловьёва': True,
        'Странадкина': True,
        'Страх': True,
        'Ульяшина': False,
        'Шевчик': True,
        'Юнчиц': True,
        'Якутович': True,
        'Янушкевич': True,
    }
    return _dict


def get_questions_list(file_name) -> dict:
    with open(file_name, 'r', encoding='utf-8') as o_f:
        lines = o_f.readlines()
    _dict = {}
    for line in lines:
        number = line.split('.')[0]
        question = '.'.join(line.split('.')[1:])
        question = question.strip()
        _dict[number] = question
    return _dict


def format_questions(file_name):
    with open(file_name, 'r', encoding='utf-8') as o_f:
        lines = o_f.readlines()
    _lines = []
    for line in lines:
        line = line.replace('.', '. ')
        line = unicodedata.normalize('NFKD', line)
        line = line.replace('\n', '')
        line = line.replace('\t', '')
        line = line.strip()
        while '  ' in line:
            line = line.replace('  ', ' ')
        if line in ('\n', ''):
            continue
        _lines.append(line)
    with open(file_name, 'w', encoding='utf-8') as n_f:
        to_write = '\n'.join(_lines)
        n_f.write(to_write)


def write_answer(file_name: str, answer: str):
    destination_name = f'Распределение {file_name}'
    with open(destination_name, 'w', encoding='utf-8') as o_f:
        o_f.write(answer)


if __name__ == '__main__':
    clear_questions = True
    file_name = 'Ком деят.txt'
    if clear_questions:
        format_questions(file_name)
        sys.exit()
    names = get_names_dict()
    questions = get_questions_list(file_name)
    answer = generate(names, questions)
    write_answer(file_name, answer)
    print(answer)
