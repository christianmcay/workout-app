from WorkoutDict import workout

class Maxcalc:
	def __init__(self):
		print('This is a one rep max calcualtor')
		weight = input('Weight lifted\n')
		reps = input('How many reps\n')
		self.weight = weight
		self.reps = reps

		
	def formula4max(self):
		weight = int(self.weight)
		reps = int(self.reps)
		
		# Epley Formula
		epleymax = weight * (1 + (reps/30))
		# Brzycki Formula
		brzyckimax = weight * (36 /( 37 - reps))

		# McGlothin Formula
		mcglothinmax = (100 * weight) / (101.3 - 2.67123 * reps)

		average_max = (epleymax + brzyckimax + mcglothinmax) / 3

		print(f'With the Epley formula your max is {epleymax}')

		print(f'With the Brzycki formula your max is {brzyckimax}')

		print(f'With the McGlothin formula your max is {mcglothinmax}')

		print(f'Your average max is {average_max}')
         
		

maxtime = Maxcalc()
maxtime.formula4max()
workout()















