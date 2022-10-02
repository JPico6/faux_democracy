from create_world import State


state1 = State() #5,10,10,10,90)
print(state1.generate_attributes())
print(state1.pop)

# update state characteristics
ex_dict = {'pop': 1.08, 'religious_level': 0.91}
state1.update_attributes(ex_dict)
print(vars(state1))

