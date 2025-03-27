# WebRTCDataChannelExtension

Inherits: WebRTCDataChannel < PacketPeer < RefCounted < Object

There is currently no description for this class. Please help us by
contributing one!

## Methods

void | _close() virtual  
---|---  
int | _get_available_packet_count() virtual const  
int | _get_buffered_amount() virtual const  
int | _get_id() virtual const  
String | _get_label() virtual const  
int | _get_max_packet_life_time() virtual const  
int | _get_max_packet_size() virtual const  
int | _get_max_retransmits() virtual const  
Error | _get_packet(r_buffer: `const uint8_t **`, r_buffer_size: `int32_t*`) virtual  
String | _get_protocol() virtual const  
ChannelState | _get_ready_state() virtual const  
WriteMode | _get_write_mode() virtual const  
bool | _is_negotiated() virtual const  
bool | _is_ordered() virtual const  
Error | _poll() virtual  
Error | _put_packet(p_buffer: `const uint8_t*`, p_buffer_size: int) virtual  
void | _set_write_mode(p_write_mode: WriteMode) virtual  
bool | _was_string_packet() virtual const  
  
## Method Descriptions

void _close() virtual

There is currently no description for this method. Please help us by
contributing one!

int _get_available_packet_count() virtual const

There is currently no description for this method. Please help us by
contributing one!

int _get_buffered_amount() virtual const

There is currently no description for this method. Please help us by
contributing one!

int _get_id() virtual const

There is currently no description for this method. Please help us by
contributing one!

String _get_label() virtual const

There is currently no description for this method. Please help us by
contributing one!

int _get_max_packet_life_time() virtual const

There is currently no description for this method. Please help us by
contributing one!

int _get_max_packet_size() virtual const

There is currently no description for this method. Please help us by
contributing one!

int _get_max_retransmits() virtual const

There is currently no description for this method. Please help us by
contributing one!

Error _get_packet(r_buffer: `const uint8_t **`, r_buffer_size: `int32_t*`)
virtual

There is currently no description for this method. Please help us by
contributing one!

String _get_protocol() virtual const

There is currently no description for this method. Please help us by
contributing one!

ChannelState _get_ready_state() virtual const

There is currently no description for this method. Please help us by
contributing one!

WriteMode _get_write_mode() virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _is_negotiated() virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _is_ordered() virtual const

There is currently no description for this method. Please help us by
contributing one!

Error _poll() virtual

There is currently no description for this method. Please help us by
contributing one!

Error _put_packet(p_buffer: `const uint8_t*`, p_buffer_size: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _set_write_mode(p_write_mode: WriteMode) virtual

There is currently no description for this method. Please help us by
contributing one!

bool _was_string_packet() virtual const

There is currently no description for this method. Please help us by
contributing one!

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

