# Publicis Sapient Engineering QA Technical Exercise
Implement a Test Automation Framework using the tool of your choice that allows you to: 
-Write the scenarios in Gherkin from a Google keyword search;
-Do the implementation of the scenario Gherkin steps;
-Explain how to set up a build in the CI to run the tests and how to integrate it into the product deployment process;
-Document the setup in the README 
 
## Getting started

These instructions allow you to obtain a copy of the project to test it on your machine.

### Prerequisites

As the program is written in Python, it is essential that it is installed on your machine. You can download Python:
* [Download Python](https://www.python.org/downloads/)  

### Installation

In order not to conflict with other existing projects, it is best to run the program in a virtual environment.
Here are the main commands for :

1. Creating a virtual environment 

mac/linux : ```sudo pip3 install pipenv```
windows : ```pip install pipenv ```

2. Activate the virtual environment

windows/mac/linux : ```pipenv shell```

3. Install python module : ```pip install -r requirements.txt ``` 

For more details on setting up a virtual environment, see the Python documentation
* [Python documentation](https://docs.python.org/3/search.html?q=virtual+environment)  

## Start-up

Once the console has been placed in the program features folder, simply run the following command in the virtual environment:

```behave searchingKeywords.feature```

## Development done with:
[PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) - Text editor

## Improvement point
This keyword search test can be organized in an object-oriented programming style.


## Author

* **Jean Penan Goumou** [Linkedin link](https://www.linkedin.com/in/jean-penan-goumou-78b265162/) 