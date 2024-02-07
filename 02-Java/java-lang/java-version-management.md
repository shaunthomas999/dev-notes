# Java Version Management

## Mac OS

### Version check

* See all versions of java - `/usr/libexec/java_home -V`

## SDKMAN

* Ref: https://blog.codeleak.pl/2020/01/manage-multiple-java-sdks-with-sdkman.html

### .sdkmanrc
* Setup
* Option-1 - `sdk env init`
* Option-2 - Create `.sdkmanrc` file

`.sdkmanrc` ref
```ini
# Add the following to ~/.sdkman/etc/config
# sdkman_auto_env=true
# Ref: https://sdkman.io/usage#config
java=17.0.3-tem
maven=3.9.5
```
* Ref
  * https://blog.mrhaki.com/2020/10/automatic-switching-of-java-versions.html 

## jenv

* Ref: https://medium.com/@brunofrascino/working-with-multiple-java-versions-in-macos-9a9c4f15615a

* `brew install jenv`
* `jenv add <JAVA_HOME>`
* `jenv versions`
* `jenv global 1.8.0.121`
* `jenv local 1.8.0.121`
* `jenv remove oracle64–1.7.0.79`
