import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1
protocol = {'udp': 0, 'tcp': 1, 'icmp': 2}
# 2
typeA = {'other': 0, 'private': 1, 'http': 2, 'remote_job': 3, 'ftp_data': 4, 'name': 5, 'netbios_ns': 6, 'eco_i': 7, 'mtp': 8, 'telnet': 9, 'finger': 10, 'domain_u': 11, 'supdup': 12, 'uucp_path': 13, 'Z39_50': 14, 'smtp': 15, 'csnet_ns': 16, 'uucp': 17, 'netbios_dgm': 18, 'urp_i': 19, 'auth': 20, 'domain': 21, 'ftp': 22, 'bgp': 23, 'ldap': 24, 'ecr_i': 25, 'gopher': 26, 'vmnet': 27, 'systat': 28, 'http_443': 29, 'efs': 30, 'whois': 31, 'imap4': 32, 'iso_tsap': 33, 'echo': 34,
         'klogin': 35, 'link': 36, 'sunrpc': 37, 'login': 38, 'kshell': 39, 'sql_net': 40, 'time': 41, 'hostnames': 42, 'exec': 43, 'ntp_u': 44, 'discard': 45, 'nntp': 46, 'courier': 47, 'ctf': 48, 'ssh': 49, 'daytime': 50, 'shell': 51, 'netstat': 52, 'pop_3': 53, 'nnsp': 54, 'IRC': 55, 'pop_2': 56, 'printer': 57, 'tim_i': 58, 'pm_dump': 59, 'red_i': 60, 'netbios_ssn': 61, 'rje': 62, 'X11': 63, 'urh_i': 64, 'http_8001': 65, 'aol': 66, 'http_2784': 67, 'tftp_u': 68, 'harvest': 69}
# 3
typeB = {'SF': 0, 'S0': 1, 'REJ': 2, 'RSTR': 3, 'SH': 4,
         'RSTO': 5, 'S1': 6, 'RSTOS0': 7, 'S3': 8, 'S2': 9, 'OTH': 10}
# 4
lable = {'normal': 0, 'neptune': 1, 'warezclient': 2, 'ipsweep': 3, 'portsweep': 4, 'teardrop': 5, 'nmap': 6, 'satan': 7, 'smurf': 8, 'pod': 9, 'back': 10, 'guess_passwd': 11, 'ftp_write': 12, 'multihop': 13, 'rootkit': 14, 'buffer_overflow': 15, 'imap': 16, 'warezmaster': 17, 'phf': 18, 'land': 19,
         'loadmodule': 20, 'spy': 21, 'perl': 22, 'saint': 23, 'mscan': 24, 'apache2': 25, 'snmpgetattack': 26, 'processtable': 27, 'httptunnel': 28, 'ps': 29, 'snmpguess': 30, 'mailbomb': 31, 'named': 32, 'sendmail': 33, 'xterm': 34, 'worm': 35, 'xlock': 36, 'xsnoop': 37, 'sqlattack': 38, 'udpstorm': 39}


def NSL_KDD_X_Y_Train():
    pathTrain = "D:\\NCKH\\IDS_SDN\\datasets\\NSL_KDD_Train.csv"
    dataTrain = pd.read_csv(pathTrain)
    train = dataTrain.values
    for item in train:
        if (item[1] in protocol):
            item[1] = protocol[item[1]]
        if (item[2] in typeA):
            item[2] = typeA[item[2]]
        if (item[3] in typeB):
            item[3] = typeB[item[3]]
        if (item[-1] in lable):
            item[-1] = lable[item[-1]]
    X_train = train[:, :-1]
    Y_train = train[:, -1]
    return (X_train, Y_train)


def NSL_KDD_X_Y_Test():
    pathTest = "D:\\NCKH\\IDS_SDN\\datasets\\NSL_KDD_Test.csv"
    dataTest = pd.read_csv(pathTest)
    test = dataTest.values
    for item in test:
        if (item[1] in protocol):
            item[1] = protocol[item[1]]
        if (item[2] in typeA):
            item[2] = typeA[item[2]]
        if (item[3] in typeB):
            item[3] = typeB[item[3]]
        if (item[-1] in lable):
            item[-1] = lable[item[-1]]
    X_test = test[:, :-1].astype('int')
    Y_test = test[:, -1].astype('int')
    return (X_test, Y_test)


def visualization(Y_train):
    x = []
    y = []
    for item in lable:
        x.append(item)
        y.append(0)
    for i in Y_train:
        y[i] = y[i] + 1
    return (x, y)


if __name__ == "__main__":
    _, Y_train = NSL_KDD_X_Y_Train()
    x, y = visualization(Y_train=Y_train)
    X = np.array(x)
    Y = np.array(y)
    plt.barh(X, Y)
    plt.grid(axis='x')
    plt.xlabel("number of instances")
    plt.ylabel("type")
    plt.show()
