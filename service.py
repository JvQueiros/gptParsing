# #from pydantic import BaseModel, Field
# from typing import Dict, Optional, List
# from pathlib import Path
# from openai import OpenAI
# import base64
# import os
# import json
# import time
# import ast

# # MARK: Generate bs64
# def pdf_bs64_txt(path_file,path_destination,filename,delimiter=",",multi_bs64=True):
# 	"""" For test purpouses! """
	
# 	extension = ".json"
# 	list_base64 = []

# 	for pdf_file in os.listdir(path_file):
# 		filename_pdf = Path(pdf_file).suffix
		
# 		if filename_pdf == ".pdf":
# 			with open(os.path.join(path_file,pdf_file), "rb") as f: data = f.read()
# 			bs64 = base64.b64encode(data).decode("utf-8-sig")

# 			if multi_bs64 == False:
# 				abs_path_destination = os.path.join(path_destination,Path(pdf_file).stem+extension)
# 				if os.path.isfile(abs_path_destination): os.remove(abs_path_destination)
# 				time.sleep(3)
				
# 				with open(abs_path_destination, "w") as f: f.write(str([[2020+1/10,bs64]]).replace("'",'"'))
# 			else: list_base64.append(bs64)

	
# 	list_size = len(list_base64)-1
# 	if multi_bs64 ==  True:
# 		filename = filename + extension
# 		abs_path_destination = os.path.join(path_destination,filename)

# 		if os.path.isfile(abs_path_destination): os.remove(abs_path_destination)
# 		time.sleep(3)

	
# 		with open(abs_path_destination, "w") as f: f.write("[")
# 		for i in range(len(list_base64)):
# 			if len(list_base64) == 1:
# 				with open(abs_path_destination, "a") as f: f.write(str([2020+i/10,list_base64[i]]).replace("'",'"'))
# 			else:
# 				if i < list_size: 
# 					with open(abs_path_destination, "a") as f: f.write(str([2020+i/10,list_base64[i]]).replace("'",'"')+delimiter)
# 				else: 
# 					with open(abs_path_destination, "a") as f: f.write(str([2020+i/10,list_base64[i]]).replace("'",'"'))
# 		with open(abs_path_destination, "a") as f: f.write("]")


# # MARK: Read bs64 Text File
# def file_txt_read(path_absolute):
# 	"""" For test purpouses! """

# 	#txt file
# 	#with open(path_absolute, 'r', encoding='utf-8') as file: file = file.read() 
	
# 	#txt file with json strcuture
# 	#with open(path_absolute, 'r', encoding='utf-8') as file: file = file.read().strip()
# 	#return(json.loads(file))
	
# 	#json file
# 	with open(path_absolute, 'r', encoding='utf-8') as file: data = json.load(file)
# 	return(data)
 
# # MARK: Request
# def request(token,filename,gpt_version,base64_string):
# 	client = OpenAI(api_key=token)

# 	msg = [
# 		{"role": "system", "content": "Você é um especialista em contabilidade. Você é capaz de localizar as categorias listadas abaixo. Após a extração, você deve devolver os dados no formato JSON"},
# 		{"role": "user", "content": [
# 				{"type": "file", "file":  {"filename": f"{filename}", "file_data": f"data:application/pdf;base64,{base64_string}",}	},
# 				{"type": "text", "text": "Comece analisando duas vezes o documento inteiro.Se as contas estiverem divididas entre Controladora e Consolidado, devemos ler os valores de **Consolidado**. Procure pelas demonstrações contábeis sintetizadas referente os anos de 2021, 2022, 2023 e 2024."},
# 			]
# 		},
# 	]

