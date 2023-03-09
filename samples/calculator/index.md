# De Calculator voor osman

```python
def berekenen(a, b):
    return int(a) + int(b)
    
```


```html

<template component="app">
    <div>
        Hoe is het? {{ var1 }}

        Waarde 1 <input v-model="waarde1"><br>
        Waarde 2 <input v-model="waarde2"><br>
        <button @click="berekenen">Bereken de shit</button>
        <div v-if="antwoord">
            <hr>
            De som van deze dingen is {{ antwoord }}
        </div>
    </div>
    <script>
    return class vue {
        var1 = 'hallo'
        waarde1 = null;
        waarde2 = null;
        antwoord = null;

        mounted() { 

        }

        async berekenen() {
            this.antwoord = await api.berekenen(this.waarde1, this.waarde2)
        }
    }
    </script>
</template>
    
<style>
    main {
        padding: 25px;
    }
</style>

```