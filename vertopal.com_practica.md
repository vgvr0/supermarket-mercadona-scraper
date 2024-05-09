---
jupyter:
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.12.3
  nbformat: 4
  nbformat_minor: 2
---

::: {.cell .markdown}
```{=html}
<h1 style="color: navy; font-weight: bold;">Práctica Tema 4: Inteligencia Artificial Generativa en estrategias de Marketing</h1>
```
:::

::: {.cell .markdown}
![Foto de portada](FotoPortada.png)
:::

::: {.cell .markdown}
## `<h2 style="color: navy; font-weight: bold;">`{=html}Configuración inicial`</h2>`{=html}
:::

::: {.cell .code execution_count="1"}
``` python
# Configuración inicial 
import os
from openai import OpenAI
import pandas as pd
```
:::

::: {.cell .code execution_count="2"}
``` python
key = 'sk-proj-CR9MauC7LGqQ5MomvghoT3BlbkFJmqwFKVUUPHKmqhq1f4xK'

os.environ['OPENAI_API_KEY'] = key
client = OpenAI()
```
:::

::: {.cell .code execution_count="38"}
``` python
# Funcion para generar y procesar múltiples respuestas. Incluye argumentos predefinidos pero puedes los que desees
def gpt(prompt, engine="gpt-3.5-turbo-instruct", max_tokens=100, temperature=0.2, n=1, frequency_penalty=0.2, stop_sequence=None, top_p=None, **kwargs):
    response = client.completions.create(
        model=engine,  # Motor que se utilizará
        prompt=prompt,  # Instrucciones
        max_tokens=max_tokens,  # Número máximo de tokens a generar en la completitud
        temperature=temperature,  # Temperatura para controlar la creatividad de las respuestas
        n=n,  # Número de respuestas a generar
        frequency_penalty=frequency_penalty,  # Penaliza la generación de tokens repetidos
        stop=stop_sequence,  # Secuencia de parada opcional
        top_p=top_p,  # Limita la selección de tokens a los más probables
        **kwargs # Opción para introducir otros argumentos como best_of, logit_bias, echo...
    )
    responses = [choice.text.strip() for choice in response.choices]
    for i, result in enumerate(responses, start=1):
        print(f"Respuesta {i}:\n{result}\n")
    return responses

# Ejemplo para comprobar el funcionamiento
prompt = "¿Cuál es el mejor equipo de fútbol?"
response = gpt(prompt, engine="gpt-3.5-turbo-instruct", max_tokens=100, temperature=0.7, n=2)
```

::: {.output .stream .stdout}
    Respuesta 1:
    Esta es una pregunta subjetiva y cada persona puede tener una opinión diferente. Algunos podrían argumentar que el mejor equipo de fútbol es el Real Madrid, ya que ha ganado la Liga de Campeones de la UEFA más veces que cualquier otro equipo (13 veces). Otros podrían decir que el FC Barcelona es el mejor por su estilo de juego atractivo y su éxito en la liga española. Otros podrían argumentar por

    Respuesta 2:
    Esta es una pregunta muy subjetiva y depende del criterio de cada persona. Algunos podrían considerar al Real Madrid como el mejor equipo de fútbol debido a su extenso palmarés y grandes jugadores, mientras que otros podrían optar por el FC Barcelona por su estilo de juego atractivo y su éxito reciente. Otros posibles candidatos podrían ser el Bayern Munich, el Manchester United, el Liverpool o el Juventus. En
:::
:::

::: {.cell .markdown}
## `<h2 style="color: navy; font-weight: bold;">`{=html}Generación de contenido con mejores prácticas para prompt `</h2>`{=html} {#generación-de-contenido-con-mejores-prácticas-para-prompt-}
:::

::: {.cell .code}
``` python
```
:::
