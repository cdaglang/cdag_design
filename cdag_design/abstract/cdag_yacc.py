# CDAG_YACC
"""
YACC: é onde se constroi a sintaxe da linguagem
"""

import yacc
from cdag_lex import lexer, tokens

# código vai aqui:


def p_s1(p):
    """s1 : subj comma action lbra objs rbra"""
    if len(p) == 7:
        p[0] = ({'subj': (p[1],)},
                (
                    {
                        'action': (p[3],),
                        'obj': p[5]
                    }
                ,)
                )


def p_s2(p):
    """subj : id"""
    p[0] = p[1]


def p_action(p):
    """action : adds"""
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


parser = yacc.yacc()


def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, lexer=lexer, debug=debug)
    if parser.error:
        return None
    return p
