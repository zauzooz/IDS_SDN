#!/usr/bin/python
"""
simple IDS in SDN (1 ids, 1 switch and 4 host)
"""
from mininet.net import Containernet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import info, setLogLevel
setLogLevel('info')
if __name__=="__main__":
    net = Containernet(controller=None)
    info('*** Adding controller\n')
    net.addController(name='ryu', controller=RemoteController, ip='172.17.0.1', port=6633)
    info('*** Adding host\n')
    ids = net.addHost('ids', ip='10.0.0.10', dimage="ubuntu:trusty")
    d1 = net.addHost('d1', ip='10.0.0.1', dimage="ubuntu:trusty")
    d2 = net.addHost('d2', ip='10.0.0.2', dimage="ubuntu:trusty")
    d3 = net.addHost('d3', ip='10.0.0.3', dimage="ubuntu:trusty")
    d4 = net.addHost('d4', ip='10.0.0.4', dimage="ubuntu:trusty")
    info('*** Adding switch\n')
    sw1 = net.addSwitch('sw1')
    info('*** Adding links\n')
    net.addLink(ids, sw1)
    net.addLink(d1, sw1)
    net.addLink(d2, sw1)
    net.addLink(d3, sw1)
    net.addLink(d4, sw1)
    info('*** Mirroring Start\n')
    ids.cmd('./mirroring.sh')
    info('*** Network Start\n')
    net.start()
    info('*** Network Stop\n')
    CLI(net)
    net.stop()

