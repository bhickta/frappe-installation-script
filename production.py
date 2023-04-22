# Variables
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
