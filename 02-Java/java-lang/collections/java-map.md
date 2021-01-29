# Maps

## Methods

### computeIfAbsent

```java
private Map<String, Object01> myMap = new HashMap<>();
myMap.computeIfAbsent("key01", this::method01);
```

* `computeIfAbsent` will call `method01` if key `key01` is not present in the map or if it is `null`.
* Above method `method01` can accept the key value as parameter

```java
private Object01 method01(String key) {
  // do something ...
  return object01;
}

```
