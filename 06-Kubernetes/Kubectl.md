# Kubectl

## Cluster check
* `kubectl get --raw='/readyz?verbose&exclude=etcd'`
  * To check whether everything in the Kubernetes cluster has started up properly 
  * `kubectl get --raw='/readyz?verbose&exclude=etcd'` to exclude some

## Version

* `kubectl version -o json`

## Config

* `kubectl config view`
  * Contexts needs to be configured
* `kubectl config get-contexts`
* `kubectl config current-context`
* `kubectl config use-context <my-cluster-name>`
* `kubectl get cluster details`
* `kubectl cluster-info`
* `curl -u <username> -o kube_config_file -v <url> && export KUBECONFIG=kube_config_file`

## Apply

* `kubectl apply -f app.yml`
  * `kubectl apply -f *.yml`

## Describe

* `kubectl describe <_>`

## Scale

* `kubectl scale –replicas=3 <container_name>`
* `kubectl autoscale`

## Logs

* `kubectl logs -f <pod_name> --all-containers`
* `kubectl logs -f <pod_name> -c <container_name>`
* `kubectl logs <pod-name> --previous`
* `kubectl -c <container> logs <pod-name>` - container logs
* Deployment
  * `kubectl logs -f deploy/<pod_name>`

## All

* `kubectl get all`

## Pods

* `kubectl get pods`
* `kubectl describe pod <pod_name>` - To know all details about a pod including config details, errors, activity etc.
* `kubectl delete pod <pod_name>`
    * Deleting a pod will temporarily remove a pod but kubernetes will respawn that instance almost immediately.
    * Deleting a pod therefore works as a restart.
* `kubectl get pod <pod_name> -w` - Watch a pod
  * `kubectl get pods -w --namespace default`
* `watch -n 1 kubectl get pod <pod_name>`
  * `brew install watch`
* `kubectl get pods --selector=<label_name>=<label_value>`
  * `kubectl get pods --selector=aurora.env=ae` 
* `kubectl get pods -l env=ae`

## Nodes

* `kubectl get nodes`
* `kubectl get nodes -o wide`


## Events

* `kubectl get events`

## Services

* `kubectl get services`
* `kubectl describe service <service-name>`

## Deployment

* `kubectl get deployment`
* `kubectl delete deployment <container_name>`
* `kubectl delete deployment aurora-file-service-ute`

## Ingress

* `kubectl get ingresses`
* `kubectl describe ingress <ingress-name>`

## Exec

* `kubectl exec -it <pod-name> -- /bin/bash`

```
* Connect to a pod: kubectl -n acp exec -it <pod-id> -- /bin/sh
* After you've connected to the pod: jcmd to get the PID of you process
* jcmd <PID> GC.heap_dump filename=/tmp/app.hprof
* Disconnect from the pod (ctrl + c)
* Run kubectl -n acp cp <pod-id>:/tmp/app.hprof /tmp/copied-dump.hprof to copy the dump to your local machine
```

## Port-forward

* Forward port from local to pod/service/deployment
* `kubectl port-forward <pod_name> 8080:8080`
  * `kubectl port-forward pod/<pod_name> 8080:8080`
  * `kubectl port-forward service/<service_name> 8080:8080`
  * `kubectl port-forward deployment/<deployment_name> 8080:8080`

## Proxy

* kubectl proxy is used for accessing the K8s API server, allowing you to interact with various K8s resources
* `kubectl proxy`
  
## Kubectl Plugins

### Krew

* Install - [https://krew.sigs.k8s.io/docs/user-guide/setup/install/]()
* Useful plugins
  * `tree` - Helps to visualise relationship b/w k8s resources related to a deployment like pod, replicatSet, services etc.
    *  `kubectl tree deployment <deployment-name>`
