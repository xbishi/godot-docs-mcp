# Popup

Inherits: Window < Viewport < Node < Object

Inherited By: PopupMenu, PopupPanel

Base class for contextual windows and panels with fixed position.

## Description

Popup is a base class for contextual windows and panels with fixed position.
It's a modal by default (see Window.popup_window) and provides methods for
implementing custom popup behavior.

## Properties

bool | borderless | `true` (overrides Window)  
---|---|---  
bool | popup_window | `true` (overrides Window)  
bool | transient | `true` (overrides Window)  
bool | unresizable | `true` (overrides Window)  
bool | visible | `false` (overrides Window)  
bool | wrap_controls | `true` (overrides Window)  
  
## Signals

popup_hide()

Emitted when the popup is hidden.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

