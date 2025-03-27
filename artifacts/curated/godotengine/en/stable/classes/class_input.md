# Input

Inherits: Object

A singleton for handling inputs.

## Description

The Input singleton handles key presses, mouse buttons and movement, gamepads,
and input actions. Actions and their events can be set in the Input Map tab in
Project > Project Settings, or with the InputMap class.

Note: Input's methods reflect the global input state and are not affected by
Control.accept_event() or Viewport.set_input_as_handled(), as those methods
only deal with the way input is propagated in the SceneTree.

## Tutorials

  * Inputs documentation index

  * 2D Dodge The Creeps Demo

  * 3D Voxel Demo

## Properties

bool | emulate_mouse_from_touch  
---|---  
bool | emulate_touch_from_mouse  
MouseMode | mouse_mode  
bool | use_accumulated_input  
  
## Methods

void | action_press(action: StringName, strength: float = 1.0)  
---|---  
void | action_release(action: StringName)  
void | add_joy_mapping(mapping: String, update_existing: bool = false)  
void | flush_buffered_events()  
Vector3 | get_accelerometer() const  
float | get_action_raw_strength(action: StringName, exact_match: bool = false) const  
float | get_action_strength(action: StringName, exact_match: bool = false) const  
float | get_axis(negative_action: StringName, positive_action: StringName) const  
Array[int] | get_connected_joypads()  
CursorShape | get_current_cursor_shape() const  
Vector3 | get_gravity() const  
Vector3 | get_gyroscope() const  
float | get_joy_axis(device: int, axis: JoyAxis) const  
String | get_joy_guid(device: int) const  
Dictionary | get_joy_info(device: int) const  
String | get_joy_name(device: int)  
float | get_joy_vibration_duration(device: int)  
Vector2 | get_joy_vibration_strength(device: int)  
Vector2 | get_last_mouse_screen_velocity()  
Vector2 | get_last_mouse_velocity()  
Vector3 | get_magnetometer() const  
BitField[MouseButtonMask] | get_mouse_button_mask() const  
Vector2 | get_vector(negative_x: StringName, positive_x: StringName, negative_y: StringName, positive_y: StringName, deadzone: float = -1.0) const  
bool | is_action_just_pressed(action: StringName, exact_match: bool = false) const  
bool | is_action_just_released(action: StringName, exact_match: bool = false) const  
bool | is_action_pressed(action: StringName, exact_match: bool = false) const  
bool | is_anything_pressed() const  
bool | is_joy_button_pressed(device: int, button: JoyButton) const  
bool | is_joy_known(device: int)  
bool | is_key_label_pressed(keycode: Key) const  
bool | is_key_pressed(keycode: Key) const  
bool | is_mouse_button_pressed(button: MouseButton) const  
bool | is_physical_key_pressed(keycode: Key) const  
void | parse_input_event(event: InputEvent)  
void | remove_joy_mapping(guid: String)  
void | set_accelerometer(value: Vector3)  
void | set_custom_mouse_cursor(image: Resource, shape: CursorShape = 0, hotspot: Vector2 = Vector2(0, 0))  
void | set_default_cursor_shape(shape: CursorShape = 0)  
void | set_gravity(value: Vector3)  
void | set_gyroscope(value: Vector3)  
void | set_magnetometer(value: Vector3)  
bool | should_ignore_device(vendor_id: int, product_id: int) const  
void | start_joy_vibration(device: int, weak_magnitude: float, strong_magnitude: float, duration: float = 0)  
void | stop_joy_vibration(device: int)  
void | vibrate_handheld(duration_ms: int = 500, amplitude: float = -1.0)  
void | warp_mouse(position: Vector2)  
  
## Signals

joy_connection_changed(device: int, connected: bool)

Emitted when a joypad device has been connected or disconnected.

## Enumerations

enum MouseMode:

MouseMode MOUSE_MODE_VISIBLE = `0`

Makes the mouse cursor visible if it is hidden.

MouseMode MOUSE_MODE_HIDDEN = `1`

Makes the mouse cursor hidden if it is visible.

MouseMode MOUSE_MODE_CAPTURED = `2`

Captures the mouse. The mouse will be hidden and its position locked at the
center of the window manager's window.

Note: If you want to process the mouse's movement in this mode, you need to
use InputEventMouseMotion.relative.

