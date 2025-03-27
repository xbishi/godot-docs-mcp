# JavaObject

Inherits: RefCounted < Object

Represents an object from the Java Native Interface.

## Description

Represents an object from the Java Native Interface. It can be returned from
Java methods called on JavaClass or other JavaObjects. See JavaClassWrapper
for an example.

Note: This class only works on Android. On any other platform, this class does
nothing.

Note: This class is not to be confused with JavaScriptObject.

## Methods

JavaClass | get_java_class() const  
---|---  
  
## Method Descriptions

JavaClass get_java_class() const

Returns the JavaClass that this object is an instance of.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

