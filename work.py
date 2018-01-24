class animal():
	eyes = 2	
	weight = 0	# kg
	speech = ''

	def __init__(self, weight, speech):
		self.weight = weight
		self.speech = speech

	def speak(self):
		print(self.speech)

class bird(animal):
	wings = True
	fly_skill = None

	def __init__(self, weight, fly_skill, speech):
		super().__init__(weight, speech)
		self.fly_skill = fly_skill

class artiodactyla(animal):
	legs = 4
	speed = None

	def __init__(self, weight, speed, speech):
		super().__init__(weight, speech)
		self.speed = speed

duck = bird(3, 10, 'Wack, wack!')
hen = bird(5, 2, 'Kooo, kooo...')
goose = bird(10, 5, 'Kra, kra!')

print('Утки говорят:', end=' ')
duck.speak()
print('Курицы говорят:', end=' ')
hen.speak()
print('Гуси говорят:', end=' ')
goose.speak()

cow = artiodactyla(150, 20, 'Muuuuuuu...')
goat = artiodactyla(30, 25, 'Meeeeeee...')
sheep = artiodactyla(50, 30, 'Beeeeeee...')
pig = artiodactyla(100, 15, 'Hru, hru!')
print('Коровы говорят:', end=' ')
cow.speak()
print('Козы говорят:', end=' ')
goat.speak()
print('Овцы говорят:', end=' ')
sheep.speak()
print('Свиньи говорят:', end=' ')
pig.speak()
