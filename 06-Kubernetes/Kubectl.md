# Kubectl

## Cluster check
* `kubectl get --raw='/readyz?verbose&exclude=etcd'`
  * To check whether everything in the Kubernetes cluster has started up properly 
  * `kubectl get --raw='/readyz?verbose&exclude=etcd'` to exclude some

## Logs

* `kubectl logs -f <pod_name> --all-containers`
* `kubectl logs -f <pod_name> -c <container_name>`

## Pods

* `kubectl get pods`
