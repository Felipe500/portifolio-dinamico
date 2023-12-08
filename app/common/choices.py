from model_utils import Choices

USE_WEBSITE = Choices(
    ("is_using", "Usar"),
    ("not_using", "Não Usar"),
)

TYPE_HISTORIC = Choices(
    ("professional", "EXPERIÊNCIAS PROFISSIONAIS"),
    ("academic", "HISTÓRICO ACADÊMICO"),
)

TYPE_HARD_SKILL = Choices(
    ("front_end", "FRONT-END"),
    ("back_end", "BACK-END"),
    ("mobile", "MOBILE"),
    ("desktop", "DESKTOP"),
    ("dev_ops", "DevOps"),
)

TYPE_PROJECT = Choices(
    ("full_stack", "Full-Stack"),
    ("front_end", "Front-end"),
    ("back_end", "Back-end"),
    ("mobile", "Mobile"),
    ("desktop", "Desktop"),
)


TIME_EXPERIENCE_SKILL = Choices(
    ("_0_year_0_month", "INICIANDO ESTUDOS"),
    ("_0_year_6_month", "6 MESES"),
    ("_1_year_0_month", "1 ANO"),
    ("_1_year_6_month", "1 ANO E 6 MESES"),
    ("_2_year_0_month", "2 ANO"),
    ("_2_year_6_month", "2 ANO E 6 MESES"),
    ("_3_year_0_month", "3 ANO"),
    ("_3_year_6_month", "3 ANO E 6 MESES"),
    ("_4_year_0_month", "4 ANO"),
    ("_5_year_0_month", "5 ANO"),
    ("_6_year_0_month", "6 ANO"),
    ("_7_year_0_month", "7 ANO"),
    ("_8_year_0_month", "8 ANO"),
    ("_9_year_0_month", "9 ANO"),
    ("_10_year_0_month", "10 ANO OU MAIS"),
)
