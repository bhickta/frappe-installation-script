import subprocess

subprocess.run(['sudo', 'swapon', '--show'])
subprocess.run(['free', '-h'])
subprocess.run(['df', '-h'])
subprocess.run(['sudo', 'fallocate', '-l', '5G', '/swapfile'])
subprocess.run(['ls', '-lh', '/swapfile'])
subprocess.run(['sudo', 'chmod', '600', '/swapfile'])
subprocess.run(['sudo', 'mkswap', '/swapfile'])
subprocess.run(['sudo', 'swapon', '/swapfile'])
subprocess.run(['sudo', 'swapon', '--show'])
subprocess.run(['free', '-h'])

subprocess.run(['sudo', 'cp', '/etc/fstab', '/etc/fstab.bak'])
subprocess.run(["echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab"], shell=True)

with open('/etc/sysctl.conf', 'a') as file:
    file.write('\n#Swap\nvm.swappiness=10\nvm.vfs_cache_pressure=50\n')