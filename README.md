# Flask_data_analysis
This application used data sets stored at mysql. It will pull the requested data and display graph using Matplotlib, Pandas and Seaborn. 

## Step 1:
Create a folder.

$ mkdir realestate_graph

Create a virtual enviroment. 

$pip install virtualenv

$ cd realestate_graph

$ virtualenv env

$ source env/bin/activate

## Step 2:
Install requirements.txt

$pip install -r requirements.txt

## Step 3:
Edit config.py with database credentials.

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/database'

## Step 4:
Edit main_app.py with database credentials.

engine=create_engine('mysql+pymysql://username:password@localhost/database')

## Step 5:
Create a MySQL database "houseprice" and table "realestate" in our case.

CREATE TABLE `realestate` (
  `MLS` int(11) DEFAULT NULL,
  `Location` text,
  `Price` double DEFAULT NULL,
  `Bedrooms` int(11) DEFAULT NULL,
  `Bathrooms` int(11) DEFAULT NULL,
  `Size` int(11) DEFAULT NULL,
  `Pricesq` double DEFAULT NULL,
  `Status` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

## Step 6:
Run project.

$ python main_app.py
