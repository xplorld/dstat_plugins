### Author: Ruiyang Wang <rywang014@gmail.com>
### Modified from dstat_nvidia_gpu by: Vasilis Vryniotis <bbriniotis@datumbox.com>

class dstat_plugin(dstat):
    """
    Total GPU memory usage for NVIDIA cards. Requires the nvidia-ml-py package.

    Usage: dstat --nvidia-gpu-mem
    """

    def __init__(self):
        self.name = 'nv-gpu memory used' 
        self.type = 'd'
        self.width = 5
        self.cols = 1
        self.samples = 10

    def check(self):
        try:
            import pynvml
            pynvml.nvmlInit()
        except:
            raise Exception('The "pynvml" library is missing from this system.')

    def vars(self):
        ret = ['total']
        if op.full:
            import pynvml
            deviceCount = pynvml.nvmlDeviceGetCount()
            for i in range(0, deviceCount):
                ret.append('gpu%d' % i)
        return ret

    def extract(self):
        stats = self._getUsagePerGPU(self.samples)
        stats['total'] = self._getTotalUsage(stats)
        for name in self.vars:
            self.val[name] = stats[name]

    def _getUsagePerGPU(self, samples):
        import pynvml
        usage = {}
        deviceCount = pynvml.nvmlDeviceGetCount()
        for iter in range(0, samples):
            for i in range(0, deviceCount):
                name = 'gpu%d' % i
                handle = pynvml.nvmlDeviceGetHandleByIndex(i)
                if name not in usage:
                    usage[name] = 0.0
                usage[name] += pynvml.nvmlDeviceGetMemoryInfo(handle).used / float(samples)
        return usage

    def _getTotalUsage(self, usage_per_gpu):
        return sum(usage_per_gpu.values())


