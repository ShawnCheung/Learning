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
    如果ping不通www.github.com,找其他电脑ping，确定github.com的ip地址。


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

* E: Sub-process /usr/bin/dpkg returned an error code (1)
    ```bash
    1.$ sudo mv /var/lib/dpkg/info /var/lib/dpkg/info_old //现将info文件夹更名
    2.$ sudo mkdir /var/lib/dpkg/info //再新建一个新的info文件夹
    3.$ sudo apt-get update && sudo apt-get -f install //不用解释了吧
    4.$ sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info_old //执行完上一步操作后会在新的info文件夹下生成一些文件，现将这些文件全部移到info_old文件夹下

    5.$ sudo rm -rf /var/lib/dpkg/info //把自己新建的info文件夹删掉
    6.$ sudo mv /var/lib/dpkg/info_old /var/lib/dpkg/info //把以前的info文件夹重新改
    ```
* 创建新环境 
    ```bash
    pyenv virtualenv 3.6.6 my-env
    ```

* gcc 版本升降
    1. 添加PPA到本地仓库sudo add-apt-repository ppa:ubuntu-toolchain-r/test
    2. 更新本地库： sudo apt-get update
    3. 安装自己想要的版本： sudo apt-get install gcc-7 g++-7
    4. gcc版本切换，手动更换软链接
        ```bash
        sudo ln -s /usr/bin/gcc-7 /usr/bin/gcc -f
        sudo ln -s /usr/bin/gcc-ar-7 /usr/bin/gcc-ar -f
        sudo ln -s /usr/bin/gcc-nm /usr/bin/gcc-nm -f
        sudo ln -s /usr/bin/g++-nm /usr/bin/g++-nm -f
        sudo ln -s /usr/bin/g++-ar-7 /usr/bin/g++-ar -f
        sudo ln -s /usr/bin/g++-7 /usr/bin/g++ -f
        ```
    5. 查看gcc版本命令： `gcc -v`
    
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