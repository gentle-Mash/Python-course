sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'

dictionary = {word:len(word) for word in sentence.split(" ")}
print(dictionary)



temperature_C = {
    'saturday':35,
    'sunday':34,
    'monday':36.5,
    'tuesday':34.5,
    'wednesday':37,
    'thursday':35.7,
    'friday':40,
}

temperature_F = {day:temperature*(9/5)+32 for (day, temperature) in temperature_C.items()}
print(temperature_F)