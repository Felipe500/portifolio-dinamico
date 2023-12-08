from django import template

register = template.Library()


@register.filter
def get_skills(skills, id_filter):
    print('skills_get ', skills.get(id_filter))
    return skills.get(id_filter)
