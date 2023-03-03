# GeoDjango-Kenya-Counties
GeoDjango-Kenya-Counties is a project that provides geographic data for Kenya's counties. It uses GeoDjango, a geographic framework for Django, to create and manage geographic data in a web application.

## Requirements
To use GeoDjango-Kenya-Counties, you need to have the following installed on your system:

1. Python 3.x
2. Django 2.x or higher
3. GDAL
4. GeoDjango

## Installation

To install GeoDjango-Kenya-Counties, follow these steps:

1.Clone this repository to your local machine.

`git clone https://github.com/username/GeoDjango-Kenya-Counties.git`

2.Create a virtual environment and activate it.

`python3 -m venv env
source env/bin/activate
`
3.Install the required packages.
`pip install -r requirements.txt
`
5.Create a database.
`python manage.py migrate
`
7.Load the data for Kenya's counties.
`python manage.py shell`

<!-- for county -->

`from geo import county
county.run()
`
<!-- for constituency -->
`from geo import const
const.run()
`
## Usage
Once you have installed GeoDjango-Kenya-Counties, you can use it to display Kenya's counties on a map. You can also add additional features and functionality to the web application, such as searching for a specific county or displaying additional information about each county.

