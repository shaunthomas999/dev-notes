# Helm

## Helm Commands

* `helm repo list`
* `helm repo update`
* `helm list --all-namespaces`
  * `helm list -n <namespace>`
  * Shows
    * Release name
    * Chart name
    * etc.
* `helm status <release-name> -n <namespace>`
* `helm history <release-name> -n <namespace>`
* `helm show values <chart-name>`
* `helm show readme <chart-name>`
* `helm install <release-name> <chart-path-or-name> --dry-run --debug`
* `helm upgrade <release-name> <chart-path-or-name> --dry-run --debug`