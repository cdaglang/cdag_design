# CDAG_LANG_TEST
"""
LANG TEST: testar as funções do YACC (sintaxe)
"""

import cdag_yacc as cy

code = """main: adds [1 3]"""

print(cy.parse(code))


