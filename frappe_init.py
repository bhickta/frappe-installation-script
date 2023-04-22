import os
import click
from production import site, db_name, db_password

@click.command()
def frappe_install():
    os.system('bench init --frappe-branch version-14 frappe-bench')
    os.system('chmod -R o+rx /home/frappe')
    os.chdir('/home/frappe/frappe-bench')
    os.system(f'bench new-site {site} --db-name {db_name} --db-password {db_password}')
    
    apps = {
        'erpnext': '--branch version-14 erpnext',
        # 'hrms': '--branch version-14 hrms',
        'ecommerce_integrations':'ecommerce_integrations --branch main',
        'india_compliance':'--branch version-14 https://github.com/resilient-tech/india-compliance.git',
        'helpdesk':'helpdesk'
    }
    for k, v in apps.items():
        os.system(f'bench get-app {v}')
        print(f"{k} has been pulled")
        os.system(f'bench --site {site} install-app {k}')
        print(f"{k} has been installed")
