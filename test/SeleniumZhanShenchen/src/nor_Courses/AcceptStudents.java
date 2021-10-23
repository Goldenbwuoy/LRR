package nor_Courses;


import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import nor.SignIn;
// 6
public class AcceptStudents {
	public WebDriver webDriver = SignIn.webDriver;
	//批准加入脚本
	public void acceptScript() {
		webDriver.switchTo();
		WebElement accept = webDriver.findElement(By.xpath("/html/body/div/div[2]/div/a[1]"));
		accept.click();
	}
	/*public static void main(String[] args) {
		SignIn signIn = new SignIn();
		signIn.InitDriver();
		signIn.loginScript("1404325791@qq.com", "64566325cc");
		AcceptStudents students = new AcceptStudents();
		students.acceptScript();
	}*/
}
