import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm  # sklearn provides supported vector machine learning algorthim
from sklearn import ensemble
from sklearn import tree
import sys

def svm_train(rssi) :
    X=[[0.0, -81.0, 0.0, 0.0, -86.0, 0.0, 0.0, 0.0, -91.0, 0.0, 0.0, -95.0, -94.0, 0.0, 0.0, -96.0, -93.0, -75.0, -86.0, -70.0, -84.0], [0.0, -75.0, 0.0, 0.0, -94.0, 0.0, 0.0, -89.0, -88.0, -98.0, -75.0, -89.0, -89.0, 0.0, 0.0, -84.0, -74.0, -70.0, -85.0, -82.0, -89.0], [0.0, -83.0, 0.0, 0.0, -70.0, 0.0, 0.0, 0.0, -94.0, -100.0, -78.0, -89.0, -92.0, 0.0, -94.0, 0.0, -77.0, -81.0, -96.0, -80.0, -74.0], [0.0, -56.0, 0.0, 0.0, -75.0, 0.0, -98.0, 0.0, -94.0, -95.0, -66.0, -82.0, -93.0, 0.0, -94.0, -83.0, -82.0, -88.0, -77.0, -74.0, -76.0], [0.0, -60.0, 0.0, 0.0, -82.0, 0.0, -97.0, -98.0, -82.0, -85.0, -67.0, -82.0, -94.0, 0.0, -92.0, -86.0, -70.0, -94.0, -78.0, -74.0, -84.0], [0.0, -75.0, 0.0, 0.0, -78.0, 0.0, -93.0, 0.0, -85.0, -73.0, -90.0, -64.0, -81.0, -92.0, -88.0, -86.0, -72.0, -97.0, -68.0, -84.0, -76.0], [0.0, -73.0, 0.0, 0.0, -81.0, 0.0, -92.0, 0.0, -85.0, -82.0, -86.0, -80.0, -92.0, 0.0, -78.0, -94.0, -88.0, 0.0, -85.0, 0.0, -90.0], [0.0, 0.0, 0.0, -73.0, -75.0, 0.0, -90.0, 0.0, -80.0, -75.0, -97.0, -72.0, -96.0, 0.0, -59.0, -92.0, -76.0, -96.0, -85.0, -93.0, -92.0], [0.0, 0.0, 0.0, -94.0, 0.0, 0.0, -85.0, 0.0, -89.0, -83.0, -100.0, -90.0, -82.0, 0.0, -83.0, -84.0, -86.0, 0.0, -89.0, 0.0, -90.0], [0.0, -83.0, 0.0, 0.0, -69.0, 0.0, -96.0, 0.0, 0.0, -94.0, 0.0, -94.0, -97.0, 0.0, -82.0, -90.0, 0.0, 0.0, -88.0, -95.0, -92.0]]
    Y=[124893,124892,124891,124890,124889,124888,124887,124886,124885,124884]
    classifier = svm.SVC(kernel='rbf', C=1.0, gamma='scale')
    classifier.fit(X, Y)
    rssi_=[0 for x in range(21)]
    rssi=eval(rssi)
    list_rssi=[' 47:48:12:5A:51:F4 ', ' 64:CB:14:D0:BE:F0 ', ' 70:04:10:9D:89:BF ', ' 73:E6:C9:F5:21:36 ', ' A4:50:46:B5:18:3D ', ' C2:06:8D:56:37:AC ', ' C2:22:A8:4B:F5:53 ', ' C2:22:F3:4A:02:DA ', ' C2:2F:85:BC:0E:0C ', ' C2:33:CD:DD:31:80 ', ' C2:39:FE:74:C0:43 ', ' C2:47:71:78:11:7E ', ' C2:6E:E7:12:A9:37 ', ' C2:76:6A:94:73:50 ', ' C2:8C:29:D7:42:AD ', ' C2:98:98:BB:96:D6 ', ' C2:AB:6C:5F:23:1D ', ' C2:C3:89:4F:28:05 ', ' C2:D8:67:CD:91:AC ', ' C2:D9:E5:4F:A4:EC ', ' E4:46:DA:C8:D9:DA ']

    for i in rssi:
        if i["device_addr"] in list_rssi:
                index=list_rssi.index(i["device_addr"])
                rssi[index]=i["device_rssi"]
    rssi_=[rssi_]
    y_pre = classifier.predict(rssi_)
    y=int(y_pre[0])


    return y

if __name__ == "__main__":
    #rssi = sys.argv
    rssi='[{"device_addr":"74:70:FD:C5:3A:D6","device_name":"DESKTOP-7KDBJR3","device_rssi":-58},{"device_addr":"6E:52:2B:88:C5:3E","device_name":"设备名为空","device_rssi":-80}]'
    result = svm_train(rssi)
    print(result)
