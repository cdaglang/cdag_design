
import cdag_yacc as cy
from cdag_mem import pointer, mem
from hashlib import md5

# TODO:
# - criar o hash para definir atributos distintamente
# - definir o valor e nome das variaveis para colocar no pointer e no mem
# - transferir os dados para o pointer e mem, por onde as ações vão ser executadas

counter = 0


def create_code_hash(text):
    return md5(text.encode()).hexdigest()


def get_code(main_code):
    parsed_code = cy.parse(main_code)
    return parsed_code


def put_attr2mem(attr_name, attr_value):
    global counter
    counter += 1
    pointer.update({attr_name: {'mem': counter}})
    mem.update({counter: {'value': attr_value}})


def get_attr(attr_name):
    val_pointer = pointer.get(attr_name, None)
    if val_pointer:
        val_mem = val_pointer['mem']
        val = mem.get(val_mem, None)
        if val:
            return val['value']
    return None


def action_adds(*args):
    sum_ = 0
    for k in args:
        sum_ += k
    return [sum_]


def action_outputs(*args):
    print(*args)
    return []


actions_dict = {'adds': action_adds, 'outputs': action_outputs}


code = """main: adds [1 3] as v1 adds [10 v1] as v2 outputs [v1 v2]"""
pcode = get_code(code)


def interp(parsed_code, hash_code, subj=None, action=None):
    interp_list = []
    if subj is None:
        subj = ''
    if action is None:
        action = ''
    attr = []
    res = None
    print('-', hash_code, subj, action)
    if isinstance(parsed_code, tuple):
        for k in parsed_code:
            res, subj = interp(k, hash_code, subj, action)
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
                        obj.append(interp(i, hash_code, subj, action)[0])
                elif k == 'attr':
                    for i in v:
                        attr_name = '_'.join([hash_code, subj, i])
                        print(f'-- atributo achado! {i}')
                        print(f'-- nome atributo: {attr_name}')
                        attr.append(attr_name)

                if action not in ['', None] and obj:
                    res = actions_dict[action](*obj)
                    if attr:
                        for i1, i2 in zip(attr, res):
                            put_attr2mem(i1, i2)
                    print(f'action result: {res}')
    elif isinstance(parsed_code, (int, float)):
        res = parsed_code
    elif isinstance(parsed_code, str):
        if parsed_code.startswith('"') or parsed_code.startswith("'"):
            res = parsed_code
        else:
            attr_name = '_'.join([hash_code, subj, parsed_code])
            res = get_attr(attr_name)
    return res, subj


def exec_code(main_code):
    try:
        pcode = get_code(main_code)
    except Exception:
        result = []
    else:
        hash_code = create_code_hash(main_code)
        result, _ = interp(pcode, hash_code)
    return result


print(f'==> code:\n {code}\n')
print(f'==> parsed:\n {pcode}\n')
print(f'==> interp:\n {exec_code(code)}\n\n')
print('** memory usage **')
print(f'==> pointer:\n {pointer}\n')
print(f'==> mem:\n {mem}\n\n')

#
# print(f'==> code:\n {code}')
# print()
# print(f'==> parsed code:\n {pcode}')
# print()
# print(f'==> interp:\n {interp(pcode)}')
#
#
