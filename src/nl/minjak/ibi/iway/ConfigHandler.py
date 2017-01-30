import win32service
import win32serviceutil
import traceback


class ConfigHandler:
    _configs = list()

    def get_iway_configs(self):
        if self._configs.count == 0:
            accessSrv = win32service.SC_MANAGER_ALL_ACCESS
            hscm = win32service.OpenSCManager(None, None, accessSrv)
            # Enumerate Service Control Manager DB

            typeFilter = win32service.SERVICE_WIN32
            stateFilter = win32service.SERVICE_STATE_ALL

            statuses = win32service.EnumServicesStatus(hscm, typeFilter, stateFilter)
            for (short_name, desc, status) in statuses:
                # print(short_name, desc, status)
                if str(short_name).startswith("iWay7"):
                    self._configs.append(short_name)
        return self._configs

    def restart_config(self, name):
        service_name = "iWay7 "+name
        if service_name in self._configs:
            try:
                win32serviceutil.RestartService(service_name)
                print('{} restarted'.format(service_name))
            except:  # Exception as e:
                # print(str(e))
                traceback.print_exc()

    def restart_base_config(self):
        service_name = "iWay7 base"
        if service_name in self._configs:
            try:
                win32serviceutil.RestartService(service_name)
                print('{} restarted'.format(service_name))
            except:
                traceback.print_exc()

    def getIwayBaseStatus(self):
        service_name = 'iWay7 base'
        try:
            status = win32serviceutil.QueryServiceStatus(service_name)
            print(status)
            return status
        except:  # Exception as e:
            # print(str(e))
            traceback.print_exc()


def test():
    t = ConfigHandler()
    print(t.get_iway_configs())

if __name__ == "__main__":
    test()