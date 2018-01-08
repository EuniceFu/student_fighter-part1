class StudentFighter(object):
	def __init__(self, strength, health, name):
		self.strength = strength
		self.name = name
		self.health = health

Eunice = StudentFighter(strength=3, health=100, name="Eunice")
Katerina = StudentFighter(strength=5, health=100, name="Katerina")

print(Eunice.name, Eunice.strength, Eunice.health)
print(Katerina.name, Katerina.strength, Katerina.health)
