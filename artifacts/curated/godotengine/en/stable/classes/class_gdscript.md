# GDScript

Inherits: Script < Resource < RefCounted < Object

A script implemented in the GDScript programming language.

## Description

A script implemented in the GDScript programming language, saved with the
`.gd` extension. The script extends the functionality of all objects that
instantiate it.

Calling new() creates a new instance of the script. Object.set_script()
extends an existing object, if that object's class matches one of the script's
base classes.

If you are looking for GDScript's built-in functions, see @GDScript instead.

## Tutorials

  * GDScript documentation index

## Methods

Variant | new(...) vararg  
---|---  
  
## Method Descriptions

Variant new(...) vararg

Returns a new instance of the script.

    
    
    var MyClass = load("myclass.gd")
    var instance = MyClass.new()
    print(instance.get_script() == MyClass) # Prints true
    

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[vararg]: This method accepts any number of arguments after the ones described here.

