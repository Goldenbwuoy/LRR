package Test;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import nor.RecoverLostPassword;
import nor.SignIn;
import nor.VisitorPortal;
import nor_Courses.CreateNewCoursePortal;
import nor_Courses.ExtendDeadline;
import nor_Courses.PostNewLabAssignment;

public class test {
	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver","F:\\chromedriver.exe");
		WebDriver webDriver = new ChromeDriver();
		webDriver.get("http://118.25.96.118/nor/");
	}
}
