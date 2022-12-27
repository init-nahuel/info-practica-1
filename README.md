Informacion general sobre temas relacionados a la practica 1.

# Conceptos Importantes

* **Internet Socket**: Un socket es un punto final de un enlace de comunicacion bidireccional entre dos programas que se ejecutan en la red (enviar y recibir datos a traves de la red). Un socket esta vinculado a un numero de puerta para que la capa TCP pueda identificar la aplicacion a la que se envian los datos.
  * Un socket queda definido por un par de direcciones IP local y remota, un protocolo de transporte y un par de numeros de puerto local y remoto.
* **Round trip time (RTT)**: El tiempo de ida y vuelta (RTT) es el tiempo que tarda un paquete de datos en enviarse a un destino más el tiempo que tarda el receptor en enviar un mensaje acusando el recibo de este paquete.
* **Jitter**: Concepto utilizado para referirse a la demora en el tiempo de envio de un paquete de datos a traves de la conexion de red. Usualmente ocurre por una congestion en la red.
* **Transmision Control Protocol (TCP)**: Protocolo de comunicaciones orientado a la conexión que facilita el intercambio de mensajes entre dispositivos informáticos en una red. Es el protocolo más común en las redes que utilizan el Protocolo de Internet (IP); juntos se denominan a veces TCP/IP.
* **Bandwidth**: Cantidad maxima de datos transmitidos a traves de una conexion a internet en un periodo de tiempo determinado. El ancho de banda suele confundirse con la **velocidad del internet**, sin embargo es el volumen de informacion que puede enviarse a traves de una conexion en un periodo de tiempo medido, calculado en megabits por segundo (Mbps).
* **VoIP**: Metodo que permite hacer llamadas de voz utilizando una conexion a internet de banda ancha en lugar de una linea telefonica normal (Ej: Skype, Whatsapp).
* **Internet Control Message Protocol (ICMP)**: El protocolo de control de mensajes de internet es un protocolo en la **capa de red** que utilizan los dispostivos de red pra  diagnosticar problemas de comunicacion en la red. El ICMP se utiliza principalmente para determinar si los datos llegan o no a su destino a su debido tiempo. El protocolo ICMP se suele utilizar en dispositivos de red, como los enrutadores. El ICMP es crucial para informar de errores y realizar pruebas.
* **TCP Three-Way HandShake (TCP 3-way)**: Es un proceso que se utiliza en una red TCP/IP para establece una conexion entre el servidor y el cliente. Es un proceso de tres pasos que requiere que tanto el cliente como el servidor intercambien paquetes de sincronizacion y reconocimiento antes de que comience el proceso real de comunicacion de datos, luego de esto se establece formalmente la conexion.
* **Virtual Private Network (VPN)**: Una red privada virtual es un servicio de seguridad que permite que los usuarios accedan a Internet como si estuvieran conectados a una red privada. Esto encripta las comunicaciones de internet, ademas de proporcionar un alto grado de anonimato. Una conexion VPN implica los siguientes 4 pasos:
  * El cliente VPN se conecta al ISP mediante una conexion encriptada.
  * El ISP conecta al cliente VPN con el servidor VPN, mantiendo la conexion encriptada, asi el ISP no puede ver la actividad del usuario.
  * El servidor VPN descifra los datos del dispositivo del usuario y, a continuacion, se conecta a internet para acceder al servidor web en una comunicacion no encriptada.
  * El servidor VPN crea una conexion encriptada con el cliente, que se conoce como **tunel VPN**. Las comunicaciones del servidor VPN con internet no estan encriptadas, pero los servidores web solo registraran la direccion IP del servidor VPN, lo cual no les da informacion alguna sobre el usuario.
