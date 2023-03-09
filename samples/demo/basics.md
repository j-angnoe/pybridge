
```python
import sys

def say_hello():
    return "hello from python %s" % sys.version
```

```html
<html>
    <head>
        <title>PyBridge Hello World</title>
    </head>

    <body style="padding:25px;">
        <script>
        async function sayHello() {
            document.write(await api.say_hello())
        }
        sayHello()
        </script>
    </body>
</html>
```