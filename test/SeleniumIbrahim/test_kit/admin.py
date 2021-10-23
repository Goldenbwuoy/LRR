from actor import Actor
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, traceback

class Admin(Actor):
	def __init__(self, password, student_id, utility):
		super().__init__(password, student_id)
		self.utility = utility


	def create_new_account(self, acc_id, type="TA"):
		"""This method automates and insturctor creating new account from
		"Admin" page in LRR.

		Parameters:
		- type: string
			instructor: creates a new instructor account.
			TA: creates a new teaching assistant account, This is the default.
		- acc_id: string
			account ID.

		Returns:
			- 0 on success.
			- 1 on failure to complete case execution.
		"""

		try:
			#Initiate driver session and login
			driver = self.utility.login(self)

			#Locate "Admin" tab.
			wait = WebDriverWait(driver, 10)
			admin = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/form/a[1]")))
			admin.click()

			#Locate "Create Lecturer/TA account" form
			wait2 = WebDriverWait(driver, 10)
			new_account_form = wait2.until(EC.presence_of_element_located((By.ID, "frm_create_acc")))

			#Fill in the form fields
			name_field = new_account_form.find_element(By.XPATH, "//input[@name='fullname']")
			f_name = self.utility.random_string(4)
			l_name = self.utility.random_string(5)
			name_field.send_keys(f_name+" "+l_name)

			email_field = new_account_form.find_element(By.XPATH, "//input[@name='email']")
			email_field.send_keys(f_name+"."+l_name+"@testing.com")

			id_field = new_account_form.find_element(By.XPATH, "//input[@name='passport']")
			id_field.send_keys(acc_id)

			#If "Lecturer" is specified in type parameter, select Lecturer account type, else use default
			if type == "Lecturer":
				type_radio = new_account_form.find_element(By.XPATH, "//input[@value='Lecturer']")
			else:
				type_radio = new_account_form.find_element(By.XPATH, "//input[@value='TA']")

			type_radio.click()

			submit_btn = new_account_form.find_element(By.XPATH, "//input[@type='submit'][@value='Create']")
			submit_btn.click()

			return 0

		except:
			print("There was a problem executing this test case")
			print("Error in \"create_new_account()\" method, see error_log.txt for more details")
			err_msg = traceback.format_exc()
			self.utility.log_error(err_msg)
			print("Treminating session")
			self.utility.killSession(driver)
			return 1

	def batch_create_acc(self, lst):
		"""This method automates an instructor batch creating new student account
		under "Admin" tab.

		Paramaeters:
		- lst: list
			A list of student number strings to be batch created.

		Return:
			- 0 on success
			- 1 on failure to complete case execution.
		"""

		try:
			#Initiate and login
			driver = self.utility.login(self)

			#Locate the "Admin" tab.
			wait = WebDriverWait(driver, 10)
			admin = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/form/a[1]")))
			admin.click()

			#Navigate to "Batch create form"
			wait2 = WebDriverWait(driver, 10)
			batch_tab = wait2.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/ul/li[2]/a")))
			batch_tab.click()

			#Fill in the form
			wait3 = WebDriverWait(driver, 10)
			batch_form = wait3.until(EC.presence_of_element_located((By.ID, "frm_batch_acc")))
			
			text_area = batch_form.find_element(By.XPATH, "//textarea[@name='users']")
			for i in range(len(lst)):
				text_area.send_keys(lst[i]+" ")

			submit_btn = batch_form.find_element(By.XPATH, "//input[@type='submit'][@value='Create All']")
			submit_btn.click()

		except:
			print("There was a problem executing this test case")
			print("Error in \"batch_create_acc()\" method, see error_log.txt for more details")
			err_msg = traceback.format_exc()
			self.utility.log_error(err_msg)
			print("Treminating session")
			self.utility.killSession(driver)
			return 1

	def account_block_activate(self, op):
		"""This method automates an instructor blocking/activating an existing account
		under "Admin" page.

		Parameters:
		op: string
			- block: to block first account on existing account table
			- activate: to activate first account on existing account table

		Returns:
			- 0 on success
			- 1 on failure to complete case execution.
		"""
		try:
			#Initiate web driver session and login
			driver = self.utility.login(self)

			#Locate the "Admin" tab.
			wait = WebDriverWait(driver, 10)
			admin = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/form/a[1]")))
			admin.click()

			#Navigate to "Exisitin Accounts" table
			wait2 = WebDriverWait(driver, 10)
			exist_acc_tab = wait2.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/ul/li[3]/a")))
			exist_acc_tab.click()		
			
			#Alternate between block and activate
			if op == "block":
				#Locate first account and block it on existing account table
				wait3 = WebDriverWait(driver, 10)
				button = driver.find_element_by_id("block_acc_1")
			elif op == "activate":
				wait3 = WebDriverWait(driver, 10)
				button = driver.find_element_by_id("activate_acc_1")
			
			driver.execute_script("arguments[0].click();", button)

			#Confirm pop-up alert
			wait4 = WebDriverWait(driver, 10)
			alert = wait4.until(EC.alert_is_present())
			alert.accept()

			return 0

		except:
			print("There was a problem executing this test case")
			print("Error in \"account_block_activate()\" method, see error_log.txt for more details")
			err_msg = traceback.format_exc()
			self.utility.log_error(err_msg)
			print("Treminating session")
			self.utility.killSession(driver)
			return 1

	def assign_TA(self):
		"""This method automates an instructor assigning a TA to a course
		under "Admin" page.

		Returns:
			- 0 on success
			- 1 on failure to complete case execution. 
		"""
		try:
			#Initiate web driver session and login
			driver = self.utility.login(self)

			#Locate the "Admin" tab.
			wait = WebDriverWait(driver, 10)
			admin = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/form/a[1]")))
			admin.click()

			#Navigate to "Existing Courses" table.
			wait2 = WebDriverWait(driver, 10)
			courses_table = wait2.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/ul/li[2]/a")))
			courses_table.click()

			#Assign TA to the first course in "Existing Courses" table
			wait3 = WebDriverWait(driver, 10)
			drop_menu_form = wait3.until(EC.presence_of_element_located((By.XPATH, "//*[@id='menub']/table/tbody/tr[2]/td[5]/form")))
			assign_btn = drop_menu_form.find_element(By.XPATH, "//input[@type='submit'][@value='assign']")
			assign_btn.click()

			return 0

		except:
			print("There was a problem executing this test case")
			print("Error in \"assign_TA()\" method, see error_log.txt for more details")
			err_msg = traceback.format_exc()
			self.utility.log_error(err_msg)
			print("Treminating session")
			self.utility.killSession(driver)
			return 1