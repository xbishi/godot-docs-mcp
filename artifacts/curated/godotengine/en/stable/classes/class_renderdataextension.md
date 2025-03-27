# RenderDataExtension

Inherits: RenderData < Object

This class allows for a RenderData implementation to be made in GDExtension.

## Description

This class allows for a RenderData implementation to be made in GDExtension.

## Methods

RID | _get_camera_attributes() virtual const  
---|---  
RID | _get_environment() virtual const  
RenderSceneBuffers | _get_render_scene_buffers() virtual const  
RenderSceneData | _get_render_scene_data() virtual const  
  
## Method Descriptions

RID _get_camera_attributes() virtual const

Implement this in GDExtension to return the RID for the implementation's
camera attributes object.

RID _get_environment() virtual const

Implement this in GDExtension to return the RID of the implementation's
environment object.

RenderSceneBuffers _get_render_scene_buffers() virtual const

Implement this in GDExtension to return the implementation's
RenderSceneBuffers object.

RenderSceneData _get_render_scene_data() virtual const

Implement this in GDExtension to return the implementation's
RenderSceneDataExtension object.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

