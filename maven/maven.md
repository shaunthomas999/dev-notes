mvn commands
============

## General Syntax
* `mvn [life cycle commands] [plugin:target] [-Doption=value] [dots]`

## Debug
* `mvn -X` - Will print more logs

## Cores to use
* `mvn -T 1C` - Create threads as much as the number of cores
* `mvn -T 2C` - Create threads double the number of cores

## Create a new project in interactive mode
* `mvn archetype:generate`

## Create a new project in non-interactive mode
* `mvn archetype:generate -DgroudId=<Artifact Group | Package name> -DartifactId=<Artifact ID | Project name> -DinteractiveMode=false`

## Create a new project in non-interactive mode based on existing template
* `mvn archetype:generate -DgroudId=<Artifact Group | Package name> -DartifactId=<Artifact ID | Project name> -DarchetypeArtifactId=<Archetype Artifact ID | Existing maven template project ID> -DinteractiveMode=false`

## Life cycle execution
Run the following commands inside the folder containing pom.xml files
* `mvn clean`
* `mvn test`
* `mvn compile`
* `mvn package`
* `mvn install` - Install Artifact locally
  * `-o` - Run in offline mode

### Skip Testing
* `mvn install -Dmaven.test.skip=true`
  * Execute 'install' life cycle without running tests
  * Doesn't compile test files at all
* `mvn install -DskipTests`
  * Short alternative to skip tests
  * Here test files are compiled, but it is not run

## Run a single unit test
* `mvn -Dtest=TestClass#testMethod test`

## Command line options
* `-B` - Runs Maven in batch mode. It avoids Maven's reporting of downloading progress.
* `-e` - Configures Maven to report detailed information about errors

## Analyze dependencies
* `mvn dependency:analyze` - Helps to get information on "Used undeclared dependencies", "Unused declared dependencies" etc.
* `mvn dependency:tree` - To see dependency tree
  * `-Dverbose` - This will show options not displayed because of duplication
  * `-Dincludes=[group]:[artifact_name]:[type]:[version]` - E.g., `mvn dependency:tree -Dincludes=:hibernate*`. Use wild card `*` to cover different possibilities
  * Ref: [filtering-the-dependency-tree](https://maven.apache.org/plugins/maven-dependency-plugin/examples/filtering-the-dependency-tree.html)
  * Ref: [resolving-conflicts-using-the-dependency-tree](https://maven.apache.org/plugins/maven-dependency-plugin/examples/resolving-conflicts-using-the-dependency-tree.html)

### Relative dependency comparison
* Run `mvn compile dependency:tree >> temp_v01.txt` to store dependency tree to the file
* Then make the necessary changes
* And, run `mvn compile dependency:tree >> temp_v02.txt` to store new dependency tree to the file
* Compare 2 files to see the difference

## Update snapshots
* `mvn -U` - Check for updated snapshots on remote repositories

## Install a downloaded or local jar into maven local repository
* `mvn install:install-file -Dfile=my-jar.jar -DgroupId=com.shaunthomas999 -DartifactId=my-jar -Dversion=LOCAL -Dpackaging=jar`

## Maven Dependencies

### Scope

`<scope>` values

1. compile - default - transitive
2. provided - provided at runtime by JDK or container - not transitive (available in compile and test only). E.g. servlet API
3. system - like provided but dependency path should be explicitly specified by `<systemPath>` property

    ```xml
    <dependency>
        <groupId>com.baeldung</groupId>
        <artifactId>custom-dependency</artifactId>
        <version>1.3.2</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/libs/custom-dependency-1.3.2.jar</systemPath>
    </dependency>
    ```
4. runtime - required at runtime - not in compile time but in test and runtime. E.g. JDBC driver
5. test - required for testing - not transitive. E.g., JUnit
6. import

#### References

* https://www.baeldung.com/maven-dependency-scopes
* https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html

## Bump version

* `mvn versions:set -DgenerateBackupPoms=false -DnewVersion=<Put_New_Version_Here>`

## Deploy

* `mvn deploy`

## Cheatsheet - Look at Google Drive
