from selenium import webdriver

class SeleniumDriver:
    _driver = None

    def __init__(self):
        self._driver = webdriver.PhantomJS(executable_path='E:\\phantomjs-2.1.1\\bin\\phantomjs')

    def __init__(self, driver, executable):
        if driver == 'phantomjs':
            _driver = webdriver.PhantomJS(executable_path=executable)
        if driver == 'firefox':
            _driver = webdriver.Firefox(executable_path=executable)
        if driver == 'chrome':
            _driver = webdriver.Chrome(executable_path=executable)

    def get_driver(self):
        return _driver