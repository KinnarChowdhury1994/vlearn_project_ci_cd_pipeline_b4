#! /bin/sh
REPO="vlearn_project_ci_cd_pipeline_b4"
cd /home/kinnar/deployment/
ls -la
cd .venv/bin && source activate
cd ../.. && pwd && ls
cd $REPO
ls 
pip3 install -r requirements.txt
pip3 list
echo "Executing automate.py from Shell"
python3 automate.py
echo "_cronScript Executed Successfully."