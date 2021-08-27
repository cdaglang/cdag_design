# CDAG_LANG_TEST
"""
LANG TEST: testar as funções do YACC (sintaxe)
"""

import json
import cdag_yacc as cy


code = """main: adds [1 3] 
                adds [4 5]
                adds [8 9]"""

print(cy.parse(code))


