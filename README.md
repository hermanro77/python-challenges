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

## Git. A tool for version control.

If you are new to git and want to learn, I reccommend to create your own `branch` before you start implementing your solutions. You can create a branch for each challenge if you want.

How do I create a branch? It is simple. When you ran the `git clone` command you already initialized your repository with git. So all you need to do is use the `git` command. Here are some helpful git commands to get started that you can run in your terminal within the repository folder:

`git checkout -b challenge_1` This will create a branch called `challenge_1` \
`git status` This will give you an overview over all changes you have made to your files since you cloned the repository \
`git add .` This will stage all your changed files, making them ready to be committed \
`git commit -m "This is my first commit message"` This will commit you changed files, meaning they are recorded in a commit history containing all commits ever done within this repository. All changes made on your local computer that are commited will be ready to be pushed/sent to the cloud for you to access via internet \
`git push` This will push all commits from your local computer to the cloud, such that all the changes you made to your files are stored in the remote commit history \
`git pull` This will fetch new changes from the cloud/remote branch. In the case where one of your team memebers have made some changes to some files in this repository and pushed them, you are able to pull them into your local computer. \
