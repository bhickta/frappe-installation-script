# Variables
import os
import click

site = input("Enter your site domain name without https or https \n")
user = input("Enter user name that will use frappe \n")
db_name = input("Enter database name \n")
db_password = input("Enter your database password \n")

production_commands = [
    f'bench --site {site} enable-scheduler',
    f'bench --site {site} set-maintenance-mode off',
    f'sudo bench setup production {user}',
    f'bench setup nginx',
    'sudo supervisorctl restart all',
    f'sudo bench setup production {user}'
]

# production
for command in production_commands:
    os.system(command)