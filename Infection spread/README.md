# ABM of epidemic spread
This research devoted to modeling the epidemic spread. In this model agents have one status of four possbile: susceptible, infected, healthy, recovered. The author's model name is SIHR-model.
initial population|result
---|---
<img src="https://psv4.userapi.com/c856436/u451824612/docs/d14/5e546bd10182/step_1.png?extra=FnssMp8f7Z8UyPeVp1bUvSVy5ZWKg4DvNbAR7JU-FUDaiY36IjiBJlPv3NFH2jfFwK2eFRey_s6D9XR4YYi0CRFxn0jVhqPaokg27yyv5cqWvJx0p9ohCr7PoT1GPg4-0paC8gh_smOBr96uLRHIUK4" width=400 height=400>|<img src="https://psv4.userapi.com/c856436/u451824612/docs/d17/6a5e05079c67/step_final.png?extra=QLj3pGvy_BvtlixavNyU3yzuY_YbM1dwYGZwk-iw6RsipG7jzidvCiPYKYHH2gLz6xtvy7tJokh4j68zW2hmKoFF98PRnrlwYZ2zxJC_OiepyiEbfbdDhvf2GvmRvIl5TF_g8Xv54Gemyq5hVNl9AB8" width=400 height=400>

Variables|Meanings
---|---
num_p|the number of population
num_inf|the beginning percent of infected people
death_limit|the age at which people with low immunity die
incubation_period|the time after exposed people become infected
delta|the contact rate
k|the number of contacts (different for each agent)

