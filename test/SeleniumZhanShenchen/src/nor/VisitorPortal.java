package nor;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
//16
public class VisitorPortal {
	public static WebDriver webDriver;
	//初始化webDriver 打开网页
	public void InitDriver() {
		System.setProperty("webdriver.chrome.driver","F:\\chromedriver.exe");
		webDriver = new ChromeDriver();
		webDriver.get("http://118.25.96.118/nor/");
		webDriver.manage().window().maximize();
	}
	//访客门户
	public void visitorPortalScript() {
		WebElement visitor = webDriver.findElement(By.xpath("//*[@id=\"navbarColor02\"]/ul/li[2]/a"));
		visitor.click();
		WebElement files = webDriver.findElement(By.xpath("/html/body/div/div[2]/span/a"));
		files.click();
	}
	/*public static void main(String[] args) {
		VisitorPortal visitorPortal = new VisitorPortal();
		visitorPortal.InitDriver();
		visitorPortal.visitorPortalScript();
	}*/
}
