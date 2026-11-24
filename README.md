# Simulación de una conexión TCP y tráfico WWW en Python

## Presentación del proyecto

Este proyecto simula, con Python y la librería estándar `socket`, cómo se establece una conexión TCP entre un cliente y un servidor web, y cómo después se transmite el tráfico de la World Wide Web (WWW) con el protocolo HTTP.

El servidor escucha en `http://127.0.0.1:8080`. Cuando un cliente se conecta, primero se completa el TCP 3-way handshake y después el cliente envía una petición HTTP. El servidor responde con una página HTML sencilla.

## Temas del programa

- **Protocolos HTTP/HTTPS:** HTTP es el protocolo con el que el navegador pide páginas web. HTTPS es la versión segura, con los datos cifrados.
- **FTP:** es el protocolo para transferir archivos entre computadoras.
- **WWW:** es la World Wide Web, el sistema de páginas web que se consultan con un navegador.
- **TCP:** es el protocolo de transporte orientado a conexión. Antes de enviar datos, el cliente y el servidor negocian la conexión.

## Objetivo

Observar cómo se establece una conexión segura antes de transferir datos (el protocolo TCP) y simular el tráfico de la World Wide Web.

## ¿Qué ocurre paso a paso?

1. **Crear el socket:** `socket.socket(AF_INET, SOCK_STREAM)` le indica al sistema operativo que se quieren usar sockets de Internet (AF_INET) orientados a conexión y fiables, es decir, TCP (SOCK_STREAM).
2. **Vincular y escuchar:** el servidor se vincula a la IP `127.0.0.1` y al puerto `8080`, y queda en modo escucha con `listen(1)`.
3. **El Handshake:** cuando el cliente llama a `connect()`, el sistema operativo maneja automáticamente el intercambio de los tres paquetes TCP: **SYN, SYN-ACK y ACK**. Una vez que `connect()` termina sin errores, el canal está sincronizado y listo.
4. **Tráfico WWW:** inmediatamente después del handshake, el cliente envía un flujo de texto con formato HTTP (`GET / HTTP/1.1...`), simulando lo que hace un navegador web cuando visita una página.
5. **Respuesta del servidor:** el servidor responde con `HTTP/1.1 200 OK` y una página HTML.
6. **Cierre:** se cierra la conexión.

## Archivos del proyecto

- `main.py`: servidor TCP que simula un servidor web básico.
- `cliente.py`: cliente TCP que se conecta al servidor y envía una petición HTTP.
- `README.md`: presentación del proyecto.

## Requisitos

- Python 3 instalado.
- No se necesita instalar ninguna librería extra, solo la librería estándar `socket`.

## Cómo ejecutar el proyecto

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar el servidor:

```bash
python main.py
```

3. Abrir otra terminal en la misma carpeta.
4. Ejecutar el cliente:

```bash
python cliente.py
```

También se puede probar desde el navegador, visitando:

```
http://127.0.0.1:8080
```

## Resultado esperado

En la terminal del servidor se ve:

```text
[*] Servidor escuchando en http://127.0.0.1:8080
[*] Esperando a que ocurra el TCP 3-way handshake...

[+] ¡Conexión TCP establecida con éxito desde ('127.0.0.1', puerto)!
--- Solicitud recibida del cliente ---
GET / HTTP/1.1
Host: 127.0.0.1:8080

[*] Conexión cerrada por el servidor.
```

En la terminal del cliente se ve la respuesta HTML:

```text
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<html><body><h1>¡Hola desde el servidor TCP simulado de la WWW!</h1></body></html>
```

## Conclusión

Con este proyecto se comprueba que, antes de enviar cualquier página web, primero debe establecerse la conexión TCP con el 3-way handshake. Solo después de eso se puede enviar la petición HTTP y recibir la respuesta HTML.
