```
1. k diff -f /tmp/update
2. k scale deploy ipa-backend -n ipa-dev --replica=3
3. k logs -f -l app=ipa-webshell -n ipa-dev
4. k get
    po - pod
    nodes
    sc - StorageClass
    pvc
    svc - service
    cm - ConfigMap
    deploy - deployments
    ds - daemonset
```

5. k delete pod <PODNAME> --grace-period=0 --force --namespace <NAMESPACE>
6. WATCH k get all -n helmdb <- check tat ca resource

Dynamic Volume Provisioning: tao pvc -> tu dong tao pv

- DaemonSet: ensures that the pod runs on all the nodes of the cluster
- StatefulSets: 
- Deployments

- ClusterIP:
- NodePod:

delete node: cordon -> delete node -> terminate ec2 instance
```
