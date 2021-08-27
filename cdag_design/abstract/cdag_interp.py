
import cdag_yacc as cy
from cdag_mem import pointer, mem
from hashlib import md5

# TODO:
# - criar o hash para definir atributos distintamente
# - definir o valor e nome das variaveis para colocar no pointer e no mem
# - transferir os dados para o pointer e mem, por onde as ações vão ser executadas


def create_code_hash(text):
    return md5(text.encode()).hexdigest()


def get_code(main_code):
    parsed_code = cy.parse(main_code)
    return parsed_code


def action_adds(*args):
    sum_ = 0
    for k in args:
        sum_ += k
    return sum_


actions_dict = {'adds': action_adds}


code = """main: adds [1 3] adds[4 5]"""
pcode = get_code(code)


def interp(parsed_code):
    interp_list = []
    subj = ''
    action = ''
    res = None
    if isinstance(parsed_code, tuple):
        for k in parsed_code:
            res = interp(k)
    elif isinstance(parsed_code, dict):
        obj = []
        for k, v in parsed_code.items():
            if k == 'subj':
                subj = v[0]
            else:
                if k == 'action':
                    action = v[0]
                elif k == 'obj':
                    for i in v:
                        obj.append(interp(i))

                if action:
                    res = actions_dict[action](*obj)
    elif isinstance(parsed_code, (int, float, str)):
        res = parsed_code
    return res


print(f'==> code:\n {code}')
print()
print(f'==> parsed code:\n {pcode}')
print()
print(f'==> interp:\n {interp(pcode)}')


