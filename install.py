import os
import sys
from scrpits.kde import install_kde

check= input("Have you read the README file? [y/n]")
if(check.lower()=="n"):
    print("You must read the README file")
    sys.exit()
else:
    precaution = input("Are you sure you want to install NINOS?[y/n]")
    if(precaution.lower()=="n"):
        print("Abort...........")
        sys.exit()
    else:
        print("Installing NINOS......")
        print("What type of install do you want?")
        print("[1] Full (Recomanded)")
        print("[2] Custom")
        install=input("[?] -> ")
        if(install != "1" and install != "2"):
            print("Abort.........")
            sys.exit()
        if(install=="1"):
            install_kde()
        else:
            print("Custom install isn't supported yet.")


        