#from root for mac/linux (terminal):
# sh ./webapp-flask/utils/run_app.sh

# load a virtualenv
pipenv --rm
pip install --user pipenv

# ensure dependencies downloaded
pipenv install -r requirements.txt --python 3.7.7

# run app
pipenv run python ./webapp-flask/app.py