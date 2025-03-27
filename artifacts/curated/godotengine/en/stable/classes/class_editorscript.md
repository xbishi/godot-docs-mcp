# EditorScript

Inherits: RefCounted < Object

Base script that can be used to add extension functions to the editor.

## Description

Scripts extending this class and implementing its _run() method can be
executed from the Script Editor's File > Run menu option (or by pressing
``Ctrl` + `Shift` + `X``) while the editor is running. This is useful for
adding custom in-editor functionality to Godot. For more complex additions,
consider using EditorPlugins instead.

Note: Extending scripts need to have `tool` mode enabled.

Example: Running the following script prints "Hello from the Godot Editor!":

GDScriptC#

    
    
    @tool
    extends EditorScript
    
    func _run():
        print("Hello from the Godot Editor!")
    
    
    
    using Godot;
    
    [Tool]
    public partial class HelloEditor : EditorScript
    {
        public override void _Run()
        {
            GD.Print("Hello from the Godot Editor!");
        }
    }
    

Note: The script is run in the Editor context, which means the output is
visible in the console window started with the Editor (stdout) instead of the
usual Godot Output dock.

Note: EditorScript is RefCounted, meaning it is destroyed when nothing
references it. This can cause errors during asynchronous operations if there
are no references to the script.

## Methods

void | _run() virtual  
---|---  
void | add_root_node(node: Node)  
EditorInterface | get_editor_interface() const  
Node | get_scene() const  
  
## Method Descriptions

void _run() virtual

This method is executed by the Editor when File > Run is used.

void add_root_node(node: Node)

Makes `node` root of the currently opened scene. Only works if the scene is
empty. If the `node` is a scene instance, an inheriting scene will be created.

EditorInterface get_editor_interface() const

Deprecated: EditorInterface is a global singleton and can be accessed directly
by its name.

Returns the EditorInterface singleton instance.

Node get_scene() const

Returns the edited (current) scene's root Node. Equivalent of
EditorInterface.get_edited_scene_root().

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

