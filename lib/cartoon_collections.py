def roll_call_dwarves(dwarves):
    number = 1
    for dwarf in dwarves:
        print(f"{number}. {dwarf}")
        number +=1


def summon_captain_planet(calls):
    new_calls = [call.title()+'!' for call in calls]
    return new_calls


def long_planeteer_calls(list):
    if [len(item) for item in list if len(item) > 4]:
        return True
    else:
        return False


cheeses = ["cheddar", "gouda", "camembert"]
def find_the_cheese(list):
    for food in list:
        if food in cheeses:
            return food
    return None
