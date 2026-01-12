import requests
import os
import json


with open('config.json', 'r') as config_file:
	config = json.load(config_file)
	

def get_auth_token(url):
	payload = {
		"username": config['payload_username'],
		"password": config['payload_password'],
		"grant_type": config['payload_grant_type']
	}
	
	response = requests.post(url, headers=config['header_authorization'].headers, data=payload)
	print(response)
	try:
		return response.json().get("access_token")
	except Exception as error:
		print(error)
	
# def send_data(url,token,result_process):
# 	headers = {
# 		"Authorization": f"Bearer{token}"
# 		,"Content-Type": "application/json"
# 	}

# 	requests.post(url, headers=headers, json=result_process)


# def send_external_api(result_process):
# 	with open(os.path.join(os.getcwd(),"config.json"), 'r', encoding="utf-8") as js_file:
# 		config_json = json.load(js_file)

# 	token = get_auth_token(url=config_json["url_token"])

# 	try:
# 		send_data(url=config_json["url_send_data"],token=token,result_process=result_process)
# 		print("Arquivos enviados com sucesso!")
# 	except Exception as error:
# 		print(f"deu ruim: {error}")