MouseMode MOUSE_MODE_CONFINED = `3`

Confines the mouse cursor to the game window, and make it visible.

MouseMode MOUSE_MODE_CONFINED_HIDDEN = `4`

Confines the mouse cursor to the game window, and make it hidden.

MouseMode MOUSE_MODE_MAX = `5`

Max value of the MouseMode.

enum CursorShape:

CursorShape CURSOR_ARROW = `0`

Arrow cursor. Standard, default pointing cursor.

CursorShape CURSOR_IBEAM = `1`

I-beam cursor. Usually used to show where the text cursor will appear when the
mouse is clicked.

CursorShape CURSOR_POINTING_HAND = `2`

Pointing hand cursor. Usually used to indicate the pointer is over a link or
other interactable item.

CursorShape CURSOR_CROSS = `3`

Cross cursor. Typically appears over regions in which a drawing operation can
be performed or for selections.

CursorShape CURSOR_WAIT = `4`

Wait cursor. Indicates that the application is busy performing an operation,
and that it cannot be used during the operation (e.g. something is blocking
its main thread).

CursorShape CURSOR_BUSY = `5`

Busy cursor. Indicates that the application is busy performing an operation,
and that it is still usable during the operation.

CursorShape CURSOR_DRAG = `6`

Drag cursor. Usually displayed when dragging something.

Note: Windows lacks a dragging cursor, so CURSOR_DRAG is the same as
CURSOR_MOVE for this platform.

CursorShape CURSOR_CAN_DROP = `7`

Can drop cursor. Usually displayed when dragging something to indicate that it
can be dropped at the current position.

CursorShape CURSOR_FORBIDDEN = `8`

Forbidden cursor. Indicates that the current action is forbidden (for example,
when dragging something) or that the control at a position is disabled.

CursorShape CURSOR_VSIZE = `9`

Vertical resize mouse cursor. A double-headed vertical arrow. It tells the
user they can resize the window or the panel vertically.

CursorShape CURSOR_HSIZE = `10`

Horizontal resize mouse cursor. A double-headed horizontal arrow. It tells the
user they can resize the window or the panel horizontally.

CursorShape CURSOR_BDIAGSIZE = `11`

Window resize mouse cursor. The cursor is a double-headed arrow that goes from
the bottom left to the top right. It tells the user they can resize the window
or the panel both horizontally and vertically.

CursorShape CURSOR_FDIAGSIZE = `12`

Window resize mouse cursor. The cursor is a double-headed arrow that goes from
the top left to the bottom right, the opposite of CURSOR_BDIAGSIZE. It tells
the user they can resize the window or the panel both horizontally and
vertically.

CursorShape CURSOR_MOVE = `13`

Move cursor. Indicates that something can be moved.

CursorShape CURSOR_VSPLIT = `14`

Vertical split mouse cursor. On Windows, it's the same as CURSOR_VSIZE.

CursorShape CURSOR_HSPLIT = `15`

Horizontal split mouse cursor. On Windows, it's the same as CURSOR_HSIZE.

CursorShape CURSOR_HELP = `16`

Help cursor. Usually a question mark.

## Property Descriptions

bool emulate_mouse_from_touch

  * void set_emulate_mouse_from_touch(value: bool)

  * bool is_emulating_mouse_from_touch()

If `true`, sends mouse input events when tapping or swiping on the
touchscreen. See also
ProjectSettings.input_devices/pointing/emulate_mouse_from_touch.

bool emulate_touch_from_mouse

  * void set_emulate_touch_from_mouse(value: bool)

  * bool is_emulating_touch_from_mouse()

If `true`, sends touch input events when clicking or dragging the mouse. See
also ProjectSettings.input_devices/pointing/emulate_touch_from_mouse.

MouseMode mouse_mode

  * void set_mouse_mode(value: MouseMode)

  * MouseMode get_mouse_mode()

Controls the mouse mode. See MouseMode for more information.

bool use_accumulated_input

  * void set_use_accumulated_input(value: bool)

  * bool is_using_accumulated_input()

If `true`, similar input events sent by the operating system are accumulated.
When input accumulation is enabled, all input events generated during a frame
will be merged and emitted when the frame is done rendering. Therefore, this
limits the number of input method calls per second to the rendering FPS.

