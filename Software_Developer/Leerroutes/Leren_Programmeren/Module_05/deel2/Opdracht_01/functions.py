import math
import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, \
    COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY


##################### M04.D02.O2 #####################

def copper2silver(amount: int) -> float:
    return amount / 10


def silver2gold(amount: int) -> float:
    return amount / 5


def copper2gold(amount: int) -> float:
    silver = copper2silver(amount)
    return silver2gold(silver)


def platinum2gold(amount: int) -> float:
    return amount * 25


def getPersonCashInGold(personCash: dict) -> float:
    gold = personCash['gold']
    gold += copper2gold(personCash['copper'])
    gold += silver2gold(personCash['silver'])
    gold += platinum2gold(personCash['platinum'])
    return gold


##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people: int, horses: int) -> float:
    copperCosts = JOURNEY_IN_DAYS * (people * COST_FOOD_HUMAN_COPPER_PER_DAY)
    gold = copper2gold(copperCosts)
    copperCosts = JOURNEY_IN_DAYS * (horses * COST_FOOD_HORSE_COPPER_PER_DAY)
    gold += copper2gold(copperCosts)
    return round(gold, 2)


##################### M04.D02.O5 #####################

def getFromListByKeyIs(list: list, key: str, value: any) -> list:
    listing = []
    for x in list:
        if x[key] == value:
            listing.append(x)
    return listing


def getAdventuringPeople(people: list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)


def getShareWithFriends(friends: list) -> list:  # Hier stond eerst int, klopte dit?
    return getFromListByKeyIs(friends, "shareWith", True)


def getAdventuringFriends(friends: list) -> list:
    listing = []
    adv = getAdventuringPeople(friends)
    share = getShareWithFriends(friends)
    for x in adv:
        if x['adventuring'] and x['shareWith'] and x not in listing:
            listing.append(x)
    for y in share:
        if y['adventuring'] and y['shareWith'] and y not in listing:
            listing.append(y)
    return listing


##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people: int) -> int:
    return math.ceil(people / 2)


def getNumberOfTentsNeeded(people: int) -> int:
    return math.ceil(people / 3)


def getTotalRentalCost(horses: int, tents: int) -> float:
    tenties = math.ceil(JOURNEY_IN_DAYS / 7) * (tents * COST_TENT_GOLD_PER_WEEK)
    horsies = horses * (JOURNEY_IN_DAYS * COST_HORSE_SILVER_PER_DAY)
    return tenties + silver2gold(horsies)


##################### M04.D02.O7 #####################

def getItemsAsText(items: list) -> str:
    itemText = []
    for item in items:
        itemText.append(f"{item['amount']}{item['unit']} {item['name']}")
    return ', '.join(itemText)


def getItemsValueInGold(items: list) -> float:
    value = float()
    for item in items:
        amount = item['amount']
        pricetype = item['price']['type']
        price = item['price']['amount']

        if pricetype == 'copper':
            value += amount * copper2gold(price)
        elif pricetype == 'silver':
            value += amount * silver2gold(price)
        elif pricetype == 'platinum':
            value += amount * platinum2gold(price)
        else:
            value += price
    return value


##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people: list) -> float:
    pass


##################### M04.D02.O9 #####################

def getInterestingInvestors(investors: list) -> list:
    pass


def getAdventuringInvestors(investors: list) -> list:
    pass


def getTotalInvestorsCosts(investors: list, gear: list) -> float:
    pass


##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    pass


def getJourneyInnCostsInGold(nightsInInn: int, people: int, horses: int) -> float:
    pass


##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold: float, investors: list) -> list:
    pass


def getAdventurerCut(profitGold: float, investorsCuts: list, fellowship: list) -> float:
    pass


##################### M04.D02.O13 #####################

def getEarnigs(profitGold: float, mainCharacter: dict, friends: list, investors: list) -> list:
    pass


##################### view functions #####################
def print_colorvars(txt: str = '{}', vars: list = [], color: str = 'yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']), vars)
    print(txt.format(*vars))


def print_title(name: str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')


def print_chapter(number: int, name: str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')


def nextStep(secwait: int = 1) -> None:
    print('')
    time.sleep(secwait)


def ifOne(amount: int, yes: str, no: str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()
