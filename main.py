from prerequisite import prerequisites, restart_prompt, pip_packages
from mysql import mysql_conf, mysql_secure_installation
from production import production_commands, domain_commands, ssh_commands
import os, click
from frappe_init import frappe_install
from production import site


def main():
    # remove prompts
    os.system(restart_prompt)

    # prerequisite
    for prerequisite in prerequisites:
        os.system(f"sudo apt install -y {prerequisite}")
    for package in pip_packages:
        os.system(package)

    # mysql
    mysql_secure_installation()
    mysql_conf()

    # frappe-init
    frappe_install()

    # production
    os.chdir('./frappe-bench/')
    commands = production_commands + domain_commands + ssh_commands
    for command in commands:
        os.system(command)
    os.system(f'bench setup add-domain {site}')

    # Success
    click.echo(click.style('Frappe installation completed successfully!', fg='green', bold=True))

if __name__ == "__main__":
    main()