Input accumulation can be disabled to get slightly more precise/reactive input
at the cost of increased CPU usage. In applications where drawing freehand
lines is required, input accumulation should generally be disabled while the
user is drawing the line to get results that closely follow the actual input.

Note: Input accumulation is enabled by default.

## Method Descriptions

void action_press(action: StringName, strength: float = 1.0)

This will simulate pressing the specified action.

The strength can be used for non-boolean actions, it's ranged between 0 and 1
representing the intensity of the given action.

Note: This method will not cause any Node._input() calls. It is intended to be
used with is_action_pressed() and is_action_just_pressed(). If you want to
simulate `_input`, use parse_input_event() instead.

void action_release(action: StringName)

If the specified action is already pressed, this will release it.

void add_joy_mapping(mapping: String, update_existing: bool = false)

Adds a new mapping entry (in SDL2 format) to the mapping database. Optionally
update already connected devices.

void flush_buffered_events()

Sends all input events which are in the current buffer to the game loop. These
events may have been buffered as a result of accumulated input
(use_accumulated_input) or agile input flushing
(ProjectSettings.input_devices/buffering/agile_event_flushing).

The engine will already do this itself at key execution points (at least once
per frame). However, this can be useful in advanced cases where you want
precise control over the timing of event handling.

Vector3 get_accelerometer() const

Returns the acceleration in m/s of the device's accelerometer sensor, if the
device has one. Otherwise, the method returns Vector3.ZERO.

Note this method returns an empty Vector3 when running from the editor even
when your device has an accelerometer. You must export your project to a
supported device to read values from the accelerometer.

Note: This method only works on Android and iOS. On other platforms, it always
returns Vector3.ZERO.

Note: For Android, ProjectSettings.input_devices/sensors/enable_accelerometer
must be enabled.

float get_action_raw_strength(action: StringName, exact_match: bool = false)
const

Returns a value between 0 and 1 representing the raw intensity of the given
action, ignoring the action's deadzone. In most cases, you should use
get_action_strength() instead.

If `exact_match` is `false`, it ignores additional input modifiers for
InputEventKey and InputEventMouseButton events, and the direction for
InputEventJoypadMotion events.

float get_action_strength(action: StringName, exact_match: bool = false) const

Returns a value between 0 and 1 representing the intensity of the given
action. In a joypad, for example, the further away the axis (analog sticks or
L2, R2 triggers) is from the dead zone, the closer the value will be to 1. If
the action is mapped to a control that has no axis such as the keyboard, the
value returned will be 0 or 1.

If `exact_match` is `false`, it ignores additional input modifiers for
InputEventKey and InputEventMouseButton events, and the direction for
InputEventJoypadMotion events.

float get_axis(negative_action: StringName, positive_action: StringName) const

Get axis input by specifying two actions, one negative and one positive.

This is a shorthand for writing `Input.get_action_strength("positive_action")
- Input.get_action_strength("negative_action")`.

Array[int] get_connected_joypads()

Returns an Array containing the device IDs of all currently connected joypads.

CursorShape get_current_cursor_shape() const

Returns the currently assigned cursor shape (see CursorShape).

Vector3 get_gravity() const

Returns the gravity in m/s of the device's accelerometer sensor, if the device
has one. Otherwise, the method returns Vector3.ZERO.

Note: This method only works on Android and iOS. On other platforms, it always
returns Vector3.ZERO.

Note: For Android, ProjectSettings.input_devices/sensors/enable_gravity must
be enabled.

Vector3 get_gyroscope() const

Returns the rotation rate in rad/s around a device's X, Y, and Z axes of the
gyroscope sensor, if the device has one. Otherwise, the method returns
Vector3.ZERO.

Note: This method only works on Android and iOS. On other platforms, it always
returns Vector3.ZERO.

Note: For Android, ProjectSettings.input_devices/sensors/enable_gyroscope must
be enabled.

float get_joy_axis(device: int, axis: JoyAxis) const

Returns the current value of the joypad axis at given index (see JoyAxis).

String get_joy_guid(device: int) const

Returns an SDL2-compatible device GUID on platforms that use gamepad
remapping, e.g. `030000004c050000c405000000010000`. Returns an empty string if
it cannot be found. Godot uses the SDL2 game controller database to determine
gamepad names and mappings based on this GUID.

On Windows, all XInput joypad GUIDs will be overridden by Godot to
`__XINPUT_DEVICE__`, because their mappings are the same.

