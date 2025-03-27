# TCPServer

Inherits: RefCounted < Object

A TCP server.

## Description

A TCP server. Listens to connections on a port and returns a StreamPeerTCP
when it gets an incoming connection.

Note: When exporting to Android, make sure to enable the `INTERNET` permission
in the Android export preset before exporting the project or using one-click
deploy. Otherwise, network communication of any kind will be blocked by
Android.

## Methods

int | get_local_port() const  
---|---  
bool | is_connection_available() const  
bool | is_listening() const  
Error | listen(port: int, bind_address: String = "*")  
void | stop()  
StreamPeerTCP | take_connection()  
  
## Method Descriptions

int get_local_port() const

Returns the local port this server is listening to.

bool is_connection_available() const

Returns `true` if a connection is available for taking.

bool is_listening() const

Returns `true` if the server is currently listening for connections.

Error listen(port: int, bind_address: String = "*")

Listen on the `port` binding to `bind_address`.

If `bind_address` is set as `"*"` (default), the server will listen on all
available addresses (both IPv4 and IPv6).

If `bind_address` is set as `"0.0.0.0"` (for IPv4) or `"::"` (for IPv6), the
server will listen on all available addresses matching that IP type.

If `bind_address` is set to any valid address (e.g. `"192.168.1.101"`,
`"::1"`, etc.), the server will only listen on the interface with that address
(or fail if no interface with the given address exists).

void stop()

Stops listening.

StreamPeerTCP take_connection()

If a connection is available, returns a StreamPeerTCP with the connection.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

