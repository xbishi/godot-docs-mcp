# OpenXRExtensionWrapperExtension

Inherits: Object

Allows clients to implement OpenXR extensions with GDExtension.

## Description

OpenXRExtensionWrapperExtension allows clients to implement OpenXR extensions
with GDExtension. The extension should be registered with
register_extension_wrapper().

## Methods

int | _get_composition_layer(index: int) virtual  
---|---  
int | _get_composition_layer_count() virtual  
int | _get_composition_layer_order(index: int) virtual  
Dictionary | _get_requested_extensions() virtual  
PackedStringArray | _get_suggested_tracker_names() virtual  
Array[Dictionary] | _get_viewport_composition_layer_extension_properties() virtual  
Dictionary | _get_viewport_composition_layer_extension_property_defaults() virtual  
void | _on_before_instance_created() virtual  
bool | _on_event_polled(event: `const void*`) virtual  
void | _on_instance_created(instance: int) virtual  
void | _on_instance_destroyed() virtual  
void | _on_main_swapchains_created() virtual  
void | _on_post_draw_viewport(viewport: RID) virtual  
void | _on_pre_draw_viewport(viewport: RID) virtual  
void | _on_pre_render() virtual  
void | _on_process() virtual  
void | _on_register_metadata() virtual  
void | _on_session_created(session: int) virtual  
void | _on_session_destroyed() virtual  
void | _on_state_exiting() virtual  
void | _on_state_focused() virtual  
void | _on_state_idle() virtual  
void | _on_state_loss_pending() virtual  
void | _on_state_ready() virtual  
void | _on_state_stopping() virtual  
void | _on_state_synchronized() virtual  
void | _on_state_visible() virtual  
void | _on_viewport_composition_layer_destroyed(layer: `const void*`) virtual  
int | _set_android_surface_swapchain_create_info_and_get_next_pointer(property_values: Dictionary, next_pointer: `void*`) virtual  
int | _set_hand_joint_locations_and_get_next_pointer(hand_index: int, next_pointer: `void*`) virtual  
int | _set_instance_create_info_and_get_next_pointer(next_pointer: `void*`) virtual  
int | _set_projection_views_and_get_next_pointer(view_index: int, next_pointer: `void*`) virtual  
int | _set_session_create_and_get_next_pointer(next_pointer: `void*`) virtual  
int | _set_swapchain_create_info_and_get_next_pointer(next_pointer: `void*`) virtual  
int | _set_system_properties_and_get_next_pointer(next_pointer: `void*`) virtual  
int | _set_viewport_composition_layer_and_get_next_pointer(layer: `const void*`, property_values: Dictionary, next_pointer: `void*`) virtual  
OpenXRAPIExtension | get_openxr_api()  
void | register_extension_wrapper()  
  
## Method Descriptions

int _get_composition_layer(index: int) virtual

Returns a pointer to an `XrCompositionLayerBaseHeader` struct to provide the
given composition layer.

This will only be called if the extension previously registered itself with
OpenXRAPIExtension.register_composition_layer_provider().

int _get_composition_layer_count() virtual

Returns the number of composition layers this extension wrapper provides via
_get_composition_layer().

This will only be called if the extension previously registered itself with
OpenXRAPIExtension.register_composition_layer_provider().

int _get_composition_layer_order(index: int) virtual

Returns an integer that will be used to sort the given composition layer
provided via _get_composition_layer(). Lower numbers will move the layer to
the front of the list, and higher numbers to the end. The default projection
layer has an order of `0`, so layers provided by this method should probably
be above or below (but not exactly) `0`.

This will only be called if the extension previously registered itself with
OpenXRAPIExtension.register_composition_layer_provider().

Dictionary _get_requested_extensions() virtual

Returns a Dictionary of OpenXR extensions related to this extension. The
Dictionary should contain the name of the extension, mapped to a `bool *` cast
to an integer:

  * If the `bool *` is a `nullptr` this extension is mandatory.

  * If the `bool *` points to a boolean, the boolean will be updated to `true` if the extension is enabled.

PackedStringArray _get_suggested_tracker_names() virtual

Returns a PackedStringArray of positional tracker names that are used within
the extension wrapper.

Array[Dictionary] _get_viewport_composition_layer_extension_properties()
virtual

Gets an array of Dictionarys that represent properties, just like
Object._get_property_list(), that will be added to OpenXRCompositionLayer
nodes.

Dictionary _get_viewport_composition_layer_extension_property_defaults()
virtual

