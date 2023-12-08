apt-get update -y
apt-get install python3 python3-pip -y 
python3 -m pip install virtualenv
python3 -m venv env
env/bin/python3 -m pip install -r requirements.txt
