# ResourceImporter

Inherits: RefCounted < Object

Inherited By: EditorImportPlugin, ResourceImporterBitMap,
ResourceImporterBMFont, ResourceImporterCSVTranslation,
ResourceImporterDynamicFont, ResourceImporterImage, ResourceImporterImageFont,
ResourceImporterLayeredTexture, ResourceImporterMP3, ResourceImporterOBJ,
ResourceImporterOggVorbis, ResourceImporterScene, ResourceImporterShaderFile,
ResourceImporterTexture, ResourceImporterTextureAtlas, ResourceImporterWAV

Base class for resource importers.

## Description

This is the base class for Godot's resource importers. To implement your own
resource importers using editor plugins, see EditorImportPlugin.

## Tutorials

  * Import plugins

## Enumerations

enum ImportOrder:

ImportOrder IMPORT_ORDER_DEFAULT = `0`

The default import order.

ImportOrder IMPORT_ORDER_SCENE = `100`

The import order for scenes, which ensures scenes are imported after all other
core resources such as textures. Custom importers should generally have an
import order lower than `100` to avoid issues when importing scenes that rely
on custom resources.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

