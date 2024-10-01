from models.llama import get_llama_model  # get_llama_model 함수를 import

def generate_resume(resume_prompt, extracted_data, final_keywords, repo_names):
    """
    추출된 데이터를 바탕으로 이력서를 생성하는 함수.
    값이 없는 경우 None 또는 기본값을 넣고 진행.
    """
    # 값이 비어 있는 항목은 None 또는 기본값으로 설정
    filtered_data = {
        "name": extracted_data.get("name", None),  
        "experience_years": extracted_data.get("experience_years", None),
        "experience_years_end": extracted_data.get("experience_years_end", None),
        "project_name": extracted_data.get("project_name", None),
        "project_description": extracted_data.get("project_description", None),
        "technologies_used": extracted_data.get("technologies_used", None),
        "education_start": extracted_data.get("education_start", None),
        "education_end": extracted_data.get("education_end", None),
        "degree_name": extracted_data.get("degree_name", None),
        "award_date": extracted_data.get("award_date", None),
        "award_name": extracted_data.get("award_name", None),
        "project_name_award": extracted_data.get("project_name_award", None),
        "achievements": extracted_data.get("achievements", None),
        "project_start": extracted_data.get("project_start", None),
        "project_end": extracted_data.get("project_end", None),
        "project_title": extracted_data.get("project_title", None),
        "project_technologies": extracted_data.get("project_technologies", None),
        "project_achievements": extracted_data.get("project_achievements", None),
        "github_profile": f"레포지토리: {', '.join(repo_names)}\nKeywords: {', '.join(final_keywords)}"
    }

    try:
        # 값이 None인 항목도 그대로 템플릿에 전달
        resume_result = get_llama_model(resume_prompt.format(**filtered_data))
    except KeyError as e:
        print(f"필수 데이터 누락: {e}")
        return ""
    except IndexError as e:
        print(f"IndexError 발생: {e}")
        return ""
    
    return resume_result

