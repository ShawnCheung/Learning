# 2021.12.22
1. 测试了三维标注软件3d-bat，适合于自动驾驶。<https://github.com/walzimmer/3d-bat>
2. 测试了labelCloud标注软件，适合于任何点云。<https://github.com/ch-sa/labelCloud>

# 2021.12.23
1. 联系了点云目标框标注公司，咨询价格
2. 合成一些XYZRGB数据

# 2021.12.24
1. 典型数据标注外包公司有百度数据众包平台、数据堂等
2. 已经向百度数据众包平台（10W起标）、数据堂（签订合同需要提供老师信息）、淘宝圣宝网络公司提交需求（公司设备调试）
3. 看PointPillar论文，查看代码(适合自动驾驶场景，不适合动车场景)
4. 看youtube上[Charles](http://stanford.edu/~rqi/ "主页")大神（PointNet与PoinNet++创始人）讲[Frustum PoinNets](<https://www.youtube.com/watch?v=Ew24Rac8eYE&t=9s>)
5. 阅读论文Frustum PointNets for 3D Object Detection from RGB-D Data[[code](https://github.com/charlesq34/frustum-pointnets "超链接title")]
6. 下载[SUN RGB-D](http://rgbd.cs.princeton.edu/ "RGB-D")数据集

# 2021.12.25
1. 研究dense depth算法
2. 查看SUN RGB-D数据集，里面不包含点云数据，3D目标检测

# 2021.12.26
1. 在pcl环境下测试Frustum-PointNets-Pytorch

# 2021.12.27
1. 联系海天瑞声数据标注，留183号码（无回应）
2. 联系景联文科技标注，贴合度要求，分割要求(晚点报价)
3. 联系澳鹏标注
4. 统计框标raw = [12, 0,1,1,9,16,16,8,11,0,13,2,6,4,8,9,9,15,0,0,0,0,0,0,0,7,0,0,0,6,1,10,6,1,18,0,12,2,2,0,5,5,6,4,11,13,8,17,8,4,0,2,2,0,1,4,0,16,8,9,2,0,1,0,0,2,9,0,0,0,4,9,0,1,10,4,7,0,0,12,6,2,1,3,1,3,0,0,2,0,3,1,1,3,2,2,0,1,3,0,0,3,3,2,5,4,0,1,0,3,1,3,0,3,3,3,3,3,1,2,4,1,0,12,2,6,1]， 平均数4
5. 准备研究深度图补全算法[monocular-depth-estimation](https://github.com/sxfduter/monocular-depth-estimation)
6. 研读[Attention-based Context Aggregation Network for Monocular Depth Estimation](https://arxiv.org/pdf/1901.10137v1.pdf) [[code](https://github.com/miraiaroha/ACAN)]

# 2021.12.28
1. anydesk：886749586， passwd:name
2. NYU DATASET
3. 清理磁盘gparted明令可以分区

# 2022.01.05
1. ssh kb457@10.42.0.92
2. git push --set-upstream origin RAW
3. source ~/.pyenv/versions/pcl/bin/activate
4. pip freeze > d:\requirements.txt

# 2022.01.06
1. 奥鹏标注0.49/框。
2. Attention-depth算法代码。
3. 训练过程出现nan，是因为学习率过大的原因。
4. 启动tensorboard`tensorboard --logdir .\my_log_dir\`
5. screen -S attention-raw

# 2022.01.07
1. 上传澳鹏OSS数据。
2. 80类别 The 50th epoch, fps 333.39 | {'a1': 0.99007, 'a2': 0.99885, 'a3': 0.99977, 'rmse': 22.96294, 'rmse_log': 0.05945, 'log10': 0.04034, 'abs_rel': 0.04085, 'sq_rel': 1.44395}
=> Checkpoint was saved successfully!
Finished training! Best epoch 49 best acc 0.9903
Spend time: 8.59h

# 2022.01.10
1. 180classes attention-depth on raw. train: {'a1': 0.99079, 'a2': 0.99889, 'a3': 0.99982, 'rmse': 17.06729, 'rmse_log': 0.04389, 'log10': 0.02557, 'abs_rel': 0.02566, 'sq_rel': 0.91568};
test:{'a1': 0.98601, 'a2': 0.99862, 'a3': 0.99982, 'rmse': 24.32791, 'rmse_log': 0.06222, 'log10': 0.04694, 'abs_rel': 0.04681, 'sq_rel': 1.81376}
2. 512classes attention-depth on raw. test:{'a1': 0.9603, 'a2': 0.99493, 'a3': 0.99879, 'rmse': 38.00303, 'rmse_log': 0.09997, 'log10': 0.08097, 'abs_rel': 0.08101, 'sq_rel': 4.37271}
3. 80classes attention-depth on nyu: {'a1': 0.81746, 'a2': 0.95975, 'a3': 0.98898, 'rmse': 0.55554, 'rmse_log': 0.19197, 'log10': 0.13756, 'abs_rel': 0.14328, 'sq_rel': 0.10942}
4. NUSCENS注册：邮箱xuhao_zhang@qq.com,密码:_Zxh1103138402

# 2022.01.11
1. 512 classes attention-depth on raw: Testing done, fps 46.07 | {'a1': 0.9603, 'a2': 0.99493, 'a3': 0.99879, 'rmse': 38.00303, 'rmse_log': 0.09997, 'log10': 0.08097, 'abs_rel': 0.08101, 'sq_rel': 4.37271}
2. https://www.nuscenes.org/nuscenes#download

# 2022.01.15
1. 小罗来教研室陪我学习，带了一串烤肠。

# 2022.01.16
1. 需要统计三个类别的mean_size,计算size的残差

# 2022.01.17
1. yolox.
2. code frustum PointNet.
3. OHEM 180 train on raw, fps 10.16 | {'a1': 0.94749, 'a2': 0.99448, 'a3': 0.9992, 'rmse': 41.23414, 'rmse_log': 0.10361, 'log10': 0.07611, 'abs_rel': 0.07771, 'sq_rel': 4.69999}
  test:fps 2.70 | {'a1': 0.9412, 'a2': 0.99356, 'a3': 0.99887, 'rmse': 41.09248, 'rmse_log': 0.10474, 'log10': 0.08198, 'abs_rel': 0.08308, 'sq_rel': 5.1187}
4. CE 180 train on raw, fps 7.47 | {'a1': 0.9476, 'a2': 0.99452, 'a3': 0.99921, 'rmse': 41.44036, 'rmse_log': 0.10404, 'log10': 0.07671, 'abs_rel': 0.07817, 'sq_rel': 4.72609}
  test:fps 2.46 | {'a1': 0.93995, 'a2': 0.99295, 'a3': 0.99886, 'rmse': 41.79632, 'rmse_log': 0.1056, 'log10': 0.08217, 'abs_rel': 0.08273, 'sq_rel': 5.21741}

# 2022.01.20
1. 澳鹏验收，网址：<https://ui.appen.com.cn/>，账户：<xuhao_zhang@qq.com>, 密码：<'7y,Y}kM>
2. 验收850条数据

# 2022.01.21
1. 验收500条数据。
2. 100个txt标注文件。

# 2022.01.24
1. [https://zhuanlan.zhihu.com/p/283015520]直角坐标系转换公式

# 2022.01.31
1. SSD-6D: Making RGB-Based 3D Detection and 6D Pose Estimation Great Again

# 2022.02.04
原理：
对每一点的邻域进行统计分析，基于点到所有邻近点的距离分布特征，过滤掉一些不满足要求的离群点。该算法对整个输入进行两次迭代：在第一次迭代中，它将计算每个点到最近k个近邻点的平均距离，得到的结果符合高斯分布。接下来，计算所有这些距离的平均值 μ 和标准差 σ 以确定距离阈值 thresh_d ，且 thresh_d = μ + k·σ。 k为标准差乘数。在下一次迭代中，如果这些点的平均邻域距离分别低于或高于该阈值，则这些点将被分类为内点或离群点。
1. 统计滤波算法流程
输入：含有噪声的点云{P} \in \mathbb{R}^{N \times 3}，邻域点个数K，标准差乘数c
输出：滤除噪声点云{Q} \in \mathbb{R}^{M \times 3}
for i=0; i<N; i=i+1 do
  取距离Pi距离最近的k个样本
  统计d_{i}=\frac{1}{K} \sum_{k=1}^{K} distance\left(P_{i}, P_{i \rightarrow k}\right)
end
平均值\mu = average(d)
标准差\sigma=\sqrt{\frac{\sum_{i=1}^{N}\left(d_{i}-\mu\right)^{2}}{N}}
距离阈值\text { thresh_d }=\mu+\mathrm{c} \cdot \sigma
i=0;
j=0
for ;i<N; i=i+1 do
  if d_{i}<\text { thresh_d }
    Q_{j}=P_{i}
    i=i+1
    j=j+1
  end
end
返回Q

#2022.02.21
http://www.nra.gov.cn/xxgkml/xxgk/xxgkml/202003/t20200327_107026.shtml
https://blog.csdn.net/clover_my/article/details/92794719