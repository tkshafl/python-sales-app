python3 -m venv /home/tusha/python-sales-app/sa-venv
source /home/tusha/python-sales-app/sa-venv/bin/activate
pip install -r /home/tusha/python-sales-app/requirement.txt
sudo supervisorctl restart cicd_demo 