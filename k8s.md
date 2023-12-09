k diff -f /tmp/update

k scale deploy ipa-backend -n ipa-dev --replica=3

k logs -f -l app=ipa-webshell -n ipa-dev


```
kubectl get po/nodes/sc (StorageClass)/pvc/svc (service)/ConfigMap/deployments

kubectl delete pod <PODNAME> --grace-period=0 --force --namespace <NAMESPACE>
WATCH k get all -n helmdb <- check tat ca resource

Dynamic Volume Provisioning: tao pvc -> tu dong tao pv

- DaemonSet: ensures that the pod runs on all the nodes of the cluster
- StatefulSets: 
- Deployments

- ClusterIP:
- NodePod:

delete node: cordon -> delete node -> terminate ec2 instance
```
