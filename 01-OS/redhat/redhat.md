# Redhat

## Docker images

* registry.access.redhat.com/ubi7/ubi:7.9-483
* redhat/ubi8:latest

## Update

PS: Always a good idea to back-up VM before updating

* `yum check-update` - Check for updates
* `sudo yum update --security` - Update only the security patches
* `sudo yum update --cve <CVE-CODE>` - Update package to fix CVE issue
* `sudo yum update` - Update all packages
* `sudo yum update zlib` - Update only zlib package
* `yum updateinfo list installed` - Check all installed updates
