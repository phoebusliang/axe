
# Prerequisites

You will need the following things properly installed on your computer.

### Homebrew (Mac)

* [Python](https://www.python.org/) (3.5) - `brew install python3`

### FBSimulatorControl and WebDriverAgent

* Download the [FBSimulatorControl](https://github.com/facebook/FBSimulatorControl) and [WebDriverAgent](https://github.com/facebook/webdriveragent)

### Python / Prerequisites

(Pip3 install: download and `python3 get-pip.py`(which may require administrator access) to install)

* In `axe` folder: `pip3 install -r tests/python/requirements.txt`

# Running iOS Automation Tests with Python's "Behave" Framework

* sh *setup.sh* (You should modify uuid, bundle id or app_path for your own use)

* Go to `axe/tests/python` folder and execute command `behave tests/python/features --processes 4 --parallel-element feature --tags=complete --junit --format pretty -k --no-skipped --no-capture` to run tests as parallel
