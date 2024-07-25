# Configuración de NGROK para Desarrollo Local

Este repositorio contiene scripts y configuraciones para facilitar el uso de NGROK en entornos de desarrollo local, especialmente útil para compartir proyectos en desarrollo con equipos remotos o realizar pruebas de integración.

## Requisitos previos

- Asegúrate de tener **WSL (Windows Subsystem for Linux)** instalado en tu sistema.
- Descarga este repositorio y sigue las instrucciones a continuación para configurar NGROK.

## Instalación

1. Ejecuta el archivo `install.sh` para instalar las dependencias necesarias.
2. Posteriormente, ejecuta `ngrok-and-jq.sh` para configurar NGROK y JQ.

## Configuración de tokens NGROK

1. Crea dos cuentas en [ngrok.com](https://ngrok.com) si aún no las tienes.

2. Navega al directorio raíz del usuario (`cd ~`) y modifica el archivo `.config`. Si este archivo no existe, busca la carpeta donde está NGROK y crea una carpeta llamada `~/.ngrok2`. Dentro de esta carpeta, crea dos archivos de configuración: `ngrok.yml` para el túnel del frontend y `ngrok2.yml` para el túnel del backend.

### Configuración del frontend (`ngrok.yml`)

```yaml
front:
  version: "2"
  authtoken: [TOKEN_DEL_FRONTEND]
  tunnels:
    web:
      proto: http
      addr: 3000
```

### Configuración del backend (`ngrok2.yml`)

```yaml
back:
  version: "2"
  authtoken: [TOKEN_DEL_BACKEND]
  tunnels:
    api:
      proto: http
      addr: 8000
```

3. Abre el archivo `ngrok.sh` y modifica las rutas de los archivos de configuración según sea necesario.

## Uso

1. Ejecuta `up.sh` para iniciar el servicio.

2. Posteriormente, ejecuta `ngrok.sh` para establecer los túneles NGROK.

## Cambios en los archivos

- En la carpeta `back`, modifica el archivo `.env` según la configuración específica de tu proyecto.
- Asegúrate de que `main.py` en la carpeta `back` esté configurado para tomar la variable de entorno NGROK.
- La carpeta `front` no necesita cambios en el archivo `.env`.

- Cambia los nombres de las carpetas `front` y `back` según corresponda y crea la base de datos si es necesario.

## Docker

Por último, agrega los archivos Docker para cada proyecto para facilitar la configuración y ejecución en entornos de desarrollo y producción.

¡Listo! Ahora estás listo para compartir tus proyectos en desarrollo o realizar pruebas de integración con NGROK en tu entorno de desarrollo local.

## Tumbar Servicions

Para detener los túneles de NGROK, ejecuta el siguiente comando en tu terminal:

```bash
sudo killall ngrok
```

Y para detener los contenedores de Docker, utiliza el siguiente script:

```bash
sudo ./deleter.sh
```
