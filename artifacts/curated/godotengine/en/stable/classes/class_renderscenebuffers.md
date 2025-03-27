# RenderSceneBuffers

Inherits: RefCounted < Object

Inherited By: RenderSceneBuffersExtension, RenderSceneBuffersRD

Abstract scene buffers object, created for each viewport for which 3D
rendering is done.

## Description

Abstract scene buffers object, created for each viewport for which 3D
rendering is done. It manages any additional buffers used during rendering and
will discard buffers when the viewport is resized.

Note: This is an internal rendering server object, do not instantiate this
from script.

## Methods

void | configure(config: RenderSceneBuffersConfiguration)  
---|---  
  
## Method Descriptions

void configure(config: RenderSceneBuffersConfiguration)

This method is called by the rendering server when the associated viewports
configuration is changed. It will discard the old buffers and recreate the
internal buffers used.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

