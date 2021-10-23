package nor_Courses;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import nor.SignIn;
//17
public class Remarking {
	public WebDriver webDriver = SignIn.webDriver;
	//重新打分
	public void remarkScript(String number,String marks1,String feedback1) {//课程的位置 分数 评论
		webDriver.switchTo();
		WebElement course = webDriver.findElement(By.xpath("/html/body/div/div[1]/a["+number+"]/div"));
		course.click();
		webDriver.switchTo();
		WebElement view = webDriver.findElement(By.xpath("/html/body/div[2]/div[2]/div/span/span/a[2]"));
		view.click();
		WebElement ReMarkingRequests  = webDriver.findElement(By.xpath("/html/body/div[2]/div/ul/li[3]/a"));
		ReMarkingRequests.click();
		webDriver.switchTo();
		WebElement remark = webDriver.findElement(By.xpath("//*[@id=\"menu3\"]/k/div/span/button"));
		remark.click();
		WebElement marks = webDriver.findElement(By.name("marks"));
		marks.sendKeys(marks1);
		WebElement feedback = webDriver.findElement(By.name("feedback"));
		feedback.sendKeys(feedback1);
		WebElement submit = webDriver.findElement(By.xpath("/html/body/div[4]/div[2]/div/button[1]/span"));
		submit.click();
	}
	public static void main(String[] args) {
		SignIn signIn = new SignIn();
		signIn.InitDriver();
		signIn.loginScript("1404325791@qq.com", "64566325cc");
		Remarking remarking = new Remarking();
		remarking.remarkScript("6", "100", "abc");
	}
}