# 	rf={
# 		"title": "Generated schema for Root",
# 		"type": "object",
# 		"properties": {
# 			"2021": {
# 			"type": "object",
# 			"properties": {
# 				"total_ativo_circulante": {
# 				"type": "string"
# 				},
# 				"total_ativo_nao_circulante": {
# 				"type": "string"
# 				},
# 				"total_patrimonio_liquido": {
# 				"type": "string"
# 				},
# 				"receita_operacional_liquida": {
# 				"type": "string"
# 				},
# 				"lucro_bruto": {
# 				"type": "string"
# 				},
# 				"lucro_operacional": {
# 				"type": "string"
# 				},
# 				"desp_rec_financeiras_liquidas": {
# 				"type": "string"
# 				},
# 				"lucro_liquido": {
# 				"type": "string"
# 				},
# 				"lucro_antes_ir_csll": {
# 				"type": "string"
# 				},
# 				"total_ativo_permanente": {"type": "string"},
# 				"total_passivo_circulante": {"type": "string"},
# 				"total_passivo_nao_circulante": {"type": "string"},
# 				"lucro_antes_ir": {"type": "string"}
# 			},
# 			"required": [
# 				"total_ativo_circulante",
# 				"total_ativo_nao_circulante",
# 				"total_patrimonio_liquido",
# 				"receita_operacional_liquida",
# 				"lucro_bruto",
# 				"lucro_operacional",
# 				"desp_rec_financeiras_liquidas",
# 				"lucro_liquido",
# 				"lucro_antes_ir_csll",
# 				"total_ativo_permanente",
# 				"total_passivo_circulante",
# 				"total_passivo_nao_circulante",
# 				"lucro_antes_ir"
# 			]
# 			,"additionalProperties": False
# 			},
# 			"2022": {
# 			"type": "object",
# 			"properties": {
# 				"total_ativo_circulante": {
# 				"type": "string"
# 				},
# 				"total_ativo_nao_circulante": {
# 				"type": "string"
# 				},
# 				"total_patrimonio_liquido": {
# 				"type": "string"
# 				},
# 				"receita_operacional_liquida": {
# 				"type": "string"
# 				},
# 				"lucro_bruto": {
# 				"type": "string"
# 				},
# 				"lucro_operacional": {
# 				"type": "string"
# 				},
# 				"desp_rec_financeiras_liquidas": {
# 				"type": "string"
# 				},
# 				"lucro_antes_ir_csll": {
# 				"type": "string"
# 				},
# 				"lucro_liquido": {
# 				"type": "string"
# 				},
# 				"total_ativo_permanente": {"type": "string"},
# 				"total_passivo_circulante": {"type": "string"},
# 				"total_passivo_nao_circulante": {"type": "string"},
# 				"lucro_antes_ir": {"type": "string"}
# 			},
# 			"required": [
# 				"total_ativo_circulante",
# 				"total_ativo_nao_circulante",
# 				"total_patrimonio_liquido",
# 				"receita_operacional_liquida",
# 				"lucro_bruto",
# 				"lucro_operacional",
# 				"desp_rec_financeiras_liquidas",
# 				"lucro_liquido",
# 				"lucro_antes_ir_csll",
# 				"total_ativo_permanente",
# 				"total_passivo_circulante",
# 				"total_passivo_nao_circulante",
# 				"lucro_antes_ir"
# 			]
# 			,"additionalProperties": False
# 			},
# 			"2023": {
# 			"type": "object",
# 			"properties": {
# 				"total_ativo_circulante": {
# 				"type": "string"
# 				},
# 				"total_ativo_nao_circulante": {
# 				"type": "string"
# 				},
# 				"total_patrimonio_liquido": {
# 				"type": "string"
# 				},
# 				"receita_operacional_liquida": {
# 				"type": "string"
# 				},
# 				"lucro_bruto": {
# 				"type": "string"
# 				},
# 				"lucro_operacional": {
# 				"type": "string"
# 				},
# 				"desp_rec_financeiras_liquidas": {
# 				"type": "string"
# 				},
# 				"lucro_antes_ir_csll": {
# 				"type": "string"
# 				},
# 				"lucro_liquido": {
# 				"type": "string"
# 				},
# 				"total_ativo_permanente": {"type": "string"},
# 				"total_passivo_circulante": {"type": "string"},
# 				"total_passivo_nao_circulante": {"type": "string"},
# 				"lucro_antes_ir": {"type": "string"}
# 			},
# 			"required": [
# 				"total_ativo_circulante",
# 				"total_ativo_nao_circulante",
# 				"total_patrimonio_liquido",
# 				"receita_operacional_liquida",
# 				"lucro_bruto",
# 				"lucro_operacional",
# 				"desp_rec_financeiras_liquidas",
# 				"lucro_liquido",
# 				"lucro_antes_ir_csll",
# 				"total_ativo_permanente",
# 				"total_passivo_circulante",
# 				"total_passivo_nao_circulante",
# 				"lucro_antes_ir"
# 			]
# 			,"additionalProperties": False
# 			},
# 			"2024": {
# 			"type": "object",
# 			"properties": {
# 				"total_ativo_circulante": {
# 				"type": "string"
# 				},
# 				"total_ativo_nao_circulante": {
# 				"type": "string"
# 				},
# 				"total_patrimonio_liquido": {
# 				"type": "string"
# 				},
# 				"receita_operacional_liquida": {
# 				"type": "string"
# 				},
# 				"lucro_bruto": {
# 				"type": "string"
# 				},
# 				"lucro_operacional": {
# 				"type": "string"
# 				},
# 				"desp_rec_financeiras_liquidas": {
# 				"type": "string"
# 				},
# 				"lucro_antes_ir_csll": {
# 				"type": "string"
# 				},
# 				"lucro_liquido": {
# 				"type": "string"
# 				},
# 				"total_ativo_permanente": {"type": "string"},
# 				"total_passivo_circulante": {"type": "string"},
# 				"total_passivo_nao_circulante": {"type": "string"},
# 				"lucro_antes_ir": {"type": "string"}
# 			},
# 			"required": [
# 				"total_ativo_circulante",
# 				"total_ativo_nao_circulante",
# 				"total_patrimonio_liquido",
# 				"receita_operacional_liquida",
# 				"lucro_bruto",
# 				"lucro_operacional",
# 				"desp_rec_financeiras_liquidas",
# 				"lucro_liquido",
# 				"lucro_antes_ir_csll",
# 				"total_ativo_permanente",
# 				"total_passivo_circulante",
# 				"total_passivo_nao_circulante",
# 				"lucro_antes_ir"
# 			]
# 			,"additionalProperties": False
# 			}
# 		},
# 		"required": [
# 			"2021",
# 			"2022",
# 			"2023",
# 			"2024"
# 		]
# 		,"additionalProperties": False
# 	}

