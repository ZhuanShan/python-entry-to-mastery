# 8-15

import printing_functions

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("printing model: " + current_design)
        completed_models.append(current_design)



unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
printing_functions.show_completed_models(completed_models)
print(unprinted_designs)


# 8-16

import module_name