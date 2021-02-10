import csv 

with open('user_info.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(f'Column names are {" , ".join(row)}')
			line_count += 1
		else:
			print(f'\t{row[0]} is {row[1]} years old, weighs {row[2]} pounds, is {row[3]} inches tall.\n\t{row[0]}\'s maxes are:\n\tbench: {row[4]}\n\tsquat: {row[5]}\n\tdeadlift: {row[6]}')
			
		



with open('another_user.csv', mode= 'w') as user_file:
	user_writer = csv.writer(user_file, delimiter=',', quotechar= '"', quoting = csv.QUOTE_MINIMAL)
	name = input('What\'s your name ?\n')
	age = input('How old are you ?\n')
	weight = input('How much do you weigh ?\n')		
	height = input('How tall are you ?\n')
	benchmax = input('What\'s your Bench press max ?\n')
	squatmax = input('What\'s your Squat max ?\n')
	deadliftmax = input('What\'s your deadlift max ?\n')
	print(f'{name}\n {age}\n {weight}\n {height}\n {benchmax}\n {squatmax}\n {deadliftmax}\n')
	validation_info = input('Is this information all correct ?')

	if validation_info == 'yes' or validation_info == 'Yes':
		user_writer.writerow(f'{name},{age},{weight},{height},{benchmax},{squatmax},{deadliftmax}')

	else:
		print('Start Over')

