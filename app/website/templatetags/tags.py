from django import template

register = template.Library()


@register.filter
def get_skills(skills, id_filter):
    return skills.get(id_filter)


@register.filter
def format_list_language(languages, string=''):
    for language in languages:
        string += language + ', '
    return string[:-2]

