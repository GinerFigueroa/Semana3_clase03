# -*- coding: utf-8 -*-
"""Semana3_ 2.varibles.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jUZB_ozAbE_RquoQXewkm2QGjZ1L60Y5

Semana 03

Figueroa Gonzalez

Temas:
 1. Numeros
 2. variables
 3. Manejo de cadenas
 4. Ingreso por teclado
 5. Operciones
"""

# In[1]:


4+6

# In[2]:


10/9

# In[3]:


7*6

#este es mi primer comentario
nombre = "Giner"

# In[11]:


nombre

# In[21]:


apellido=" figueroa Giner"

# In[22]:


apellido

# In[23]:


nombrecompleto =nombre +apellido

# In[24]:


nombrecompleto

# In[44]:


#aber el tipo de mi variable
numero =50

# In[37]:


numeros=100
cadena=str(numero)
cadena

# Definir una función que toma dos argumentos y devuelve su suma
def suma(a, b):
    resultado = a + b  # Variable local resultado
    return resultado

# Llamar a la función y almacenar el resultado en una variable
x = 5
y = 3
resultado_suma = suma(x, y)

# Imprimir el resultado
print("La suma de", x, "y", y, "es:", resultado_suma)