* **Internet Service Provider (ISP)**: Un proveedor de servicios de internet es una empresa que se dedica a ofrecer servicios de acceso a internet a sus clientes.
* **Secure Sockets Layer (SSL)**: Es un protocolo de internet basado en el cifrado (predecesor de TLS). 
  * Para ofrecer un alto grado de privacidad, SSL cifra los datos que se transmiten por la web.
  * SSL inicia un proceso de autenticacion, conocido como establecimiento de comunicacion, entre dos dispositivos que se comunican para garantizar que ambos sean lo que aparentan.
  * Ademas, SSL firma digitalmente los datos para proporcionar integridad de datos, que verifica que no se hayan manipulado los datos antes de alcanzar al destinatario designado.
* **Transport Layer Security (TLS)**: Es un protocolo de seguridad diseñado para facilitar la privacidad y la seguridad de los datos en las comunicaciones por Internet. Un caso de uso primario de TLS es la encriptacion de las comunicaciones entre aplicaciones web y servidores, como los navegadores que cargan un sitio web. TLS tambien puede usarse para encriptar otras comunicaciones como el correo electronico, los mensajes y la voz sobre IP (VoIP). Existe tres componentes principales en las funciones del protocolo TLS:
  * **Encriptacion**: Oculta los datos que se transfieren a terceras partes.
  * **Autenticacion**: Garantiza que las partes que intercambian informacion sean quienes afirman ser.
  * **Integridad**: Verifica que los datos no han sido falsificados o alterados.
  * **Diferencias entre HTTPS y TLS**: HTTPS es una implementacion de la encriptacion TLS en el protocolo HTTP, usado por todos los sitios web asi como otros servicios web. Todos los sitios web que usan HTTPS emplean por tanto la encriptacion TLS.
* **Hypertext Transfer Protocol Secure (HTTPS)**: El protocolo de transferencia de hipertexto seguro es la version segura de HTTP, que es el principal protocolo utilizado para enviar datos entre un navegador web y un sitio web. El HTTPS esta encriptado para aumentar la seguridad de las transferencias de datos. HTTPS utiliza un protocolo de encriptacion para encriptar las comunicaciones, el protocolo se conoce como TLS, este protocolo asegura las comunicaciones mediante el uso de lo que se conoce como **infraestructura de clave publica asimetrica**. Este titipo de sistema de seguridad utiliza dos claves diferentes para encriptar las comunicaciones entre dos partes:
  * **La clave privada**: Esta clave la controla el propietario de un sitio web y se mantiene privada. Esta clave esta ubicada en un servidor web que se utiliza para desencriptar la informacion encriptada por la clave publica.
  * **La clave publica**: ESta clave está disponible para todos los que quieran interactuar con el servidor de forma segura. La informacion encriptada por la clave publica solo puede ser desencriptada por la clave privada.

  * **OBS**: HTTPS no es un protocolo distinto de HTTP, simplemente utiliza la encriptacion TLS/SSL sobre el protocolo HTTP. HTTPS se basa en la transmision de los certificados TLS/SSL, que verifican que un determinado proveedor es quien dice ser. 


# Links utiles

[Cloudfare](https://www.cloudflare.com/es-es/learning/) sirve harto para aprender sobre la capa de red y protocolos :)


* [Sockets](https://docs.oracle.com/javase/tutorial/networking/sockets/definition.html)
* [Tipos de protocolos de redes y usos](https://www.geeksforgeeks.org/types-of-network-protocols-and-their-uses/)
* [3 tipos de protocolos de redes imortantes](https://www.cdw.com/content/cdw/en/articles/networking/types-of-network-protocols.html)
* [Capa de red](https://www.cloudflare.com/es-es/learning/network-layer/what-is-the-network-layer/)
* [TCP 3-way](https://www.guru99.com/tcp-3-way-handshake.html)
* [VPN](https://www.cloudflare.com/es-es/learning/access-management/what-is-a-vpn/)

Protocolos:

* [TLS](https://www.cloudflare.com/es-es/learning/ssl/transport-layer-security-tls/)
* [HTTPS](https://www.cloudflare.com/es-es/learning/ssl/what-is-https/)
* [TCP](https://www.sdxcentral.com/resources/glossary/transmission-control-protocol-tcp/)
* [ICMP](https://www.cloudflare.com/es-es/learning/ddos/glossary/internet-control-message-protocol-icmp/)