# StreamPeerTCP

Inherits: StreamPeer < RefCounted < Object

A stream peer that handles TCP connections.

## Description

A stream peer that handles TCP connections. This object can be used to connect
to TCP servers, or also is returned by a TCP server.

Note: When exporting to Android, make sure to enable the `INTERNET` permission
in the Android export preset before exporting the project or using one-click
deploy. Otherwise, network communication of any kind will be blocked by
Android.

## Methods

Error | bind(port: int, host: String = "*")  
---|---  
Error | connect_to_host(host: String, port: int)  
void | disconnect_from_host()  
String | get_connected_host() const  
int | get_connected_port() const  
int | get_local_port() const  
Status | get_status() const  
Error | poll()  
void | set_no_delay(enabled: bool)  
  
## Enumerations

enum Status:

Status STATUS_NONE = `0`

The initial status of the StreamPeerTCP. This is also the status after
disconnecting.

Status STATUS_CONNECTING = `1`

A status representing a StreamPeerTCP that is connecting to a host.

Status STATUS_CONNECTED = `2`

A status representing a StreamPeerTCP that is connected to a host.

Status STATUS_ERROR = `3`

A status representing a StreamPeerTCP in error state.

## Method Descriptions

Error bind(port: int, host: String = "*")

Opens the TCP socket, and binds it to the specified local address.

This method is generally not needed, and only used to force the subsequent
call to connect_to_host() to use the specified `host` and `port` as source
address. This can be desired in some NAT punchthrough techniques, or when
forcing the source network interface.

Error connect_to_host(host: String, port: int)

Connects to the specified `host:port` pair. A hostname will be resolved if
valid. Returns @GlobalScope.OK on success.

void disconnect_from_host()

Disconnects from host.

String get_connected_host() const

Returns the IP of this peer.

int get_connected_port() const

Returns the port of this peer.

int get_local_port() const

Returns the local port to which this peer is bound.

Status get_status() const

Returns the status of the connection, see Status.

Error poll()

Poll the socket, updating its state. See get_status().

void set_no_delay(enabled: bool)

If `enabled` is `true`, packets will be sent immediately. If `enabled` is
`false` (the default), packet transfers will be delayed and combined using
Nagle's algorithm.

Note: It's recommended to leave this disabled for applications that send large
packets or need to transfer a lot of data, as enabling this can decrease the
total available bandwidth.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

