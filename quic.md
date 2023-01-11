# QUIC

Como bien sabemos QUIC opera sobre UDP encargandose de los handshakes tanto UDP como TLS, para posteriormente realizar las request HTTP, utilizando la version 3 de este protocolo (HTTP/3).

![](img/quic.png)


Notas de lectura:

**Matching Packets to Connections**

* The first packet for an unsupported version can use different semantics and encodings for any version-specific field. In particular, different packet protection keys might be used for different versions. Servers that do not support a particular version are unlikely to be able to decrypt the payload of the packet or properly interpret the result. Servers SHOULD respond with a Version Negotiation packet, provided that the datagram is sufficiently long.

  Packets with a supported version, or no Version field, are matched to a connection using the connection ID or -- for packets with zero-length connection IDs -- the local address and port. These packets are processed using the selected connection; otherwise, the server continues as described below.

  If the packet is an Initial packet fully conforming with the specification, the server proceeds with the handshake (Section 7). This commits the server to the version that the client selected.


**Version Negotiation**

* Version negotiation allows a server to indicate that it does not support the version the client used. A server sends a Version Negotiation packet in response to each packet that might initiate a new connection.

The size of the first packet sent by a client will determine whether a server sends a Version Negotiation packet. Clients that support multiple QUIC versions SHOULD ensure that the first UDP datagram they send is sized to the largest of the minimum datagram sizes from all versions they support, using PADDING frames as necessary. This ensures that the server responds if there is a mutually supported version. A server might not send a Version Negotiation packet if the datagram it receives is smaller than the minimum size specified in a different version.

  A Version Negotiation packet is not acknowledged. It is only sent in response to a packet that indicates an unsupported version.

  The Version Negotiation packet does not include the Packet Number and Length fields present in other packets that use the long header form. Consequently, a Version Negotiation packet consumes an entire UDP datagram.
# Links utiles

* [HTTP/3](https://www.cloudflare.com/es-es/learning/performance/what-is-http3/)
* [QUIC](https://blog.cloudflare.com/the-road-to-quic/) y mas [QUIC negociacion versiones](https://blog.cloudflare.com/head-start-with-quic/) ([mas](https://blogs.keysight.com/blogs/tech/nwvs.entry.html/2021/07/17/looking_into_quicpa-pUtF.html))