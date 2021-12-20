* 查看Linux内核<br>
> uname -a<br>
> cat /proc/version<br>

* 查看Linux发行版本<br>
> cat /etc/issue<br>
> lsb_release -a<br>

* vim编辑，使用搜索后取消高亮显示<br>
> :noh<br>

* 软连接，硬链接<br>
> 软连接：ln -s   softlink<br>
> 硬链接：ln     hartlink<br>
> 概念：inode, index node, index node ID<br>

* 查看文献引用关系<br>
> <https://www.connectedpapers.com/><br>

* V2ray搭建教程<br>
> <https://blog.codefat.cn/2020/11/15/v2ray%E8%AF%A6%E7%BB%86%E6%90%AD%E5%BB%BA%E4%BD%BF%E7%94%A8FanQ/><br>
```
v2ray:   curl -Ls https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh | sudo bash
或者
bash <(curl -s -L https://git.io/v2ray-setup.sh)
```
* SSR搭建教程<br>
```bash
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssr.sh && chmod +x ssr.sh && bash ssr.sh
```
* 查找arXiv上文章的收录期刊<br>
> <https://github.com/yuchenlin/rebiber.git><br>

* 查看pdf命令<br>
> evince xx.pdf<br>

* 更换虚拟机内核版本<br>
> <https://blog.csdn.net/sinat_38816924/article/details/120344282>

* Linux Kernel Mail List
> <https://lkml.org/>

* http://vger.kernel.org/
> <http://vger.kernel.org/>

* crontab -e定时执行python脚本有时候某些包的引入会导致无法执行python脚本
> 正确做法先在命令行中env查看当前shell下的环境变量
> 编辑定时任务* * * * * env > /tmp/env.output查看crontab下的环境变量
> 通过比较crontab的env与shell的env，找出不同，在定时任务设置一下环境变量。
> 比如这个实验中我们添加如下内容在crontab -e中
> ```shell
> DISPLAY=:1
> XAUTHORITY=/run/user/1000/gdm/Xauthority
> PATH=/usr/local/texlive/2021/texmf-dist/scripts/latexindent:/usr/local/texlive/2021/bin/x86_64-linux:/home/shawn/.pyenv/plugins/pyenv-virtualenv/shims:/home/shawn/.pyenv/shims:/home/shawn/.pyenv/bin:/usr/local/anaconda3/bin:/usr/local/pycharm-community-2020.3.2/bin:/home/shawn/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/blender-2.92.0-linux64:/usr/local/pycharm-community-2020.3.2/bin:/usr/local/cuda/bin
> ```

https://blog.csdn.net/xiaoqiangclub/article/details/112195070?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link

* DNS_PROBE_FINISHED_NXDOMAIN
```
sudo vim /etc/resolv.conf
```
添加如下DNS
```
nameserver 8.8.8.8
nameserver 8.8.4.4
```
刷新DNS
```
sudo systemd-resolve --flush-caches
```
check the statistics in order to make sure that your cache size is now zero.
```
sudo systemd-resolve --statistics
```

* cuda多版本共存<br>
1. 删除原有cuda<br>
```bash
sudo rm -rf /usr/local/cuda
```
2. 建立新的软链接
```bash
sudo ln -s /usr/local/cuda-9.2 /usr/local/cuda
```

* cudnn改变<br>
<https://developer.nvidia.com/cuDNN><br>
cuDNN Archive | NVIDIA Developer<br>
选择你要下载的版本<br>
1. 解压出一个名为cuda的文件夹，文件夹中有include和lib64两个文件夹<br>
2. 删除原来的cudnn<br>
    ```bash
    sudo rm -rf /usr/local/cuda/include/cudnn.h
    sudo rm -rf /usr/local/cuda/lib64/libcudnn*
    ```
3. 安装安装需要版本的cudnn，在终端cd到刚解压的cuda文件夹<br>
    ```bash
    sudo cp include/cudnn.h /usr/local/cuda/include/
    sudo cp lib64/lib* /usr/local/cuda/lib64/
    ```
4. cd到/usr/local/cuda/lib64/文件夹下，建立软链接（注意版本号换成你自己的）<br>
    ```bash
    sudo chmod +r libcudnn.so.5.0.5  
    sudo ln -sf libcudnn.so.5.0.5 libcudnn.so.5  
    sudo ln -sf libcudnn.so.5 libcudnn.so  
    sudo ldconfig  
    ```
5. 检测
    ```bash
    cd /usr/local/cuda/lib64/
    ll
    ```
    会显示出你已经建立的软链接记录。至此，cudnn版本更新完毕。

* 查看cudnn版本
    ```bash
    cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
    ```

* 查看cuda版本
    ```bash
    nvcc -V
    ```

* This is probably because cuDNN failed to initialize解决办法<br>
试过改变cuddn版本，但是没啥效果。感觉应该是显存的问题，如下修改：<br>

    **tensorflow：**
    ```python
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    with tf.Session(config=config) as session:
    ```
    **keras：**
    ```python
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    keras.backend.tensorflow_backend.set_session(tf.Session(config=config))
    ```