import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

def passcard_content(passcards):
    index = int(input('Введите индекс пропуска, по которому необходима информация: \n'))
    passcard_note = passcards[index]
    print(f'owner_name: {passcard_note.owner_name}')
    print(f'passcode: {passcard_note.passcode}')
    print(f'created at: {passcard_note.created_at}')
    print(f'is_active: {passcard_note.is_active}')
    return

if __name__ == '__main__':
    passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)

    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    print('Активных пропусков: ', len(active_passcards))
    passcard_content(passcards)