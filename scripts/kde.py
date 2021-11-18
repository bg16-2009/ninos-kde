import pacman
import os

def install_kde():
    print("Installing kde.......")
    pacman.install(["xorg", "plasma", "plasma-wayland-session", "kde-applications", "networkmanager"])
    print("Configuring kde........")
    os.system("systemctl enable sddm.service")
    os.system("systemctl enable NetworkManager.service")
