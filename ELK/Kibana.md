# Kibana

## Filters

```json
{
  "query": {
    "bool": {
      "must": {
        "wildcard": {
          "url.original": "/internal*"
        }
      }
    }
  }
}
```
