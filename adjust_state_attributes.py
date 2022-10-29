from utils_state import val_from_normal_dist
import json


def new_turn():
    # identify length of turn, lets say it's a week, so
    turn_length = 7 # (days)

    with open("data/turn_dat.json", "r") as jsonFile:
        game_data = json.load(jsonFile)
#    f = open(f"data/turn_dat.json")
#    game_data = json.loads(f.read())
    current_turn = game_data['game_dat']['turn']
    next_turn = current_turn + 1

    # def adjust_approval():

    # population change
    # variant on
    # (a) population health, which affects
    #       i. birth and
    #       ii. death rate
    # (b) approval - more upset people get, the more they leave the state. The happier, the more immigrants
    #               (which could lead to other political crises)

    # load game_data

    # get current turn


    def population_change():

        #       get current birth rate:
        #       a. random number modified by health_level
        #       b. and healthcare budget/policy (TBD)
        #       c. and religiousity
        #       d. and economy (TBD)
        #       based on world averages for first world nations:
        #       birth rate between 11 - 15 per 1, 000 people death rate between 6 - 10 per 1, 000 people
        #               or like 13 with SD of 2
        #       need to adjust by turn length, is it a week? if so, like 12/52 per 1,000 people
        #       DO: it would be cool to have a birth rate that is historical - like it's part of the culture

        # build modifier
        base_avg = 50
        mu = 13
        sigma = 2
        health_level = game_data[f'turn{current_turn}']['health_level']
        religious_level = game_data[f'turn{current_turn}']['religious_level']

        pop_health_modifier = (health_level-base_avg)/base_avg   #% that health_level is less than average
        pop_religious_modifier = (religious_level-base_avg)/base_avg
        pop_total_modifier = pop_health_modifier + pop_religious_modifier
        # pass it into the random number generator
        birth_rate = val_from_normal_dist(mu=mu*(1+pop_total_modifier), sigma=sigma)

        # death rate
        mu=8
        sigma=2
        death_rate = val_from_normal_dist(mu=mu*(1-pop_health_modifier), sigma=sigma)

        game_data[f'turn{current_turn}']['birth_rate'] = birth_rate
        game_data[f'turn{current_turn}']['death_rate'] = death_rate

        return birth_rate, death_rate


    birth_rate, death_rate = population_change()

    def change_in_politics():

        pass
        # change in party memberships
        # increase/decrease in extremists

    def approval_change():

        pass

        # by subgroups
        # multiply by subgroups portion of population * pop
        # calculate total approval from the sum of the subgroups

    def update_population_values():

        # we want to save the birth and death rates for plotting
        # but need to use the x/365 to make actual population adjustments, assuming we're doing weeks
        current_population = game_data[f'turn{current_turn}']['pop']
        births = current_population*birth_rate/turn_length/1000
        deaths = current_population*death_rate/turn_length/1000
        net_pop_change = births-deaths
        new_pop = int(current_population + net_pop_change)
        # print(f"current pop {current_population}")
        # print(f"new pop {new_pop}")

        game_data[f'turn{current_turn}']['pop'] = new_pop
        game_data[f'turn{current_turn}']['birth_rate'] = birth_rate
        game_data[f'turn{current_turn}']['death_rate'] = death_rate

        return new_pop, birth_rate, death_rate

    # test other values, like really unhealthy pop - will it decrease?

    def update_turn():

        # increment turn
        new_pop, birth_rate, death_rate = update_population_values()
        game_data[f'turn{current_turn}']['pop'] = new_pop
        game_data[f'turn{current_turn}']['birth_rate'] = birth_rate
        game_data[f'turn{current_turn}']['death_rate'] = death_rate

        with open("data/turn_dat.json", "r") as jsonFile:
            orig_game_data = json.load(jsonFile)

        orig_game_data['game_dat']['turn'] = next_turn
        orig_game_data[f'turn{next_turn}'] = game_data[f'turn{current_turn}']

        # save new json
        with open(f'data/turn_dat.json', 'w') as f:
            json.dump(orig_game_data, f)
            # print('game data saved to data/game_dat.json')

    update_turn()


if __name__ == "__main__":
    new_turn()
