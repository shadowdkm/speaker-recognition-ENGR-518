import numpy as np
import scipy


class myFilterX6:
    def __init__(self):
        self.data = np.array([])
        self.dataLength=8000*5
        decayConst=0.001

        self.b1 = [0.9912420586742017, -1.980955693940585, 0.9912420586742017]
        self.b2 = [0.9917786469285315, -1.977442648698882, 0.9917786469285315]
        self.b3 = [0.9919323489165897, -1.970113454284546, 0.9919323489165897]
        self.b4 = [0.9920410751314517, -1.948938600601612, 0.9920410751314517]
        self.b5 = [0.9920927987596064, -1.913860937684276, 0.9920927987596064]
        self.b6 = [0.992116299621277, -1.877253410651705, 0.992116299621277]

        self.a1 = [1, -1.980955693940585, 0.9824841173484032]
        self.a2 = [1, -1.977442648698882, 0.9835572938570628]
        self.a3 = [1, -1.970113454284546, 0.9838646978331792]
        self.a4 = [1, -1.948938600601612, 0.9840821502629032]
        self.a5 = [1, -1.913860937684276, 0.9841855975192129]
        self.a6 = [1, -1.877253410651705, 0.984232599242554]

        self.lpB = np.array([decayConst])
        self.lpA = np.array([1, decayConst-1])


    def filter(self,x):
        self.data=np.append(self.data,x)
        self.data=self.data[-self.dataLength:]

        v1 = self.notchAndLowpass(self.b1, self.a1, self.lpB, self.lpA, self.data)
        v2 = self.notchAndLowpass(self.b2, self.a2, self.lpB, self.lpA, self.data)
        v3 = self.notchAndLowpass(self.b3, self.a3, self.lpB, self.lpA, self.data)
        v4 = self.notchAndLowpass(self.b4, self.a4, self.lpB, self.lpA, self.data)
        v5 = self.notchAndLowpass(self.b5, self.a5, self.lpB, self.lpA, self.data)
        v6 = self.notchAndLowpass(self.b6, self.a6, self.lpB, self.lpA, self.data)

        return np.array([1, v1,v2,v3,v4,v5,v6])

    def notchAndLowpass(self,notchB, notchA, lpB, lpA, x):
        val = scipy.signal.lfilter(notchB, notchA, x)
        val = x -val
        val = np.abs(val)
        val = scipy.signal.lfilter(lpB, lpA, val)
        return np.log10(val[-1])
