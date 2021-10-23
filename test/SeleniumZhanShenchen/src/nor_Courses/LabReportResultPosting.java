package nor_Courses;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import nor.SignIn;
//14
public class LabReportResultPosting {
	public WebDriver webDriver = SignIn.webDriver;
	//打分
	public void labReportResultPostingScript(String number,String marks1,String feedback1) {//课程的位置 分数 评论
		webDriver.switchTo();
		WebElement course = webDriver.findElement(By.xpath("/html/body/div/div[1]/a["+number+"]/div"));
		course.click();
		webDriver.switchTo();
		WebElement view = webDriver.findElement(By.xpath("/html/body/div[2]/div[2]/div/span/span/a[2]"));
		view.click();
		WebElement MarkSubmission = webDriver.findElement(By.xpath("//*[@id=\"menu1\"]/k/div/span/button"));
		MarkSubmission.click();
		webDriver.switchTo();
		WebElement marks = webDriver.findElement(By.name("marks"));
		marks.sendKeys(marks1);
		WebElement feedback = webDriver.findElement(By.name("feedback"));
		feedback.sendKeys(feedback1);
		WebElement submit = webDriver.findElement(By.xpath("/html/body/div[4]/div[2]/div/button[1]/span"));
		submit.click();
	}
	/*public static void main(String[] args) {
		SignIn signIn = new SignIn();
		signIn.InitDriver();
		signIn.loginScript("1404325791@qq.com", "64566325cc");
		LabReportResultPosting labReportResultPosting = new LabReportResultPosting();
		labReportResultPosting.labReportResultPostingScript("6", "90", "feedback1");
	}*/
}
