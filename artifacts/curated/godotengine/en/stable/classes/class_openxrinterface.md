# OpenXRInterface

Inherits: XRInterface < RefCounted < Object

Our OpenXR interface.

## Description

The OpenXR interface allows Godot to interact with OpenXR runtimes and make it
possible to create XR experiences and games.

Due to the needs of OpenXR this interface works slightly different than other
plugin based XR interfaces. It needs to be initialized when Godot starts. You
need to enable OpenXR, settings for this can be found in your games project
settings under the XR heading. You do need to mark a viewport for use with XR
in order for Godot to know which render result should be output to the
headset.

## Tutorials

  * Setting up XR

## Properties

float | display_refresh_rate | `0.0`  
---|---|---  
bool | foveation_dynamic | `false`  
int | foveation_level | `0`  
float | render_target_size_multiplier | `1.0`  
float | vrs_min_radius | `20.0`  
float | vrs_strength | `1.0`  
  
## Methods

Array | get_action_sets() const  
---|---  
Array | get_available_display_refresh_rates() const  
Vector3 | get_hand_joint_angular_velocity(hand: Hand, joint: HandJoints) const  
BitField[HandJointFlags] | get_hand_joint_flags(hand: Hand, joint: HandJoints) const  
Vector3 | get_hand_joint_linear_velocity(hand: Hand, joint: HandJoints) const  
Vector3 | get_hand_joint_position(hand: Hand, joint: HandJoints) const  
float | get_hand_joint_radius(hand: Hand, joint: HandJoints) const  
Quaternion | get_hand_joint_rotation(hand: Hand, joint: HandJoints) const  
HandTrackedSource | get_hand_tracking_source(hand: Hand) const  
HandMotionRange | get_motion_range(hand: Hand) const  
bool | is_action_set_active(name: String) const  
bool | is_eye_gaze_interaction_supported()  
bool | is_foveation_supported() const  
bool | is_hand_interaction_supported() const  
bool | is_hand_tracking_supported()  
void | set_action_set_active(name: String, active: bool)  
void | set_motion_range(hand: Hand, motion_range: HandMotionRange)  
  
## Signals

instance_exiting()

Informs our OpenXR instance is exiting.

pose_recentered()

Informs the user queued a recenter of the player position.

refresh_rate_changed(refresh_rate: float)

Informs the user the HMD refresh rate has changed.

Note: Only emitted if XR runtime supports the refresh rate extension.

session_begun()

Informs our OpenXR session has been started.

session_focussed()

Informs our OpenXR session now has focus.

session_loss_pending()

Informs our OpenXR session is in the process of being lost.

session_stopping()

Informs our OpenXR session is stopping.

session_visible()

Informs our OpenXR session is now visible (output is being sent to the HMD).

## Enumerations

enum Hand:

Hand HAND_LEFT = `0`

Left hand.

Hand HAND_RIGHT = `1`

Right hand.

Hand HAND_MAX = `2`

Maximum value for the hand enum.

enum HandMotionRange:

HandMotionRange HAND_MOTION_RANGE_UNOBSTRUCTED = `0`

Full hand range, if user closes their hands, we make a full fist.

HandMotionRange HAND_MOTION_RANGE_CONFORM_TO_CONTROLLER = `1`

Conform to controller, if user closes their hands, the tracked data conforms
to the shape of the controller.

HandMotionRange HAND_MOTION_RANGE_MAX = `2`

Maximum value for the motion range enum.

enum HandTrackedSource:

HandTrackedSource HAND_TRACKED_SOURCE_UNKNOWN = `0`

The source of hand tracking data is unknown (the extension is likely
unsupported).

HandTrackedSource HAND_TRACKED_SOURCE_UNOBSTRUCTED = `1`

The source of hand tracking is unobstructed, this means that an accurate
method of hand tracking is used, e.g. optical hand tracking, data gloves, etc.

HandTrackedSource HAND_TRACKED_SOURCE_CONTROLLER = `2`

The source of hand tracking is a controller, bone positions are inferred from
controller inputs.

HandTrackedSource HAND_TRACKED_SOURCE_MAX = `3`

Maximum value for the hand tracked source enum.

enum HandJoints:

HandJoints HAND_JOINT_PALM = `0`

Palm joint.

HandJoints HAND_JOINT_WRIST = `1`

Wrist joint.

HandJoints HAND_JOINT_THUMB_METACARPAL = `2`

Thumb metacarpal joint.

HandJoints HAND_JOINT_THUMB_PROXIMAL = `3`

Thumb proximal joint.

HandJoints HAND_JOINT_THUMB_DISTAL = `4`

