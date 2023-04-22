import os
import click

@click.command()
def adding_user():
    user = click.prompt('Enter Frappe User')
    click.confirm(f'Do you want to add the user with sudo access and switch to that user? {user}?', abort=True)
    os.system(f'sudo adduser {user}')
    os.chdir(f'/home/{user}')
    os.system(f'usermod -aG sudo {user}')
    os.system(f'su {user}')

if __name__ == '__main__':
    adding_user()