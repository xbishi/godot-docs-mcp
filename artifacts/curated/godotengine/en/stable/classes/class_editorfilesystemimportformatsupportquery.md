# EditorFileSystemImportFormatSupportQuery

Inherits: RefCounted < Object

Used to query and configure import format support.

## Description

This class is used to query and configure a certain import format. It is used
in conjunction with asset format import plugins.

## Methods

PackedStringArray | _get_file_extensions() virtual const  
---|---  
bool | _is_active() virtual const  
bool | _query() virtual const  
  
## Method Descriptions

PackedStringArray _get_file_extensions() virtual const

Return the file extensions supported.

bool _is_active() virtual const

Return whether this importer is active.

bool _query() virtual const

Query support. Return `false` if import must not continue.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

