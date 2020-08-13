import random
from math import sqrt
#class of Emitter, who puts stocks up for sale
class Emitter:
    def __init__(self, **kwargs):
        self.agency = kwargs.get("agency", 1)
        self.numEmitters = kwargs.get("numEmitters", 10)
        self.id = 'e'
        self.numStocks = kwargs.get("numStocks", 100)
        self.numObligations = kwargs.get("numObligations", 100)
        self.location = (random.uniform(0, 1), random.uniform(0, 1))
        self.price = self.numStocks / self.numEmitters / sqrt(self.agency)
        self.period = kwargs.get("period", 30)
        # self.offer = self.numStocks//self.period
        self.exchange = False

    def offering_stocks(self):
        self.exchange = True

    def sell_stocks(self, request_stocks: int) -> int:
        stocks = 0
        if request_stocks < self.numStocks:
            stocks = request_stocks
            self.numStocks = self.numStocks - request_stocks
        elif request_stocks == self.numStocks:
            stocks = self.numStocks
            self.numStocks = 0
        else:
            if self.numStocks > 0:
                stocks = self.numStocks
                self.numStocks = 0
            else:
                stocks = 0
        return stocks


#class of Broker, who help buy stocks and get revenue from profit
class Broker:
    def __init__(self, percent):
        self.percent = percent #revenue percent of profit
        self.id = 'b'
        self.location = (random.uniform(0, 1), random.uniform(0, 1))
        self.stocks = [] #the list of stocks purchased fron different emitters
        self.investors = [] #the list of investors with he works

    def choose_emitters(self, emitters):
        return

    def buy_stocks(self, emitters: list):
        # for inv in self.investors:
        for emitter in emitters:

                try:
                    request = 100/len(emitters)/emitter.price
                    self.stocks.append((emitter, emitter.sell_stocks(int(request))))
                except ZeroDivisionError:
                    return

        return self.stocks


#class of Investor, who buy stocks and pays the broker
class Investor:
    def __init__(self, budget):
        self.budget = budget
        self.id = 'i'
        self.location = (random.uniform(0, 1), random.uniform(0, 1))
        self.perc_agreement = random.uniform(0, 1)
        self.broker = ''

    def find_broker(self, brokers: list):
        for agent in brokers:
            if self.perc_agreement >= agent.percent:
                self.broker = agent
                agent.investors.append(self)

        return self.broker

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
        res = 0.01
    elif a <= x < m:
        res = ((x-a)**2)/(m-a)
    elif m <= x < b:
        res = (b-a) - ((b-x)**2)/(b-m)
    else:
        res = 1
    return res

#the main function for initialize players on the financial market
def initialize(players, period, numEmitters, numBrokers, numInvestors, numAgency, numStocks, numObligations,\
                                list_emitters, list_brokers, list_investors):
    for _ in range(numEmitters):
        agency = random.choice([i for i in range(1, numAgency+1)])
        emitter = Emitter(agency=agency, numStocks=numStocks, numObligations=numObligations, period=period,\
                                    numEmitters=numEmitters)
        players.append(emitter)
        list_emitters.append(emitter)

    for _ in range(numBrokers):
        percent = random.uniform(0, 1)
        broker = Broker(percent)
        players.append(broker)
        list_brokers.append(broker)

    for _ in range(numInvestors):
        budget = triangular_distr(1000, 10000)
        investor = Investor(budget)
        players.append(investor)
        list_investors.append(investor)

players = []
list_emitters = []
list_brokers = []
list_investors = []
period = 24
numEmitters = 10
numBrokers = 40
numInvestors = 100
numAgency = random.randint(1, 10)
numStocks = random.randint(50, 200)
numObligations = random.randint(10, 100)

def simulation(period):
    # while period != 0:
        for player in players:
            if player.id == 'e':
                player.offering_stocks()
            if player.id == 'i':
                player.find_broker(list_brokers)
            if player.id == 'b':
                player.buy_stocks(list_emitters)
        period -= 1

if __name__ == "__main__":
    initialize(players, period, numEmitters, numBrokers, numInvestors, numAgency, numStocks, numObligations,\
                    list_emitters, list_brokers, list_investors)
    simulation(period)

print(players[22].stocks) #the broker bought stocks from certain emitters
print(players[70].broker.investors)
# print(list_investors[10].find_broker(list_brokers)) #the certain broker for investor
