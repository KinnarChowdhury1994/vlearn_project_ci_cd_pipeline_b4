#! /bin/bash

cd /home/ubuntu/repo/
ls
cd vlearn_project_ci_cd_pipeline_b4
ls -la
git pull
git branch
ls
git checkout main
git pull
rm -rf /var/www/html/*
cp -r index.html /var/www/html/

sudo systemctl restart nginx

echo "Thank You Deployment Completed"
