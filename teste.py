import os
from dotenv import load_dotenv

# carregando variáveis de ambiente.
load_dotenv()
host = os.environ['host']
port= os.environ['port']
database= os.environ['database']
user= os.environ['user']
password= os.environ['password']

print(user)