# 	response = client.chat.completions.create(
# 		model = gpt_version,
# 		messages=msg,
# 		response_format={
# 			"type": "json_schema",
# 			"json_schema": {
# 				"name": "bloodwork",
# 				"schema": rf,
# 				"strict": True,
# 			},
# 		},

# 	)

# 	#ast.literal_eval remove string to get a real dict instead of txt
# 	return(ast.literal_eval(response.choices[0].message.content))


# def debug_code(message,var=None,debug=False):
# 	if debug is True:
# 		if not var is None: print(f"[Debug] {message}: {var}")
# 		else: print(f"[Debug] {message}")


# def check_dict(dict,debug=False):
# 	re_run = False
# 	count=0

# 	for key in dict.keys():
# 		debug_code("key", key, debug)

# 		for sub_key in dict[key]:
# 			debug_code("sub key", sub_key, debug)
# 			value = dict[key][sub_key]

# 			if value in ['', ' ']: 
# 				re_run = True
# 				break
# 			else: count+=1
# 		if re_run == True:
# 			debug_code("sequencial not nulls", count, debug)
# 			break

# 		debug_code("sequencial not nulls", count, debug)
# 	return (re_run)

# # MARK: GPT Request
# def gpt_read_bs64(content,filename,running_times,token,gpt_version,wait_time,debug):
# 	result_set = []

# 	for array in content:
# 		dict = {}

# 		for i in range(running_times):
# 			debug_code(f"GPT's read bs64[{array[0]}] request", i, debug)
# 			api_start = time.time()

