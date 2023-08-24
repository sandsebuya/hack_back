# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask,request
from flask_restful import Resource, Api
import psycopg2

app = Flask(__name__)
api = Api(app)
@app.route("/")
def start_p():
	return "Тут ничего нет, просто пустота...... ", 404



class Quote(Resource):
	def get(self,id=0):
		id=int(request.args.get('id'))
		if id==0:
			return get_starting(curs),200
		else:
			try:
				curs.execute(f"select name, description from hackaton where id = {id}")
				list_data=[]
				list_keys = ["name", "description"]
				responce= curs.fetchall()
				if responce==[]:
					return "error", 404
				for i in responce:
					list_data.append(dict(zip(list_keys, i)))
				return list_data,200
			except:
				return "error",404
	def post(self):
		print(request.form.get("test"))
		return "nn", 201
def connect_to_db():
	try:
		# пытаемся подключиться к базе данных
		conn = psycopg2.connect(dbname='nzsjlari', user='nzsjlari', password='DAKyGuo8-6zj5VI6XYOW2jEZXGVrCiTf', host='snuffleupagus.db.elephantsql.com')
	except:
		print('Can`t establish connection to database')
	cursor = conn.cursor()
	return conn,cursor

def get_starting(cursor):
	cursor.execute("select id,name,longitude,latitude from hackaton")
	list_data=[]
	list_keys=["id","name","longitude","latitude"]
	for i in cursor.fetchall():
		list_data.append(dict(zip(list_keys,i)))
	return list_data
api.add_resource(Quote,"/api","/api/<int:id>")


if __name__ == '__main__':
	conn,curs= connect_to_db()
	get_starting(curs)
	app.run(debug=False)
	conn.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


