from decouple import config
from dataclasses import dataclass


@dataclass
class Config:
    frappe_user = config("FRAPPE_USER")
    site_name = config("SITE_NAME")
    db_name = config("DB_NAME")
    db_password = config("DB_PASSWORD")
    apps = {
        "payments": " --branch develop payments",
        "erpnext": "--branch version-14 erpnext",
        "hrms": "--branch develop hrms",
        "india_compliance": "--branch version-14 https://github.com/resilient-tech/india-compliance.git",
        "ecommerce_integrations": "ecommerce_integrations --branch main",
        "raplbaddi": "git@github.com:bhickta/raplbaddi.git",
        "helpdesk": "helpdesk",
        "insights": "--branch develop insights",
    }
    prod_dependencies = [
        "mariadb-server",
        "mariadb-client",
        "redis-server",
        "supervisor",
        "curl",
        "git",
        "python3-dev",
        "python3.10-dev",
        "python3-setuptools",
        "python3-pip",
        "python3-distutils",
        "python3.10-venv",
        "software-properties-common",
        "xvfb",
        "libfontconfig",z
        "wkhtmltopdf",
        "libmysqlclient-dev",
        "certbot",
    ]
    append = '''
    # Frappe
    [mysqld]
    character-set-client-handshake = FALSE
    character-set-server = utf8mb4
    collation-server = utf8mb4_unicode_ci

    [mysql]
    default-character-set = utf8mb4
    '''