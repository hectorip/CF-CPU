# Ejercicios

Codifica los siguientes instrucciones en el lenguaje que en el que hayas hecho tu CPU y ejecúta el programa.

## Ejercicio: suma de dos números

```python
# Suma de dos números

[
    ('CONST', 'Ra', 10),
    ('CONST', 'Rb', 20),
    ('ADD', 'Ra', 'Rb', 'Rc'),
    ('HALT'),
]
```

```python
# Suma de los primeros números
[
    ('CONST', 'Ra', 11),
    ('CONST', 'Rb', 1),
    ('CONST', 'Rc', 0),
    ('CONST', 'Rd', 4), # Dirección en donde empieza el bucle
    ('CMP', '<=', 'Rb', 'Ra', 'Rd'),
    ('ADD', 'Rb', 'Rc', 'Rc'),
    ('JMP', 'Rd', 0),
    ('HALT')
]
```