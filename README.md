# Union Budget Board [CMS Module]

## Getting Started

Untill the first release, please checkout the develop branch. 

The project follows - [GitFlow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). 


### Prerequisites

[Virtualenv](https://virtualenv.pypa.io/en/stable/installation/) - Use a isolated python virtual environment. 

### Installing

#### Create a virtual environment.
```
virtualenv union-budget-board
source union-budget-board/bin/activate
pip install --upgrade pip
```

#### Clone the project. 
```
cd to/path/where/you-want-to-setup
git clone https://github.com/cbgaindia/union-budget-board.git
cd union-budget-board
```
#### Install the dependencies. 
```
pip install -r requirements.txt
```

#### Final steps
```
python manage.py migrate # Generate the schema for database.
python manage.py createsuperuser #Run the setup to create an admin.
python manage.py runserver # Fire up the server. 
```

#### Check the development branch 
```
git checkout develop
```

## Contributing

Contributing guides would be up soon. If still want to contribute and can't wait till the first release, ping the Contributors. 

## Contributors

* **Akshay Verma** - *OpenBudgetsIndia* - [akshay2905](https://github.com/akshay2905)
* **Jayant** - *OpenBudgetsIndia* - [heaven00](https://github.com/heaven00)
* **Gaurav Godhwani** - *OpenBudgetsIndia* - [gggodhwani](https://github.com/gggodhwani)
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Note
README is still in progress. A detailed documentation would soon be provided. 
