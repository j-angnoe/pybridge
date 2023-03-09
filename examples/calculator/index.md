# A simple calculator

Here we demonstrate a simple calculator

Python is used to perform calculate the sum of two integers

```python
def calculate(a, b):
    return int(a) + int(b)
```

This Vue component will allow the user to enter two numbers
allows the user to submit values to be calculated.

```html
<template component="app">
    <form @submit.prevent="calculate">
        
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

