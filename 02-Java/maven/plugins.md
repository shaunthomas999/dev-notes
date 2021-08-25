# Maven Plugins

## Checkstyle
* To skip checkstyle during local development use `mvn` argument `-Dcheckstyle.skip`

## PMD
* `mvn pmd:pmd` - To run pmd manually
* `mvn pmd:check` - To make the build fail if pmd finds any violation

### Reference

* https://pmd.github.io/latest/pmd_userdocs_tools_maven.html
* https://pmd.github.io/latest/pmd_userdocs_tools.html

## Versions

```xml
<plugin>
  <groupId>org.codehaus.mojo</groupId>
  <artifactId>versions-maven-plugin</artifactId>
  <version>2.8.1</version>
</plugin>
```

* `mvn versions:display-dependency-updates`
* `mvn versions:display-plugin-updates`
* Ref: https://dzone.com/articles/general-considerations-on-updating-enterprise-java
