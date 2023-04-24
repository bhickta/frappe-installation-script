import os
import click

site = input("Enter your site domain name without https or https \n")
user = input("Enter user name that will use frappe \n")
db_name = input("Enter database name \n")
db_password = input("Enter your database password \n")

domain_commands = [
    f'bench setup add-domain {site}',
    'bench setup nginx',
    'sudo service nginx reload'
]

for command in domain_commands:
    os.system(command)