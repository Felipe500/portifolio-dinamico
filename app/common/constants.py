from datetime import datetime

default_header = {
    "title": "Mensagem de boas-vindas",
    "profession": "Desenvolvedor fullstack",
    "subtitle": "Fale comigo",
    "photo": "",
}

default_about = {
    "title": "Sobre Mim",
    "content": """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an 
                 unknown printer took a galley of type and scrambled it to make a type specimen book.""",
    "name": "seu nome",
    "email": "email@email.com",
    "phone": "86999556677",
    "birth_date": datetime.now().date(),
    "yars_life": 20,
    "is_freelance": True,
    "nationality": "Brasileira",
    "address": "Teresina-PI",
    "languages": ["português"],
}

default_historic = {
    'academic':  [{'id': 1, 'name': 'Analise e desenvolvimento de sistemas', 'institution_company': 'Academia', 'description': 'Estudei em diversas fases da criação de um sistema computacional: levantamento de requisitos, projeto, especificação, documentação, implantação, testes e manutenções. ', 'type': 'academic', 'start_date': 'Dezembro 2017', 'end_date': 'Dezembro 2018', 'address': 'Teresina-PI', 'website': 1}],
    'professional': [{'id': 2, 'name': 'Back-end', 'institution_company': 'Empresa BR', 'description': 'Trabalhei em aplicações para gerenciar cursos online, fazendo melhorias e adicionando nova features...', 'type': 'academic', 'start_date': 'Dezembro 2017', 'end_date': 'Dezembro 2018', 'address': 'Teresina-PI', 'website': 1}]
}


default_skill_card = [{'id': 1, 'name': 'Backend'}]


default_skills = {1: [{'id': 2, 'name': 'Python', 'card_id': 1, 'time_experience': '<li><i class="fa-sharp fa-solid fa-star"></i></li><li><i class="fa-solid fa-star-half-stroke"></i></li>'},
                      {'id': 3, 'name': 'Django', 'card_id': 1, 'time_experience': '<li><i class="fa-sharp fa-solid fa-star"></i></li>'},
                      {'id': 1, 'name': 'DRF', 'card_id': 1, 'time_experience': '<li><i class="fa-solid fa-star-half-stroke"></i></li>'}]}


default_contact = {
    "email": "email@email.com",
    "whatsapp": 86999507878,
    "github": "https://github.com",
    "gitlab": "https://gitlab.com",
    "stackoverflow": "https://stackoverflow.com/",
    "linkedin": "https://www.linkedin.com",
    "facebook": "https://www.facebook.com",
}

default_website = {
    "header": default_header,
    "about": default_about,
    "historic": default_historic,
    "skills": default_skills,
    "skills_card": default_skill_card,
    "contact": default_contact
}

TIME_EXPERIENCE_SKILL = """<li><i class="fa-sharp fa-solid fa-star"></i></li>"""

ICONS = {
    "plain": """
    <li class="d-flex align-items-center">
        <i class="devicon-{}-plain"></i>
    </li>
        """,
    "original": """
    <li class="d-flex align-items-center">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/{}/{}-original.svg" />
    </li>
        """,
}

SET_PLAIN_ICONS = {
    'django': 'plain'
}