Dictionary get_joy_info(device: int) const

Returns a dictionary with extra platform-specific information about the
device, e.g. the raw gamepad name from the OS or the Steam Input index.

On Windows, the dictionary contains the following fields:

`xinput_index`: The index of the controller in the XInput system. Undefined
for DirectInput devices.

`vendor_id`: The USB vendor ID of the device.

`product_id`: The USB product ID of the device.

On Linux:

`raw_name`: The name of the controller as it came from the OS, before getting
renamed by the godot controller database.

`vendor_id`: The USB vendor ID of the device.

`product_id`: The USB product ID of the device.

`steam_input_index`: The Steam Input gamepad index, if the device is not a
Steam Input device this key won't be present.

Note: The returned dictionary is always empty on Web, iOS, Android, and macOS.

String get_joy_name(device: int)

Returns the name of the joypad at the specified device index, e.g. `PS4
Controller`. Godot uses the SDL2 game controller database to determine gamepad
names.

float get_joy_vibration_duration(device: int)

Returns the duration of the current vibration effect in seconds.

Vector2 get_joy_vibration_strength(device: int)

Returns the strength of the joypad vibration: x is the strength of the weak
motor, and y is the strength of the strong motor.

Vector2 get_last_mouse_screen_velocity()

Returns the last mouse velocity in screen coordinates. To provide a precise
and jitter-free velocity, mouse velocity is only calculated every 0.1s.
Therefore, mouse velocity will lag mouse movements.

Vector2 get_last_mouse_velocity()

Returns the last mouse velocity. To provide a precise and jitter-free
velocity, mouse velocity is only calculated every 0.1s. Therefore, mouse
velocity will lag mouse movements.

Vector3 get_magnetometer() const

Returns the magnetic field strength in micro-Tesla for all axes of the
device's magnetometer sensor, if the device has one. Otherwise, the method
returns Vector3.ZERO.

Note: This method only works on Android and iOS. On other platforms, it always
returns Vector3.ZERO.

Note: For Android, ProjectSettings.input_devices/sensors/enable_magnetometer
must be enabled.

BitField[MouseButtonMask] get_mouse_button_mask() const

Returns mouse buttons as a bitmask. If multiple mouse buttons are pressed at
the same time, the bits are added together. Equivalent to
DisplayServer.mouse_get_button_state().

Vector2 get_vector(negative_x: StringName, positive_x: StringName, negative_y:
StringName, positive_y: StringName, deadzone: float = -1.0) const

Gets an input vector by specifying four actions for the positive and negative
X and Y axes.

This method is useful when getting vector input, such as from a joystick,
directional pad, arrows, or WASD. The vector has its length limited to 1 and
has a circular deadzone, which is useful for using vector input as movement.

By default, the deadzone is automatically calculated from the average of the
action deadzones. However, you can override the deadzone to be whatever you
want (on the range of 0 to 1).

bool is_action_just_pressed(action: StringName, exact_match: bool = false)
const

Returns `true` when the user has started pressing the action event in the
current frame or physics tick. It will only return `true` on the frame or tick
that the user pressed down the button.

This is useful for code that needs to run only once when an action is pressed,
instead of every frame while it's pressed.

If `exact_match` is `false`, it ignores additional input modifiers for
InputEventKey and InputEventMouseButton events, and the direction for
InputEventJoypadMotion events.

Note: Returning `true` does not imply that the action is still pressed. An
action can be pressed and released again rapidly, and `true` will still be
returned so as not to miss input.

Note: Due to keyboard ghosting, is_action_just_pressed() may return `false`
even if one of the action's keys is pressed. See Input examples in the
documentation for more information.

Note: During input handling (e.g. Node._input()), use
InputEvent.is_action_pressed() instead to query the action state of the
current event.

bool is_action_just_released(action: StringName, exact_match: bool = false)
const

Returns `true` when the user stops pressing the action event in the current
frame or physics tick. It will only return `true` on the frame or tick that
the user releases the button.

Note: Returning `true` does not imply that the action is still not pressed. An
action can be released and pressed again rapidly, and `true` will still be
returned so as not to miss input.

If `exact_match` is `false`, it ignores additional input modifiers for
InputEventKey and InputEventMouseButton events, and the direction for
InputEventJoypadMotion events.

