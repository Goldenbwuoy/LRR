package nor_students;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class SignInStudents {
	public static WebDriver webDriver;
	//初始化webDriver 打开网页
	public void InitDriver() {
		System.setProperty("webdriver.chrome.driver","F:\\chromedriver.exe");
		webDriver = new ChromeDriver();
		webDriver.get("http://118.25.96.118/nor/");
		webDriver.manage().window().maximize();
	}
	//登录脚本
	public void loginStudentsScript(String username,String password) {
		webDriver.findElement(By.className("btn-primary"));
		WebElement user = webDriver.findElement(By.name("user"));
		user.isDisplayed();
		WebElement passwd = webDriver.findElement(By.name("password"));
		passwd.isDisplayed();
		WebElement loginBtn = webDriver.findElement(By.className("btn-primary"));
		loginBtn.isDisplayed();
		user.sendKeys(username);
		passwd.sendKeys(password);
		loginBtn.click();
		webDriver.switchTo();//切换窗口
		WebElement loginInfo = webDriver.findElement(By.className("form-inline"));
		System.out.println(loginInfo.getText());
	}
	/*public static void main(String[] args) {
		SignInStudents signInStudents = new SignInStudents();
		signInStudents.InitDriver();
		signInStudents.loginStudentsScript("201631900128", ">[@+cO03");
	}*/
}
