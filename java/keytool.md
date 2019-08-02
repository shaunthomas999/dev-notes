# Keytool

## Commands

* Add key

```bash
sudo keytool -import -noprompt -trustcacerts -alias rootca_b64 -file rootca_b64.cer -keystore $JAVA_HOME/jre/lib/security/cacerts -storepass "changeit"
```

* Delete key

```bash
sudo keytool -delete -alias rootg3_b64 -keystore $JAVA_HOME/jre/lib/security/cacerts -storepass "changeit"
```

## Reference

* [http://tutorials.jenkov.com/java-cryptography/keytool.html]()
