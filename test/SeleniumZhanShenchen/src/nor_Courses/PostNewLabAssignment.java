package nor_Courses;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import nor.SignIn;
//14
public class PostNewLabAssignment {
	public WebDriver webDriver = SignIn.webDriver;
	//新建Assignment脚本
	public void createAsscript(String number,String date1,String deadlinetime1,String title1,String instructions1,String marks1) {
		WebElement classname = webDriver.findElement(By.xpath("/html/body/div[1]/div[1]/a["+number+"]/div"));
		classname.click();
		webDriver.switchTo();
		WebElement date = webDriver.findElement(By.id("date"));
		date.sendKeys(date1);
		WebElement deadlinetime = webDriver.findElement(By.name("deadlinetime"));
		deadlinetime.sendKeys(deadlinetime1);
		WebElement title = webDriver.findElement(By.name("title"));
		title.sendKeys(title1);
		WebElement instructions = webDriver.findElement(By.name("instructions"));
		instructions.sendKeys(instructions1);
		WebElement marks = webDriver.findElement(By.name("marks"));
		marks.sendKeys(marks1);
		List<WebElement> elements = webDriver.findElements(By.name("type"));
		for(WebElement radio:elements) {
			boolean flag = radio.isSelected();
			if (flag==false) {
				radio.click();
				break;
			}
		}
		WebElement post = webDriver.findElement(By.className("btn-primary"));
		post.submit();
	}
	public static void main(String[] args) {
		SignIn signIn = new SignIn();
		signIn.InitDriver();
		signIn.loginScript("1404325791@qq.com", "64566325cc");
		PostNewLabAssignment postNewLabAssignment = new PostNewLabAssignment();
		postNewLabAssignment.createAsscript("5","0020200412", "22:00", "test02", "111", "100");
	}
}
