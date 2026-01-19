# 👀 Observer

Uma lib completamente inútil com o objetivo de observar.

Criada **de propósito** para o ** Evento | Bibliotecas Inúteis**.  
Ela observa valores, percorre estruturas e **não faz absolutamente nada com isso**.

---

## 🤔 O que é isso?

A `observer` é uma biblioteca Python que:

- Recebe valores
- Observa silenciosamente
- Não retorna nada
- Não altera nada
- Não resolve nada

Ela apenas existe.  
E isso já é o suficiente.

---

## 📦 Instalação

Não está no PyPI.  
Não tem setup.  
Não tem versão.

Copie o arquivo `observer.py` e coloque no seu projeto.  
Ou não coloque. Dá no mesmo.

```
observer/
 ├── observer.py
 └── main.py (opcional e igualmente inútil)
```

---

## 🚀 Uso

### Observação simples

```python
from observer import observe

observe(123)
observe("hello")
observe([1, 2, 3])
```

Resultado: nada acontece.

---

### Observação profunda (mais inútil ainda)

```python
from observer import observe_deeply

observe_deeply({"a": [1, 2, 3], "b": "texto"})
```

Ela percorre tudo:
- Strings letra por letra
- Listas, tuplas, sets
- Dicionários (chaves e valores)
- Evita loop infinito

E mesmo assim…  
**não retorna nada.**

---

### Observa ou não observa

```python
from observer import observe_or_not

observe_or_not("talvez")
```

Ela decide aleatoriamente se vai observar.  
Nem ela se importa.

---

### Confirmação de existência

```python
from observer import confirm_existence

confirm_existence(1, 2, 3)
```

Saída:

```text
True
```

Sem argumentos:

```python
confirm_existence()
```

```text
False
```

A função mais útil da biblioteca.  
Ainda inútil.

---

## 🧠 Por que isso existe?

Porque o desafio pediu.  
E porque nem toda biblioteca precisa ser útil.

---

## 🏆 Nível de inutilidade

- Retorna algo? ❌
- Faz algo relevante? ❌
- Poderia não existir? ✅

---

## 📜 Licença

Use como quiser.  
Ela não vai reclamar.

---

Observer observa.  
Você perde tempo.  
Todo mundo ganha.
