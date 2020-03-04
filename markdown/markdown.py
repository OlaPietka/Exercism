import re


def parse(markdown):
    res = ''
    in_list = False
    for i in markdown.split('\n'):
        if i.startswith('###### '):
            i = '<h6>' + i[7:] + '</h6>'
        elif i.startswith('## '):
            i = '<h2>' + i[3:] + '</h2>'
        elif i.startswith('# '):
            i = '<h1>' + i[2:] + '</h1>'
        elif i.startswith('* '):
            i = '<li>' + i[2:] + '</li>'
            if not in_list:
                i = '<ul>' + i
                in_list = True
        else:
            i = '<p>' + i + '</p>'
            if in_list:
                i = '</ul>' + i
                in_list = False

        strong = re.match('(.*)__(.*)__(.*)', i)
        if strong:
            i = strong.group(1) + '<strong>' + strong.group(2) + '</strong>' + strong.group(3)
        em = re.match('(.*)_(.*)_(.*)', i)
        if em:
            i = em.group(1) + '<em>' + em.group(2) + '</em>' + em.group(3)
        res += i

    if in_list:
        res += '</ul>'
    return res