# A simple calculator

Here we demonstrate a simple calculator

Python is used to perform calculate the sum of two integers

To run this example: run `pybridge --examples calculator`

```python
def calculate(a, b):
    a = a if a else 0
    b = b if b else 0
    return int(a) + int(b)
```

This Vue component will allow the user to enter two numbers
allows the user to submit values to be calculated.

```html
<template component="app">
    <form @submit.prevent="calculate">
        <p>Enter 2 numbers and press calculate!</p>

        Calculator: 
        <input v-model="value1" size=4> +
        <input v-model="value2" size=4> 
        <span v-if="answer"> = {{ answer }}</span>
        <button @click="calculate">Calculate</button>
    </form>
    <script>
    return class vue {
        value1 = null;
        value2 = null;
        answer = null;

        mounted() { 

        }

        async calculate() {
            this.answer = await api.calculate(this.value1, this.value2)
        }
    }
    </script>
</template>
    
<style>
    body {
        padding: 25px;
    }
</style>

```

