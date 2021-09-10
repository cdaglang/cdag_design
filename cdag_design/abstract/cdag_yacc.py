# CDAG_YACC
"""
YACC: é onde se constroi a sintaxe da linguagem
"""

import yacc
from cdag_lex import lexer, tokens

# código vai aqui:


def p_s0(p):
    """s0 : subjs actions_obj_attr"""
    p[0] = (p[1], p[2])


def p_subjs(p):
    """subjs : subj comma"""
    p[0] = {'subj': (p[1],)}


def p_actions_etc(p):
    """actions_obj_attr : action lbra objs rbra
                        | action lbra objs rbra actions_obj_attr
                        | action lbra objs rbra as attrs
                        | action lbra objs rbra as attrs actions_obj_attr"""
    if len(p) == 5:
        p[0] = ({'action': (p[1],), 'obj': p[3]},)
    elif len(p) == 6:
        p[0] = ({'action': (p[1],), 'obj': p[3]},) + p[5]
    elif len(p) == 7:
        p[0] = ({'action': (p[1],), 'obj': p[3], 'attr': p[6]},)
    elif len(p) == 8:
        p[0] = ({'action': (p[1],), 'obj': p[3], 'attr': p[6]},) + p[7]


def p_s2(p):
    """subj : id"""
    p[0] = p[1]


def p_action(p):
    """action : adds
              | outputs"""
    p[0] = p[1]


def p_s3(p):
    """objs : id
            | int1
            | str1
            | id objs
            | int1 objs
            | str1 objs"""
    if len(p) == 2:
        p[0] = (p[1],)
    elif len(p) == 3:
        p[0] = (p[1],) + p[2]


def p_s4(p):
    """attrs : id
             | id attrs"""
    if len(p) == 2:
        p[0] = (p[1],)
    elif len(p) == 3:
        p[0] = (p[1],) + p[2]


parser = yacc.yacc()


def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, lexer=lexer, debug=debug)
    if parser.error:
        return None
    return p
