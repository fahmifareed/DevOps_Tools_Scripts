
### 1-2 CentOS 7 Virtual Machines

| VM Name | IP               |
|---------|------------------|
| master  | 172.16.120.191   |
| node01  | 172.16.120.192   |

#### Changing Hostnames
```bash
hostnamectl --static set-hostname master
hostnamectl --static set-hostname node01
```

#### Download the kubeadm.sh script and set executable permissions
```bash
chmod a+x kubeadm.sh
```

#### Execute the following command on the master node:
```bash
sh kubeadm.sh --node-type master --master-address 172.16.120.191
```

#### Execute the following command on the node:
```bash
sh kubeadm.sh --node-type node --master-address 172.16.120.191
```

#### Reset Installation:
```bash
sh kubeadm.sh reset
```

#### If the cluster fails to start after the machine reboots and kubelet starts with errors:
You can check if it's due to swap not being disabled, causing the startup failure, by using:
```bash
cat /var/log/messages
```
If the issue is due to swap not being disabled, you can comment out the swap-related configuration in `/etc/fstab`, then reboot the machine, and the cluster should start normally.

