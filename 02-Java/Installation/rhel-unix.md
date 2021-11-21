# RHEL

## alternatives

* Native support for different versions of java

* update-alternatives --install "/bin/java" "java" /usr/lib/jvm/java-11-openjdk-11.0.13.0.8-1.el7_9.x86_64/bin/java 1
* update-alternatives --set java /usr/lib/jvm/java-11-openjdk-11.0.13.0.8-1.el7_9.x86_64/bin/java
* alternatives --list
* alternatives --config java
