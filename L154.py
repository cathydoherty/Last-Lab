#Cathy Doherty and Amanda Miloserny
class Fabric:
    def __init__(self, countryOfOrigin, color):
        self.countryOfOrigin = countryOfOrigin
        self.color = color

    def __str__(self):
        return self.countryOfOrigin + "("+ str(self.color) + ")"

p1= Fabric("Italy", "red")

print(p1)
