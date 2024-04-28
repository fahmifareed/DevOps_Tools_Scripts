
# 1 Environment

1-2 CentOS 7 Virtual Machines

| VM Name | IP              |
|---------|-----------------|
| master  | 172.16.120.151  |
| node01  | 172.16.120.152  |

The scripts `kubeadm-master.sh` and `kubeadm-node.sh` use kubeadm for installation, utilizing domestic mirrors for a simple and fast setup.

# 2 Master Node Installation
```bash
sh kubeadm-master.sh 172.16.120.151
```

# 3 Node Installation
```bash
sh kubeadm-node.sh 172.16.120.151
```
