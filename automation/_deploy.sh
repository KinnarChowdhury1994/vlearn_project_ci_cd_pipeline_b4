#! /bin/bash

cd /home/kinnar/deployment/repo/
ls
LOCATION="vlearn_project_ci_cd_pipeline_b4"
if [ -d $LOCATION ]
then
    echo "File LOCATION already exists"
    cd $LOCATION
    git pull
else
    echo "Creating FOLDER........"
    git clone https://github.com/KinnarChowdhury1994/vlearn_project_ci_cd_pipeline_b4.git
    cd $LOCATION
    ls -la
fi
git branch
ls -la
git checkout main
ls -la

rm -rf /var/www/html/index.html
cp -r index.html /var/www/html/

sudo systemctl restart nginx

echo "Thank You Deployment Completed"