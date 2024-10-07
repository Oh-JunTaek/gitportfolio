from pymongo import MongoClient
from dotenv import load_dotenv
import os

mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri)
db = client["vector_storage"]
collection = db["vectors"]

mongo_uri = os.getenv("MONGODB_URI")
db = client["resume"]  # DB 이름 설정
collection = db["resume_data"]  # 컬렉션 설정

def save_vectors_to_db(vectors, metadata):
    """벡터와 메타데이터를 MongoDB에 저장"""
    collection.insert_one({
        "vectors": vectors.tolist(),
        "metadata": metadata
    })
    print("벡터가 MongoDB에 저장되었습니다.")