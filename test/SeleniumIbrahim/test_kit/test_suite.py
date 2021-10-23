"""
LRR Testing automation scripts, written by Ibrahim M.I. Ismail in Feb 2021 as part
of the undergraduate thesis "Defect Analysis for LRR".

These scripts are written with the intention of them being a tool to accelerate the maintenance 
process, and as a regression test for feature integrations or bug fixes.

These scripts depend heavily on the structure of html elements in the source code by using
xpath to locate certain elements. Therefore, make sure that all web elements in LRR source 
code are unchanged for this script to run properly. And if any change is necessary, then make
sure to adjust its corresponding xpath on these scripts.

Note: see "Writing history, number 4" the later part about xpath dependency is significantly reduced.

IMPORTANT!
Do not change the order of the test cases in the file "test_suite.py", since many of the later test cases in the file 
order depends on the execution of previous ones in the same file. If must change, make sure that you understand
the dependency between test cases completely.

Contact us for any help or suggestions at:
Mr. Hui Lan (lanhui at zjnu dot edu dot cn)
Ibrahim M.I. Ismail (1525200991 at qq dot com)

Writing history:
1- Feb 06, 2021: wrote the class skeleton. Ibrahim M.I. Ismail
2- Feb 07, 2021: implemented login(), create_course_portal() functions. Ibrahim M.I. Ismail
3- Feb 08, 2021: implemented post_lab_report(), manage_deadline() functions. Ibrahim M.I. Ismail
4- Mar 10, 2021: reduced the amount of web element locators that uses xpath by replacing finding elements
		 by xpath with IDs, as well introduced id attributes for some web elements on LRR's php files.
5- Mar 11, 2021: final fixes and enhancments.
"""

from utility import MyUtility
from instructor import Instructor
from student import Student
from admin import Admin

utility = MyUtility("http://127.0.0.1/edsa-LRR3/")
instructor = Instructor("aA124536!","202032070221", utility)
student = Student("aA124536!", "202032070222", utility)
admin = Admin("aA124536!","202032070221", utility)

cond = 0
f_name = utility.random_string(4)
l_name = utility.random_string(5)

std_ids = ['202032020725', '202032020726', '202032020727', '202032020728', '202032020729']

def test_case_00():
	admin.batch_create_acc(std_ids) == cond

def test_case_01():
	admin.create_new_account('202032020730') == cond

def test_case_02():
	admin.account_block_activate('block') == cond

def test_case_03():
	admin.account_block_activate('activate') == cond

def test_case_04():
	utility.signup(f_name+' '+l_name, f_name+'.'+l_name+'@testing.com', 'aA124536!') == cond

def test_case_05():
    instructor.create_course_portal() == cond

def test_case_06():
    instructor.post_lab_report() == cond

def test_case_07():
	student.join_course() == cond

def test_case_08():
	student.submit_assignment() == cond

def test_case_09():
	instructor.mark_submission() == cond

def test_case_10():
	student.request_remarking() == cond

def test_case_11():
	instructor.manage_deadline() == cond

def test_case_12():
	instructor.create_course_portal() == cond

def test_case_13():
	instructor.post_lab_report(group = 1) == cond

def test_case_14():
	student.join_course() == cond

def test_case_15():
	student.create_course_group() == cond

def test_case_16():
	admin.assign_TA() == cond