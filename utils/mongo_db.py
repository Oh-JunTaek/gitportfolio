from pymongo import MongoClient
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 불러오기
load_dotenv()

# MongoDB 연결
mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri)
db = client["resume"]  # DB 이름 설정
collection = db["resume_data"]  # 컬렉션 설정

def save_resume_data(repo_name, data):# 레포지토리 이름과 핵심 데이터를 MongoDB에 저장하는 함수
    document = {
        "repo_name": repo_name,
        "data": data
    }
    collection.insert_one(document)
    print(f"MongoDB에 {repo_name} 데이터 저장 완료.")

def get_resume_data(repo_name):# MongoDB에서 특정 레포지토리의 데이터를 불러오는 함수
    document = collection.find_one({"repo_name": repo_name})
    if document:
        return document["data"]
    else:
        return f"{repo_name}에 대한 데이터가 존재하지 않습니다."
