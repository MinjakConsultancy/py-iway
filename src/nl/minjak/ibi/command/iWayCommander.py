import sys, os, os.path, runpy
from nl.minjak.ibi.iway.BusinessService import BusinessService
import nl.minjak.util.WindowsAdmin as admin

# def start():
def do_action():

    args = sys.argv
    print(args)
    if len(args) < 0:
        print('missing action argument')
    else:
        action = args[1]
        if action not in ['rebuildConfig','rebuildChannel', 'rebuildProcessflow']:
            print('No valid action : ' + action)
            exit()
        iWayBS = BusinessService()
        iWayBS.init()
        if action == 'rebuildConfig':
            config = args[2]
            # for now use defaults
            print('Rebuilding config ' + config)
            iWayBS.rebuild_config(config)
        elif action == 'rebuildCChannel':
            config = args[2]
            channel_name = args[3]
            # for now use defaults
            iWayBS.rebuild_channel(config, channel_name)
        elif action == 'rebuildProcessflow':
            config = args[2]
            channel_name = args[3]
            # for now use defaults
            iWayBS.rebuild_processflow(config, channel_name)


if __name__ == '__main__':
    if not admin.isUserAdmin():
        # print(sys.argv)
        os.environ['PYTHONPATH'] = 'E:\\git\\py-iway\\src'
        # print('not runnig as admin')
        run_list = list()
        run_list.append(sys.executable)
        run_list.append("-m")
        run_list.append("nl.minjak.ibi.command.iWayCommander")
        for i in range(1, len(sys.argv)):
            run_list.append(sys.argv[i])
        # print(run_list)
        admin.runAsAdmin(run_list)
    else:
        do_action()
        response = input("Finished")
