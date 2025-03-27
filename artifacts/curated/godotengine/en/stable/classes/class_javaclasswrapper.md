# JavaClassWrapper

Inherits: Object

Provides access to the Java Native Interface.

## Description

The JavaClassWrapper singleton provides a way for the Godot application to
send and receive data through the Java Native Interface (JNI).

Note: This singleton is only available in Android builds.

    
    
    var LocalDateTime = JavaClassWrapper.wrap("java.time.LocalDateTime")
    var DateTimeFormatter = JavaClassWrapper.wrap("java.time.format.DateTimeFormatter")
    
    var datetime = LocalDateTime.now()
    var formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")
    
    print(datetime.format(formatter))
    

Warning: When calling Java methods, be sure to check get_exception() to check
if the method threw an exception.

## Methods

JavaObject | get_exception()  
---|---  
JavaClass | wrap(name: String)  
  
## Method Descriptions

JavaObject get_exception()

Returns the Java exception from the last call into a Java class. If there was
no exception, it will return `null`.

Note: This method only works on Android. On every other platform, this method
will always return `null`.

JavaClass wrap(name: String)

Wraps a class defined in Java, and returns it as a JavaClass Object type that
Godot can interact with.

Note: This method only works on Android. On every other platform, this method
does nothing and returns an empty JavaClass.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

