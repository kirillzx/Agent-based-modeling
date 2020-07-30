# Agent-based modeling
These works are devoted to the study agent based models of surrounding world.

*Telegram: @kirillzx*
# Epidemic spread
This research devoted to modeling the epidemic spread. In this model agents have one status of four possbile: susceptible, infected, healthy, recovered. The author's model name is HSEIR-model.

initial population|intermediate result|final result
---|---|---
<img src="https://github.com/kirillzx/Agent-based-modeling/raw/master/images/step1.jpg" width=250 height=250/>|<img src="https://github.com/kirillzx/Agent-based-modeling/raw/master/images/step2.png" width=250 height=250/>|<img src="https://github.com/kirillzx/Agent-based-modeling/raw/master/images/step3.png" width=250 height=250/>

The number of agent groups at each step without isolation

<img src="https://github.com/kirillzx/Agent-based-modeling/raw/master/images/plot1.png" width=400 height=300/>
The number of agent groups at each step with isolation

<img src="https://github.com/kirillzx/Agent-based-modeling/raw/master/images/plot2.png" width=400 height=300/>
contacts occur with a certain probability

<img src="https://github.com/kirillzx/Agent-based-modeling/raw/master/images/probability.png" width=500 height=100/>

Variables|Meanings
---|---
num_p|the number of population
num_inf|the beginning percent of infected people
death_limit|the age at which people with low immunity die
incubation_period|the time after exposed people become infected
delta|the contact rate
k|the number of contacts (different for each agent)

color|status
---|---
green|healthy
green|susceptible
orange|exposed
red|infected
blue|recovered




