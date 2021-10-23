package nor_Courses_Students;


import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import nor_students.SignInStudents;
//6

public class FindCourse {
	public WebDriver webDriver = SignInStudents.webDriver;
	//通过code寻找和申请加入课程
	public void findCourseScript(String code) {//课程code
		webDriver.switchTo();
		WebElement search = webDriver.findElement(By.name("search"));
		search.sendKeys(code);
		WebElement searchbtn = webDriver.findElement(By.xpath("/html/body/div[2]/div[2]/form/div/div[2]/input"));
		searchbtn.click();
		WebElement join = webDriver.findElement(By.xpath("/html/body/div[2]/div[1]/div[1]/a"));
		join.click();
	}
	/*public static void main(String[] args) {
		SignInStudents signInStudents = new SignInStudents();
		signInStudents.InitDriver();
		signInStudents.loginStudentsScript("201632110128", ">[@+cO03");
		FindCourse findCourse = new FindCourse();
		findCourse.findCourseScript("3");
	}*/
}
