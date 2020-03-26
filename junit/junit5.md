# JUnit 5

## All assertions in JUnit 5

```java
assertEquals() and assertNotEquals()
assertArrayEquals()
assertIterableEquals()
assertLinesMatch()
assertNotNull() and assertNull()
assertNotSame() and assertSame()
assertTimeout() and assertTimeoutPreemptively()
assertTrue() and assertFalse()
assertThrows()
fail()
```

Ref: https://howtodoinjava.com/junit5/junit-5-assertions-examples/

## Maven

### Aggregator

#### junit-jupiter

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.4.2</version>
    <scope>test</scope>
</dependency>
```

* Aggregates - junit-jupiter-api, junit-jupiter-engine, junit-jupiter-params and junit-jupiter-migrationsupport
* Reference: [https://junit.org/junit5/docs/current/user-guide/#dependency-metadata-junit-jupiter]()

#### bom

* Reference - [https://junit.org/junit5/docs/current/user-guide/#dependency-metadata-junit-bom]()
