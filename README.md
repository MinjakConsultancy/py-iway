# py-iway
Repository to make an iWay Developer's life a bit easier with help of python

It takes care of redeploying processflows, channels including a restart of the configuration

````
 Required dependencies
* pywin32   : https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/
* selenium  : http://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium
* phantomJS : 
````

To start a rebuild add the source directory to you PYTHONPATH

start a rebuild with :
``
python -m nl.minjak.ibi.command.iWayCommander rebuidConfig base
``