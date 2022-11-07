import random
from utils_state import val_from_normal_dist, modify_dist_mean, check_bounds


class State:

    def __init__(
            self,
            pop=None,
            religious_level=None,
            education_level=None,
            economy_level=None,
            individual_tax_level=None,
            corporate_tax_level=None,
            revenue=None,
            crime_level=None,
            conservative_level=None,
            liberal_level=None,
            approval_level=None,
            extr_conservative_level=None,
            extr_liberal_level=None,
            extr_conservative_size=None,
            extr_liberal_size=None,
            approval_conservative=None,
            approval_liberal=None,
            approval_extr_conservative=None,
            approval_extr_liberal=None,
            health_level=None,
            birth_rate=None,
            death_rate=None,
            police_level=None,
            military_level=None,
            environment_level=None,
            infrastructure_level=None,
            social_programs_level=None
    ):
        self.__dict__.update(locals())

    def generate_attributes(self):

        if not self.pop:
            self.pop = random.randint(100000, 1000000)
        if not self.religious_level:
            self.religious_level = val_from_normal_dist()
        if not self.education_level:
            self.education_level = val_from_normal_dist(modify_dist_mean(self.religious_level))
        if not self.economy_level:
            self.economy_level = val_from_normal_dist()
        if not self.individual_tax_level:
            self.individual_tax_level = 0.25
        if not self.corporate_tax_level:
            self.corporate_tax_level = 0.25
        if not self.revenue:
            self.revenue = int(((self.pop*50000*self.individual_tax_level*self.economy_level*0.02)/52) + \
                           ((self.corporate_tax_level*self.pop*0.25*20000*self.economy_level*0.02)/52))
        if not self.crime_level:
            self.crime_level = val_from_normal_dist()
        if not self.conservative_level:
            self.conservative_level = val_from_normal_dist(modify_dist_mean(self.religious_level, inv=True))
        if not self.liberal_level:
            self.liberal_level = 100 - self.conservative_level
        if not self.approval_level:
            self.approval_level = 50
        if not self.extr_conservative_level:
            self.extr_conservative_level = 50
        if not self.extr_liberal_level:
            self.extr_liberal_level = 50
        if not self.extr_conservative_size:
            self.extr_conservative_size = val_from_normal_dist(mu=10)
        if not self.extr_liberal_size:
            self.extr_liberal_size = val_from_normal_dist(mu=10)
        if not self.approval_conservative:
            self.approval_conservative = 50
        if not self.approval_liberal:
            self.approval_liberal = 50
        if not self.approval_extr_conservative:
            self.approval_extr_conservative = 50
        if not self.approval_extr_liberal:
            self.approval_extr_liberal = 50
        if not self.health_level:
            self.health_level = 50
        if not self.birth_rate:
            self.birth_rate = 13
        if not self.death_rate:
            self.death_rate = 8
        if not self.police_level:
            self.police_level = 50
        if not self.military_level:
            self.military_level = 50
        if not self.environment_level:
            self.environment_level = 50
        if not self.infrastructure_level:
            self.infrastructure_level = 50
        if not self.social_programs_level:
            self.social_programs_level = 50

        labels = ['pop',
                  'religious_level',
                  'education_level',
                  'economy_level',
                  'individual_tax_level',
                  'corporate_tax_level',
                  'revenue',
                  'crime_level',
                  'conservative_level',
                  'liberal_level',
                  'approval_level',
                  'extr_conservative_level',
                  'extr_liberal_level',
                  'extr_conservative_size',
                  'extr_liberal_size',
                  'approval_conservative',
                  'approval_liberal',
                  'approval_extr_conservative',
                  'approval_extr_liberal',
                  'health_level',
                  'birth_rate',
                  'death_rate',
                  'police_level',
                  'military_level',
                  'environment_level',
                  'infrastructure_level',
                  'social_programs_level'
        ]

        vals = [self.pop,
                self.religious_level,
                self.education_level,
                self.economy_level,
                self.individual_tax_level,
                self.corporate_tax_level,
                self.revenue,
                self.crime_level,
                self.conservative_level,
                self.liberal_level,
                self.approval_level,
                self.extr_conservative_level,
                self.extr_liberal_level,
                self.extr_conservative_size,
                self.extr_liberal_size,
                self.approval_conservative,
                self.approval_liberal,
                self.approval_extr_conservative,
                self.approval_extr_liberal,
                self.health_level,
                self.birth_rate,
                self.death_rate,
                self.police_level,
                self.military_level,
                self.environment_level,
                self.infrastructure_level,
                self.social_programs_level
                ]
        state_attributes = dict(zip(labels, vals))

        return state_attributes

    # def update_attributes(self, attribute_mod_dict):
    #
    #     # modify each population attribute based on current events / player decisions per turn
    #     for key, value in attribute_mod_dict.items():
    #         orig_value = getattr(self, key, value)
    #         new_value = orig_value * value
    #         setattr(self, key, check_bounds(key, new_value))


def initiate_game():
    # A. initiate game
    game_data = {}
    game_dat = {}
    game_dat['turn'] = 1
    game_dat['turns_next_election'] = 208

    # b. initiate state(s)
    state1 = State()
    state1_attributes = state1.generate_attributes()
    game_data['game_dat'] = game_dat
    game_data['turn1'] = state1_attributes

    return game_data


# TODO: when an attribute value reaches 100 and modifiers continue to push it up, that should affect the extremist proportions
# TODO: as attributes get more extreme, they should more slowly modify further towards the extremes
# e.g., the modifier should be reduced when going up from 80 but should be able to drop at normal speed
