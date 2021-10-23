package nor;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
//17
public class RecoverLostPassword {
	public static WebDriver webDriver;
	//初始化webDriver 打开网页
	public void InitDriver() {
		System.setProperty("webdriver.chrome.driver","F:\\chromedriver.exe");
		webDriver = new ChromeDriver();
		webDriver.get("http://118.25.96.118/nor");
		webDriver.manage().window().maximize();
	}
	//找回密码脚本
	public void recpwdScript(String email) {
		WebElement reca = webDriver.findElement(By.xpath("/html/body/div[1]/div[2]/div/div/form/a"));
		reca.click();
		webDriver.switchTo();
		WebElement emailinput = webDriver.findElement(By.name("email"));
		emailinput.sendKeys(email);
		WebElement recover = webDriver.findElement(By.className("btn-primary"));
		recover.submit();
		webDriver.switchTo();
		WebElement alert = webDriver.findElement(By.className("alert-danger"));
		System.out.println(alert.getText());
	}
	public static void main(String[] args) {
		RecoverLostPassword recoverlostpassword = new RecoverLostPassword();
		recoverlostpassword.InitDriver();
		recoverlostpassword.recpwdScript("");
	}
}
