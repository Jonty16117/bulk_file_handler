#!/bin/bash
#run "dos2unix ./installer.sh" after editing this file in windows or dos environment
chmod +x main.py
mv main.py main
mkdir -p ~/bin
cp main ~/bin
export PATH=$PATH":$HOME/bin"
echo 'export PATH=$PATH":$HOME/bin"' >> .profile
source .profile
echo "Install Successfull!..."