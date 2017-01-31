import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException


class WebInteraction:
    _username = None
    _password = None
    _server = None
    _port = None
    _base_url = None
    _driver = None

    @staticmethod
    def check_exists_by_xpath(driver, xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    # def wait_for_alert(self):
    #     try:
    #         WebDriverWait(self._driver, 3).until(EC.alert_is_present(),
    #                                     'Timed out waiting for PA creation ' +
    #                                     'confirmation popup to appear.')
    #
    #         alert = self._driver.switch_to.alert
    #         alert.accept()
    #         print("alert accepted")
    #     except TimeoutException:
    #         print("no alert")


    def init(self, username, password, server, port):
        self._username = username
        self._password = password
        self._server = server
        self._port = port
        self._base_url = "http://" + username + ":" + password + "@" + server + ":" + port + "/ism"
        self._driver = webdriver.PhantomJS(executable_path='E:\\phantomjs-2.1.1\\bin\\phantomjs')
        # self._driver = webdriver.Chrome(executable_path='E:\\chromedriver')
        # self._driver = webdriver.Firefox(executable_path='E:\\geckodriver')
        # self._driver.set_page_load_timeout(60)

    def rebuild_config(self, config):
        url = self._base_url + "?configuration=" + config
        driver = self._driver
        driver.get(url=url)

        # Save all channels
        driver.find_element_by_link_text("Deployments").click()
        driver.find_element_by_link_text("Channels").click()
        webchannels = driver.find_elements_by_partial_link_text("_CHN")
        channels = list()
        for webchannel in webchannels:
            channels.append(webchannel.text)

        # Rebuild channels
        driver.find_element_by_link_text("Registry").click()
        driver.find_element_by_link_text("Channels").click()
        for channel_name in channels:
            xpath = "//td[contains(a/text(),'" + channel_name  + "')]/preceding-sibling::td/input[@type='checkbox']"
            # print(xpath)
            driver.find_element_by_xpath(xpath).click()
        assert ("Build" == driver.find_element_by_name("Test").get_attribute("value"))
        driver.find_element_by_name("Test").click()

        # Redeploy all channels
        driver.find_element_by_link_text("Deployments").click()
        driver.find_element_by_link_text("Channels").click()
        # for channelName in channelList:
        #     xpath = "//td[contains(a/text(),'" + channelName + "')]/preceding-sibling::td/input[@type='checkbox']"
        #     # print(xpath)
        #     driver.find_element_by_xpath(xpath).click()
        driver.find_element_by_name("all").click()
        assert ("Redeploy" == driver.find_element_by_xpath("(//input[@name='Add'])[3]").get_attribute("value"))
        driver.find_element_by_xpath("(//input[@name='Add'])[3]").click()

        # Redeploy all processes
        driver.find_element_by_link_text("Deployments").click()
        driver.find_element_by_link_text("Services").click()
        driver.find_element_by_name("all").click()
        assert ("Redeploy" == driver.find_element_by_xpath("(//input[@name='Test'])[2]").get_attribute("value"))
        driver.find_element_by_xpath("(//input[@name='Test'])[2]").click()
        driver.close()

    def rebuild_channel(self, config, channel_name):
        url = self._base_url + "?configuration=" + config
        driver = self._driver
        driver.get(url=url)
        time.sleep(3)
        try:
            driver.switch_to_alert().accept()
        except:
            pass
        time.sleep(3)

        # Rebuild channel
        driver.find_element_by_link_text("Registry").click()
        driver.find_element_by_link_text("Channels").click()
        xpath = "//td[contains(a/text(),'" + channel_name + "')]/preceding-sibling::td/input[@type='checkbox']"
        if self.check_exists_by_xpath(driver, xpath):
            driver.find_element_by_xpath(xpath).click()
            assert ("Build" == driver.find_element_by_name("Test").get_attribute("value"))
            driver.find_element_by_name("Test").click()
            print('Rebuild Channel')

            # Redeploy channel
            driver.find_element_by_link_text("Deployments").click()
            driver.find_element_by_link_text("Channels").click()
            xpath = "//td[contains(a/text(),'" + channel_name + "')]/preceding-sibling::td/input[@type='checkbox']"
            if self.check_exists_by_xpath(driver, xpath):
                driver.find_element_by_xpath(xpath).click()
                # driver.find_element_by_name("all").click()
                assert ("Redeploy" == driver.find_element_by_xpath("(//input[@name='Add'])[3]").get_attribute("value"))
                driver.find_element_by_xpath("(//input[@name='Add'])[3]").click()
                driver.close()
                print('Redeployed channel')
                return True
            else:
                print('Cannot find channel ' + channel_name + ' within configuration ' + config)
                return False
        else:
            print('Cannot find channel '+channel_name)
            return False

    def rebuild_processflow(self, config, processflow):
        url = self._base_url + "?configuration=" + config
        driver = self._driver
        driver.get(url=url)
        time.sleep(3)
        try:
            driver.switch_to_alert().accept()
        except:
            pass
        time.sleep(3)
        # driver.switchTo().alert().accept();
        driver.find_element_by_link_text("Registry").click()
        driver.find_element_by_link_text("Deployments").click()
        driver.find_element_by_link_text("Services").click()
        xpath = "//input[@value='"+processflow+"']"
        if self.check_exists_by_xpath(driver, xpath):
            driver.find_element_by_xpath(xpath).click()
            assert ("Redeploy" == driver.find_element_by_xpath("(//input[@name='Test'])[2]").get_attribute("value"))
            driver.find_element_by_xpath("(//input[@name='Test'])[2]").click()
            driver.close()
            print('PRocessflow redeployed')
            return True
        else:
            print('Cannot find procesflow '+processflow+' within configuration '+config)
            return False


def test():
    t = WebInteraction()
    t.init("iway", "iway", "localhost", "9999")
    t.rebuild_config("base")

if __name__ == '__main__':
    test()