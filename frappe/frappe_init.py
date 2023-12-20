import os
from config.config import Config
import subprocess


class FrappeInit:
    def __init__(self) -> None:
        self.config = Config

    def frappe_install(self):
        os.system("bench init --frappe-branch version-14 frappe-bench")
        os.system("chmod -R o+rx /home/frappe")
        os.chdir("/home/frappe/frappe-bench")
        os.system(
            f"bench new-site {self.config.site_name} --db-name {self.config.db_name} --db-password {self.config.db_password}"
        )

        for k, v in self.apps.items():
            os.system(f"bench get-app {v}")
            print(f"{k} has been pulled")
            os.system(f"bench --site {self.site} install-app {k}")
            print(f"{k} has been installed")

class DATABASE:
    def __init__(self) -> None:
        self.append = Config.append

    def mysql_secure_installation(self):
        subprocess.call(['sudo','mysql_secure_installation'])

    def mysql_conf(self):
        subprocess.call(['sudo', 'sh', '-c', f'echo "{self.append}" >> /etc/mysql/my.cnf'])

    def restart_mysql_server(self):
        subprocess.call(['sudo', 'service', 'mysql', 'restart'])
