import subprocess

def mysql_secure_installation():
    subprocess.call['sudo','mysql_secure_installation']

def mysql_conf():
    # Define the new MySQL configuration
    append = '''
    # Frappe
    [mysqld]
    character-set-client-handshake = FALSE
    character-set-server = utf8mb4
    collation-server = utf8mb4_unicode_ci

    [mysql]
    default-character-set = utf8mb4
    '''

    # Use sudo to modify the my.cnf file
    subprocess.call(['sudo', 'sh', '-c', f'echo "{append}" >> /etc/mysql/my.cnf'])

    # Restart mysql server
    subprocess.call(['sudo', 'service', 'mysql', 'restart'])
