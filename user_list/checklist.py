#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def checklist_users(users):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format('-' * 4,
                                          '-' * 20,
                                          '-' * 18,
                                          '-' * 10)
    print(line)
    print('| {:^4} | {:^20} | {:^18} | {:^10} |'.format(
        '№',
        'Название',
        'Номер телефона',
        'Дата'
    ))
    print(line)

    for idx, user in enumerate(users, 1):
        print(
            '| {:^4} | {:^20} | {:^18} | {:^10} |'.format(
                idx,
                user['name'],
                user['phone_number'],
                ' '.join(map(str, user['year']))
            )
        )
        print(line)
