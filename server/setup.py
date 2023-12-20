import os
from config.config import Config


class Setup:
    def __init__(self, config: Config) -> None:
        self.user = Config.frappe_user
        self.site = Config.site_name
        self.prod_dependencies = config.prod_dependencies
        self.pip_packages = [
            "pip3 install --upgrade --user pip",
            "sudo pip3 install frappe-bench",
        ]

    def adding_user(self):
        user = self.user
        os.system(f"sudo adduser {user}")
        os.chdir(f"/home/{user}")
        os.system(f"usermod -aG sudo {user}")
        os.system(f"su {user}")

    def install_prerequisites(self):
        for dependencies in self.prod_dependencies:
            os.system(f"sudo apt install -y {dependencies}")

    def install_pip_packages(self):
        for package in self.pip_packages:
            os.system(package)
        
    def setup(self):
        self.adding_user()
        self.install_prerequisites()
        self.install_pip_packages()


class Production:
    def __init__(self) -> None:
        self.production_commands = [
            f"bench --site {self.site} enable-scheduler",
            f"bench --site {self.site} set-maintenance-mode off",
            f"sudo bench setup production {self.site}",
            f"bench setup nginx",
            "sudo supervisorctl restart all",
            f"sudo bench setup production {self.site}",
        ]
        self.domain_commands = [
            f"bench setup add-domain {self.site}",
            "bench setup nginx",
            "sudo service nginx reload",
        ]
        self.ssh_commands = [
            "bench config dns_multitenant on",
            "bench setup nginx",
            "sudo service nginx reload",
        ]

    def setup_production(self):
        for command in self.production_commands:
            os.system(command)

    def setup_domain(self):
        for command in self.domain_commands:
            os.system(command)

    def setup_ssh(self):
        for command in self.ssh_commands:
            os.system(command)
        os.system(f"sudo -H bench setup lets-encrypt {self.site}")
