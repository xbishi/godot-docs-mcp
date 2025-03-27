# LightmapperRD

Inherits: Lightmapper < RefCounted < Object

The built-in GPU-based lightmapper for use with LightmapGI.

## Description

LightmapperRD ("RD" stands for RenderingDevice) is the built-in GPU-based
lightmapper for use with LightmapGI. On most dedicated GPUs, it can bake
lightmaps much faster than most CPU-based lightmappers. LightmapperRD uses
compute shaders to bake lightmaps, so it does not require CUDA or OpenCL
libraries to be installed to be usable.

Note: Only usable when using the RenderingDevice backend (Forward+ or Mobile
renderers), not Compatibility.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

