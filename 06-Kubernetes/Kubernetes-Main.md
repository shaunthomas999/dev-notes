# Kubernetes General

## Kubernetes Local Cluster Management Tools

### (1) Kind

### (2) Minikube

* `brew install minikube`
*  Reference
   *  https://minikube.sigs.k8s.io/docs/start/

### (3) Kubeadm

### (4) Podman

* https://podman.io/

### Reference

* * Ref: https://kubernetes.io/docs/tasks/tools/

## Kubectl tools

### CLI

* Kubectl - see other md file in same folder

### GUI

* Kubernetes Dashboard (kube-dashboard)
  * from Google
* Lens
  * Desktop Electron based
  * `brew reinstall --cask lens`
  * Register - and opt for free desktop version
  * Make lens point to the rights kubeconfig file
* Octant
  * web app
  * `brew install octant`
  * In terminal > `octant` to start the application
* kubenav
  * Android and iOS support
  
* Ref: https://medium.com/dictcp/kubernetes-gui-clients-in-2020-kube-dashboard-lens-octant-and-kubenav-ce28df9bb0f0#01a8

## Other tools

* Skaffold - https://skaffold.dev/ - Tool to create a workflow to build, tag, push and deploy application in Kubernetes cluster
* Telepresence - https://github.com/telepresenceio/telepresence - Code and test microservices locally against a remote Kubernetes cluster.
