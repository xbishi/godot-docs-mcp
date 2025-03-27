# PackedDataContainerRef

Inherits: RefCounted < Object

An internal class used by PackedDataContainer to pack nested arrays and
dictionaries.

## Description

When packing nested containers using PackedDataContainer, they are recursively
packed into PackedDataContainerRef (only applies to Array and Dictionary).
Their data can be retrieved the same way as from PackedDataContainer.

    
    
    var packed = PackedDataContainer.new()
    packed.pack([1, 2, 3, ["nested1", "nested2"], 4, 5, 6])
    
    for element in packed:
        if element is PackedDataContainerRef:
            for subelement in element:
                print("::", subelement)
        else:
            print(element)
    

Prints:

    
    
    1
    2
    3
    ::nested1
    ::nested2
    4
    5
    6
    

## Methods

int | size() const  
---|---  
  
## Method Descriptions

int size() const

Returns the size of the packed container (see Array.size() and
Dictionary.size()).

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

