## Fondeadora Challenge
Escribe un código en Python que aplane un arreglo de enteros o arreglos de enteros (que puede estar anidado arbitrariamente) a un arreglo plano de enteros.

Por ej. para el arreglo:
```sh
[1, [2, [3, [4, 5]]]]
```
Tu código debe devolver:
```sh
[1, 2, 3, 4, 5]
```
### Installation

Clonación del proyecto
```sh
git clone https://github.com/jdht1992/fondeadora.git
```

Aqui se requiere cualquier gestor de entornos virtuales de Python
```sh
pyenv virtualenv 3.8 env_fondeadora
pyenv activate env_fondeadora

```
Instalacion de paquetes.
```
cd fondeadora
pip install -r requirements.txt
```

### Ejecutar proyecto .

Si se requiere ejecutar el script descomentamos la invocacion a la funcion que esta en el archivo flatten.py y ejecutamos
```sh
python flatten.py
```

### Ejecutar test .

Para ejecutar los test solo añadimos el comando en la terminarl
```sh
pytest -v
```