class Actor:
	def __init__(self, password, student_id):
		self.password = password
		self.student_id = student_id

	def setPassword(self, password):
		self.password = password

	def setStudentID(self, student_id):
		self.student_id = student_id

	def getPassword(self):
		return self.password

	def getStudentID(self):
		return self.student_id