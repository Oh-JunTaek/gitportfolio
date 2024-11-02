from langchain.prompts import PromptTemplate

def get_resume_keywords_prompt_template():
    template = """
    너는 사용자가 추출한 GitHub 레포지토리 정보들을 사용하여 이력서를 생성할 수 있도록 각 섹션에 필요한 데이터를 추출해야 해. 만약 정보가 없으면 "NULL"로 표시해.
    
    ## Skills


    ## Languages
    {languages}

    ## Interests
    {interests}

    $$
    \\small \\textbf  \\
    \\Huge \\textbf {name} \\
    \\small AI(LLM)-Developer
    $$

    <aside>
    📍 Location: {location}
    </aside>
    <aside>
    ☎️ Contact: {contact}
    </aside>
    <aside>
    📧 Email: {email}
    </aside>

    ### 🧑‍💻 About Me
    안녕하세요! **’Comfort-Zone에서 벗어나 끊임없이 도전을 하는 개발자’** {name}입니다.

    - **Self-Motivation**: 어떤 일이든 관심이 생기면 망설임 없이 도전하여 실행에 옮깁니다.
    - **Optimization-Driven**: 코드 한 줄까지도 성능 최적화에 집중하여 시스템의 효율성을 극대화합니다.
    - **Collaborative Growth**: 개인적 성장을 넘어서, 함께 발전하는 문화를 추구합니다.

    ### 🏢 Work Experience
    **{experience_years} - {experience_years_end}**
    **Job Title** - ***{company_name}***

    **Project Name:** {project_name}
    - {project_description}
    - Technologies: {technologies_used}

    ### 🎓 Education
    **{education_start} - {education_end}**
    **{degree_name}** - **{university_name}**

    ### 🏆 Awards
    **{award_date}**
    **{award_name}** - **{organization_name}**
    - Project: {project_name_award}
    - Achievements: {achievements}

    ### 🤼 Projects
    **{project_start} - {project_end}**
    **{project_title}** - **{project_company}**
    - Technologies: {project_technologies}
    - Achievements: {project_achievements}

    ## GitHub Activity Data
    GitHub 레포지토리 정보:
    {github_data}
    """

    return PromptTemplate(
        template=template,
        input_variables=[
            "github_data", "skills", "languages", "interests", "name", 
            "location", "contact", "email", "experience_years", "experience_years_end",
            "company_name", "project_name", "project_description", "technologies_used",
            "education_start", "education_end", "degree_name", "university_name",
            "award_date", "award_name", "organization_name", "achievements",
            "project_start", "project_end", "project_title", "project_company",
            "project_technologies", "project_achievements"
        ]
    )
