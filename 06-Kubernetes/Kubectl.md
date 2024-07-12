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
* `kubectl get cluster details`
* `kubectl cluster-info`

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
* `watch -n 1 kubectl get pod <pod_name>`
  * `brew install watch`
* `kubectl get pods --selector <label_name>=<label_value>`
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

## Ingress

* `kubectl get ingresses`
* `kubectl describe ingress <ingress-name>`

## Exec

* `kubectl exec -it <pod-name> -- /bin/bash`

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
