# CDAG_LEX
"""
LEX: é onde se constroi os tokens da linguagem
"""

import regex as re
import lex
from lex import TOKEN

# tokens
actions = ("adds",)
misc = ("comma", "lbra", "rbra")  # :, [, ]
types = ("string", "integer")  # --> type(1), type('oi')
reserved = actions + misc + types

# valores / variaveis
values = ("str1", "int1")  # --> 1, 'oi'
ids = ("id",)  # var1, var2, subj1, subj2

tokens = reserved + values + ids

t_ignore = '\n\t ,;'
t_str1 = r'\".*?\"|\'.*?\''
int1_token = r'[+|-]?\d+'  # r'[+|-]?\d+[^\.]'
id_token = r'[a-zA-Z]+[\w]+'
t_comma = r':'
t_lbra = r'\['
t_rbra = r'\]'


@TOKEN(int1_token)
def t_int1(t):
    t.value = int(t.value)
    return t


@TOKEN(id_token)
def t_id(t):
    if t.value in reserved:
        t.type = t.value
    else:
        t.type = 'id'
    return t


def t_error(t):
    print('error')
    t.lexer.skip(1)


lexer = lex.lex()


if __name__ == '__main__':
    print(re.findall(t_int1, '120 +130 -130 13.0 0.0'))
    print(re.findall(t_str1, '"oi" \'tudo b\'em?'))