Gets a Dictionary containing the default values for the properties returned by
_get_viewport_composition_layer_extension_properties().

void _on_before_instance_created() virtual

Called before the OpenXR instance is created.

bool _on_event_polled(event: `const void*`) virtual

Called when there is an OpenXR event to process. When implementing, return
`true` if the event was handled, return `false` otherwise.

void _on_instance_created(instance: int) virtual

Called right after the OpenXR instance is created.

void _on_instance_destroyed() virtual

Called right before the OpenXR instance is destroyed.

void _on_main_swapchains_created() virtual

Called right after the main swapchains are (re)created.

void _on_post_draw_viewport(viewport: RID) virtual

Called right after the given viewport is rendered.

Note: The draw commands might only be queued at this point, not executed.

void _on_pre_draw_viewport(viewport: RID) virtual

Called right before the given viewport is rendered.

void _on_pre_render() virtual

Called right before the XR viewports begin their rendering step.

void _on_process() virtual

Called as part of the OpenXR process handling. This happens right before
general and physics processing steps of the main loop. During this step
controller data is queried and made available to game logic.

void _on_register_metadata() virtual

Allows extensions to register additional controller metadata. This function is
called even when the OpenXR API is not constructed as the metadata needs to be
available to the editor.

Extensions should also provide metadata regardless of whether they are
supported on the host system. The controller data is used to setup action maps
for users who may have access to the relevant hardware.

void _on_session_created(session: int) virtual

Called right after the OpenXR session is created.

void _on_session_destroyed() virtual

Called right before the OpenXR session is destroyed.

void _on_state_exiting() virtual

Called when the OpenXR session state is changed to exiting.

void _on_state_focused() virtual

Called when the OpenXR session state is changed to focused. This state is the
active state when the game runs.

void _on_state_idle() virtual

Called when the OpenXR session state is changed to idle.

void _on_state_loss_pending() virtual

Called when the OpenXR session state is changed to loss pending.

void _on_state_ready() virtual

Called when the OpenXR session state is changed to ready. This means OpenXR is
ready to set up the session.

void _on_state_stopping() virtual

Called when the OpenXR session state is changed to stopping.

void _on_state_synchronized() virtual

Called when the OpenXR session state is changed to synchronized. OpenXR also
returns to this state when the application loses focus.

void _on_state_visible() virtual

Called when the OpenXR session state is changed to visible. This means OpenXR
is now ready to receive frames.

void _on_viewport_composition_layer_destroyed(layer: `const void*`) virtual

Called when a composition layer created via OpenXRCompositionLayer is
destroyed.

`layer` is a pointer to an `XrCompositionLayerBaseHeader` struct.

int
_set_android_surface_swapchain_create_info_and_get_next_pointer(property_values:
Dictionary, next_pointer: `void*`) virtual

Adds additional data structures to Android surface swapchains created by
OpenXRCompositionLayer.

`property_values` contains the values of the properties returned by
_get_viewport_composition_layer_extension_properties().

int _set_hand_joint_locations_and_get_next_pointer(hand_index: int,
next_pointer: `void*`) virtual

Adds additional data structures when each hand tracker is created.

int _set_instance_create_info_and_get_next_pointer(next_pointer: `void*`)
virtual

Adds additional data structures when the OpenXR instance is created.

int _set_projection_views_and_get_next_pointer(view_index: int, next_pointer:
`void*`) virtual

Adds additional data structures to the projection view of the given
`view_index`.

int _set_session_create_and_get_next_pointer(next_pointer: `void*`) virtual

Adds additional data structures when the OpenXR session is created.

int _set_swapchain_create_info_and_get_next_pointer(next_pointer: `void*`)
virtual

Adds additional data structures when creating OpenXR swapchains.

int _set_system_properties_and_get_next_pointer(next_pointer: `void*`) virtual

Adds additional data structures when querying OpenXR system abilities.

int _set_viewport_composition_layer_and_get_next_pointer(layer: `const void*`,
property_values: Dictionary, next_pointer: `void*`) virtual

Adds additional data structures to composition layers created by
OpenXRCompositionLayer.

`property_values` contains the values of the properties returned by
_get_viewport_composition_layer_extension_properties().

`layer` is a pointer to an `XrCompositionLayerBaseHeader` struct.

OpenXRAPIExtension get_openxr_api()

Returns the created OpenXRAPIExtension, which can be used to access the OpenXR
API.

void register_extension_wrapper()

Registers the extension. This should happen at core module initialization
level.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[void]: No return value.

