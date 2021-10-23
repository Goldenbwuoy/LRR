package nor_Courses_Students;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import nor_students.SignInStudents;
//13
public class StudentsGroup {
	public WebDriver webDriver = SignInStudents.webDriver;
	public void createGroupScript(String number, String name1) {
		webDriver.switchTo();
		WebElement course = webDriver.findElement(By.xpath("/html/body/div[2]/div[1]/div["+number+"]/a[1]"));
		course.click();
		webDriver.switchTo();
		WebElement group = webDriver.findElement(By.className("btn-primary"));
		group.click();
		webDriver.switchTo();
		WebElement groupname = webDriver.findElement(By.name("name"));
		groupname.sendKeys(name1);
		WebElement submit = webDriver.findElement(By.xpath("/html/body/div[6]/div[2]/div/button[1]/span"));
		submit.click();
	}
	/*public static void main(String[] args) {
		SignInStudents signInStudents = new SignInStudents();
		signInStudents.InitDriver();
		signInStudents.loginStudentsScript("201632110128", ">[@+cO03");
		StudentsGroup studentsGroup = new StudentsGroup();
		studentsGroup.createGroupScript("4", "group4");
	}*/
}
