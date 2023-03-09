# PyBridge Markdown demo


```python
import sys

def doe_dit():
    return 'hoi'
    
def hallo():
    return f"hoe is het, ik ben python {sys.version} %s" % doe_dit()

```


```html
<style>
    body { padding: 25px; }
</style>

<template component="app" props="">
    <div>
        Server said: {{ server_data }}        
    </div>
    <style scoped>
    </style>
    <script>
    return class vue {
        server_data = 'loading';
        async mounted() {
            this.server_data = await api.hallo()
        }
    }
    </script>
</template>
```
