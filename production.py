# Variables
import os
site = 'dev.raplbaddi.com'
user = "frappe"
db_name = 'raplbaddi'
db_password = "Impossible.dev1@"

production_commands = [
    f'bench --site {site} enable-scheduler',
    f'bench --site {site} set-maintenance-mode off',
    f'sudo bench setup production {user}',
    f'bench setup nginx',
    'sudo supervisorctl restart all',
    f'sudo bench setup production {user}'
]
domain_commands = [
    f'bench setup add-domain {site}',
    'bench setup nginx',
    'sudo service nginx reload'
]
ssh_commands = [
    'bench config dns_multitenant on',
    'bench setup nginx',
    'sudo service nginx reload'
]

# production
commands = production_commands + domain_commands + ssh_commands
for command in commands:
    os.system(command)
os.system(f'bench setup add-domain {site}')