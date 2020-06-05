#from root for windows machine (powershell):
# .\utils\run_app.ps1

# load a virtualenv
pip install --user pipenv

# ensure dependencies downloaded
pipenv install -r requirements.txt --python 3.7.7

# run app
pipenv run python app.py