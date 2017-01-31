import nl.minjak.util.WindowsAdmin as admin
import win32service
import win32serviceutil
import traceback


class ConfigHandler:
    _configs = list()

    def get_iway_configs(self):
        print(len(self._configs))
        if len(self._configs) == 0:
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
        print('restarting '+ name)
        self.get_iway_configs()
        service_name = "iWay7 "+name
        if service_name in self._configs:
            try:
                win32serviceutil.RestartService(service_name)
                print('{} restarted.'.format(service_name))
            except:
                traceback.print_exc()
            #     pass
            # win32serviceutil.StartService(service_name)
            # win32serviceutil.StopService(service_name)
        else:
            print('config not in configlist...')

    def restart_base_config(self):
        self.get_iway_configs()
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
    t.restart_base_config()

if __name__ == "__main__":
    print('ok1')
    if not admin.isUserAdmin():
        print('ok2')
        admin.runAsAdmin()
    else:
        print('ok3')
        import sys, os, os.path
        os.environ['PYTHONPATH'] = 'E:\\git\\py-iway\\src'

        test()
        test = input('ok')
