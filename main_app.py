from flask import Flask, render_template, request, url_for, redirect,session, flash
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from sqlalchemy import create_engine
from sqlalchemy.sql import exists

app= Flask(__name__)

# Base Configration
# app.config.from_object('config.BaseConfig')

#Development config
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

class RealEstate(db.Model):
	__tablename__='realestate'
	MLS=db.Column('MLS',db.Integer, primary_key=True)
	Location=db.Column('Location',db.Text)
	Price=db.Column('Price',db.Float)
	Bedrooms=db.Column('Bedrooms',db.Integer)
	Bathrooms=db.Column('Bathrooms',db.Integer)
	Size=db.Column('Size',db.Integer)
	Pricesq=db.Column('Pricesq',db.Float)
	Status=db.Column('Status',db.Text)

	def as_dict(self):
		return {'Location':self.Location}

engine=create_engine('mysql+pymysql://username:password@localhost/database')
table_name='realestate'

'''-------------------
home page to display all properties
-------------------'''

@app.route('/')
def index():
	homes=RealEstate.query.all()
	# result= RealEstate.query.filter_by(Location='city').all()
	return render_template('index.html',myhomes=homes)


'''-------------------
Single search option with only search and display properties by their city name
-------------------'''

@app.route('/regular_search',methods=['POST',"GET"])
def regular_search():
	location=request.form['location']
	homes=RealEstate.query.filter_by(Location=location).all()
	if not homes:
		flash("Sorry No Result Found")
		return redirect(url_for('index'))
	return render_template('index.html',homes=homes)


'''-------------------
helper function to check whether city name exists or not using jquery
---------------------'''

@app.route('/check')
def check():
	res = RealEstate.query.all()
	list_con = [r.as_dict() for r in res ]
	a=[i for n, i in enumerate(list_con) if i not in list_con[n + 1:]]
	return jsonify(a)

'''-------------------
Advance search option to check property by city name and number of bedrooms
-------------------'''

@app.route('/search',methods=['POST','GET'])
def search():
	loc=request.form['location']
	rooms=request.form['bedrooms']
	
	df=pd.read_sql_table(table_name,engine)

	df1=df[(df['Location']==loc) & (df['Bedrooms']==int(rooms))][['Price','Bedrooms']]
	dataframe_length = len(df1)
	if not dataframe_length:
		flash("Sorry No Result Found")
		return redirect(url_for('index'))
	if dataframe_length >= 2:
		img=io.BytesIO()
		fig,axes=plt.subplots(figsize=(14,10))
		sns.distplot(df1['Price'])
		plt.plot()
		plt.savefig(img,format='png')
		img.seek(0)
		final=base64.b64encode(img.getvalue()).decode()
		return render_template('index.html',final=final,data=df1)
	else:
		return render_template('index.html',data=df1)


if __name__=='__main__':
	app.run()







