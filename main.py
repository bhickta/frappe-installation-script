from prerequisite import prerequisites, restart_prompt, pip_packages, node
from mysql import mysql_conf, mysql_secure_installation
from production import production_commands, domain_commands, ssh_commands
import os, click, subprocess

def main():
    # remove prompts
    os.system(restart_prompt)

    # prerequisite
    for prerequisite in prerequisites:
        os.system(f"sudo apt install -y {prerequisite}")
    for package in pip_packages:
        os.system(package)
    for command in node:
        subprocess.call(command, shell=True)

    # mysql
    mysql_secure_installation()
    mysql_conf()

    # production
    for production_command, domain_command, ssh_command in zip(production_commands, domain_commands, ssh_commands):
        os.system(production_command)
        os.system(domain_command)
        os.system(ssh_command)

    click.echo(click.style('Frappe installation completed successfully!', fg='green', bold=True))

if __name__ == "__main__":
    main()
