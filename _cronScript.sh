#! /bin/sh
cd /home/kinnar/deployment/
ls -la
cd .venv/bin && source activate
cd ../.. && pwd && ls
cd automation
pip3 install -r requirements.txt
python3 automate.py
echo "Executed Successfully"