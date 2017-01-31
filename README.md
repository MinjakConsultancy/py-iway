# py-iway
Repository to make an iWay Developer's life a bit easier with help of python

It takes care of redeploying processflows, channels including a restart of the configuration

My installation...:

````
* install anaconda with python 3                              : https://www.continuum.io/downloads  
* install pywin32                                             : https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/
* install pycharm  (in case you want to make some changes..)  : https://www.jetbrains.com/pycharm/download/#section=windows
* download phantomJS                                          : http://phantomjs.org/download.html
* pull this repo
* create the conda environment with the environment.yml
* from within pycharm create a new project, point your python-executable to the conda-environment we created 
````


To start a rebuild of a configuration:
``
python -m nl.minjak.ibi.command.iWayCommander rebuidConfig <config>
``

To start a rebuild of a channel:
``
python -m nl.minjak.ibi.command.iWayCommander rebuidChannel <config> <channel>
``

To start a rebuild of a processflow:
``
python -m nl.minjak.ibi.command.iWayCommander rebuidProcessflow <config> <channel>
``

