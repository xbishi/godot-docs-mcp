# VisualShaderNodeColorConstant

Inherits: VisualShaderNodeConstant < VisualShaderNode < Resource < RefCounted
< Object

A Color constant to be used within the visual shader graph.

## Description

Has two output ports representing RGB and alpha channels of Color.

Translated to `vec3 rgb` and `float alpha` in the shader language.

## Properties

Color | constant | `Color(1, 1, 1, 1)`  
---|---|---  
  
## Property Descriptions

Color constant = `Color(1, 1, 1, 1)`

  * void set_constant(value: Color)

  * Color get_constant()

A Color constant which represents a state of this node.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

