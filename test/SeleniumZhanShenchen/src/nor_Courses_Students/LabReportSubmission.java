package nor_Courses_Students;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import nor_students.SignInStudents;
//19:52 20:21
public class LabReportSubmission {
	public WebDriver webDriver = SignInStudents.webDriver;
	//提交报告 
	public void subLPScript(String number,String name1,String file1) {//课程的位置 标题 文件路径
		webDriver.switchTo();
		WebElement course = webDriver.findElement(By.xpath("/html/body/div[2]/div[1]/div["+number+"]/a[1]"));
		course.click();
		webDriver.switchTo();
		WebElement submitLP = webDriver.findElement(By.className("btn-info"));
		submitLP.click();
		webDriver.switchTo();
		WebElement title = webDriver.findElement(By.name("title"));
		title.sendKeys(name1);
		WebElement inputfile = webDriver.findElement(By.name("attachment1"));
		inputfile.sendKeys(file1);
		WebElement submit = webDriver.findElement(By.xpath("/html/body/div[2]/div/div[2]/input[3]"));
		submit.click();
	}
	/*public static void main(String[] args) {
		SignInStudents signInStudents = new SignInStudents();
		signInStudents.InitDriver();
		signInStudents.loginStudentsScript("201632110128", ">[@+cO03");
		LabReportSubmission labReportSubmission = new LabReportSubmission();
		labReportSubmission.subLPScript("4", "test1", "D:/bjg.txt");
	}*/
}
