# PCKPacker

Inherits: RefCounted < Object

Creates packages that can be loaded into a running project.

## Description

The PCKPacker is used to create packages that can be loaded into a running
project using ProjectSettings.load_resource_pack().

GDScriptC#

    
    
    var packer = PCKPacker.new()
    packer.pck_start("test.pck")
    packer.add_file("res://text.txt", "text.txt")
    packer.flush()
    
    
    
    var packer = new PckPacker();
    packer.PckStart("test.pck");
    packer.AddFile("res://text.txt", "text.txt");
    packer.Flush();
    

The above PCKPacker creates package `test.pck`, then adds a file named
`text.txt` at the root of the package.

Note: PCK is Godot's own pack file format. To create ZIP archives that can be
read by any program, use ZIPPacker instead.

## Methods

Error | add_file(target_path: String, source_path: String, encrypt: bool = false)  
---|---  
Error | add_file_removal(target_path: String)  
Error | flush(verbose: bool = false)  
Error | pck_start(pck_path: String, alignment: int = 32, key: String = "0000000000000000000000000000000000000000000000000000000000000000", encrypt_directory: bool = false)  
  
## Method Descriptions

Error add_file(target_path: String, source_path: String, encrypt: bool =
false)

Adds the `source_path` file to the current PCK package at the `target_path`
internal path. The `res://` prefix for `target_path` is optional and stripped
internally.

Error add_file_removal(target_path: String)

Registers a file removal of the `target_path` internal path to the PCK. This
is mainly used for patches. If the file at this path has been loaded from a
previous PCK, it will be removed. The `res://` prefix for `target_path` is
optional and stripped internally.

Error flush(verbose: bool = false)

Writes the files specified using all add_file() calls since the last flush. If
`verbose` is `true`, a list of files added will be printed to the console for
easier debugging.

Error pck_start(pck_path: String, alignment: int = 32, key: String =
"0000000000000000000000000000000000000000000000000000000000000000",
encrypt_directory: bool = false)

Creates a new PCK file at the file path `pck_path`. The `.pck` file extension
isn't added automatically, so it should be part of `pck_path` (even though
it's not required).

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

