# RDVertexAttribute

Inherits: RefCounted < Object

Vertex attribute (used by RenderingDevice).

## Description

This object is used by RenderingDevice.

## Properties

DataFormat | format | `218`  
---|---|---  
VertexFrequency | frequency | `0`  
int | location | `0`  
int | offset | `0`  
int | stride | `0`  
  
## Property Descriptions

DataFormat format = `218`

  * void set_format(value: DataFormat)

  * DataFormat get_format()

The way that this attribute's data is interpreted when sent to a shader.

VertexFrequency frequency = `0`

  * void set_frequency(value: VertexFrequency)

  * VertexFrequency get_frequency()

The rate at which this attribute is pulled from its vertex buffer.

int location = `0`

  * void set_location(value: int)

  * int get_location()

The location in the shader that this attribute is bound to.

int offset = `0`

  * void set_offset(value: int)

  * int get_offset()

The number of bytes between the start of the vertex buffer and the first
instance of this attribute.

int stride = `0`

  * void set_stride(value: int)

  * int get_stride()

The number of bytes between the starts of consecutive instances of this
attribute.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

