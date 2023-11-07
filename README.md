# Python Challenges
Welcome to these small Python challenges!!
 
You can find all the challenges in the `challenges` folder. 
The solution can be found in the `.solution` folder. But this should only be used if you are really stuck, try and solve the tasks by googling yourself. This is the best way to learn a new programming language. 

Furthermore, all challenges can be tested via unit tests in the `tests` folder. 
By running these you know if you found the correct solution. See below for how to run the tests.

## Setup

### Make sure to have Python installed with pip

First check if you already have pytehon and pip with `python --version` and `pip --version`

If you don't have it installed you can use Homebrew, a package manager for Mac, to easily install Python with pip

1. To install Homebrew, run `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` in your terminal
2. To install Python, run `brew install python` in your terminal


### How to clone this repositry

1. Make a folder where you would like to copy/clone this repository into. You can create a folder from the terminal with `mkdir MyFolder`
2. Run `git clone https://github.com/hermanro77/python-challenges.git` in your terminal in a folder you would like to clone this repository 


## Test your solutions
After you have implemented a solution for your first task, you can find out if it is a correct solution to the challenge by running the corresponding test.

`python main.py` will run all unit tests for all challenges at once.

### Testing with Intellij/Pycharm
If you want to run the test specifically for one challenge after implementing your solution you can run the tests in intellij from the interface by clicking the green execute test button in the file.

### Testing with other IDEs or text editors
If you are using another IDE than Intellij the following approach is recommended:

Install `pytest` with pip by:

`pip install pytest`

Execute a test with for example:

`pytest path_to_test_to_execute.py` 
