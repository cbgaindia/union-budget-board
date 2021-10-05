# Union Budget Explorer

## Background

### Union Budget of India

Every year on February 1, the Finance Minister of the Republic of India gives a budget speech and submits the Annual Financial Statement to the Parliament for the upcoming financial year. These documents are a reflection of the values and priorities of the government and the people they represent. Littered across several hundreds of documents, these are often difficult to find, access, download, analayse and consume. Citizens of India are expected to go through these highly technical documents in a short span of time to be able to engage with their parliamentary representatives before it gets approved. 

![budget_cycle](https://user-images.githubusercontent.com/64309749/135972021-fbffff2c-a271-4241-9eff-2c8075293f78.png)

### Open Budgets India initiative

Open Budgets India initiative was born out of the necessity to ensure easy access to these vital documents. The platform has more than 15,600 budget documents from across the country making it India’s largest open repository of fiscal information. While the platform houses several thousands of important documents, gleaning meaning and insights out of it often requires specialised knowledge about India’s fiscal infrastructure. 

![CivicDataLab_ Srishti Masterclass - Mapping Data for Change (1)](https://user-images.githubusercontent.com/64309749/135971973-6e3eeb56-a470-44cb-8cc1-36305bfd8d3b.png)

### Union Budget Explorer

This explorer solves the key problems faced by citizens as they try to navigate budget documents - find, access, download, analyse and consume the budget data in an easy to understand manner. With the help of data visualisations, citizens can understand the differences between the promises made by the government (i.e. the budget estimates and revised estimates) & the eventual realisations of such promises (i.e. the actuals). 

#### Key Sections of Union Budget Explorer

1. Budget Profile: This section presents the comprehensive money flow data of the Union Budget. It presents both the sources of revenue of the Union Government and the expenditure commitments it has made. 

![chrome_0DzQO19waA](https://user-images.githubusercontent.com/64309749/135971894-320742cb-de21-4091-b0c5-b0c15f4f6ad1.png)

2. Budget Summary: This section provides a small snapshot of the expenditure (spending) and receipts (income) of the union government. 

![chrome_gZSVyZW8WX](https://user-images.githubusercontent.com/64309749/135971914-bff74ab3-7419-4fec-afa0-12bd8d62986c.png)

3. Expenditure (Ministry & department-wise): This section presents the ministry-wise and department-wise allocations presented in the Union Budget. It provides a comprehensive searchable table to find expenditure by more than 100 ministries and departments. 

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
