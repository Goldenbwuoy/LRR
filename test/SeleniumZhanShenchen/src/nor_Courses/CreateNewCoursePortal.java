package nor_Courses;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;


import nor.SignIn;
//21
public class CreateNewCoursePortal {
	public WebDriver webDriver = SignIn.webDriver;
	//新建course脚本
	public void createScript(String name1,String code1,String url1,String academic1,String faculty1) {
		webDriver.switchTo();
		WebElement name = webDriver.findElement(By.name("name"));
		name.sendKeys(name1);
		WebElement code = webDriver.findElement(By.name("code"));
		code.sendKeys(code1);
		WebElement url = webDriver.findElement(By.name("url"));
		url.sendKeys(url1);
		WebElement academic = webDriver.findElement(By.name("academic"));
		academic.sendKeys(academic1);
		WebElement faculty = webDriver.findElement(By.name("faculty"));
		faculty.sendKeys(faculty1);
		List<WebElement> elements = webDriver.findElements(By.name("verify"));
		for(WebElement radio:elements) {
			boolean flag = radio.isSelected();
			if (flag==false) {
				radio.click();
				break;
			}
		}
		WebElement create = webDriver.findElement(By.xpath("/html/body/div/div[2]/form/input[11]"));
		create.submit();
	}
	public static void main(String[] args) {
		SignIn signin = new SignIn();
		signin.InitDriver();
		CreateNewCoursePortal cPortal = new CreateNewCoursePortal();
		signin.loginScript("1404325791@qq.com","64566325cc");
		cPortal.createScript("test3", "3", "", "2020", "2");
	}
}
