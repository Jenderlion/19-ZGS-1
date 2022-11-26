def main():
    last_names = [
        'Ульяшина', 'Русович', 'Луговская', 'Захарова', 'Нехай', 'Козловская', 'Страх', 'Мишук', 'Барткявичюте',
        'Самолазов', 'Владыко', 'Богдевич', 'Роговенко', 'Кононович', 'Горбатюк', 'Климашевская', 'Юнчиц', 'Рабцевич',
        'Соловьёва', 'Филютчик', 'Якутович'
    ]
    _last_names_dict = {_last_name: [] for _last_name in last_names}  # генерируется словарь фамилий
    questions = {str(i) for i in range(1, 61)}  # генерируется список вопросов
    reserve = 4  # количество резервных вопросов
    reserve = [questions.pop() for _ in range(reserve)]  # резервные вопросы убираются из общего списка
    average_integer_questions_per_last_name = len(questions) // len(last_names)  # минимальное количество вопросов на человека

    for last_name, _list in _last_names_dict.items():  # распределяется минимальное количество вопросов
        for _ in range(average_integer_questions_per_last_name):
            _list.append(questions.pop())

    if questions:  # если остались нераспределённые вопросы...
        _last_names = {_last_name for _last_name in _last_names_dict}
        while questions:  # распределить остаток на везунчиков
            lucky = _last_names.pop()
            _last_names_dict[lucky].append(questions.pop())

    output_list = []
    for last_name, _list in _last_names_dict.items():  # вывести список фамилий с вопросами
        _list = [int(i) for i in _list]
        _list.sort()
        _list = [str(i) for i in _list]
        output_list.append(f'{last_name} {" ".join(_list)}')
    output_list.sort()

    print('\n'.join(output_list))
    print(f'\nОсталось в резерве: {" ".join(reserve)}')  # вывести резерв


if __name__ == '__main__':
    main()
