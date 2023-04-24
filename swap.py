import os

def add_swap():
    os.system('sudo swapon --show')
    os.system('free -h')
    os.system('df -h')
    os.system('sudo fallocate -l 5G /swapfile')
    os.system('ls -lh /swapfile')
    os.system('sudo chmod 600 /swapfile')
    os.system('sudo mkswap /swapfile')
    os.system('sudo swapon /swapfile')
    os.system('sudo swapon --show')
    os.system('free -h')
    os.system('sudo cp /etc/fstab /etc/fstab.bak')
    os.system('echo "/swapfile none swap sw 0 0" | sudo tee -a /etc/fstab')
    os.system('sudo sh -c "echo \'\n#Swap\nvm.swappiness=10\nvm.vfs_cache_pressure=50\' >> /etc/sysctl.conf"')