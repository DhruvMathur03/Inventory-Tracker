# Shopify Challenge Summer 2022

## Requirements

This project is made using Python and HTML
It requires the following libraries/modules :

-flask
-Flask-SQLAlchemy
-Flask-Testing

This project works on a virtual environment (venv in this case)

Create a virtual environment with venv :
```
python3 -m venv <name-of-virtual-environment>
```
Activate the virtual environment :
```
source <name-of-virtual-environment>/bin/activate
```
Deactivate the virtual environment :
```
deactivate
```

## Installation : 
Installing Python on MacOS :

First you'll need Xcode on your Mac, you might already have it, if not then you can get it from the app store
[Xcode](https://apps.apple.com/us/app/xcode/id497799835?ls=1&mt=12)

Now you will need to install homebrew :
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Your terminal will ask for Super User level access, which means you'll need to type your password to run this command.

Finally you can install python3 :
```
brew install python3
```

Installing Python on Windows :

-Navigate to [Python Downloads for Windows](https://www.python.org/downloads/windows/) and install 
 your desired version of python3 (Python 3.10.1 in this case)
-Run the executable installer(select install for all Users and Add Python to PATH checkboxes)
-Verify installation by navigating to the directory in which Python was installed, and then double clicking 'python.exe'
-OR you could go to command prompt, navigate to said directory, and entering 'python3'


Install with pip3 in the virtual environment:

Virtual Environment :
```
pip3 install virtualenv
```
Flask : 
```
pip3 install flask
```
SQLALchemy : 
```
pip3 install -U Flask-SQLAlchemy
```
Flask-Testing : 
```
pip3 install Flask-Testing
```

## Flask-SQLAlchemy server Configuration :

```
app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inv_tracker.db'
db = SQLAlchemy(app)
```

## Flask-SQLAlchemy test Configuration :

```
app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inv_tracker.db'
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False
```

## Run Flask 

```
python3 server.py
```

## Run Tests

```
python3 test.py
```