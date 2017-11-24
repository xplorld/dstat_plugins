### Authority: Wang Ruiyang <rywang014@gmail.com>

global dstat_cpu_pid
dstat_cpu_pid = os.getenv('DSTAT_CPU_PID') or os.getenv('DSTAT_PID')

class dstat_plugin(dstat):
    """
    Most expensive CPU process.

    Displays the process that uses the CPU the most during the monitored
    interval. The value displayed is the percentage of CPU time for the total
    amount of CPU processing power. Based on per process CPU information.
    """
    def __init__(self):
        self.name = '{} cpu usage'.format(dstat_cpu_pid)
        self.vars = ('all', 'usr', 'sys')
        self.type = 'd'
        self.width = 4
        self.scale = 100
        self.prev_myproc = {"usr":0.0, "sys":0.0}

    def extract(self):
        self.val = {"usr":0.0, "sys":0.0, "all": 0.0}
        myproc  = {"usr":0.0, "sys":0.0}

        try:
            l = proc_splitline('/proc/%s/stat' % dstat_cpu_pid)
        except IOError:
            return

        if len(l) < 15: 
            return 
        
        myproc['usr'] = long(l[13])
        myproc['sys'] = long(l[14])
        
        diff_myproc  = { key: myproc[key] -  self.prev_myproc[key]  for key in myproc.keys() }


        self.val['usr'] = 1.0 * diff_myproc['usr'] / elapsed / cpunr
        self.val['sys'] = 1.0 * diff_myproc['sys'] / elapsed / cpunr
        self.val['all'] = 1.0 * (diff_myproc['usr'] + diff_myproc['sys']) / elapsed / cpunr

        # small = 0.000000001

        # self.val['usr'] = 100 * diff_myproc['usr'] / (diff_allproc['usr'] + small)
        # self.val['sys'] = 100 * diff_myproc['sys'] / (diff_allproc['sys'] + small)
        # self.val['all'] = 100 * (diff_myproc['usr'] + diff_myproc['sys']) / (diff_allproc['usr'] + diff_allproc['sys'] + small)
    
        self.prev_myproc = myproc
        
# vim:ts=4:sw=4:et