Thumb distal joint.

HandJoints HAND_JOINT_THUMB_TIP = `5`

Thumb tip joint.

HandJoints HAND_JOINT_INDEX_METACARPAL = `6`

Index metacarpal joint.

HandJoints HAND_JOINT_INDEX_PROXIMAL = `7`

Index proximal joint.

HandJoints HAND_JOINT_INDEX_INTERMEDIATE = `8`

Index intermediate joint.

HandJoints HAND_JOINT_INDEX_DISTAL = `9`

Index distal joint.

HandJoints HAND_JOINT_INDEX_TIP = `10`

Index tip joint.

HandJoints HAND_JOINT_MIDDLE_METACARPAL = `11`

Middle metacarpal joint.

HandJoints HAND_JOINT_MIDDLE_PROXIMAL = `12`

Middle proximal joint.

HandJoints HAND_JOINT_MIDDLE_INTERMEDIATE = `13`

Middle intermediate joint.

HandJoints HAND_JOINT_MIDDLE_DISTAL = `14`

Middle distal joint.

HandJoints HAND_JOINT_MIDDLE_TIP = `15`

Middle tip joint.

HandJoints HAND_JOINT_RING_METACARPAL = `16`

Ring metacarpal joint.

HandJoints HAND_JOINT_RING_PROXIMAL = `17`

Ring proximal joint.

HandJoints HAND_JOINT_RING_INTERMEDIATE = `18`

Ring intermediate joint.

HandJoints HAND_JOINT_RING_DISTAL = `19`

Ring distal joint.

HandJoints HAND_JOINT_RING_TIP = `20`

Ring tip joint.

HandJoints HAND_JOINT_LITTLE_METACARPAL = `21`

Little metacarpal joint.

HandJoints HAND_JOINT_LITTLE_PROXIMAL = `22`

Little proximal joint.

HandJoints HAND_JOINT_LITTLE_INTERMEDIATE = `23`

Little intermediate joint.

HandJoints HAND_JOINT_LITTLE_DISTAL = `24`

Little distal joint.

HandJoints HAND_JOINT_LITTLE_TIP = `25`

Little tip joint.

HandJoints HAND_JOINT_MAX = `26`

Maximum value for the hand joint enum.

flags HandJointFlags:

HandJointFlags HAND_JOINT_NONE = `0`

No flags are set.

HandJointFlags HAND_JOINT_ORIENTATION_VALID = `1`

If set, the orientation data is valid, otherwise, the orientation data is
unreliable and should not be used.

HandJointFlags HAND_JOINT_ORIENTATION_TRACKED = `2`

If set, the orientation data comes from tracking data, otherwise, the
orientation data contains predicted data.

HandJointFlags HAND_JOINT_POSITION_VALID = `4`

If set, the positional data is valid, otherwise, the positional data is
unreliable and should not be used.

HandJointFlags HAND_JOINT_POSITION_TRACKED = `8`

If set, the positional data comes from tracking data, otherwise, the
positional data contains predicted data.

HandJointFlags HAND_JOINT_LINEAR_VELOCITY_VALID = `16`

If set, our linear velocity data is valid, otherwise, the linear velocity data
is unreliable and should not be used.

HandJointFlags HAND_JOINT_ANGULAR_VELOCITY_VALID = `32`

If set, our angular velocity data is valid, otherwise, the angular velocity
data is unreliable and should not be used.

## Property Descriptions

float display_refresh_rate = `0.0`

  * void set_display_refresh_rate(value: float)

  * float get_display_refresh_rate()

The display refresh rate for the current HMD. Only functional if this feature
is supported by the OpenXR runtime and after the interface has been
initialized.

bool foveation_dynamic = `false`

  * void set_foveation_dynamic(value: bool)

  * bool get_foveation_dynamic()

Enable dynamic foveation adjustment, the interface must be initialized before
this is accessible. If enabled foveation will automatically adjusted between
low and foveation_level.

Note: Only works on compatibility renderer.

int foveation_level = `0`

  * void set_foveation_level(value: int)

  * int get_foveation_level()

Set foveation level from 0 (off) to 3 (high), the interface must be
initialized before this is accessible.

Note: Only works on compatibility renderer.

float render_target_size_multiplier = `1.0`

  * void set_render_target_size_multiplier(value: float)

  * float get_render_target_size_multiplier()

The render size multiplier for the current HMD. Must be set before the
interface has been initialized.

float vrs_min_radius = `20.0`

  * void set_vrs_min_radius(value: float)

  * float get_vrs_min_radius()

The minimum radius around the focal point where full quality is guaranteed if
VRS is used as a percentage of screen size.

