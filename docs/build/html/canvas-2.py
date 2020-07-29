from bamboo.templates import get_template_1
from bamboo.objects import Canvas

author = 'Author'
title = 'Title'
template = get_template_1()
canvas = Canvas(template=template, author=author, title=title)