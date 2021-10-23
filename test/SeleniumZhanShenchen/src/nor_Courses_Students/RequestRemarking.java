package nor_Courses_Students;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import nor_students.SignInStudents;
//11
public class RequestRemarking {
	public WebDriver webDriver = SignInStudents.webDriver;
	//申请重新打分
	public void requestRemarkScript(String number,String reason) {//课程的位置 理由
		webDriver.switchTo();
		WebElement course = webDriver.findElement(By.xpath("/html/body/div[2]/div[1]/div["+number+"]/a[1]"));
		course.click();
		WebElement MarkedSubmissions = webDriver.findElement(By.xpath("/html/body/div[3]/div[1]/ul/li[4]/a"));
		MarkedSubmissions.click();
		WebElement requestRemark = webDriver.findElement(By.xpath("//*[@id=\"menu4\"]/k/div/button"));
		requestRemark.click();
		webDriver.switchTo().alert().sendKeys(reason);
		webDriver.switchTo().alert().accept();
	}
	/*public static void main(String[] args) {
		SignInStudents signInStudents = new SignInStudents();
		signInStudents.InitDriver();
		signInStudents.loginStudentsScript("201632110128", ">[@+cO03");
		RequestRemarking requestRemarking = new RequestRemarking();
		requestRemarking.requestRemarkScript("4","123");
	}*/
}
