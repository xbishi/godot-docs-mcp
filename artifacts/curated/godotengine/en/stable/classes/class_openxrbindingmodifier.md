# OpenXRBindingModifier

Inherits: Resource < RefCounted < Object

Inherited By: OpenXRActionBindingModifier, OpenXRIPBindingModifier

Binding modifier base class.

## Description

Binding modifier base class. Subclasses implement various modifiers that alter
how an OpenXR runtime processes inputs.

## Methods

String | _get_description() virtual const  
---|---  
PackedByteArray | _get_ip_modification() virtual  
  
## Method Descriptions

String _get_description() virtual const

Return the description of this class that is used for the title bar of the
binding modifier editor.

PackedByteArray _get_ip_modification() virtual

Returns the data that is sent to OpenXR when submitting the suggested
interacting bindings this modifier is a part of.

Note: This must be data compatible with a `XrBindingModificationBaseHeaderKHR`
structure.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

