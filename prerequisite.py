import subprocess

# Stop restart prompt in ubuntu 22.04
restart_prompt = '''sudo sh -c "echo '$nrconf{restart} = '\''a'\'';' >> /etc/needrestart/needrestart.conf"'''

# Prequisites
prerequisites = [
    'mariadb-server', 'mariadb-client', 'redis-server',
    'supervisor',
    'curl', 'git',
    'python3-dev', 'python3.10-dev', 'python3-setuptools', 'python3-pip', 'python3-distutils', 'python3.10-venv',
    'software-properties-common',
    'xvfb', 'libfontconfig', 'wkhtmltopdf', 'libmysqlclient-dev, certbot'
]
    
# Install bench
pip_packages = [
    'pip3 install --upgrade --user pip',
    'sudo pip3 install frappe-bench',
]

def install_node():
    # Install Node.js
    subprocess.call(['curl', '-sL', 'https://deb.nodesource.com/setup_18.x', '|', 'sudo', '-E', 'bash', '-'])
    subprocess.call(['sudo', 'apt-get', 'install', '-y', 'nodejs'])

    # Install npm
    subprocess.call(['sudo', 'apt-get', 'install', '-y', 'npm'])

    # Install yarn
    subprocess.call(['sudo', 'npm', 'install', '-g', 'yarn'])
