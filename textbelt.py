import requests
class Client():
	def __init__(self):
		self.api="https://textbelt.com"
	def status(self,Id:str):
		return requests.get(f"{self.api}/status/{id}").json()
	def quota(self,quota_Id):
		return requests.get(f"{self.api}/quota/{quota_Id}").json()
	def text(self,phone:str,message:str,key:str="textbelt"):
		  	data={"phone" : phone,"message" : message,"key" : key}
		  	return requests.post(f"{self.api}/text",data=data).json()