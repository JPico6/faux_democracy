from create_world import State
import json

new_game = False

if new_game:
#    turn = 1

# 1. ititiate game

    # jsondata = {}
    # agent = {}
    # content = {}
    # agent['agentid'] = 'john'
    # content['eventType'] = 'view'
    # content['othervar'] = "new"
    #
    # jsondata['agent'] = agent
    # jsondata['content'] = content
    # print(json.dumps(jsondata))


    # A. initiate world
    game_data = {}
    state1 = {}
    game_dat = {}
    game_dat['turn'] = 1

    # b. initiate state(s)
    state1 = State()
    state1_attributes = state1.generate_attributes()
    print(state1_attributes)
    game_data['game_dat'] = game_dat
    game_data['state1'] = state1_attributes
    #game_data = json.dumps(game_data)
    print(game_data)

    with open('data/turn_dat.json', 'w') as f:
        json.dump(game_data, f)


if not new_game:

    # load game data
    f = open('data/turn_dat.json')
    game_data = json.load(f)

    print(game_data.get('state1'))

    # c. generate state report for player
        # i. basic population attributes (which are shared, which are hidden?)
        # ii. random events
        # iii. fixed events
    # d. player decisions
        # i. economic (spending)
        # ii. cultural
        # iii. ...


# run turn
    # 1. update state characteristics
        #
    # 2. check for random and fixed events

# example of updating pop and religious level:
#ex_dict = {'pop': 1.08, 'religious_level': 0.91}
#state1.update_attributes(ex_dict)
#print(vars(state1))

#turn = turn+1
#back up prior game data before overwriting it