import matplotlib.pyplot as plt

plt.figure()
l1=plt.plot([450,2070],[0.22,1], color='brown', label='point size')
l2=plt.plot([450,2070],[0.065,0.315], color='blue', label='z noise')
l3=plt.plot([850,2070],[0.01,0.01], color='cyan', label='range')

plt.xticks([450,630,810,990,1170,1350,1530, 1710,1890,2070])
plt.yticks([0,0.25,0.5,0.75,1])
plt.xlabel("扫描距离")
plt.ylabel("单位：毫米")
plt.legend(loc='upper right')
plt.axhline(y=0,ls="--",c="gray", lw=1)#添加水平直线
plt.axhline(y=0.25,ls="--",c="gray", lw=1)#添加水平直线
plt.axhline(y=0.5,ls="--",c="gray", lw=1)#添加水平直线
plt.axhline(y=0.75,ls="--",c="gray", lw=1)#添加水平直线
plt.axhline(y=1,ls="--",c="gray", lw=1)#添加水平直线
plt.axvline(x=450,ls="--",c="gray", lw=1)#添加水平直线
plt.axvline(x=630,ls="--",c="gray", lw=1)#添加水平直线
plt.axvline(x=810,ls="--",c="gray", lw=1)#添加水平直线
plt.axvline(x=990,ls="--",c="gray", lw=1)#添加水平直线
plt.axvline(x=1170,ls="--",c="gray", lw=1)#添加水平直线
plt.axvline(x=1350,ls="--",c="gray", lw=1)#添加水平直线
plt.axvline(x=1530,ls="--",c="gray", lw=1)#添加水平直线
plt.axvline(x=1710,ls="--",c="gray", lw=1)#添加水平直线
plt.axvline(x=1890,ls="--",c="gray", lw=1)#添加水平直线
plt.axvline(x=2070,ls="--",c="gray", lw=1)#添加水平直线

plt.show()

