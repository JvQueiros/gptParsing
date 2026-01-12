from celery import Celery
# from send import send_external_api
from service import call_service
import json

with open('config.json') as config_file:
    config = json.load(config_file)

celery = Celery('tasks', broker= config['celery_broker_url'], backend= config['celery_result_backend'])

@celery.task
def process_file_task(id,content):
	try:
		print(content[:5]+content[-5:],type(content))
		# result_process = call_controller(id,content)
		result_process = call_service(id, content)
		print("Requisição a API bem sucedida!")
		# send_external_api(result_process)
	
	except Exception as e:
		print(f"Erro de sintaxe ao processar o conteúdo: {e}")
		return f"Erro de sintaxe: {str(e)}"
	
	return("Tarefa concluida!")


#################################################################################

# def call_controller(id, content):
#     return jsonify({"bs64":call_service(file)})
#     return call_service(id,file)