Note: Mobile and Forward+ renderers only. Requires Viewport.vrs_mode to be set
to Viewport.VRS_XR.

float vrs_strength = `1.0`

  * void set_vrs_strength(value: float)

  * float get_vrs_strength()

The strength used to calculate the VRS density map. The greater this value,
the more noticeable VRS is. This improves performance at the cost of quality.

Note: Mobile and Forward+ renderers only. Requires Viewport.vrs_mode to be set
to Viewport.VRS_XR.

## Method Descriptions

Array get_action_sets() const

Returns a list of action sets registered with Godot (loaded from the action
map at runtime).

Array get_available_display_refresh_rates() const

Returns display refresh rates supported by the current HMD. Only returned if
this feature is supported by the OpenXR runtime and after the interface has
been initialized.

Vector3 get_hand_joint_angular_velocity(hand: Hand, joint: HandJoints) const

Deprecated: Use XRHandTracker.get_hand_joint_angular_velocity() obtained from
XRServer.get_tracker() instead.

If handtracking is enabled, returns the angular velocity of a joint (`joint`)
of a hand (`hand`) as provided by OpenXR. This is relative to XROrigin3D!

BitField[HandJointFlags] get_hand_joint_flags(hand: Hand, joint: HandJoints)
const

Deprecated: Use XRHandTracker.get_hand_joint_flags() obtained from
XRServer.get_tracker() instead.

If handtracking is enabled, returns flags that inform us of the validity of
the tracking data.

Vector3 get_hand_joint_linear_velocity(hand: Hand, joint: HandJoints) const

Deprecated: Use XRHandTracker.get_hand_joint_linear_velocity() obtained from
XRServer.get_tracker() instead.

If handtracking is enabled, returns the linear velocity of a joint (`joint`)
of a hand (`hand`) as provided by OpenXR. This is relative to XROrigin3D
without worldscale applied!

Vector3 get_hand_joint_position(hand: Hand, joint: HandJoints) const

Deprecated: Use XRHandTracker.get_hand_joint_transform() obtained from
XRServer.get_tracker() instead.

If handtracking is enabled, returns the position of a joint (`joint`) of a
hand (`hand`) as provided by OpenXR. This is relative to XROrigin3D without
worldscale applied!

float get_hand_joint_radius(hand: Hand, joint: HandJoints) const

Deprecated: Use XRHandTracker.get_hand_joint_radius() obtained from
XRServer.get_tracker() instead.

If handtracking is enabled, returns the radius of a joint (`joint`) of a hand
(`hand`) as provided by OpenXR. This is without worldscale applied!

Quaternion get_hand_joint_rotation(hand: Hand, joint: HandJoints) const

Deprecated: Use XRHandTracker.get_hand_joint_transform() obtained from
XRServer.get_tracker() instead.

If handtracking is enabled, returns the rotation of a joint (`joint`) of a
hand (`hand`) as provided by OpenXR.

HandTrackedSource get_hand_tracking_source(hand: Hand) const

Deprecated: Use XRHandTracker.hand_tracking_source obtained from
XRServer.get_tracker() instead.

If handtracking is enabled and hand tracking source is supported, gets the
source of the hand tracking data for `hand`.

HandMotionRange get_motion_range(hand: Hand) const

If handtracking is enabled and motion range is supported, gets the currently
configured motion range for `hand`.

bool is_action_set_active(name: String) const

Returns `true` if the given action set is active.

bool is_eye_gaze_interaction_supported()

Returns the capabilities of the eye gaze interaction extension.

Note: This only returns a valid value after OpenXR has been initialized.

bool is_foveation_supported() const

Returns `true` if OpenXR's foveation extension is supported, the interface
must be initialized before this returns a valid value.

Note: This feature is only available on the compatibility renderer and
currently only available on some stand alone headsets. For Vulkan set
Viewport.vrs_mode to `VRS_XR` on desktop.

bool is_hand_interaction_supported() const

Returns `true` if OpenXR's hand interaction profile is supported and enabled.

Note: This only returns a valid value after OpenXR has been initialized.

bool is_hand_tracking_supported()

Returns `true` if OpenXR's hand tracking is supported and enabled.

Note: This only returns a valid value after OpenXR has been initialized.

void set_action_set_active(name: String, active: bool)

Sets the given action set as active or inactive.

void set_motion_range(hand: Hand, motion_range: HandMotionRange)

If handtracking is enabled and motion range is supported, sets the currently
configured motion range for `hand` to `motion_range`.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[BitField]: This value is an integer composed as a bitmask of the following flags.
  *[void]: No return value.

