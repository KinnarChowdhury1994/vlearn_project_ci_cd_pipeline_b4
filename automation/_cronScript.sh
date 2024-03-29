#! /bin/bash
REPO="vlearn_project_ci_cd_pipeline_b4"
HOME="/home/kinnar/deployment/"
cd $HOME
ls -la
cd .venv/bin
pwd
source activate
cd ../..
pwd
ls -la
cd $HOME/repo/$REPO/automation/
ls -la
pip3 install -r requirements.txt
pip3 list
sudo chmod +x $HOME/repo/$REPO/automation/automate.py
sudo chmod +x $HOME/repo/$REPO/automation/_deploy.sh

echo "Executing automate.py from Shell"
python3 $HOME/repo/$REPO/automation/automate.py
echo "_cronScript Executed Successfully."