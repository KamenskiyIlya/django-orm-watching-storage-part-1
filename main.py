import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

def passcard_content(passcards):
    index = int(input('Введите индекс пропуска, по которому необходима информация: \n'))
    passcard_note = passcards[index]

    passcard_details = {
        'Имя владельца' : passcard_note.owner_name,
        'Код пропуска' : passcard_note.passcode,
        'Создан' : passcard_note.created_at,
        'Активен' : passcard_note.is_active
    }

    return passcard_details

if __name__ == '__main__':
    passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)

    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    print('Активных пропусков: ', active_passcards.count())
    
    passcard_details = passcard_content(passcards)
    for details, value in passcard_details.items():
        print(f'{details}: {value}')