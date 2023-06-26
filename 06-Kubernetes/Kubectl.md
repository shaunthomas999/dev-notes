# Kubectl

## Cluster check
* `kubectl get --raw='/readyz?verbose&exclude=etcd'`
  * To check whether everything in the Kubernetes cluster has started up properly 
  * `kubectl get --raw='/readyz?verbose&exclude=etcd'` to exclude some

## Logs

* `kubectl logs -f <pod_name> --all-containers`
* `kubectl logs -f <pod_name> -c <container_name>`
* Deployment
  * `kubectl logs -f deploy/<pod_name>`

## Pods

* `kubectl get pods`
* `kubectl describe pod <pod_name>` - To know all details about a pod including config details, errors, activity etc.
* `kubectl delete pod <pod_name>`
    * Deleting a pod will temporarily remove a pod but kubernetes will respawn that instance almost immediately.
    * Deleting a pod therefore works as a restart.
* `kubectl get pod <pod_name> -w` - Watch a pod
* `watch -n 1 kubectl get pod <pod_name>`
  * `brew install watch`
* `kubectl get pods --selector <label_name>=<label_value>`
* `kubectl get pods -l env=ae`

## Events

* `kubectl get events`

## Services

* kubectl get services
* kubectl describe service <service-name>

## Ingress

* kubectl get ingresses
* kubectl describe ingress <ingress-name>

## Exec

* `kubectl exec -it <pod-name> -- /bin/bash`