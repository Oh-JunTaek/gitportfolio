def log_openai_interaction():
    from langchain_openai import ChatOpenAI  # 임포트 구문을 함수 내부로 이동
    chat_model = ChatOpenAI()
    return chat_model