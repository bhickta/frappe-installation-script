from server.setup import Setup
from config.config import Config


def main():
    Setup(Config).setup()
    # mysql_secure_installation()
    # mysql_conf()

    # # frappe-init
    # frappe_install()


if __name__ == "__main__":
    main()
