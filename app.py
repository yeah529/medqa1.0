# -*- encoding:utf-8 -*-
from flask import Flask
from flask import request
from server import train_med

app = Flask(__name__)
global tfmodel,sess
	
tfmodel = train_med.QA_MED()
sess = tfmodel.model_built()

@app.route('/hello', methods=['POST'])
def hello():
	global tfmodel
	datax = request.form.to_dict()
	return tfmodel.welcome_msg(datax['user_name'])
	
@app.route('/ask')
def ask():
	global tfmodel
	return tfmodel.ask_msg()
	

	
@app.route('/type')
def choose_type():
	global tfmodel
	return tfmodel.get_department()

@app.route('/get_qa',methods=['POST'])
def get_question():
	global tfmodel,sess
	datax = request.form.to_dict()
	key_option = int(datax['key_option'])-1
	q_file = datax['q_file']
	user = datax['user_name']
	return tfmodel.get_similar_qa(sess,key_option,q_file,user)

@app.route('/return')
def back():
	global tfmodel
	return tfmodel.backToFirst()
	
@app.route('/error')
def error_msg():
	return "说话太高深，健康小医生看不懂您的话，请重新输入"

if __name__ == '__main__':
	#global tfmodel
	app.run('0.0.0.0')
