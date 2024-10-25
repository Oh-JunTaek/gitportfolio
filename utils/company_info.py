import json

# 1. 사전 등록된 정보(JSON) 로드 함수
def get_company_from_json(company_name, json_file='data/pre_collected_company_data.json'):
    """
    JSON 파일에서 사전 등록된 회사 정보를 검색하여 반환.
    :param company_name: 회사 이름
    :param json_file: JSON 파일 경로
    :return: 회사 정보 (사전 등록된 회사의 슬로건 및 설명)
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for company in data['companies']:
                if company['name'] == company_name:
                    return company
        # 회사 정보를 찾을 수 없는 경우
        return None
    except FileNotFoundError:
        # 파일이 없는 경우 에러 메시지를 출력하고 None 반환
        print(f"{json_file} 파일을 찾을 수 없습니다.")
        return None

# 2. 유저에게 인풋 받는 함수
def get_company_from_user_input():
    """
    유저에게 회사 정보를 직접 입력받음.
    :return: 유저가 입력한 회사 정보
    """
    company_name = input("회사 이름을 입력하세요: ")
    company_slogan = input(f"{company_name}의 슬로건을 입력하세요: ")
    company_description = input(f"{company_name}의 설명을 입력하세요: ")

    return {
        "name": company_name,
        "slogan": company_slogan,
        "description": company_description
    }
