# RHEL

## alternatives

* Native support for different versions of java
* `update-alternatives --install "/bin/java" "java" /usr/lib/jvm/java-11-openjdk-11.0.13.0.8-1.el7_9.x86_64/bin/java 1`
* `update-alternatives --set java /usr/lib/jvm/java-11-openjdk-11.0.13.0.8-1.el7_9.x86_64/bin/java`
* `alternatives --list`
* `alternatives --config java`
* `sudo yum remove -y java-11-openjdk`
* Home setting
    ```java
    echo "export JAVA_HOME=$(dirname $(dirname $(readlink $(readlink $(which java)))))" >>  /home/my_user/.bash_profile
    export PATH=$JAVA_HOME/bin:$PATH
    ```
* `alternatives --display java | grep 'family java-11-openjdk' | cut -d' ' -f1`