# 			#call gpt API
# 			dict = request(token=token,filename=filename,gpt_version=gpt_version,base64_string=array[1])

# 			debug_code(message=f"request duration (sec): {(time.time() - api_start)}", debug=debug)
# 			time.sleep(wait_time)
			
# 			repeat = check_dict(dict=dict,debug=debug)
# 			if repeat == False: break

# 		result_set.append(dict)
	
# 	return(result_set)


# def dict_show(dict):
# 	for sub_dict in dict:
# 		print(sub_dict)
# 		for key,value in dict[sub_dict].items():
# 			print(f"\t{key}: {value}")


# def dictionary_merge(result_set,debug):
# 	dict_first = dict(result_set[0])
	
# 	for i in range(1,len(result_set)):
# 		dict_new = dict(result_set[i])
		
# 		for sub_dict in dict_first:
# 			for key in dict_first[sub_dict]:
# 				new_value = dict_new[sub_dict][key]
# 				if new_value != '' and new_value != ' ': dict_first[sub_dict].update({key: new_value})
				
# 	debug_code(message="Dictionary merge result",var=dict_first,debug=debug)
	
# 	return(dict_first)


# def system_data_structure(dictionary,name_key_1,name_key_2,name_key_3,name_key_4,name_key_5,name_key_6,request_id):
# 	"""dictionary accept as parameters just NOT NESTED dictionaries"""
# 	list = []
# 	new_dict = {}

# 	for sub_dict in dictionary:
# 		dict = {}
# 		dict.setdefault(name_key_3,sub_dict)
# 		dict[name_key_4] = [{name_key_5: key, name_key_6: value } for key,value in dictionary[str(sub_dict)].items()]
# 		list.append(dict)
	
# 	new_dict.setdefault(name_key_1,request_id)
# 	new_dict.setdefault(name_key_2,list)

# 	return(new_dict)


# # MARK: Call Service
def call_service(id,content):
    return{'message': f"id: {id}, content: {content}"}
# 	try:
# 		with open(os.path.join(os.getcwd(),"config.json"), 'r', encoding="utf-8") as js_file:
# 			config_json = json.load(js_file)
		
# 		debug = config_json["debug"]
# 		debug_code(message=f"{content[:20]}...'",debug=debug)
		
# 		#content = json.loads(content)
# 		content = ast.literal_eval(content)

# 		start = time.time()

# 		list_dict = gpt_read_bs64(
# 			content = content
# 			,filename = config_json["filename"]
# 			,running_times = int(config_json["empty_rerun_times"])
# 			,token = config_json["token"]
# 			,gpt_version = config_json["gpt_version"]
# 			,wait_time = config_json["sec_wait_between_request"]
# 			,debug = debug
# 		)
		
# 		debug_code(message=f"Total Request duration (sec): {(time.time() - start)}",debug=debug)		
		
# 		dict_merged = dictionary_merge(list_dict,debug)

# 		final_dictionary = system_data_structure(
# 			dictionary=dict_merged
# 			,name_key_1 = config_json["name_key_1"]
# 			,name_key_2 = config_json["name_key_2"]
# 			,name_key_3 = config_json["name_key_3"]
# 			,name_key_4 = config_json["name_key_4"]
# 			,name_key_5 = config_json["name_key_5"]
# 			,name_key_6 = config_json["name_key_6"]
# 			,request_id=id
# 		)

# 		return (final_dictionary)
	
# 	except Exception as error:
# 		return(error)
	
# def localhost_test():
# 	#pdf_bs64_txt(path_file=os.path.join(os.getcwd(),"_file_test"),path_destination=os.path.join(os.getcwd(),"_file_test"),filename="bs64",delimiter=",",multi_bs64=True)
# 	filename = "BP_2022.json"
# 	#filename = "bs64_manual.json"
# 	#filename = "bs64.json"

# 	text_file = file_txt_read(path_absolute=os.path.join(os.getcwd(),r"_file_test",filename))
# 	result = call_service(id=172,text_file=text_file)
# 	print(result)