# Bash Script Samples

## Find a data disk volume name to mount

```bash
#!/bin/bash
set -e

diskNames=$(lsblk --noheadings --raw -o NAME,SIZE,TYPE,MOUNTPOINT | awk '$1~/s.*/ && ($2 == "512G" || $2 == "256G") && $3 == "disk" && $4 == "" {print $1}')
echo "Disks to check: " $diskNames

for val in $diskNames; do
    if ! $(findmnt "/dev/${val}1"); then
      diskNameToMount=$val
      break
    fi
done

echo "Data disk name to mount: " $diskNameToMount
```
