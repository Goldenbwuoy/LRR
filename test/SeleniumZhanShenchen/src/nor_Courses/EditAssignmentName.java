package nor_Courses;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import nor.SignIn;

public class EditAssignmentName {

	public WebDriver webDriver = SignIn.webDriver;
	public void editAssignmentNameScript(String number,String title1) {
		WebElement course = webDriver.findElement(By.xpath("/html/body/div/div[1]/a["+number+"]/div"));
		course.click();
		webDriver.switchTo();
		WebElement edit = webDriver.findElement(By.xpath("/html/body/div[2]/div[2]/div/span/span/a[1]"));
		edit.click();
		webDriver.switchTo();
		WebElement title = webDriver.findElement(By.name("title"));
		title.clear();
		title.sendKeys(title1);
		WebElement type = webDriver.findElement(By.xpath("/html/body/div[2]/div[1]/form/input[10]"));
		type.click();
		WebElement submit = webDriver.findElement(By.xpath("/html/body/div[2]/div[1]/form/input[12]"));
		submit.click();
	}
	public static void main(String[] args) {
		SignIn signIn = new SignIn();
		signIn.InitDriver();
		signIn.loginScript("1404325791@qq.com", "64566325cc");
		EditAssignmentName editAssignmentName = new EditAssignmentName();
		editAssignmentName.editAssignmentNameScript("5","test2");
	}
}
