import random
from math import sqrt
#class of Emitter, who puts stocks up for sale
class Emitter:
    def __init__(self, **kwargs):
        self.agency = kwargs.get("agency", 0)
        self.id = 'e'
        self.numStocks = kwargs.get("numStocks", 100)
        self.numObligations = kwargs.get("numObligations", 100)
        self.location = (random.uniform(0, 1), random.uniform(0, 1))
        self.price = self.numStocks / self.agency / sqrt(self.agency)


    def sell_stocks(self, request_stocks):
        if request_stocks < self.numStocks:
            numStocks = numStocks - request_stocks

#class of Broker, who help buy stocks and get revenue from profit
class Broker:
    def __init__(self, percent):
        self.percent = percent #revenue percent of profit
        self.id = 'b'
        self.location = (random.uniform(0, 1), random.uniform(0, 1))

    # def buy_stocks(self):


#class of Investor, who buy stocks and pays the broker
class Investor:
    def __init__(self, budget):
        self.budget = budget
        self.id = 'i'
        self.location = (random.uniform(0, 1), random.uniform(0, 1))

def get_x(a, b):
    try:
        m = (a+b)//2
        r = random.uniform(a, b)
        if a <= r < m:
            x = sqrt(r*(m-a)) + a
        else:
            x = b - sqrt((b-a-r)*(b-m))
    except ValueError:
        x = 1
    return x, m

def triangular_distr(a, b):
    temp1 = get_x(a, b)
    x = temp1[0]
    m = temp1[1]
    res = 0
    if x < a:
        res = 0
    elif a <= x < m:
        res = ((x-a)**2)/(m-a)
    elif m <= x < b:
        res = (b-a) - ((b-x)**2)/(b-m)
    else:
        res = 1
    return res

#the main function for initialize players on the financial market
def initialize(players, numEmitters, numBrokers, numInvestors, numAgency, numStocks, numObligations):
    for _ in range(numEmitters):
        agency = random.choice([i for i in range(1, numAgency+1)])
        emitter = Emitter(agency=agency, numStocks=numStocks, numObligations=numObligations)
        players.append(emitter)

    for _ in range(numBrokers):
        percent = random.uniform(0, 1)
        broker = Broker(percent)
        players.append(broker)

    for _ in range(numInvestors):
        budget = triangular_distr(100, 1000000)
        investor = Investor(budget)
        players.append(investor)

players = []
numEmitters = 10
numBrokers = 40
numInvestors = 100
numAgency = random.randint(0, 10)
numStocks = triangular_distr(50, 200)
numObligations = triangular_distr(10, 100)

def simulation():
    for player in players:
        if player.id == 'e':
            return True

if __name__ == "__main__":
    initialize(players, numEmitters, numBrokers, numInvestors, numAgency, numStocks, numObligations)
    print(simulation())
# print(players[0].location)
