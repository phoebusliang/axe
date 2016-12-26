
# Prerequisites

You will need the following things properly installed on your computer.

### Homebrew (Mac)

* [Python](https://www.python.org/) (3.5) - `brew install python3`

* NodeJS - `brew install nodejs`

### FBSimulatorControl and WebDriverAgent

* Download the FBSimulatorControl(https://github.com/facebook/FBSimulatorControl) and WebDriverAgent (https://github.com/facebook/webdriveragent)

### Python / Prerequisites

(Pip3 install: download and `python3 get-pip.py`(which may require administrator access) to install)

* In `axe` folder: `pip3 install -r tests/python/requirements.txt`

# Running iOS Automation Tests with Python's "Behave" Framework

* sh *setup.sh*

* Go to `axe` folder and start the production `npm start`(if you didn't do that)

* In `axe` folder and execute command `python3 -m behave tests/python --tags=complete --junit --format pretty -k --no-skipped --no-capture`
