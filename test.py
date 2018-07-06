from crate import client

def get_bool(attr):
	if attr=="True":
		return True
	else:
		return False


class ControlDB():
	def __init__(self):
		self.connection = client.connect("http://localhost:4200/", username="crate")
		self.cursor = self.connection.cursor()
	def insert(self, input_id, input_retweeted):
		self.cursor.execute(
			"""INSERT INTO tweets (id, retweeted)
			VALUES (?, ?)""", (input_id, input_retweeted)
		)
	def update(self, input_set, input_id):
		self.cursor.execute(
			"""UPDATE tweets 
			SET retweeted=?
			WHERE id=?""",(input_set, input_id)
		)
	def delete(self, input_id):
		self.cursor.execute(
			"""DELETE from tweets 
			where id=?""", (input_id,)
		)
	def select(self, input_id):
		self.cursor.execute(
			"""SELECT * FROM tweets
			WHERE id=?""", (input_id,)
		)
		print(self.cursor.fetchmany(10))

def main():
	print("*** Hi! This is for CrateDB ***")
	DB = ControlDB()
	while True:
		opt = int(input("*** 1: insert  2: update  3: delete  4: select 0:finish***: "))
		if opt==1:
			in_id = input("input id: ")
			in_retweeted = get_bool(input("input retweeted: "))
			DB.insert(in_id, in_retweeted)
		elif opt==2:
			in_set = get_bool(input("input setup: "))
			in_id = input("input where: ")
			DB.update(in_set, in_id)
		elif opt==3:
			in_id = input("input where: ")
			DB.delete(in_id)
		elif opt==4:
			in_id = input("input where: ")
			DB.select(in_id)
		else:
			break
	print("*** Bye! ***")

main()