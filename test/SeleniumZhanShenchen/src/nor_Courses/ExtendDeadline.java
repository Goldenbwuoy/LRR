package nor_Courses;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import nor.SignIn;
//11
public class ExtendDeadline {
	public WebDriver webDriver = SignIn.webDriver;
	//延迟时间脚本 
	public void extendDeadlineScript(String number, String date1, String time1) {
		WebElement course = webDriver.findElement(By.xpath("/html/body/div/div[1]/a["+number+"]/div"));
		course.click();
		webDriver.switchTo();
		WebElement extend = webDriver.findElement(By.xpath("/html/body/div[2]/div[2]/div/span/span/a[3]"));
		extend.click();
		webDriver.switchTo();
		WebElement date = webDriver.findElement(By.name("date"));
		date.sendKeys(date1);
		WebElement time = webDriver.findElement(By.name("time"));
		time.sendKeys(time1);
		WebElement extendfor = webDriver.findElement(By.xpath("//*[@id=\"frm\"]/input[5]"));
		extendfor.click();
		WebElement submit = webDriver.findElement(By.xpath("/html/body/div[3]/div[2]/div/button[1]"));
		submit.click();
	}
	public static void main(String[] args) {
		SignIn signIn = new SignIn();
		signIn.InitDriver();
		signIn.loginScript("1404325791@qq.com", "64566325cc");
		ExtendDeadline extendDeadline = new ExtendDeadline();
		extendDeadline.extendDeadlineScript("5", "0020200331", "2200");
	}
}
