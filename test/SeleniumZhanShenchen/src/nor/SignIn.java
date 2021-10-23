package nor;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
//26
public class SignIn {
	public static WebDriver webDriver;
	//初始化webDriver 打开网页
	public void InitDriver() {
		System.setProperty("webdriver.chrome.driver","F:\\chromedriver.exe");
		webDriver = new ChromeDriver();
		webDriver.get("http://118.25.96.118/nor/");
		webDriver.manage().window().maximize();
	}
	//登录脚本
	public void loginScript(String username,String password) {
		WebElement user = webDriver.findElement(By.name("user"));
		user.isDisplayed();
		WebElement passwd = webDriver.findElement(By.name("password"));
		passwd.isDisplayed();
		WebElement loginBtn = webDriver.findElement(By.className("btn-primary"));
		loginBtn.isDisplayed();
		user.sendKeys(username);
		passwd.sendKeys(password);
//		user.sendKeys(Keys.chord(Keys.CONTROL + "a"));
		loginBtn.click();
		webDriver.switchTo();//切换窗口
		WebElement loginInfo = webDriver.findElement(By.className("form-inline"));
		System.out.println(loginInfo.getText());
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SignIn signin = new SignIn();
		signin.InitDriver();
		signin.loginScript("1404325791@qq.com","64566325cc");
	}
}