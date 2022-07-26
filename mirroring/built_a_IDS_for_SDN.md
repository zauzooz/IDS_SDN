# XÂY DỰNG MỘT IDS CHO MẠNG SDN ĐƠN GIẢN

## Một vài lưu ý:

- Hệ điều hành mình sử dụng là Ubuntu 20.04 LTS.
- Sử dụng python3.
- Sử dụng Remote Controller là Ryu.
- Mạng được xây dựng bởi Containernet.
- ...
- Còn nữa nhưng mà sau này cập nhật thêm :">.

## Bước 1: Xây dựng mô hình mạng (topology)

Xây dựng mô hình mạng đơn giản như sau:

- Một host đóng vai trò là IDS. Kết nối với switch (tôi sẽ gọi là **ids**).
- Một switch (**sw1**).
- 4 host là máy trong mạng, mỗi máy cùng (**d1**, **d2**, **d3** và **d4**).

```python
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
    info('*** Network Start\n')
    net.start()
    info('*** Network Stop\n')
    CLI(net)
    net.stop()
```

## Bước 2: Port mirroring

Đầu tiên thực hiện chạy controller Ryu và sau đó chạy topology.

Tại containernet console, xét **ids** kết nối với interface nào của **sw** bằng lệnh `links`

![](https://raw.githubusercontent.com/zauzooz/IDS_SDN/master/mirroring/picture/links.png)

Như đã thấy, **ids** kết nối với interface _sw1-eth1_ của **sw1**.

Tại containernet console, mở xterm của **sw1** bằng lệnh `xterm sw1`.

```console
containernet> xterm sw1
```

Sau đõ gõ 2 dòng lệnh sau trong xterm của **sw1**:

```console
ovs-vsctl del-port sw1-eth1
ovs-vsctl add-port sw1 sw1-eth1 -- --id=@p get port sw1-eth1 -- --id=@m create mirror name=m0 select-all=true output-port=@p -- set bridge sw1 mirrors=@m

```

Như vậy **ids** có thể giám sát các flow trong mạng.

Để quan sát, tại containernet console mở xterm của **ids** bằng lệnh `xterm ids`

```console
containernet> xterm ids
```

Và trong xterm của **ids**, gõ lệnh `tcpdump -v` để bắt đầu giám sát.

Trở lại với containernet console, gõ `pingall`:

![](https://raw.githubusercontent.com/zauzooz/IDS_SDN/master/mirroring/picture/pingall.png)

Và mở xterm của **ids** quan sát ta có :

![](https://raw.githubusercontent.com/zauzooz/IDS_SDN/master/mirroring/picture/monitor.png)

Vậy là xong, chúng ta đã xây dựng được một IDS cơ bản cho mạng SDN.
