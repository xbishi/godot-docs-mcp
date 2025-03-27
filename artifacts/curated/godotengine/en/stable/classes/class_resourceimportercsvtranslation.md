# ResourceImporterCSVTranslation

Inherits: ResourceImporter < RefCounted < Object

Imports comma-separated values

## Description

Comma-separated values are a plain text table storage format. The format's
simplicity makes it easy to edit in any text editor or spreadsheet software.
This makes it a common choice for game localization.

Example CSV file:

    
    
    keys,en,es,ja
    GREET,"Hello, friend!","Hola, amigo!",
    ASK,How are you?,Cmo est?,
    BYE,Goodbye,Adis,
    QUOTE,"""Hello"" said the man.","""Hola"" dijo el hombre.",
    

## Tutorials

  * Importing translations

## Properties

bool | compress | `true`  
---|---|---  
int | delimiter | `0`  
  
## Property Descriptions

bool compress = `true`

If `true`, creates an OptimizedTranslation instead of a Translation. This
makes the resulting file smaller at the cost of a small CPU overhead.

int delimiter = `0`

The delimiter to use in the CSV file. The default value matches the common CSV
convention. Tab-separated values are sometimes called TSV files.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

