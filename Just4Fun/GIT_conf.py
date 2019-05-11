import os

email = input('email: ')

name = 'Dewaldman'

os.system('git config --global user.email {}'.format(email))

os.system('git config --global user.name {}'.format(name))
