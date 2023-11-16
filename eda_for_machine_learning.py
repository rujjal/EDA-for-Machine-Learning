# -*- coding: utf-8 -*-
# """EDA for Machine Learning.ipynb

# # **Retrieving Data from CSV and JSON files**

# ### Reading CSV files

# Comma - Separated Values
# """

import pandas as pd
filepath = 'data/irish_data.csv'

#import the data
data = pd.read_csv(filepath)
data.head()

print(data.ilco[:5])

#different delimiters - tab-separated files
data = pd.read_csv(filepath, sep='\t')

#different delimiters - space-separated files
data = pd.read_csv(filepath , delim_whitespace=True)

#Don't use first row for column names
data = pd.read_csv(filepath, header = None)

#custom missing values
data = pd.read_csv(filepath, na_values=['NA', 99])

# """###JSON files

# JavaScript Object Notation
# - similar in structure to pyhton dictionaries
# """

#Read JSON files dataframe
data = pd.read_json(filepath)

#write dataframe file to JSON
data.to_json('outputfile.json')

# """# **Retrieving Data from Databases, APIs and the cloud**

# ###**SQL Databases**


# -Microsoft SQL Server
# -Postgres
# -MYSQL
# -AWS RedShift
# -Oracle DB
# -Db2 family

# **Reading SQL Data**

# using sqlite3
# """

#SQL Data imports
import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd

#Initialize path to SQLite database
path = 'data/classic_rock.db'

# Download the database
# !wget -P data https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/classic_rock.db

#Create connection SQL database
con = sq3.connection(path)       # require credentials

#Write query
query = '''SELECT * from rock_songs'''

#Execute query
data = pds.read_sql(query, con)

# """###**NOSQL Databases**

# Not-only SQL (NOSQL) databases are not relational, vary more in structure.

# Most NOSQL databases are stored in JSON format.

# Examples of NOSQL Databases:


# *   document databases - mongoDB, couchDB
# *   key-value stores - Riak, Voldemort, Redis
# *   Graph databases - HyperGraph
# *   WIde-column stores - Cassandra, HBase


# **Reading NOSQL Data**

# example using pymongo module to read file stored in MongoDB.
# """

#SQL data imports
from pymongo import MongoClient

#Create a mongo connection
con = MongoCLient()

#Choose databases (con.list_database_name() will display available databases)
db = con.database_name

#Create a cursor object using a query
cursor = db.collection_name.find(query)

#Expand cursor and construct DataFrame
df = pd.DataFrame(list(cursor))

# """# **APIs and Cloud Data Access**

# A variety of data providers make data available from Application Programming and Interfaces(APIs).

# An online available example is the UC Irvine MAchine Learning Library.
# """

#UCI car data set - url location
data_url = 'URL'

#Read data into pandas
df = pd.read_csv(data_url, header=None)









