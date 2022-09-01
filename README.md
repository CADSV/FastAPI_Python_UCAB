# FastAPI_Python_UCAB
Segundo proyecto de la materia de Python, para la carrera de Ingeniería Informática en la Universidad Católica Andrés Bello.


## Descripción

Utilizando la base de datos de demostración que tiene SQLite, la cual contiene datos de una aplicación de un sitio de música ficticio se desea hacer una prueba de concepto para un sitio real. El dueño de la tienda real quiere construir una aplicación para lo cual contrata un equipo de desarrollo del cual usted forma parte. Su función en el equipo es la del desarrollo del backend. En una primera fase se requiere que el API exponga algunos endpoints con la finalidad de ir haciendo la prueba de concepto. Es así que el API va a ser bastante sencillo y no tendrá funcionalidad de seguridad, en otras palabras no requiere que tenga funciones de chequeo de usuario y password, ni emisión de jwt o verificación usando Oauth2.

## Instrucciones

- Lee cuidadosamente todo el texto del proyecto antes de empezar a trabajar, si tiene alguna duda, consulte al profesor, según las condiciones al final del texto.
- EL proyecto DEBE ser desarrollado en Python, usando FastAPI para generar el API solicitado.
- Los endpoints que se requieren son: 

  - Proporcione una lista artistas (nombre).
  - Proporcione una lista de los álbumes de un artista, seleccionándolo con el Id del artista.
  - Proporcione una lista de las canciones de un álbum, seleccionándolo con el Id del álbum.
  - Proporcione una lista de canciones de un artista, seleccionándolo con el Id del artista.
  - Proporcione el detalle completo (todos los campos de la tabla) de una canción, incluyendo el nombre del género musical y el nombre del tipo de media donde está 
localizado.
- Los nombres de los endpoints DEBEN SER LOS SIGUIENTES:

  - music-store/api/v1/singers/ -> lista total de artistas.
  - music-store/api/v1/singers/{id}/ -> lista de álbumes de un artista.
  - music-store/api/v1/albums/{id}/ -> lista de canciones del álbum de un artista.
  - music-store/api/v1/singer/{id}/ -> lista total de canciones de un artista.
  - music-store/api/v1/song/{id}/ -> detalle de una canción por su id.

- La respuesta debe estar en formato JSON.
- La estructura de carpetas debe ser la misma que se ha usado en los ejemplo de clase.
- El proyecto debe correr en localhost:8000 y mostrar la documentación con el swagger 
incorporado de FastAPI.
- No se ponga creativo, limítese a lo que solicita el proyecto.

## Contribuciones
Formar una comunidad activa en donde todos podamos aprender y crecer juntos en nuestras jornadas de programación es muy gratificante, por lo cual cualquier contribución es muy apreciada. 
Si tienes alguna sugerencia para mejorar esto, por favor bifurca este repositorio y crea un pull request, o crea un issue con el tag `enhacement`

## Problemas y ayudas
En caso de presentar algún tipo de problema con el código, el data set o necesitar alguna ayuda para resolver una duda, por favor revisen los issues para ver si alguien anteriormente tuvo la misma duda, y sino, pueden crear uno nuevo sin problema.

## Licencia
Este proyecto utiliza una licencia del MI, cuyos detalles puedes encontrar en el archivo `LICENSE.md`. Siéntete libre de usar este proyecto como base para tus próximos proyectos.
