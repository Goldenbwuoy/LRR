package nor_Courses_Students;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import nor_students.SignInStudents;
//9
public class ViewAssignmentGrading {
	public WebDriver webDriver = SignInStudents.webDriver;
	//看分数
	public void viewAssGradeScript(String number) {//课程的位置 
		webDriver.switchTo();
		WebElement course = webDriver.findElement(By.xpath("/html/body/div[2]/div[1]/div["+number+"]/a[1]"));
		course.click();
		WebElement MarkedSubmissions = webDriver.findElement(By.xpath("/html/body/div[3]/div[1]/ul/li[4]/a"));
		MarkedSubmissions.click();
		WebElement grade = webDriver.findElement(By.xpath("//*[@id=\"menu4\"]/k/div/b"));
		System.out.println(grade.getText());
	}
	/*public static void main(String[] args) {
		SignInStudents signInStudents = new SignInStudents();
		signInStudents.InitDriver();
		signInStudents.loginStudentsScript("201632110128", ">[@+cO03");
		ViewAssignmentGrading viewAssignmentGrading = new ViewAssignmentGrading();
		viewAssignmentGrading.viewAssGradeScript("4");
	}*/
}
