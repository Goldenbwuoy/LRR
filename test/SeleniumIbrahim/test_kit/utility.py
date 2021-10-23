from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import datetime
import traceback

class MyUtility:

	"""This class is a utility class contains all the essential methods needed
	for various functions that are not bond for a specific user.

	"""
	
	def __init__(self, page_url):
		self.page_url = page_url

	def setPageURL(self, page_url):
		
		"""This method sets a new page url, it might be used to initiate new webdriver
		session with specific page of LRR in run-time.

		"""
		self.page_url = page_url
	
	def getPageURL(self):

		"""This method returns the page url provided when MyUtility object is created.

		Returns:
		- page_url: string

		"""
		return self.page_url

	def getSession(self):
		"""This method initiate new selenium webdriver session.

		Returns:
		- driver: selenium.webdriver object.
		1 on failure to complete case execution.

		"""
		try:
			driver = webdriver.Chrome()
			driver.get(self.getPageURL())
			return driver
		except:
			print("There was initiating a new session")
			print("Error in \"getSession()\" method, see error_log.txt for more details")
			err_msg = traceback.format_exc()
			self.log_error(err_msg)
			print("Treminating session")
			self.killSession(driver)
			return 1


	def login(self, obj):

		"""This method automates the login process for the instructor, it's needed for use 
		internally in order to carry on other automation operations that requires login beforehand.

		Returns: 
		- driver: logged in selenium.webdriver object.
		1 on failure to complete case execution.		 

		"""
		try:
			driver = self.getSession()
			WebDriverWait(driver, 10)
			username = driver.find_element(By.ID, "uname")
			username.send_keys(obj.getStudentID())
			password = driver.find_element(By.ID, "upass")
			password.send_keys(obj.getPassword())
			login = driver.find_element(By.ID, "log_btn")
			login.click()
			return driver
		except:
			print("There was a problem executing this test case")
			print("Error in \"login()\" method, see error_log.txt for more details")
			err_msg = traceback.format_exc()
			self.log_error(err_msg)
			print("Treminating session")
			self.killSession(driver)
			return 1

	def signup(self, name, email, password):

		"""This method automates student registration process.

		Parameters:
		- name: student name string.
		- email: student email string.
		- password: student password string.

		Returns:
		0 on success
		1 on failure to complete case execution.		
		
		"""
		try:
			#Initiate a new webdriver session
			driver = self.getSession()
			wait = WebDriverWait(driver, 10, ignored_exceptions='StaleElementReferenceException')

			#Locate the signup form and fill in the student ID
			signup_form = wait.until(EC.presence_of_element_located((By.ID, "signup_frm")))
			student_id = signup_form.find_element(By.ID, "std_id")
			std_id = self.fetch_new_student_id()
			student_id.send_keys(std_id)
			next_btn = signup_form.find_element(By.ID, "next_btn")
			next_btn.click()

			#Fill in student data and sign up.
			wait2 = WebDriverWait(driver, 10, ignored_exceptions='StaleElementReferenceException')
			reg_form = wait2.until(EC.presence_of_element_located((By.ID, "frm")))
			name_field = reg_form.find_element(By.XPATH, "//form/input[2]")
			name_field.send_keys(name)
			email_field = reg_form.find_element(By.XPATH, "//form/input[3]")
			email_field.send_keys(email)
			password_field = reg_form.find_element(By.XPATH, "//form/input[4]")
			password_field.send_keys(password)
			re_password_field = reg_form.find_element(By.XPATH, "//form/input[5]")
			re_password_field.send_keys(password)
			submit = reg_form.find_element(By.XPATH, "//form/input[6]")
			submit.click()
			return 0

		except:
			print("There was a problem executing this test case")
			print("Error in \"signup()\" method, see error_log.txt for more details")
			err_msg = traceback.format_exc()
			self.log_error(err_msg)
			print("Treminating session")
			self.killSession(driver)
			return 1			

	def killSession(self, driver):
		
		"""This method terminates the current running selenium webdriver session.

		"""
		
		driver.close()

	def getTime(self):
		
		"""This method provides the now machine local time formated like "hhmmss" for example,
		18:30:40 is formatted as "183040". Needed to construct unique name strings.

		Returns:
		- time: formatted machine local time.
		"""
		
		time = datetime.datetime.today().strftime("%H%M%S")
		return time
		
	def getTodayDate(self):

		"""This method provides today's date formatted as "ddmmyy" for example,
		18/02/2021 is formatted as "18022021". Needed to construct unique name strings.

		Returns:
		- date: formatted date string.

		"""
		date = datetime.datetime.today().strftime ('%d%m%Y')
		return date
	
	def getTomorrowDate(self):
		
		"""This method provides tomorrow's date formatted as "ddmmyyyy" for example,
		18/02/2021 is formatted as "18022021". Needed to test extend deadlines function.

		Returns:
		- date: formatted date string.

		"""		
		date = datetime.datetime.today() + datetime.timedelta(days=1)
		date_str = date.strftime('%d%m%Y')
		return date_str

	def getYesterdayDate(self):

		"""This method provides yesterday's date formatted as "ddmmyyyy" for example,
		18/02/2021 is formatted as "18022021". Needed to test extend deadlines function.

		Returns:
		- date: formatted date string.

		"""
		date = datetime.datetime.today() - datetime.timedelta(days=1)
		date_str = date.strftime('%d%m%Y')
		return date_str

	def storeCourseCode(self, course_code):

		"""This method stores the uniquely created course code from a combination of date and time
		in a text file for reuse in other automation operations.

		"""
		file = open("./course_code.txt","w")
		file.write(course_code)
		file.close()

	def getCourseCode(self):

		"""This method retrives the stored course code from the text file to be used as reference
		for various automation operations that requires access to a course portal.

		Returns:
		- code: string.
		"""
		file = open("./course_code.txt", "r")
		code = file.readline()
		file.close()
		return code

	def fetch_new_student_id(self):

		"""This method provides pre-defined student ID in a file to be used
		with signup automation operation. See "student_ids.txt" file for details.

		Returns:
		- std_id: string
			A student ID string from student_ids.txt file. 
			Note: the returned ID will be removed from the file.

		"""

		file = open("student_ids.txt", "r")
		lines = file.readlines()
		file.close()

		std_id = None
		for line in lines:
			if line[0] == "#": 		#skip comments in the file
				continue
			std_id = line
			break

		if std_id != None:
			#remove the recently fetched student ID from file
			elem_idx = lines.index(std_id) 	# 
			del lines[elem_idx]
		else:
			#if all student IDs in file are exceeded, abort
			print("No more student IDs available in file.")
			return


		#write the file lines back after removing the fetched student ID
		file = open("student_ids.txt", "w+")
		for line in lines:
		    file.write(line)

		file.close()

		return std_id.strip('\n')

	def open_course_page(self, driver):
		"""This method redirects the webdriver to a course page identified by its course code
		fetched from 'course_code.txt' file.

		Paramaters:
		driver: a selenium webdriver object.

		Returns:
		0 on success
		1 on failure to complete case execution.

		"""
		try:
			wait = WebDriverWait(driver, 10)
			course_code = self.getCourseCode()
			course_card = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,str(course_code))))
			course_card.click()
		except:
			print("There was a problem executing this test case")
			print("Error in \"open_course_page()\" method, see error_log.txt for more details")
			err_msg = traceback.format_exc()
			self.log_error(err_msg)
			print("Treminating session")
			self.killSession(driver)
			return 1			

	def log_error(self, error_msg):
		"""This method formats and writes various error messages retrieved from
		the stacktrace into 'Error_log.txt' file for debugging.
		"""
		file = open("Error_log.txt","a")
		time = datetime.datetime.today().strftime("%H:%M:%S")
		date = datetime.datetime.today().strftime ('%d/%m/%Y')
		file.write("[ERROR]"+date+"-"+time+">"+error_msg+"\n")

	def random_string(self, ch):
		"""Creates a random literal string of length ch.
		"""
		ls = []
		for i in range(ch):
			ls.append(chr(random.randint(97,122)))

		return ''.join(ls)