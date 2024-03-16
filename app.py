from langchain_community.document_loaders.csv_loader import CSVLoader
from dotenv import load_dotenv
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI

# loader = CSVLoader(file_path='/home/ec2-user/environment/AI_ML/Sample_Electric.csv')
# data = loader.load()
# print(data)

load_dotenv()

llm = ChatOpenAI(temperature=0)
agent_executer = create_csv_agent(llm,'/home/ec2-user/environment/AI_ML/Sample_Electric.csv', verbose=True)
print(agent_executer.invoke("What is the maximum Consumption?"))
