from selenium import webdriver

from nl.minjak.ibi.iway import WebInteraction, ConfigHandler


class BusinessService:
    _username = None
    _password = None
    _server = None
    _port = None
    _base_url = None
    _driver = None
    _webi = None
    _config_handler = None

    def init(self, username='iway', password='iway', server='localhost', port='9999'):
        self._username = username
        self._password = password
        self._server = server
        self._port = port
        self._base_url = "http://" + username + ":" + password + "@" + server + ":" + port + "/ism"
        self._driver = webdriver.PhantomJS(executable_path='E:\\phantomjs-2.1.1\\bin\\phantomjs')
        # self._driver = webdriver.Chrome(executable_path='E:\\chromedriver')
        self._webi = WebInteraction.WebInteraction()
        self._webi.init(username,password,server,port)
        self._config_handler = ConfigHandler.ConfigHandler()
        print('base : ' + self._base_url)


    def rebuild_config(self, config):
        self._webi.rebuild_config(config)
        self._config_handler.restart_config(config)

    def rebuild_channel(self, config, channel_name):
        self._webi.rebuild_channel(config, channel_name)
        self._config_handler.restart_config(config)


    def rebuild_processflow(self, config, processflow):
        self._webi.rebuild_processflow(config, processflow)
        self._config_handler.restart_config(config)
