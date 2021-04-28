# code

```go
func JsonPretty(obj interface{}) string {
	buf, _ := json.MarshalIndent(obj, "", "  ")
	return string(buf)
}
```
