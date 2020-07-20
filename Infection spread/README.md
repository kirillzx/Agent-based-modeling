# ABM of epidemic spread
This research devoted to modeling the epidemic spread. In this model agents have one status of four possbile: susceptible, infected, healthy, recovered. The author's model name is HSEIR-model.



initial population|intermediate result|final result
---|---|---
<img src="https://psv4.userapi.com/c856428/u451824612/docs/d6/d49feeddfbdf/Snimok_Ekrana_63.png?extra=UmCI9oGLweiEQvelVyuSFw9EUDr_EexH-P0ERuLyo6JfAhT2POy5M2-0ajXFG-Kyv7j8yfP7aTEYB3PmaIbeL7czdO7WS1EO71zj-5k2BSJnmwN0rmFDpGQMV0IeScEENpajtbdjsSYorY4f_AaR3iw" width=400 height=400>|<img src="https://psv4.userapi.com/c856428/u451824612/docs/d9/0d390ad92a59/Snimok_Ekrana_64.png?extra=fmGMQ842ckH5G7gbl0RnJdsS5VuaXj49omf5YRLsXbvh5yH7z_NdFy8b2emrVLPhpj4k_JjJjTiJUHHtO5uTKQ62LX8zb8HC_0L-UxJK-N8FGJzIKJBmZpt0MFaA46smF1hhQvVEktpYnynXXHUnM1o" width=400 height=400>|<img src="https://psv4.userapi.com/c856428/u451824612/docs/d9/6eb56e9664fc/Snimok_Ekrana_65.png?extra=Z8mpolx5BOqsN7x4YldXpdALKgsYa5cmCpm5MbM1b1eBd01P6iXRVGilWs-BsQaXycMfkGObBYd1Kkeg65luOd6hY3495ALG3BJONOGMiAtQaFVZZ1FwrvgtaQ-RSc7N49dqf_PVURfkQNNT_NDarVI" width=400 height=400>

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
black|susceptible
orange|exposed
red|infected
blue|recovered
