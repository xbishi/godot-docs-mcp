# EditorSyntaxHighlighter

Inherits: SyntaxHighlighter < Resource < RefCounted < Object

Inherited By: GDScriptSyntaxHighlighter

Base class for SyntaxHighlighter used by the ScriptEditor.

## Description

Base class that all SyntaxHighlighters used by the ScriptEditor extend from.

Add a syntax highlighter to an individual script by calling
ScriptEditorBase.add_syntax_highlighter(). To apply to all scripts on open,
call ScriptEditor.register_syntax_highlighter().

## Methods

String | _get_name() virtual const  
---|---  
PackedStringArray | _get_supported_languages() virtual const  
  
## Method Descriptions

String _get_name() virtual const

Virtual method which can be overridden to return the syntax highlighter name.

PackedStringArray _get_supported_languages() virtual const

Virtual method which can be overridden to return the supported language names.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

