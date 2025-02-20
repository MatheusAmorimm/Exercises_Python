city = str(input("What`s your city name? ")).strip()

testCity = (city.upper()[:5] == "SANTO")

print("Sua cidade comeca com SANTO: {}". format(testCity))