# dstat_nvidia_gpu_mem
dstat plugin monitoring nvidia gpu memory usage

## dstat

Dstat is a versatile replacement for vmstat, iostat, mpstat, netstat and ifstat.

![dstat](./dstat.png)

## dstat_nvidia_gpu

dstat_nvidia_gpu is a dstat plugin monitoring GPU usage, created by [Vasilis Vryniotis](https://github.com/datumbox).

[link](https://github.com/datumbox/dstat)

[blog](http://blog.datumbox.com/getting-the-gpu-usage-of-nvidia-cards-with-the-linux-dstat-tool/)

![dstat_nvidia_gpu](./dstat_nvidia_gpu.png)

### installation
```
sudo apt-get install dstat #install dstat
sudo pip install nvidia-ml-py #install Python NVIDIA Management Library
wget https://raw.githubusercontent.com/datumbox/dstat/master/plugins/dstat_nvidia_gpu.py
sudo mv dstat_nvidia_gpu.py /usr/share/dstat/ #move file to the plugins directory of dstat
```

## dstat_nvidia_gpu_mem

`dstat_nvidia_gpu` monitors GPU usage only. `dstat_nvidia_gpu_mem` is a similar tool monitoring GPU memory usage.

![dstat_nvidia_gpu_mem](./dstat_nvidia_gpu_mem.png)

### installation

```
sudo apt-get install dstat #install dstat
sudo pip install nvidia-ml-py #install Python NVIDIA Management Library
wget https://raw.githubusercontent.com/xplorld/dstat_nvidia_gpu_mem/master/dstat_nvidia_gpu_mem.py
sudo mv dstat_nvidia_gpu_mem.py /usr/share/dstat/ #move file to the plugins directory of dstat
```

### usage

```
dstat --nvidia-gpu-mem # see a single column of total GPU mem used
dstat --nvidia-gpu-mem -f # see per-device GPU mem used
```

## contact me
rywang014 AT gmail DOT com
