import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
plt.style.use('ggplot')

status = ['a', 'p']
types = ['R', 'AA', 'BA', 'P']
agents_num = 20
size = 50


class Agent:
    def __init__(self, agents_num):
        self.id = np.array(range(agents_num))

        self.x = np.random.randint(0, size, agents_num)
        self.y = np.random.randint(0, size, agents_num)
        self.age = np.random.randint(50, 100, agents_num)
        self.aw_vector = np.random.randint(0, 2, agents_num)

    def make_agent(self, status, types, age, inf):
        return [status, types, age, inf]

    def make_population(self, status, types, agents_num):

        population = []

        for i in range(agents_num):

            agent = self.make_agent(np.random.choice(status), np.random.choice(types), np.random.choice(self.age), self.aw_vector[i])
            population.append(agent)
        return population

    def count(self, population):
        t = 0.
        for agent in population:
            if agent[0] == 'a':
                t += 1
        return t / len(population)

    def choose_pair(self, population):
        i = np.random.randint(0, len(population) - 1)
        j = np.random.randint(0, len(population) - 1)

        while i == j:
            j = np.random.randint(0, len(population) - 1)

        return [population[i], population[j]]

    def interact(self, listener, producer):
        #if (listener[1] == 'R' or listener[1] == 'AA') and (producer[1] == 'R' or producer[1] == 'AA'):
        #self.age -= 1
        #if self.age
            if listener[0] == 'a' and producer[0] != 'a' and listener[3] == 1 :
                producer[0] = 'a'
                return producer
            elif listener[0] == 'a' and producer == 'a':
                return producer
            elif listener[0] != 'a' and producer[0] == 'a' and producer[3] == 1 :
                listener[0] = 'a'
                return listener
            else:
                listener[0] = np.random.choice(['a', 'p'])
                return listener

agents = Agent(agents_num)
population = agents.make_population(status, types, agents_num)
#print(agents.id)
#print(agents.x)
#print(agents.y)
#print(agents.count(population))
pair = agents.choose_pair(population)
#print(pair)
#print(agents.interact(pair[0], pair[1]))


def simulate(agents_num, k):
    population = agents.make_population(status, types, agents_num)

    proportion = []

    for i in range(k):
            pair = agents.choose_pair(population)
            agents.interact(pair[0], pair[1])
            proportion.append(agents.count(population))
            agents.choose_pair(population)[0][0] = 'p'
    return population, proportion

new_pop, proportion = simulate(agents_num, 100)
print(new_pop)

plt.plot(proportion)
plt.title('Changes in the proportion of active users over time')
plt.xlabel('Time')
plt.ylabel('Proportion of active users')
plt.show()
#plt.savefig('graphic.jpg')
