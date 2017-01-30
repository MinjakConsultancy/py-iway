from selenium import webdriver


class WebInteraction:
    _username = None
    _password = None
    _server = None
    _port = None
    _base_url = None
    _driver = None

    def init(self, username, password, server, port):
        self._username = username
        self._password = password
        self._server = server
        self._port = port
        self._base_url = "http://" + username + ":" + password + "@" + server + ":" + port + "/ism"
        self._driver = webdriver.PhantomJS(executable_path='E:\\phantomjs-2.1.1\\bin\\phantomjs')
        # self._driver = webdriver.Chrome(executable_path='E:\\chromedriver')
        # driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

    def rebuild_config(self, config):
        print(self._base_url)
        print(config)
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

        # Rebuild channels
        driver.find_element_by_link_text("Registry").click()
        driver.find_element_by_link_text("Channels").click()
        xpath = "//td[contains(a/text(),'" + channel_name  + "')]/preceding-sibling::td/input[@type='checkbox']"
        driver.find_element_by_xpath(xpath).click()
        assert ("Build" == driver.find_element_by_name("Test").get_attribute("value"))
        driver.find_element_by_name("Test").click()

        # Redeploy all channels
        driver.find_element_by_link_text("Deployments").click()
        driver.find_element_by_link_text("Channels").click()
        for channelName in channelList:
            xpath = "//td[contains(a/text(),'" + channelName + "')]/preceding-sibling::td/input[@type='checkbox']"
            # print(xpath)
            driver.find_element_by_xpath(xpath).click()
        driver.find_element_by_name("all").click()
        assert ("Redeploy" == driver.find_element_by_xpath("(//input[@name='Add'])[3]").get_attribute("value"))
        driver.find_element_by_xpath("(//input[@name='Add'])[3]").click()
        driver.close()


    def rebuild_processflow(self, config, processflow):
        url = self._base_url + "?configuration=" + config
        driver = self._driver
        driver.get(url=url)
        driver.find_element_by_link_text("Registry").click()
        driver.find_element_by_link_text("Deployments").click()
        driver.find_element_by_link_text("Services").click()
        xpath = "//input[@value='"+processflow+"']"
        driver.find_element_by_xpath(xpath).click()
        assert ("Redeploy" == driver.find_element_by_xpath("(//input[@name='Test'])[2]").get_attribute("value"))
        driver.find_element_by_xpath("(//input[@name='Test'])[2]").click()
        driver.close()

def test():
    t = WebInteraction()
    t.init("iway", "iway", "localhost", "9999")
    #t.rebuild_config("EU_OB_Invoice")
    t.rebuild_processflow("EU_IB_Orders","IB_ORDERS_GBR_96A_MorrisonsEDIFACT_To_Canonical_V01_PF")

if __name__ == '__main__':
    test()