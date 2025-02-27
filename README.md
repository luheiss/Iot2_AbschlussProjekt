# Iot2_AbschlussProjekt
## Install on Raspi:
- Make a new dir :
- clone the repo:
- make a .venv in the dir
- activate venv
- checkout to the interface branch:
- install the requirements.txt
- in ordner: sudo chmod +x start_script.sh
- lege das script an: sudo nano /etc/systemd/system/projekt_beerpong.service
- [Unit]
Description=Projekt BeerPong Autostart
After=network.target

[Service]
ExecStart=/bin/bash /home/ParryHotter/ProjektBeerPong/start_script.sh
WorkingDirectory=/home/ParryHotter/ProjektBeerPong
StandardOutput=inherit
StandardError=inherit
Restart=always
User=ParryHotter

[Install]
WantedBy=multi-user.target

- script bei start aktivieren: sudo systemctl daemon-reload
sudo systemctl enable projekt_beerpong
sudo systemctl start projekt_beerpong

