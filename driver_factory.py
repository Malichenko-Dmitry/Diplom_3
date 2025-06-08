from selenium import webdriver

class DriverFactory:

    @staticmethod
    def get_driver(browser_name):
        """Возвращает объект веб-драйвера в зависимости от браузера."""
        if browser_name.lower() == "chrome":
            return webdriver.Chrome()
        elif browser_name.lower() == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(f"Браузер {browser_name} не поддерживается")