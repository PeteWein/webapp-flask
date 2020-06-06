#from project root for windows machine (powershell):
# .\webapp-flask\utils\run_app.ps1

# load a virtualenv
pipenv --rm
pip install --user pipenv

# ensure dependencies downloaded
pipenv install -r requirements.txt --python 3.7.7

# run app
#pipenv run python .\app.py
pipenv run python .\webapp-flask\app.py