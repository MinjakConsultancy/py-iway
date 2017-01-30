import sys
from nl.minjak.ibi.iway.BusinessService import BusinessService

# def start():


if __name__ == '__main__':
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
            iWayBS.rebuild_config(config)
        elif action == 'rebuildCChannel':
            config = args[2]
            channel_name = args[3]
            # for now use defaults
            iWayBS.rebuild_channel(config, channel_name)
        elif action == 'redeployProcessflow':
            config = args[2]
            channel_name = args[3]
            # for now use defaults
            iWayBS.rebuild_processflow(config, channel_name)
    print(args[2])