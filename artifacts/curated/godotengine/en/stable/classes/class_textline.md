# TextLine

Inherits: RefCounted < Object

Holds a line of text.

## Description

Abstraction over TextServer for handling a single line of text.

## Properties

HorizontalAlignment | alignment | `0`  
---|---|---  
Direction | direction | `0`  
String | ellipsis_char | `""`  
BitField[JustificationFlag] | flags | `3`  
Orientation | orientation | `0`  
bool | preserve_control | `false`  
bool | preserve_invalid | `true`  
OverrunBehavior | text_overrun_behavior | `3`  
float | width | `-1.0`  
  
## Methods

bool | add_object(key: Variant, size: Vector2, inline_align: InlineAlignment = 5, length: int = 1, baseline: float = 0.0)  
---|---  
bool | add_string(text: String, font: Font, font_size: int, language: String = "", meta: Variant = null)  
void | clear()  
void | draw(canvas: RID, pos: Vector2, color: Color = Color(1, 1, 1, 1)) const  
void | draw_outline(canvas: RID, pos: Vector2, outline_size: int = 1, color: Color = Color(1, 1, 1, 1)) const  
float | get_line_ascent() const  
float | get_line_descent() const  
float | get_line_underline_position() const  
float | get_line_underline_thickness() const  
float | get_line_width() const  
Rect2 | get_object_rect(key: Variant) const  
Array | get_objects() const  
RID | get_rid() const  
Vector2 | get_size() const  
int | hit_test(coords: float) const  
bool | resize_object(key: Variant, size: Vector2, inline_align: InlineAlignment = 5, baseline: float = 0.0)  
void | set_bidi_override(override: Array)  
void | tab_align(tab_stops: PackedFloat32Array)  
  
## Property Descriptions

HorizontalAlignment alignment = `0`

  * void set_horizontal_alignment(value: HorizontalAlignment)

  * HorizontalAlignment get_horizontal_alignment()

Sets text alignment within the line as if the line was horizontal.

Direction direction = `0`

  * void set_direction(value: Direction)

  * Direction get_direction()

Text writing direction.

String ellipsis_char = `""`

  * void set_ellipsis_char(value: String)

  * String get_ellipsis_char()

Ellipsis character used for text clipping.

BitField[JustificationFlag] flags = `3`

  * void set_flags(value: BitField[JustificationFlag])

  * BitField[JustificationFlag] get_flags()

Line alignment rules. For more info see TextServer.

Orientation orientation = `0`

  * void set_orientation(value: Orientation)

  * Orientation get_orientation()

Text orientation.

bool preserve_control = `false`

  * void set_preserve_control(value: bool)

  * bool get_preserve_control()

If set to `true` text will display control characters.

bool preserve_invalid = `true`

  * void set_preserve_invalid(value: bool)

  * bool get_preserve_invalid()

If set to `true` text will display invalid characters.

OverrunBehavior text_overrun_behavior = `3`

  * void set_text_overrun_behavior(value: OverrunBehavior)

  * OverrunBehavior get_text_overrun_behavior()

Sets the clipping behavior when the text exceeds the text line's set width.
See OverrunBehavior for a description of all modes.

float width = `-1.0`

  * void set_width(value: float)

  * float get_width()

Text line width.

## Method Descriptions

bool add_object(key: Variant, size: Vector2, inline_align: InlineAlignment =
5, length: int = 1, baseline: float = 0.0)

Adds inline object to the text buffer, `key` must be unique. In the text,
object is represented as `length` object replacement characters.

bool add_string(text: String, font: Font, font_size: int, language: String =
"", meta: Variant = null)

Adds text span and font to draw it.

void clear()

Clears text line (removes text and inline objects).

void draw(canvas: RID, pos: Vector2, color: Color = Color(1, 1, 1, 1)) const

Draw text into a canvas item at a given position, with `color`. `pos`
specifies the top left corner of the bounding box.

void draw_outline(canvas: RID, pos: Vector2, outline_size: int = 1, color:
Color = Color(1, 1, 1, 1)) const

Draw text into a canvas item at a given position, with `color`. `pos`
specifies the top left corner of the bounding box.

float get_line_ascent() const

Returns the text ascent (number of pixels above the baseline for horizontal
layout or to the left of baseline for vertical).

float get_line_descent() const

Returns the text descent (number of pixels below the baseline for horizontal
layout or to the right of baseline for vertical).

float get_line_underline_position() const

Returns pixel offset of the underline below the baseline.

float get_line_underline_thickness() const

Returns thickness of the underline.

float get_line_width() const

Returns width (for horizontal layout) or height (for vertical) of the text.

Rect2 get_object_rect(key: Variant) const

Returns bounding rectangle of the inline object.

Array get_objects() const

Returns array of inline objects.

RID get_rid() const

Returns TextServer buffer RID.

Vector2 get_size() const

Returns size of the bounding box of the text.

int hit_test(coords: float) const

Returns caret character offset at the specified pixel offset at the baseline.
This function always returns a valid position.

bool resize_object(key: Variant, size: Vector2, inline_align: InlineAlignment
= 5, baseline: float = 0.0)

Sets new size and alignment of embedded object.

void set_bidi_override(override: Array)

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm
will be used on each range separately.

void tab_align(tab_stops: PackedFloat32Array)

Aligns text to the given tab-stops.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[BitField]: This value is an integer composed as a bitmask of the following flags.
  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

