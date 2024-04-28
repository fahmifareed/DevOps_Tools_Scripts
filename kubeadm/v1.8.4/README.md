
Kubernetes v1.8.4 has not been synced to the Alibaba Cloud Yum repository, but it is now shared on Baidu Cloud Disk. Download `kubectl`, `kubeadm`, `kubelet`, `kubernetes-cni`, `socat`, and scripts `kubeadm.sh` or `kubeadm-reset.sh` and place them in the same directory.
[Download from Baidu Cloud Disk](https://pan.baidu.com/s/1c1VAeli)

# 1 Environment

1-2 CentOS 7 Virtual Machines

| VM Name | IP              |
|---------|-----------------|
| master  | 172.16.120.151  |
| node01  | 172.16.120.152  |

#### Changing Hostnames
```bash
hostnamectl --static set-hostname master
hostnamectl --static set-hostname node01
```

Scripts `kubeadm-master.sh` and `kubeadm-node.sh` use kubeadm for installation, using local mirrors for simple and quick setup.
```bash
chmod a+x kubeadm.sh
chmod a+x kubeadm-reset.sh
```

# 2 Master Node Installation
```bash
sh kubeadm.sh 172.16.120.151 master
```

# 3 Node Installation
```bash
sh kubeadm.sh 172.16.120.151 slave
```

# 4 Reset Script
`kubeadm-reset.sh` is a reset script.

# 5 Static Pods
All components installed by kubeadm are started as static pods through kubelet.
For more information on static pods, please visit [Kubernetes Docs on Static Pods](https://kubernetes.io/cn/docs/tasks/administer-cluster/static-pod/).

# 6 Exception Handling
If the cluster fails to start after the machine reboots and kubelet starts with errors, use the following command to check if it's due to swap not being disabled, causing the startup failure. If it is due to swap not being disabled, you can comment out the swap-related configuration in `/etc/fstab`, then reboot the machine, and the cluster should start normally.
```bash
cat /var/log/messages
```

References:

- [Kubernetes Community](https://www.kubernetes.org.cn/2906.html)
- [Frognew Blog on Installing Kubernetes 1.8 with Kubeadm](https://blog.frognew.com/2017/09/kubeadm-install-kubernetes-1.8.html)

