import json
import random
from utils_state import val_from_normal_dist, modify_dist_mean, check_bounds

# class World:
#
#     def __init__(self, n_states=None):
#         if not n_states:
#             n_states=random.randint(2,10)


class State:

    def __init__(
            self,
            pop=None,
            religious_level=None,
            education_level=None,
            conservative_level=None,
            liberal_level=None,
            approval_level=None
    ):
        self.__dict__.update(locals())

        # self.pop = pop
        # self.religious_level = religious_level
        # self.education_level = education_level
        # self.conservative_level = conservative_level
        # self.liberal_level = liberal_level

    def generate_attributes(self):

        if not self.pop:
            self.pop = random.randint(100000, 1000000)
        if not self.religious_level:
            self.religious_level = val_from_normal_dist()
        if not self.education_level:
            self.education_level = val_from_normal_dist(modify_dist_mean(self.religious_level))
        if not self.conservative_level:
            self.conservative_level = val_from_normal_dist(modify_dist_mean(self.religious_level, inv=True))
        if not self.liberal_level:
            self.liberal_level = 100-self.conservative_level
        if not self.approval_level:
            self.approval_level = 50

        labels = ['pop', 'religious_level', 'education_level', 'conservative_level', 'liberal_level', 'approval_level']
        vals = [self.pop, self.religious_level, self.education_level, self.conservative_level, self.liberal_level,
                self.approval_level]
        state_attributes = dict(zip(labels, vals))

        return state_attributes

    def update_attributes(self, attribute_mod_dict):

        # modify each population attribute based on current events / player decisions per turn
        for key, value in attribute_mod_dict.items():
            orig_value = getattr(self, key, value)
            new_value = orig_value * value
            setattr(self, key, check_bounds(key, new_value))


def initiate_game():

    # A. initiate world
    game_data = {}
    game_dat = {}
    game_dat['turn'] = 1

    # b. initiate state(s)
    state1 = State()
    state1_attributes = state1.generate_attributes()
    game_data['game_dat'] = game_dat
    game_data['state_dat'] = state1_attributes
    # game_data = json.dumps(game_data)

    with open('data/turn_dat.json', 'w') as f:
        json.dump(game_data, f)

    return game_data


#    def return_attributes(self):

# TODO: determine how best to store values between turns (save to file?)
# TODO: when an attribute value reaches 100 and modifiers continue to push it up, that should affect the extremist proportions
# TODO: as attributes get more extreme, they should more slowly modify further towards the extremes
        # e.g., the modifier should be reduced when going up from 80 but should be able to drop at normal speed

