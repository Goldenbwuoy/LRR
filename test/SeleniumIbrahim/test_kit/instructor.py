from actor import Actor
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, traceback

class Instructor(Actor):
	
	"""
	This class contains all the major scenarios an instructor system actor can execute
	automated by Selenium framework.

	Attributes:
	- password: password string.
	- student_id: student ID number (or Instructor ID).
	- utility: a utility object of the MyUtility class.

	Methods:
	- private login(): automates login process.
	- post_lab_report(): automates instructor posting lab report submission portal for students
		to submit assignments.
	- create_course_portal(): automates instructor creating course portal for students
		to join a course.
	- post_lab_report_results(): automates instructor announcing lab submission marking
		decission.
	- manage_deadline(): automates instructor extending lab report submission portal deadline.

	TODO:
	- manage_deadline()
	"""

	def __init__(self, password, student_id, utility):
		super().__init__(password, student_id)
		self.utility = utility

	def post_lab_report(self, group = 0):

		"""This method automates instructor posting lab report submission portal for students
		for students to submit assignment.

		Parameters:
		- group: int
			0 indicates that this lab report submission portal is intended for individuals
			1 indicates that this lab report submission portal is intended for groups

		Returns:
		- 0 on success.
		- 1 on failure to complete case execution.

		"""

		try:
			#Login
			driver = self.utility.login(self)

			#Navigate to course page
			self.utility.open_course_page(driver)
			
			dateStr = self.utility.getTodayDate() # this is needed for deadline.

			#wait until the lab submission form shows up
			wait2 = WebDriverWait(driver, 10)
			new_lab_assignment_form = wait2.until(EC.presence_of_element_located((By.XPATH, "//form[@id='nlaf']")))
			
			#Fill the required form fields and submit.
			lab_date = new_lab_assignment_form.find_element(By.XPATH, "//input[@id='date'][@name='deadlinedate']")
			timeStr = self.utility.getTodayDate()
			lab_date.send_keys(timeStr)
			lab_title = new_lab_assignment_form.find_element(By.XPATH, "//form[@id='nlaf']/input[@id='ltitle']")
			lab_title.send_keys("TESTASSIGNMENT"+str(dateStr))
			lab_instructions = new_lab_assignment_form.find_element(By.XPATH, "//form[@id='nlaf']/textarea[@id='linstruct']")
			lab_instructions.send_keys("TESTINSTRUCTIONS"+str(dateStr))
			lab_marks = new_lab_assignment_form.find_element(By.XPATH, "//form[@id='nlaf']/input[@id='lmark']")
			lab_marks.send_keys("4")

			#if group == 0 select individual submission, if group == 1 select group submission
			if group == 0:		
				submission_type = new_lab_assignment_form.find_element(By.XPATH, "//form[@id='nlaf']/input[@id='lindi']")
			elif group == 1:
				submission_type = new_lab_assignment_form.find_element(By.XPATH, "//form[@id='nlaf']/input[@id='lgrp']")
			submission_type.click()
			submit = new_lab_assignment_form.find_element(By.XPATH, "//form[@id='nlaf']/input[@id='lbtn']")
			submit.click()
			return 0
		except:
			print("There was a problem executing this test case")
			print("Error in \"post_lab_report()\" method, see error_log.txt for more details")
			err_msg = traceback.format_exc()
			self.utility.log_error(err_msg)
			print("Treminating session")
			self.utility.killSession(driver)
			return 1

	def create_course_portal(self, joining = 0):
		
		"""This method automates instructor creating course portal for students
		to join a course.

		Parameters:
		- joining: int
			0 indicates that this course does not require approval to join
			1 indicates that this course require approval to join

		Returns:
		- 0 on success.
		- 1 on failure to complete case execution.					

		"""
		try:
			#Login first in order to create new course.
			driver = self.utility.login(self)

			#These needed to create a unique course name based on date and time.
			dateStr = self.utility.getTodayDate()
			timeStr = self.utility.getTime()
			
			#Fill the required form fields and submit
			course_name = driver.find_element(By.ID, "cname")
			course_name.send_keys("TESTCOURSE"+str(dateStr)+str(timeStr))
			
			#This URL is needed to access the same created course via its link in post_lab_report() method.
			global courseURL
			courseURL = "TESTCOURSE"+str(dateStr)+str(timeStr)
			course_code = driver.find_element(By.ID, "ccode")
			course_code.send_keys("TC"+str(dateStr)+str(timeStr))
			self.utility.storeCourseCode("TC"+str(dateStr)+str(timeStr))#Store course code to be used
			academic_year = driver.find_element(By.ID, "ayear")				#later by student.
			academic_year.send_keys("2021")
			faculty = driver.find_element(By.ID, "fac")
			faculty.send_keys("TESTING DEPARTMENT")

			#If joining == 0 does not require join approval, if joining == 1 requires join approval
			if joining == 0 :
				joining_students = driver.find_element(By.ID, "jno")
			elif group == 1:
				joining_students = driver.find_element(By.ID, "jyes")
			joining_students.click()
			submit = driver.find_element(By.ID, "portal_btn")
			submit.click()
			return 0

		except:
			print("There was a problem executing this test case")
			print("Error in \"create_course_portal()\" method, see error_log.txt for more details")
			err_msg = traceback.format_exc()
			self.utility.log_error(err_msg)
			print("Treminating session...")
			self.utility.killSession(driver)
			return 1

	def mark_submission(self):
		
		"""This method automates an instructor marking a lab submission.

		Returns:
		- 0 on success.
		- 1 on failure to complete case execution.		
		"""
		try:
			#Login
			driver = self.utility.login(self)

			#Navigate to course page
			self.utility.open_course_page(driver)

			#Wait until the submission portal card appears
			wait2 = WebDriverWait(driver, 10)
			view = wait2.until(EC.presence_of_element_located((By.ID, "view_btn")))
			view.click()

			#Locate and click the 'Mark Submission' btn
			wait3 = WebDriverWait(driver, 10)
			mark_submission = wait3.until(EC.presence_of_element_located((By.ID, "mark_btn")))
			mark_submission.click()

			#Fill and submit marking descision
			wait4 = WebDriverWait(driver, 10)
			pop_up = wait4.until(EC.presence_of_element_located((By.ID, "submit-form")))
			mark = pop_up.find_element(By.ID, "marks")
			mark.send_keys("4")
			comment = pop_up.find_element(By.ID, "feedback")
			comment.send_keys("TESTCOMMENT")
			submit = pop_up.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/button[1]")
			submit.click()
			return 0

		except:
			print("There was a problem executing this test case")
			print("Error in \"mark_submission()\" method, see error_log.txt for more details")
			err_msg = traceback.format_exc()
			self.utility.log_error(err_msg)
			print("Treminating session...")
			self.utility.killSession(driver)
			return 1

	def manage_deadline(self):

		"""This method automates instructor extending lab report submission portal deadline.

		Returns:
		- 0 on success.
		- 1 on failure to complete case execution.

		"""
		try:
			#Login
			driver = self.utility.login(self)

			#Navigate to course page
			self.utility.open_course_page(driver)

			#Wait until lab report assignment list appears.
			wait = WebDriverWait(driver, 10)
			extend_deadline = wait.until(EC.presence_of_element_located((By.ID, "ext_btn")))
			extend_deadline.click()

			#Wait until the extend deadline popup window shows up.
			wait2 = WebDriverWait(driver, 10)
			extend_deadline_form = wait2.until(EC.presence_of_element_located((By.ID, "frm")))
			
			#Insert the new deadline and submit for all.
			new_date = extend_deadline_form.find_element(By.XPATH, "//form[@id='frm']/input[3]")
			dateStr = self.utility.getTomorrowDate()
			new_date.send_keys(str(dateStr))
			target = extend_deadline_form.find_element(By.XPATH, "//form[@id='frm']/input[5]")
			target.click()
			submit = extend_deadline_form.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/button[1]")
			submit.click()
			return 0

		except:
			print("There was a problem executing this test case")
			print("Error in \"manage_deadline()\" method, see error_log.txt for more details")
			err_msg = traceback.format_exc()
			self.utility.log_error(err_msg)
			print("Treminating session...")
			self.utility.killSession(driver)
			return 1