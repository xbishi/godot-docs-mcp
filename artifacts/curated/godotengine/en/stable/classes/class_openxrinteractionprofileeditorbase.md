# OpenXRInteractionProfileEditorBase

Inherits: HBoxContainer < BoxContainer < Container < Control < CanvasItem <
Node < Object

Inherited By: OpenXRInteractionProfileEditor

Base class for editing interaction profiles.

## Description

This is a base class for interaction profile editors used by the OpenXR action
map editor. It can be used to create bespoke editors for specific interaction
profiles.

## Properties

BitField[SizeFlags] | size_flags_horizontal | `3` (overrides Control)  
---|---|---  
BitField[SizeFlags] | size_flags_vertical | `3` (overrides Control)  
  
## Methods

void | setup(action_map: OpenXRActionMap, interaction_profile: OpenXRInteractionProfile)  
---|---  
  
## Method Descriptions

void setup(action_map: OpenXRActionMap, interaction_profile:
OpenXRInteractionProfile)

Setup this editor for the provided `action_map` and `interaction_profile`.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[BitField]: This value is an integer composed as a bitmask of the following flags.
  *[void]: No return value.

