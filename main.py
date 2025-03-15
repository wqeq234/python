import datetime 

class Logger:
	def __init__(self, time, action, nickname, logs):
		self.time = time 
		self.action = action 
		self.nickname = nickname
		self.logs = logs

	def create_logs(self):
		log = f"{self.time}: {self.nickname} - {self.action}."
		self.logs.append(log)

logs = []

while True:
	nickname = input("Input nickname: ")
	path = input("Input path: ")

	select_action = input('''
	1. Broke block.
	2. Place block.
	3. Hit block.

	Select action: ''')

	time_now = datetime.datetime.now()
	time = time_now.strftime("%X")

	if select_action == "1":
		action = "Broke block"
	elif select_action == "2":
		action = "Place block"
	elif select_action == "3":
		action = "Hit block"
	else:
		print("Error: Invalid selection")
		continue

	logger = Logger(time = time, action = action, nickname = nickname, logs = logs)
	logger.create_logs()

	question = input("Exit/Continue (e/c): ").lower()

	if question == "e":
		path = input("Input path: ")
		with open(f"{path}\\log.txt", "w") as file:
			for log in logs:
				file.write(f"{log}\n")
		print("Logs saved. Exiting...")
		exit()
	elif question == "c":
		continue
	else:
		print("Error: Invalid input")
		exit()
