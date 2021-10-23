# Important notes
Before executing this test suite, there are several things need to be setup and taken into considaration.  

# Setup test environment
These test scripts are written using Python, uses selenium webdriver for automation, and pytest for test execution and reporting. Hence, you have to install
Python on your machine, then pip install selenium webdriver and pytest-selenium libraries.  

Here we guide you through the installation of selenium and pytest-selenium only assuming that you already have Python environment on your machine. If not, visit 
[the official Python page](https://www.python.org/downloads/) to download and install Python.

## Selenium webdriver
Since Selenium supports many web browsers and each browser has its own webdriver, first you will need to download 
[Google chrome webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).  
> **_NOTE:_** Make sure to download the suitable webdriver to your version of Google chrome browser  

Then, add the webdriver to your system environment variables so it would be accessible by the scripts without the need to excplicitly attach the webdriver to the test kit directory.  
To achieve that:  
1- left click on **This PC**, then choose **properties**.  
2- choose **Advanced system settings**.  
3- choose **Environment variables**.  
4- under **System variables** double-click on **path**.  
5- choose **New**, copy and paste path to the downloaded webdriver executable.  
> **_NOTE:_** To avoid problems with long path strings, it is recommended that you create a folder in your `C:\` drive such as:  
> `C:\webdriver\bin` and append the webdriver executable into it.  

To test if everything is working fine, open a command prompt and issue the following command:  
>`C:\> chromedriver`  

You should get something like the following:  

>`Starting ChromeDriver 88.0.4324.96 (68dba2d8a0b149a1d3afac56fa74648032bcf46b-refs/branch-heads/4324@{#1784}) on port 9515`  
>`Only local connections are allowed.`  
>`Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.`  
>`ChromeDriver was started successfully.`  

After that, pip install selenium library using the following command on your command prompt:  

>`C:\> pip install selenium`  

That is all for selenium, next we guide you through installing pytest-selenium.

## Pytest-selenium
Simply, on a command prompt issue the following command:  
>`C:\ pip install pytest-selenium`  

For more details about pytest-selenium visit [this page](https://pytest-selenium.readthedocs.io/en/latest/installing.html).

# Text files descriptions

As you have noticed already, there are several `.txt` files in the test kit folder, namely:  
* course_code.txt  
* DUMMY_SUBMISSION.txt
* Error_log.txt
* student_ids.txt
* Test_Users.txt  

Each file is essential to the automation operation in some sense, for example `course_code.txt` works as a short-term memory to store course codes created by the automation
scripts in some test cases that needed to be used later in a subsequent test cases that requires the same course code to successfully run the test case. And `DUMMY_SUBMISSION.txt` that is used as a dummy file to be submitted during execution of lab report submission test case.  
`Error_log.txt` is used for debugging and keeping track of problems encountered during test execution.  
`student_ids.txt` is a static memory to store several student IDs pre-inserted into `student_data` table of `lrr` database and used by signup test case automation.  
`Test_Users.txt` not used by the scripts, but contains two main system actors, namely, instructor and student accounts credentials that is provided manually inside the test scripts to carry out different operations for different system users.  

# Running the test suite

> **_NOTE:_** Before running the test suite make sure that you have followed [these instructions](https://github.com/hema-001/LRR#installation-instructions) on how to install and run LRR on your machine.  

On the same local directory of your branch of LRR, and after you have done your contribution to the source code whether it is a bug fix or a feature integration and before committing your changes, you should run this regression test suite to prevent the addition of new bugs to the source code, and to ensure master repo consistency.  

Open a command prompt and issue the following command:  
>`C:\ pytest --html test_report_xxxx_yyyy.html`  

The option `--html` tells pytest to generate an HTML test report with test execution results, which is useful and later must be provided before merging new pull requests to master repo.  
`test_report_xxxx_yyyy.html` is the name of the HTML file to be generated after the completion of test execution. Where `xxxx` stands for the date string, for example `10032021` translates to March 3rd 2021, and `yyyy` stands for now time of test execution, for example `1955` translates to 19:55.  
After running the command and if everything is setup correctly, you should see series of web automations for different main functions of LRR.  
Finally, an HTML test report file will be generated just like the example test report in the test kit folder `example_test_report_09032021_1927.html`.
