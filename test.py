from production import production_commands, domain_commands, ssh_commands

commands = production_commands + domain_commands + ssh_commands

print(commands)