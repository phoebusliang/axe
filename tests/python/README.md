
## Prerequisites

You will need the following things properly installed on your computer.

### Homebrew (Mac)

* [Python](https://www.python.org/) (3.4) - `brew install python3`
* ChromeDriver = `brew install chromedriver`
* NodeJS - `brew install nodejs`

### Node packages

* `npm install -g mountebank`

### Python / Prerequisites

(Pip3 install: download and `python3 get-pip.py`(which may require administrator access) to install)

* `pip3 install -r tests/webdriver/requirements.txt`

## Running WebDriver Tests with Python's "Behave" Framework

You will need to install required Python package and download chrome driver at first.

* Go to `pv_frontend/app` folder and start the production `npm start`(if you didn't do that)
* Back to `pv_frontend` fold and execute command `python3 -m behave tests/webdriver --tags=complete --junit --format pretty -k --no-skipped --no-capture`
