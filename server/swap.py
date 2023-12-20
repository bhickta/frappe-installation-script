import subprocess


class SwapManager:
    def __init__(self, size):
        self.display_swap_info()
        self.size = size

    def display_swap_info(self):
        subprocess.run(["sudo", "swapon", "--show"])
        subprocess.run(["free", "-h"])
        subprocess.run(["df", "-h"])

    def create_swap_file(self):
        subprocess.run(["sudo", "fallocate", "-l", self.size, "/swapfile"])
        subprocess.run(["ls", "-lh", "/swapfile"])
        subprocess.run(["sudo", "chmod", "600", "/swapfile"])
        subprocess.run(["sudo", "mkswap", "/swapfile"])
        subprocess.run(["sudo", "swapon", "/swapfile"])

    def display_updated_swap_info(self):
        subprocess.run(["sudo", "swapon", "--show"])
        subprocess.run(["free", "-h"])

    def backup_fstab(self):
        subprocess.run(["sudo", "cp", "/etc/fstab", "/etc/fstab.bak"])

    def add_swap_entry_to_fstab(self):
        with open("/etc/fstab", "a") as fstab_file:
            fstab_file.write("/swapfile none swap sw 0 0\n")

    def adjust_sysctl_conf(self):
        subprocess.run(
            [
                "sudo",
                "sh",
                "-c",
                'echo -e "\n#Swap\nvm.swappiness=10\nvm.vfs_cache_pressure=50" >> /etc/sysctl.conf',
            ]
        )
