#Lists for checkboxes, separate inputs for yes/no

score = 0

#Incentives for Environment
print("-------Environmental Incentives-------")
earth_hour = input("Have you participated in Earth Hour this year? ")
charity = input("Have you donated to any charities to support environmental incentives? ")

environment_mappings = {"yes": 1, "no": 0}
score += environment_mappings[earth_hour]
score += environment_mappings[charity]

#Sustainability
print("\n -------Sustainability-------")
print("Which of the following are applicable to your home?")
sustainability = [input("Rooftop Gardens "), input("Solar Panels on Roof ")]

sustainability_mappings = {"yes": 1, "no": 0}
score += sustainability_mappings[sustainability[0]]
score += sustainability_mappings[sustainability[1]]

print(score)
