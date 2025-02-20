metre = float(input("How many meters do you wanna know? "))
centimetres = metre * 100
millimetre = metre * 1000
decimeter = metre * 10
decameter = metre / 10
hectometer = metre / 100
kilometer = metre / 1000


print("{:.1f} metre in:\nkm: {}\nhm: {}\ndam: {}\ndm: {}\ncm: {}\nmm: {}".format(metre,kilometer,hectometer,decameter,decimeter,centimetres,millimetre))