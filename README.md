# PyBridge - Magical bridge between javascript and python

Bridges the gap between Javascript (frontend) and Python (Backend).

It's a small python webserver that serves the files from the current directory.
It will read .html, .py and .md (markdown) files.
In the HTML files a javascript `api` object will be made available that allows
you to run the python function defined in .py and .md files.

This is a nice utility for quick proof-of-concepts, demonstrations and educational
purposes.

More info:
- [PHP-Bridge](https://github.com/j-angnoe/php-bridge), same idea, different backend
- [Vue-Blocks](https://github.com/j-angnoe/vue-blocks) - more Vue, less building and compilation.

# Installation
clone this repo, put is somewhere and run cli/pybridge. You could add cli/pybridge to your $PATH.

# Usage
```
pybridge [path?] [--port?] [--no-browser?] [-h|--help?]

    by default, the current directory will be `served` on a port between 31000 and 33000
    it will open this url in your browser automatically, unless you provide the option `--no-browser`
```

# Hello world example

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

You can `serve` a markdown file that contains these two blocks
or write them to index.html and an index.py file. 

# Vue (vue-blocks) included

For purposes that require more interactivity, vue-blocks is auto-included. Vue-blocks allows you to write many Vue SFC like components inside a single html document, thus allowing us to write not only SPA but SFA (Single File Application).

```html

<template component="app">
    <div>
        <!-- a simple `layout` with navigation and router-view outlet for our pages -->
        <nav>
            <router-link to="/">Home</router-link>
            <router-link to="/page1">Page 1</router-link>
            <router-link to="/page2">Page 2</router-link>
        </nav>
        <router-view></router-view>
    </div>
</template>
<template url="/">
    <div><h1>Home</h1></div>
    <script>
    export default {
        data() {
            return {
                intro: null
            }
        }
        async mounted() {
            // vue mount function

            // load our say_hello data 
            this.intro = await api.say_hello()
        }
    }
    </script>
</template>
<template url="/page1">
    <div><h1>Page 1</h1></div>
</template>
<template url="/page2">
    <div><h1>Page 2</h1></div>
</template>

```


