# Agent-based modeling
These works are devoted to the study agent based models of surrounding world.

*Telegram: @kirillzx*
# Epidemic spread
This research devoted to modeling the epidemic spread. In this model agents have one status of four possbile: susceptible, infected, healthy, recovered. The author's model name is HSEIR-model.

initial population|intermediate result|final result
---|---|---
<img src="https://github.com/kirillzx/Agent-based-modeling/raw/master/images/step1.jpg" width=250 height=250/>|<img src="https://psv4.userapi.com/c856428/u451824612/docs/d9/0d390ad92a59/Snimok_Ekrana_64.png?extra=fmGMQ842ckH5G7gbl0RnJdsS5VuaXj49omf5YRLsXbvh5yH7z_NdFy8b2emrVLPhpj4k_JjJjTiJUHHtO5uTKQ62LX8zb8HC_0L-UxJK-N8FGJzIKJBmZpt0MFaA46smF1hhQvVEktpYnynXXHUnM1o" width=250 height=250>|<img src="https://psv4.userapi.com/c856428/u451824612/docs/d9/6eb56e9664fc/Snimok_Ekrana_65.png?extra=Z8mpolx5BOqsN7x4YldXpdALKgsYa5cmCpm5MbM1b1eBd01P6iXRVGilWs-BsQaXycMfkGObBYd1Kkeg65luOd6hY3495ALG3BJONOGMiAtQaFVZZ1FwrvgtaQ-RSc7N49dqf_PVURfkQNNT_NDarVI" width=250 height=250>

The number of agent groups at each step


<img src="https://psv4.userapi.com/c856428/u451824612/docs/d5/4702de8f3bfc/Snimok_Ekrana_66.png?extra=plwwf0Wpnkb4gTbI3shzj0_JGpngH0EFMgw0ut1DsIDx1NmU1_yNDvqqxgXiuIToV6s6DvSbkNArq_XJHu-05_DUhtASH6aEuGxpLR-RumQKIfHiksnY7C60mRgf9KvuiJ8uVHvcd_Z3hfaQ6FBEoJ0" width=400 height=300>

contacts occur with a certain probability

<img src="https://psv4.userapi.com/c856320/u451824612/docs/d3/35266b5a0fda/Snimok_Ekrana_67.png?extra=Dvz9aP7Udli-13eH04485Q3mDCTWdbruAlOCQsWSJfMoOOu7-7dgtb_DUU78bby2TVP0idvnLPVEQs47JaNOxJ0BtI_QCMgPLskAPCM3qcCDI4QjjuZrgTN34VShAYoHV_3deg8VetNvJwfwvqe2FgI" width=500 height=100>

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




