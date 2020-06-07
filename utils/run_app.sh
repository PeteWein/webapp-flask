#from root for mac/linux (bash):
# sh ./utils/run_app.sh

# load a virtualenv
pipenv --rm
pip install --user pipenv

# ensure dependencies downloaded
pipenv install -r requirements.txt --python 3.7.7

# run app
pipenv run flask run