Note: During input handling (e.g. Node._input()), use
InputEvent.is_action_released() instead to query the action state of the
current event.

bool is_action_pressed(action: StringName, exact_match: bool = false) const

Returns `true` if you are pressing the action event.

If `exact_match` is `false`, it ignores additional input modifiers for
InputEventKey and InputEventMouseButton events, and the direction for
InputEventJoypadMotion events.

Note: Due to keyboard ghosting, is_action_pressed() may return `false` even if
one of the action's keys is pressed. See Input examples in the documentation
for more information.

bool is_anything_pressed() const

Returns `true` if any action, key, joypad button, or mouse button is being
pressed. This will also return `true` if any action is simulated via code by
calling action_press().

bool is_joy_button_pressed(device: int, button: JoyButton) const

Returns `true` if you are pressing the joypad button (see JoyButton).

bool is_joy_known(device: int)

Returns `true` if the system knows the specified device. This means that it
sets all button and axis indices. Unknown joypads are not expected to match
these constants, but you can still retrieve events from them.

bool is_key_label_pressed(keycode: Key) const

Returns `true` if you are pressing the key with the `keycode` printed on it.
You can pass a Key constant or any Unicode character code.

bool is_key_pressed(keycode: Key) const

Returns `true` if you are pressing the Latin key in the current keyboard
layout. You can pass a Key constant.

is_key_pressed() is only recommended over is_physical_key_pressed() in non-
game applications. This ensures that shortcut keys behave as expected
depending on the user's keyboard layout, as keyboard shortcuts are generally
dependent on the keyboard layout in non-game applications. If in doubt, use
is_physical_key_pressed().

Note: Due to keyboard ghosting, is_key_pressed() may return `false` even if
one of the action's keys is pressed. See Input examples in the documentation
for more information.

bool is_mouse_button_pressed(button: MouseButton) const

Returns `true` if you are pressing the mouse button specified with
MouseButton.

bool is_physical_key_pressed(keycode: Key) const

Returns `true` if you are pressing the key in the physical location on the
101/102-key US QWERTY keyboard. You can pass a Key constant.

is_physical_key_pressed() is recommended over is_key_pressed() for in-game
actions, as it will make `W`/`A`/`S`/`D` layouts work regardless of the user's
keyboard layout. is_physical_key_pressed() will also ensure that the top row
number keys work on any keyboard layout. If in doubt, use
is_physical_key_pressed().

Note: Due to keyboard ghosting, is_physical_key_pressed() may return `false`
even if one of the action's keys is pressed. See Input examples in the
documentation for more information.

void parse_input_event(event: InputEvent)

Feeds an InputEvent to the game. Can be used to artificially trigger input
events from code. Also generates Node._input() calls.

GDScriptC#

    
    
    var cancel_event = InputEventAction.new()
    cancel_event.action = "ui_cancel"
    cancel_event.pressed = true
    Input.parse_input_event(cancel_event)
    
    
    
    var cancelEvent = new InputEventAction();
    cancelEvent.Action = "ui_cancel";
    cancelEvent.Pressed = true;
    Input.ParseInputEvent(cancelEvent);
    

Note: Calling this function has no influence on the operating system. So for
example sending an InputEventMouseMotion will not move the OS mouse cursor to
the specified position (use warp_mouse() instead) and sending ``Alt/Cmd` +
`Tab`` as InputEventKey won't toggle between active windows.

void remove_joy_mapping(guid: String)

Removes all mappings from the internal database that match the given GUID. All
currently connected joypads that use this GUID will become unmapped.

On Android, Godot will map to an internal fallback mapping.

void set_accelerometer(value: Vector3)

Sets the acceleration value of the accelerometer sensor. Can be used for
debugging on devices without a hardware sensor, for example in an editor on a
PC.

Note: This value can be immediately overwritten by the hardware sensor value
on Android and iOS.

void set_custom_mouse_cursor(image: Resource, shape: CursorShape = 0, hotspot:
Vector2 = Vector2(0, 0))

Sets a custom mouse cursor image, which is only visible inside the game
window. The hotspot can also be specified. Passing `null` to the image
parameter resets to the system cursor. See CursorShape for the list of shapes.

`image` can be either Texture2D or Image and its size must be lower than or
equal to 256256. To avoid rendering issues, sizes lower than or equal to
128128 are recommended.

