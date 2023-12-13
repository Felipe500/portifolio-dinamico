from datetime import datetime

default_website = {
    "header_wellcome_title": "Mensagem de boas-vindas",
    "header_profession": "Desenvolvedor fullstack",
    "header_description": "Fale comigo",
    "title": "Sobre Mim",
    "content": """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
     Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an 
     unknown printer took a galley of type and scrambled it to make a type specimen book.""",
    "name": "seu nome",
    "email": "email@email.com",
    "phone": "",
    "birth_date": datetime.now().date(),
    "is_freelance": True,
    "nationality": "Brasileira",
    "address": "Teresina-PI",
    "languages": ["portugues"],
    "github": "github",
    "gitlab": "gitlab",
    "stackoverflow": "stackoverflow",
    "linkedin": "linkedin",
    "facebook": "facebook",
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
