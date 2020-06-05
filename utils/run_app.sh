#from root for mac/linux (terminal):
# sh ./utils/run_app.sh

# load a virtualenv
pip install --user pipenv

# ensure dependencies downloaded
pipenv install -r requirements.txt --python 3.7.7

# run app
pipenv run python ./src/app.py