`hotspot` must be within `image`'s size.

Note: AnimatedTextures aren't supported as custom mouse cursors. If using an
AnimatedTexture, only the first frame will be displayed.

Note: The Lossless, Lossy or Uncompressed compression modes are recommended.
The Video RAM compression mode can be used, but it will be decompressed on the
CPU, which means loading times are slowed down and no memory is saved compared
to lossless modes.

Note: On the web platform, the maximum allowed cursor image size is 128128.
Cursor images larger than 3232 will also only be displayed if the mouse cursor
image is entirely located within the page for security reasons.

void set_default_cursor_shape(shape: CursorShape = 0)

Sets the default cursor shape to be used in the viewport instead of
CURSOR_ARROW.

Note: If you want to change the default cursor shape for Control's nodes, use
Control.mouse_default_cursor_shape instead.

Note: This method generates an InputEventMouseMotion to update cursor
immediately.

void set_gravity(value: Vector3)

Sets the gravity value of the accelerometer sensor. Can be used for debugging
on devices without a hardware sensor, for example in an editor on a PC.

Note: This value can be immediately overwritten by the hardware sensor value
on Android and iOS.

void set_gyroscope(value: Vector3)

Sets the value of the rotation rate of the gyroscope sensor. Can be used for
debugging on devices without a hardware sensor, for example in an editor on a
PC.

Note: This value can be immediately overwritten by the hardware sensor value
on Android and iOS.

void set_magnetometer(value: Vector3)

Sets the value of the magnetic field of the magnetometer sensor. Can be used
for debugging on devices without a hardware sensor, for example in an editor
on a PC.

Note: This value can be immediately overwritten by the hardware sensor value
on Android and iOS.

bool should_ignore_device(vendor_id: int, product_id: int) const

Queries whether an input device should be ignored or not. Devices can be
ignored by setting the environment variable
`SDL_GAMECONTROLLER_IGNORE_DEVICES`. Read the SDL documentation for more
information.

Note: Some 3rd party tools can contribute to the list of ignored devices. For
example, SteamInput creates virtual devices from physical devices for
remapping purposes. To avoid handling the same input device twice, the
original device is added to the ignore list.

void start_joy_vibration(device: int, weak_magnitude: float, strong_magnitude:
float, duration: float = 0)

Starts to vibrate the joypad. Joypads usually come with two rumble motors, a
strong and a weak one. `weak_magnitude` is the strength of the weak motor
(between 0 and 1) and `strong_magnitude` is the strength of the strong motor
(between 0 and 1). `duration` is the duration of the effect in seconds (a
duration of 0 will try to play the vibration indefinitely). The vibration can
be stopped early by calling stop_joy_vibration().

Note: Not every hardware is compatible with long effect durations; it is
recommended to restart an effect if it has to be played for more than a few
seconds.

Note: For macOS, vibration is only supported in macOS 11 and later.

void stop_joy_vibration(device: int)

Stops the vibration of the joypad started with start_joy_vibration().

void vibrate_handheld(duration_ms: int = 500, amplitude: float = -1.0)

Vibrate the handheld device for the specified duration in milliseconds.

`amplitude` is the strength of the vibration, as a value between `0.0` and
`1.0`. If set to `-1.0`, the default vibration strength of the device is used.

Note: This method is implemented on Android, iOS, and Web. It has no effect on
other platforms.

Note: For Android, vibrate_handheld() requires enabling the `VIBRATE`
permission in the export preset. Otherwise, vibrate_handheld() will have no
effect.

Note: For iOS, specifying the duration is only supported in iOS 13 and later.

Note: For Web, the amplitude cannot be changed.

Note: Some web browsers such as Safari and Firefox for Android do not support
vibrate_handheld().

void warp_mouse(position: Vector2)

Sets the mouse position to the specified vector, provided in pixels and
relative to an origin at the upper left corner of the currently focused Window
Manager game window.

Mouse position is clipped to the limits of the screen resolution, or to the
limits of the game window if MouseMode is set to MOUSE_MODE_CONFINED or
MOUSE_MODE_CONFINED_HIDDEN.

Note: warp_mouse() is only supported on Windows, macOS and Linux. It has no
effect on Android, iOS and Web.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[BitField]: This value is an integer composed as a bitmask of the following flags.

