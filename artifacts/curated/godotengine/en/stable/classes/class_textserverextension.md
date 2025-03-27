# TextServerExtension

Inherits: TextServer < RefCounted < Object

Inherited By: TextServerAdvanced, TextServerDummy, TextServerFallback

Base class for custom TextServer implementations (plugins).

## Description

External TextServer implementations should inherit from this class.

## Methods

void | _cleanup() virtual  
---|---  
RID | _create_font() virtual  
RID | _create_font_linked_variation(font_rid: RID) virtual  
RID | _create_shaped_text(direction: Direction, orientation: Orientation) virtual  
void | _draw_hex_code_box(canvas: RID, size: int, pos: Vector2, index: int, color: Color) virtual const  
void | _font_clear_glyphs(font_rid: RID, size: Vector2i) virtual  
void | _font_clear_kerning_map(font_rid: RID, size: int) virtual  
void | _font_clear_size_cache(font_rid: RID) virtual  
void | _font_clear_textures(font_rid: RID, size: Vector2i) virtual  
void | _font_draw_glyph(font_rid: RID, canvas: RID, size: int, pos: Vector2, index: int, color: Color) virtual const  
void | _font_draw_glyph_outline(font_rid: RID, canvas: RID, size: int, outline_size: int, pos: Vector2, index: int, color: Color) virtual const  
FontAntialiasing | _font_get_antialiasing(font_rid: RID) virtual const  
float | _font_get_ascent(font_rid: RID, size: int) virtual const  
float | _font_get_baseline_offset(font_rid: RID) virtual const  
int | _font_get_char_from_glyph_index(font_rid: RID, size: int, glyph_index: int) virtual const  
float | _font_get_descent(font_rid: RID, size: int) virtual const  
bool | _font_get_disable_embedded_bitmaps(font_rid: RID) virtual const  
float | _font_get_embolden(font_rid: RID) virtual const  
int | _font_get_face_count(font_rid: RID) virtual const  
int | _font_get_face_index(font_rid: RID) virtual const  
int | _font_get_fixed_size(font_rid: RID) virtual const  
FixedSizeScaleMode | _font_get_fixed_size_scale_mode(font_rid: RID) virtual const  
bool | _font_get_generate_mipmaps(font_rid: RID) virtual const  
float | _font_get_global_oversampling() virtual const  
Vector2 | _font_get_glyph_advance(font_rid: RID, size: int, glyph: int) virtual const  
Dictionary | _font_get_glyph_contours(font_rid: RID, size: int, index: int) virtual const  
int | _font_get_glyph_index(font_rid: RID, size: int, char: int, variation_selector: int) virtual const  
PackedInt32Array | _font_get_glyph_list(font_rid: RID, size: Vector2i) virtual const  
Vector2 | _font_get_glyph_offset(font_rid: RID, size: Vector2i, glyph: int) virtual const  
Vector2 | _font_get_glyph_size(font_rid: RID, size: Vector2i, glyph: int) virtual const  
int | _font_get_glyph_texture_idx(font_rid: RID, size: Vector2i, glyph: int) virtual const  
RID | _font_get_glyph_texture_rid(font_rid: RID, size: Vector2i, glyph: int) virtual const  
Vector2 | _font_get_glyph_texture_size(font_rid: RID, size: Vector2i, glyph: int) virtual const  
Rect2 | _font_get_glyph_uv_rect(font_rid: RID, size: Vector2i, glyph: int) virtual const  
Hinting | _font_get_hinting(font_rid: RID) virtual const  
bool | _font_get_keep_rounding_remainders(font_rid: RID) virtual const  
Vector2 | _font_get_kerning(font_rid: RID, size: int, glyph_pair: Vector2i) virtual const  
Array[Vector2i] | _font_get_kerning_list(font_rid: RID, size: int) virtual const  
bool | _font_get_language_support_override(font_rid: RID, language: String) virtual  
PackedStringArray | _font_get_language_support_overrides(font_rid: RID) virtual  
int | _font_get_msdf_pixel_range(font_rid: RID) virtual const  
int | _font_get_msdf_size(font_rid: RID) virtual const  
String | _font_get_name(font_rid: RID) virtual const  
Dictionary | _font_get_opentype_feature_overrides(font_rid: RID) virtual const  
Dictionary | _font_get_ot_name_strings(font_rid: RID) virtual const  
float | _font_get_oversampling(font_rid: RID) virtual const  
float | _font_get_scale(font_rid: RID, size: int) virtual const  
bool | _font_get_script_support_override(font_rid: RID, script: String) virtual  
PackedStringArray | _font_get_script_support_overrides(font_rid: RID) virtual  
Array[Vector2i] | _font_get_size_cache_list(font_rid: RID) virtual const  
int | _font_get_spacing(font_rid: RID, spacing: SpacingType) virtual const  
int | _font_get_stretch(font_rid: RID) virtual const  
BitField[FontStyle] | _font_get_style(font_rid: RID) virtual const  
String | _font_get_style_name(font_rid: RID) virtual const  
SubpixelPositioning | _font_get_subpixel_positioning(font_rid: RID) virtual const  
String | _font_get_supported_chars(font_rid: RID) virtual const  
PackedInt32Array | _font_get_supported_glyphs(font_rid: RID) virtual const  
int | _font_get_texture_count(font_rid: RID, size: Vector2i) virtual const  
Image | _font_get_texture_image(font_rid: RID, size: Vector2i, texture_index: int) virtual const  
PackedInt32Array | _font_get_texture_offsets(font_rid: RID, size: Vector2i, texture_index: int) virtual const  
Transform2D | _font_get_transform(font_rid: RID) virtual const  
float | _font_get_underline_position(font_rid: RID, size: int) virtual const  
float | _font_get_underline_thickness(font_rid: RID, size: int) virtual const  
Dictionary | _font_get_variation_coordinates(font_rid: RID) virtual const  
int | _font_get_weight(font_rid: RID) virtual const  
bool | _font_has_char(font_rid: RID, char: int) virtual const  
bool | _font_is_allow_system_fallback(font_rid: RID) virtual const  
bool | _font_is_force_autohinter(font_rid: RID) virtual const  
bool | _font_is_language_supported(font_rid: RID, language: String) virtual const  
bool | _font_is_multichannel_signed_distance_field(font_rid: RID) virtual const  
bool | _font_is_script_supported(font_rid: RID, script: String) virtual const  
void | _font_remove_glyph(font_rid: RID, size: Vector2i, glyph: int) virtual  
void | _font_remove_kerning(font_rid: RID, size: int, glyph_pair: Vector2i) virtual  
void | _font_remove_language_support_override(font_rid: RID, language: String) virtual  
void | _font_remove_script_support_override(font_rid: RID, script: String) virtual  
void | _font_remove_size_cache(font_rid: RID, size: Vector2i) virtual  
void | _font_remove_texture(font_rid: RID, size: Vector2i, texture_index: int) virtual  
void | _font_render_glyph(font_rid: RID, size: Vector2i, index: int) virtual  
void | _font_render_range(font_rid: RID, size: Vector2i, start: int, end: int) virtual  
void | _font_set_allow_system_fallback(font_rid: RID, allow_system_fallback: bool) virtual  
void | _font_set_antialiasing(font_rid: RID, antialiasing: FontAntialiasing) virtual  
void | _font_set_ascent(font_rid: RID, size: int, ascent: float) virtual  
void | _font_set_baseline_offset(font_rid: RID, baseline_offset: float) virtual  
void | _font_set_data(font_rid: RID, data: PackedByteArray) virtual  
void | _font_set_data_ptr(font_rid: RID, data_ptr: `const uint8_t*`, data_size: int) virtual  
void | _font_set_descent(font_rid: RID, size: int, descent: float) virtual  
void | _font_set_disable_embedded_bitmaps(font_rid: RID, disable_embedded_bitmaps: bool) virtual  
void | _font_set_embolden(font_rid: RID, strength: float) virtual  
void | _font_set_face_index(font_rid: RID, face_index: int) virtual  
void | _font_set_fixed_size(font_rid: RID, fixed_size: int) virtual  
void | _font_set_fixed_size_scale_mode(font_rid: RID, fixed_size_scale_mode: FixedSizeScaleMode) virtual  
void | _font_set_force_autohinter(font_rid: RID, force_autohinter: bool) virtual  
void | _font_set_generate_mipmaps(font_rid: RID, generate_mipmaps: bool) virtual  
void | _font_set_global_oversampling(oversampling: float) virtual  
void | _font_set_glyph_advance(font_rid: RID, size: int, glyph: int, advance: Vector2) virtual  
void | _font_set_glyph_offset(font_rid: RID, size: Vector2i, glyph: int, offset: Vector2) virtual  
void | _font_set_glyph_size(font_rid: RID, size: Vector2i, glyph: int, gl_size: Vector2) virtual  
void | _font_set_glyph_texture_idx(font_rid: RID, size: Vector2i, glyph: int, texture_idx: int) virtual  
void | _font_set_glyph_uv_rect(font_rid: RID, size: Vector2i, glyph: int, uv_rect: Rect2) virtual  
void | _font_set_hinting(font_rid: RID, hinting: Hinting) virtual  
void | _font_set_keep_rounding_remainders(font_rid: RID, keep_rounding_remainders: bool) virtual  
void | _font_set_kerning(font_rid: RID, size: int, glyph_pair: Vector2i, kerning: Vector2) virtual  
void | _font_set_language_support_override(font_rid: RID, language: String, supported: bool) virtual  
void | _font_set_msdf_pixel_range(font_rid: RID, msdf_pixel_range: int) virtual  
void | _font_set_msdf_size(font_rid: RID, msdf_size: int) virtual  
void | _font_set_multichannel_signed_distance_field(font_rid: RID, msdf: bool) virtual  
void | _font_set_name(font_rid: RID, name: String) virtual  
void | _font_set_opentype_feature_overrides(font_rid: RID, overrides: Dictionary) virtual  
void | _font_set_oversampling(font_rid: RID, oversampling: float) virtual  
void | _font_set_scale(font_rid: RID, size: int, scale: float) virtual  
void | _font_set_script_support_override(font_rid: RID, script: String, supported: bool) virtual  
void | _font_set_spacing(font_rid: RID, spacing: SpacingType, value: int) virtual  
void | _font_set_stretch(font_rid: RID, stretch: int) virtual  
void | _font_set_style(font_rid: RID, style: BitField[FontStyle]) virtual  
void | _font_set_style_name(font_rid: RID, name_style: String) virtual  
void | _font_set_subpixel_positioning(font_rid: RID, subpixel_positioning: SubpixelPositioning) virtual  
void | _font_set_texture_image(font_rid: RID, size: Vector2i, texture_index: int, image: Image) virtual  
void | _font_set_texture_offsets(font_rid: RID, size: Vector2i, texture_index: int, offset: PackedInt32Array) virtual  
void | _font_set_transform(font_rid: RID, transform: Transform2D) virtual  
void | _font_set_underline_position(font_rid: RID, size: int, underline_position: float) virtual  
void | _font_set_underline_thickness(font_rid: RID, size: int, underline_thickness: float) virtual  
void | _font_set_variation_coordinates(font_rid: RID, variation_coordinates: Dictionary) virtual  
void | _font_set_weight(font_rid: RID, weight: int) virtual  
Dictionary | _font_supported_feature_list(font_rid: RID) virtual const  
Dictionary | _font_supported_variation_list(font_rid: RID) virtual const  
String | _format_number(number: String, language: String) virtual const  
void | _free_rid(rid: RID) virtual  
int | _get_features() virtual const  
Vector2 | _get_hex_code_box_size(size: int, index: int) virtual const  
String | _get_name() virtual const  
PackedByteArray | _get_support_data() virtual const  
String | _get_support_data_filename() virtual const  
String | _get_support_data_info() virtual const  
bool | _has(rid: RID) virtual  
bool | _has_feature(feature: Feature) virtual const  
int | _is_confusable(string: String, dict: PackedStringArray) virtual const  
bool | _is_locale_right_to_left(locale: String) virtual const  
bool | _is_valid_identifier(string: String) virtual const  
bool | _is_valid_letter(unicode: int) virtual const  
bool | _load_support_data(filename: String) virtual  
int | _name_to_tag(name: String) virtual const  
String | _parse_number(number: String, language: String) virtual const  
Array[Vector3i] | _parse_structured_text(parser_type: StructuredTextParser, args: Array, text: String) virtual const  
String | _percent_sign(language: String) virtual const  
bool | _save_support_data(filename: String) virtual const  
int | _shaped_get_span_count(shaped: RID) virtual const  
Variant | _shaped_get_span_embedded_object(shaped: RID, index: int) virtual const  
Variant | _shaped_get_span_meta(shaped: RID, index: int) virtual const  
void | _shaped_set_span_update_font(shaped: RID, index: int, fonts: Array[RID], size: int, opentype_features: Dictionary) virtual  
bool | _shaped_text_add_object(shaped: RID, key: Variant, size: Vector2, inline_align: InlineAlignment, length: int, baseline: float) virtual  
bool | _shaped_text_add_string(shaped: RID, text: String, fonts: Array[RID], size: int, opentype_features: Dictionary, language: String, meta: Variant) virtual  
void | _shaped_text_clear(shaped: RID) virtual  
int | _shaped_text_closest_character_pos(shaped: RID, pos: int) virtual const  
void | _shaped_text_draw(shaped: RID, canvas: RID, pos: Vector2, clip_l: float, clip_r: float, color: Color) virtual const  
void | _shaped_text_draw_outline(shaped: RID, canvas: RID, pos: Vector2, clip_l: float, clip_r: float, outline_size: int, color: Color) virtual const  
float | _shaped_text_fit_to_width(shaped: RID, width: float, justification_flags: BitField[JustificationFlag]) virtual  
float | _shaped_text_get_ascent(shaped: RID) virtual const  
void | _shaped_text_get_carets(shaped: RID, position: int, caret: `CaretInfo*`) virtual const  
PackedInt32Array | _shaped_text_get_character_breaks(shaped: RID) virtual const  
int | _shaped_text_get_custom_ellipsis(shaped: RID) virtual const  
String | _shaped_text_get_custom_punctuation(shaped: RID) virtual const  
float | _shaped_text_get_descent(shaped: RID) virtual const  
Direction | _shaped_text_get_direction(shaped: RID) virtual const  
int | _shaped_text_get_dominant_direction_in_range(shaped: RID, start: int, end: int) virtual const  
int | _shaped_text_get_ellipsis_glyph_count(shaped: RID) virtual const  
`const Glyph*` | _shaped_text_get_ellipsis_glyphs(shaped: RID) virtual const  
int | _shaped_text_get_ellipsis_pos(shaped: RID) virtual const  
int | _shaped_text_get_glyph_count(shaped: RID) virtual const  
`const Glyph*` | _shaped_text_get_glyphs(shaped: RID) virtual const  
Vector2 | _shaped_text_get_grapheme_bounds(shaped: RID, pos: int) virtual const  
Direction | _shaped_text_get_inferred_direction(shaped: RID) virtual const  
PackedInt32Array | _shaped_text_get_line_breaks(shaped: RID, width: float, start: int, break_flags: BitField[LineBreakFlag]) virtual const  
PackedInt32Array | _shaped_text_get_line_breaks_adv(shaped: RID, width: PackedFloat32Array, start: int, once: bool, break_flags: BitField[LineBreakFlag]) virtual const  
int | _shaped_text_get_object_glyph(shaped: RID, key: Variant) virtual const  
Vector2i | _shaped_text_get_object_range(shaped: RID, key: Variant) virtual const  
Rect2 | _shaped_text_get_object_rect(shaped: RID, key: Variant) virtual const  
Array | _shaped_text_get_objects(shaped: RID) virtual const  
Orientation | _shaped_text_get_orientation(shaped: RID) virtual const  
RID | _shaped_text_get_parent(shaped: RID) virtual const  
bool | _shaped_text_get_preserve_control(shaped: RID) virtual const  
bool | _shaped_text_get_preserve_invalid(shaped: RID) virtual const  
Vector2i | _shaped_text_get_range(shaped: RID) virtual const  
PackedVector2Array | _shaped_text_get_selection(shaped: RID, start: int, end: int) virtual const  
Vector2 | _shaped_text_get_size(shaped: RID) virtual const  
int | _shaped_text_get_spacing(shaped: RID, spacing: SpacingType) virtual const  
int | _shaped_text_get_trim_pos(shaped: RID) virtual const  
float | _shaped_text_get_underline_position(shaped: RID) virtual const  
float | _shaped_text_get_underline_thickness(shaped: RID) virtual const  
float | _shaped_text_get_width(shaped: RID) virtual const  
PackedInt32Array | _shaped_text_get_word_breaks(shaped: RID, grapheme_flags: BitField[GraphemeFlag], skip_grapheme_flags: BitField[GraphemeFlag]) virtual const  
int | _shaped_text_hit_test_grapheme(shaped: RID, coord: float) virtual const  
int | _shaped_text_hit_test_position(shaped: RID, coord: float) virtual const  
bool | _shaped_text_is_ready(shaped: RID) virtual const  
int | _shaped_text_next_character_pos(shaped: RID, pos: int) virtual const  
int | _shaped_text_next_grapheme_pos(shaped: RID, pos: int) virtual const  
void | _shaped_text_overrun_trim_to_width(shaped: RID, width: float, trim_flags: BitField[TextOverrunFlag]) virtual  
int | _shaped_text_prev_character_pos(shaped: RID, pos: int) virtual const  
int | _shaped_text_prev_grapheme_pos(shaped: RID, pos: int) virtual const  
bool | _shaped_text_resize_object(shaped: RID, key: Variant, size: Vector2, inline_align: InlineAlignment, baseline: float) virtual  
void | _shaped_text_set_bidi_override(shaped: RID, override: Array) virtual  
void | _shaped_text_set_custom_ellipsis(shaped: RID, char: int) virtual  
void | _shaped_text_set_custom_punctuation(shaped: RID, punct: String) virtual  
void | _shaped_text_set_direction(shaped: RID, direction: Direction) virtual  
void | _shaped_text_set_orientation(shaped: RID, orientation: Orientation) virtual  
void | _shaped_text_set_preserve_control(shaped: RID, enabled: bool) virtual  
void | _shaped_text_set_preserve_invalid(shaped: RID, enabled: bool) virtual  
void | _shaped_text_set_spacing(shaped: RID, spacing: SpacingType, value: int) virtual  
bool | _shaped_text_shape(shaped: RID) virtual  
`const Glyph*` | _shaped_text_sort_logical(shaped: RID) virtual  
RID | _shaped_text_substr(shaped: RID, start: int, length: int) virtual const  
float | _shaped_text_tab_align(shaped: RID, tab_stops: PackedFloat32Array) virtual  
bool | _shaped_text_update_breaks(shaped: RID) virtual  
bool | _shaped_text_update_justification_ops(shaped: RID) virtual  
bool | _spoof_check(string: String) virtual const  
PackedInt32Array | _string_get_character_breaks(string: String, language: String) virtual const  
PackedInt32Array | _string_get_word_breaks(string: String, language: String, chars_per_line: int) virtual const  
String | _string_to_lower(string: String, language: String) virtual const  
String | _string_to_title(string: String, language: String) virtual const  
String | _string_to_upper(string: String, language: String) virtual const  
String | _strip_diacritics(string: String) virtual const  
String | _tag_to_name(tag: int) virtual const  
  
## Method Descriptions

void _cleanup() virtual

Optional.

This method is called before text server is unregistered.

RID _create_font() virtual

Required.

Creates a new, empty font cache entry resource.

RID _create_font_linked_variation(font_rid: RID) virtual

Optional, implement if font supports extra spacing or baseline offset.

Creates a new variation existing font which is reusing the same glyph cache
and font data.

RID _create_shaped_text(direction: Direction, orientation: Orientation)
virtual

Required.

Creates a new buffer for complex text layout, with the given `direction` and
`orientation`.

void _draw_hex_code_box(canvas: RID, size: int, pos: Vector2, index: int,
color: Color) virtual const

Optional.

Draws box displaying character hexadecimal code.

void _font_clear_glyphs(font_rid: RID, size: Vector2i) virtual

Required.

Removes all rendered glyph information from the cache entry.

void _font_clear_kerning_map(font_rid: RID, size: int) virtual

Optional.

Removes all kerning overrides.

void _font_clear_size_cache(font_rid: RID) virtual

Required.

Removes all font sizes from the cache entry.

void _font_clear_textures(font_rid: RID, size: Vector2i) virtual

Required.

Removes all textures from font cache entry.

void _font_draw_glyph(font_rid: RID, canvas: RID, size: int, pos: Vector2,
index: int, color: Color) virtual const

Required.

Draws single glyph into a canvas item at the position, using `font_rid` at the
size `size`.

void _font_draw_glyph_outline(font_rid: RID, canvas: RID, size: int,
outline_size: int, pos: Vector2, index: int, color: Color) virtual const

Required.

Draws single glyph outline of size `outline_size` into a canvas item at the
position, using `font_rid` at the size `size`.

FontAntialiasing _font_get_antialiasing(font_rid: RID) virtual const

Optional.

Returns font anti-aliasing mode.

float _font_get_ascent(font_rid: RID, size: int) virtual const

Required.

Returns the font ascent (number of pixels above the baseline).

float _font_get_baseline_offset(font_rid: RID) virtual const

Optional.

Returns extra baseline offset (as a fraction of font height).

int _font_get_char_from_glyph_index(font_rid: RID, size: int, glyph_index:
int) virtual const

Required.

Returns character code associated with `glyph_index`, or `0` if `glyph_index`
is invalid.

float _font_get_descent(font_rid: RID, size: int) virtual const

Required.

Returns the font descent (number of pixels below the baseline).

bool _font_get_disable_embedded_bitmaps(font_rid: RID) virtual const

Optional.

Returns whether the font's embedded bitmap loading is disabled.

float _font_get_embolden(font_rid: RID) virtual const

Optional.

Returns font embolden strength.

int _font_get_face_count(font_rid: RID) virtual const

Optional.

Returns number of faces in the TrueType / OpenType collection.

int _font_get_face_index(font_rid: RID) virtual const

Optional.

Returns an active face index in the TrueType / OpenType collection.

int _font_get_fixed_size(font_rid: RID) virtual const

Required.

Returns bitmap font fixed size.

FixedSizeScaleMode _font_get_fixed_size_scale_mode(font_rid: RID) virtual
const

Required.

Returns bitmap font scaling mode.

bool _font_get_generate_mipmaps(font_rid: RID) virtual const

Optional.

Returns `true` if font texture mipmap generation is enabled.

float _font_get_global_oversampling() virtual const

Optional.

Returns the font oversampling factor, shared by all fonts in the TextServer.

Vector2 _font_get_glyph_advance(font_rid: RID, size: int, glyph: int) virtual
const

Required.

Returns glyph advance (offset of the next glyph).

Dictionary _font_get_glyph_contours(font_rid: RID, size: int, index: int)
virtual const

Optional.

Returns outline contours of the glyph.

int _font_get_glyph_index(font_rid: RID, size: int, char: int,
variation_selector: int) virtual const

Required.

Returns the glyph index of a `char`, optionally modified by the
`variation_selector`.

PackedInt32Array _font_get_glyph_list(font_rid: RID, size: Vector2i) virtual
const

Required.

Returns list of rendered glyphs in the cache entry.

Vector2 _font_get_glyph_offset(font_rid: RID, size: Vector2i, glyph: int)
virtual const

Required.

Returns glyph offset from the baseline.

Vector2 _font_get_glyph_size(font_rid: RID, size: Vector2i, glyph: int)
virtual const

Required.

Returns size of the glyph.

int _font_get_glyph_texture_idx(font_rid: RID, size: Vector2i, glyph: int)
virtual const

Required.

Returns index of the cache texture containing the glyph.

RID _font_get_glyph_texture_rid(font_rid: RID, size: Vector2i, glyph: int)
virtual const

Required.

Returns resource ID of the cache texture containing the glyph.

Vector2 _font_get_glyph_texture_size(font_rid: RID, size: Vector2i, glyph:
int) virtual const

Required.

Returns size of the cache texture containing the glyph.

Rect2 _font_get_glyph_uv_rect(font_rid: RID, size: Vector2i, glyph: int)
virtual const

Required.

Returns rectangle in the cache texture containing the glyph.

Hinting _font_get_hinting(font_rid: RID) virtual const

Optional.

Returns the font hinting mode. Used by dynamic fonts only.

bool _font_get_keep_rounding_remainders(font_rid: RID) virtual const

Optional.

Returns glyph position rounding behavior. If set to `true`, when aligning
glyphs to the pixel boundaries rounding remainders are accumulated to ensure
more uniform glyph distribution. This setting has no effect if subpixel
positioning is enabled.

Vector2 _font_get_kerning(font_rid: RID, size: int, glyph_pair: Vector2i)
virtual const

Optional.

Returns kerning for the pair of glyphs.

Array[Vector2i] _font_get_kerning_list(font_rid: RID, size: int) virtual const

Optional.

Returns list of the kerning overrides.

bool _font_get_language_support_override(font_rid: RID, language: String)
virtual

Optional.

Returns `true` if support override is enabled for the `language`.

PackedStringArray _font_get_language_support_overrides(font_rid: RID) virtual

Optional.

Returns list of language support overrides.

int _font_get_msdf_pixel_range(font_rid: RID) virtual const

Optional.

Returns the width of the range around the shape between the minimum and
maximum representable signed distance.

int _font_get_msdf_size(font_rid: RID) virtual const

Optional.

Returns source font size used to generate MSDF textures.

String _font_get_name(font_rid: RID) virtual const

Optional.

Returns font family name.

Dictionary _font_get_opentype_feature_overrides(font_rid: RID) virtual const

Optional.

Returns font OpenType feature set override.

Dictionary _font_get_ot_name_strings(font_rid: RID) virtual const

Optional.

Returns Dictionary with OpenType font name strings (localized font names,
version, description, license information, sample text, etc.).

float _font_get_oversampling(font_rid: RID) virtual const

Optional.

Returns font oversampling factor, if set to `0.0` global oversampling factor
is used instead. Used by dynamic fonts only.

float _font_get_scale(font_rid: RID, size: int) virtual const

Required.

Returns scaling factor of the color bitmap font.

bool _font_get_script_support_override(font_rid: RID, script: String) virtual

Optional.

Returns `true` if support override is enabled for the `script`.

PackedStringArray _font_get_script_support_overrides(font_rid: RID) virtual

Optional.

Returns list of script support overrides.

Array[Vector2i] _font_get_size_cache_list(font_rid: RID) virtual const

Required.

Returns list of the font sizes in the cache. Each size is Vector2i with font
size and outline size.

int _font_get_spacing(font_rid: RID, spacing: SpacingType) virtual const

Optional.

Returns the spacing for `spacing` (see SpacingType) in pixels (not relative to
the font size).

int _font_get_stretch(font_rid: RID) virtual const

Optional.

Returns font stretch amount, compared to a normal width. A percentage value
between `50%` and `200%`.

BitField[FontStyle] _font_get_style(font_rid: RID) virtual const

Optional.

Returns font style flags, see FontStyle.

String _font_get_style_name(font_rid: RID) virtual const

Optional.

Returns font style name.

SubpixelPositioning _font_get_subpixel_positioning(font_rid: RID) virtual
const

Optional.

Returns font subpixel glyph positioning mode.

String _font_get_supported_chars(font_rid: RID) virtual const

Required.

Returns a string containing all the characters available in the font.

PackedInt32Array _font_get_supported_glyphs(font_rid: RID) virtual const

Required.

Returns an array containing all glyph indices in the font.

int _font_get_texture_count(font_rid: RID, size: Vector2i) virtual const

Required.

Returns number of textures used by font cache entry.

Image _font_get_texture_image(font_rid: RID, size: Vector2i, texture_index:
int) virtual const

Required.

Returns font cache texture image data.

PackedInt32Array _font_get_texture_offsets(font_rid: RID, size: Vector2i,
texture_index: int) virtual const

Optional.

Returns array containing glyph packing data.

Transform2D _font_get_transform(font_rid: RID) virtual const

Optional.

Returns 2D transform applied to the font outlines.

float _font_get_underline_position(font_rid: RID, size: int) virtual const

Required.

Returns pixel offset of the underline below the baseline.

float _font_get_underline_thickness(font_rid: RID, size: int) virtual const

Required.

Returns thickness of the underline in pixels.

Dictionary _font_get_variation_coordinates(font_rid: RID) virtual const

Optional.

Returns variation coordinates for the specified font cache entry.

int _font_get_weight(font_rid: RID) virtual const

Optional.

Returns weight (boldness) of the font. A value in the `100...999` range,
normal font weight is `400`, bold font weight is `700`.

bool _font_has_char(font_rid: RID, char: int) virtual const

Required.

Returns `true` if a Unicode `char` is available in the font.

bool _font_is_allow_system_fallback(font_rid: RID) virtual const

Optional.

Returns `true` if system fonts can be automatically used as fallbacks.

bool _font_is_force_autohinter(font_rid: RID) virtual const

Optional.

Returns `true` if auto-hinting is supported and preferred over font built-in
hinting.

bool _font_is_language_supported(font_rid: RID, language: String) virtual
const

Optional.

Returns `true`, if font supports given language (ISO 639 code).

bool _font_is_multichannel_signed_distance_field(font_rid: RID) virtual const

Optional.

Returns `true` if glyphs of all sizes are rendered using single multichannel
signed distance field generated from the dynamic font vector data.

bool _font_is_script_supported(font_rid: RID, script: String) virtual const

Optional.

Returns `true`, if font supports given script (ISO 15924 code).

void _font_remove_glyph(font_rid: RID, size: Vector2i, glyph: int) virtual

Required.

Removes specified rendered glyph information from the cache entry.

void _font_remove_kerning(font_rid: RID, size: int, glyph_pair: Vector2i)
virtual

Optional.

Removes kerning override for the pair of glyphs.

void _font_remove_language_support_override(font_rid: RID, language: String)
virtual

Optional.

Remove language support override.

void _font_remove_script_support_override(font_rid: RID, script: String)
virtual

Optional.

Removes script support override.

void _font_remove_size_cache(font_rid: RID, size: Vector2i) virtual

Required.

Removes specified font size from the cache entry.

void _font_remove_texture(font_rid: RID, size: Vector2i, texture_index: int)
virtual

Required.

Removes specified texture from the cache entry.

void _font_render_glyph(font_rid: RID, size: Vector2i, index: int) virtual

Optional.

Renders specified glyph to the font cache texture.

void _font_render_range(font_rid: RID, size: Vector2i, start: int, end: int)
virtual

Optional.

Renders the range of characters to the font cache texture.

void _font_set_allow_system_fallback(font_rid: RID, allow_system_fallback:
bool) virtual

Optional.

If set to `true`, system fonts can be automatically used as fallbacks.

void _font_set_antialiasing(font_rid: RID, antialiasing: FontAntialiasing)
virtual

Optional.

Sets font anti-aliasing mode.

void _font_set_ascent(font_rid: RID, size: int, ascent: float) virtual

Required.

Sets the font ascent (number of pixels above the baseline).

void _font_set_baseline_offset(font_rid: RID, baseline_offset: float) virtual

Optional.

Sets extra baseline offset (as a fraction of font height).

void _font_set_data(font_rid: RID, data: PackedByteArray) virtual

Optional.

Sets font source data, e.g contents of the dynamic font source file.

void _font_set_data_ptr(font_rid: RID, data_ptr: `const uint8_t*`, data_size:
int) virtual

Optional.

Sets pointer to the font source data, e.g contents of the dynamic font source
file.

void _font_set_descent(font_rid: RID, size: int, descent: float) virtual

Required.

Sets the font descent (number of pixels below the baseline).

void _font_set_disable_embedded_bitmaps(font_rid: RID,
disable_embedded_bitmaps: bool) virtual

Optional.

If set to `true`, embedded font bitmap loading is disabled.

void _font_set_embolden(font_rid: RID, strength: float) virtual

Sets font embolden strength. If `strength` is not equal to zero, emboldens the
font outlines. Negative values reduce the outline thickness.

void _font_set_face_index(font_rid: RID, face_index: int) virtual

Optional.

Sets an active face index in the TrueType / OpenType collection.

void _font_set_fixed_size(font_rid: RID, fixed_size: int) virtual

Required.

Sets bitmap font fixed size. If set to value greater than zero, same cache
entry will be used for all font sizes.

void _font_set_fixed_size_scale_mode(font_rid: RID, fixed_size_scale_mode:
FixedSizeScaleMode) virtual

Required.

Sets bitmap font scaling mode. This property is used only if `fixed_size` is
greater than zero.

void _font_set_force_autohinter(font_rid: RID, force_autohinter: bool) virtual

Optional.

If set to `true` auto-hinting is preferred over font built-in hinting.

void _font_set_generate_mipmaps(font_rid: RID, generate_mipmaps: bool) virtual

Optional.

If set to `true` font texture mipmap generation is enabled.

void _font_set_global_oversampling(oversampling: float) virtual

Optional.

Sets oversampling factor, shared by all font in the TextServer.

void _font_set_glyph_advance(font_rid: RID, size: int, glyph: int, advance:
Vector2) virtual

Required.

Sets glyph advance (offset of the next glyph).

void _font_set_glyph_offset(font_rid: RID, size: Vector2i, glyph: int, offset:
Vector2) virtual

Required.

Sets glyph offset from the baseline.

void _font_set_glyph_size(font_rid: RID, size: Vector2i, glyph: int, gl_size:
Vector2) virtual

Required.

Sets size of the glyph.

void _font_set_glyph_texture_idx(font_rid: RID, size: Vector2i, glyph: int,
texture_idx: int) virtual

Required.

Sets index of the cache texture containing the glyph.

void _font_set_glyph_uv_rect(font_rid: RID, size: Vector2i, glyph: int,
uv_rect: Rect2) virtual

Required.

Sets rectangle in the cache texture containing the glyph.

void _font_set_hinting(font_rid: RID, hinting: Hinting) virtual

Optional.

Sets font hinting mode. Used by dynamic fonts only.

void _font_set_keep_rounding_remainders(font_rid: RID,
keep_rounding_remainders: bool) virtual

Optional.

Sets glyph position rounding behavior. If set to `true`, when aligning glyphs
to the pixel boundaries rounding remainders are accumulated to ensure more
uniform glyph distribution. This setting has no effect if subpixel positioning
is enabled.

void _font_set_kerning(font_rid: RID, size: int, glyph_pair: Vector2i,
kerning: Vector2) virtual

Optional.

Sets kerning for the pair of glyphs.

void _font_set_language_support_override(font_rid: RID, language: String,
supported: bool) virtual

Optional.

Adds override for _font_is_language_supported().

void _font_set_msdf_pixel_range(font_rid: RID, msdf_pixel_range: int) virtual

Optional.

Sets the width of the range around the shape between the minimum and maximum
representable signed distance.

void _font_set_msdf_size(font_rid: RID, msdf_size: int) virtual

Optional.

Sets source font size used to generate MSDF textures.

void _font_set_multichannel_signed_distance_field(font_rid: RID, msdf: bool)
virtual

Optional.

If set to `true`, glyphs of all sizes are rendered using single multichannel
signed distance field generated from the dynamic font vector data. MSDF
rendering allows displaying the font at any scaling factor without blurriness,
and without incurring a CPU cost when the font size changes (since the font no
longer needs to be rasterized on the CPU). As a downside, font hinting is not
available with MSDF. The lack of font hinting may result in less crisp and
less readable fonts at small sizes.

void _font_set_name(font_rid: RID, name: String) virtual

Optional.

Sets the font family name.

void _font_set_opentype_feature_overrides(font_rid: RID, overrides:
Dictionary) virtual

Optional.

Sets font OpenType feature set override.

void _font_set_oversampling(font_rid: RID, oversampling: float) virtual

Optional.

Sets font oversampling factor, if set to `0.0` global oversampling factor is
used instead. Used by dynamic fonts only.

void _font_set_scale(font_rid: RID, size: int, scale: float) virtual

Required.

Sets scaling factor of the color bitmap font.

void _font_set_script_support_override(font_rid: RID, script: String,
supported: bool) virtual

Optional.

Adds override for _font_is_script_supported().

void _font_set_spacing(font_rid: RID, spacing: SpacingType, value: int)
virtual

Optional.

Sets the spacing for `spacing` (see SpacingType) to `value` in pixels (not
relative to the font size).

void _font_set_stretch(font_rid: RID, stretch: int) virtual

Optional.

Sets font stretch amount, compared to a normal width. A percentage value
between `50%` and `200%`.

void _font_set_style(font_rid: RID, style: BitField[FontStyle]) virtual

Optional.

Sets the font style flags, see FontStyle.

void _font_set_style_name(font_rid: RID, name_style: String) virtual

Optional.

Sets the font style name.

void _font_set_subpixel_positioning(font_rid: RID, subpixel_positioning:
SubpixelPositioning) virtual

Optional.

Sets font subpixel glyph positioning mode.

void _font_set_texture_image(font_rid: RID, size: Vector2i, texture_index:
int, image: Image) virtual

Required.

Sets font cache texture image data.

void _font_set_texture_offsets(font_rid: RID, size: Vector2i, texture_index:
int, offset: PackedInt32Array) virtual

Optional.

Sets array containing glyph packing data.

void _font_set_transform(font_rid: RID, transform: Transform2D) virtual

Optional.

Sets 2D transform, applied to the font outlines, can be used for slanting,
flipping, and rotating glyphs.

void _font_set_underline_position(font_rid: RID, size: int,
underline_position: float) virtual

Required.

Sets pixel offset of the underline below the baseline.

void _font_set_underline_thickness(font_rid: RID, size: int,
underline_thickness: float) virtual

Required.

Sets thickness of the underline in pixels.

void _font_set_variation_coordinates(font_rid: RID, variation_coordinates:
Dictionary) virtual

Optional.

Sets variation coordinates for the specified font cache entry.

void _font_set_weight(font_rid: RID, weight: int) virtual

Optional.

Sets weight (boldness) of the font. A value in the `100...999` range, normal
font weight is `400`, bold font weight is `700`.

Dictionary _font_supported_feature_list(font_rid: RID) virtual const

Optional.

Returns the dictionary of the supported OpenType features.

Dictionary _font_supported_variation_list(font_rid: RID) virtual const

Optional.

Returns the dictionary of the supported OpenType variation coordinates.

String _format_number(number: String, language: String) virtual const

Optional.

Converts a number from the Western Arabic (0..9) to the numeral systems used
in `language`.

void _free_rid(rid: RID) virtual

Required.

Frees an object created by this TextServer.

int _get_features() virtual const

Required.

Returns text server features, see Feature.

Vector2 _get_hex_code_box_size(size: int, index: int) virtual const

Optional.

Returns size of the replacement character (box with character hexadecimal code
that is drawn in place of invalid characters).

String _get_name() virtual const

Required.

Returns the name of the server interface.

PackedByteArray _get_support_data() virtual const

Optional.

Returns default TextServer database (e.g. ICU break iterators and
dictionaries).

String _get_support_data_filename() virtual const

Optional.

Returns default TextServer database (e.g. ICU break iterators and
dictionaries) filename.

String _get_support_data_info() virtual const

Optional.

Returns TextServer database (e.g. ICU break iterators and dictionaries)
description.

bool _has(rid: RID) virtual

Required.

Returns `true` if `rid` is valid resource owned by this text server.

bool _has_feature(feature: Feature) virtual const

Required.

Returns `true` if the server supports a feature.

int _is_confusable(string: String, dict: PackedStringArray) virtual const

Optional.

Returns index of the first string in `dict` which is visually confusable with
the `string`, or `-1` if none is found.

bool _is_locale_right_to_left(locale: String) virtual const

Required.

Returns `true` if locale is right-to-left.

bool _is_valid_identifier(string: String) virtual const

Optional.

Returns `true` if `string` is a valid identifier.

bool _is_valid_letter(unicode: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _load_support_data(filename: String) virtual

Optional.

Loads optional TextServer database (e.g. ICU break iterators and
dictionaries).

int _name_to_tag(name: String) virtual const

Optional.

Converts readable feature, variation, script, or language name to OpenType
tag.

String _parse_number(number: String, language: String) virtual const

Optional.

Converts `number` from the numeral systems used in `language` to Western
Arabic (0..9).

Array[Vector3i] _parse_structured_text(parser_type: StructuredTextParser,
args: Array, text: String) virtual const

Optional.

Default implementation of the BiDi algorithm override function. See
StructuredTextParser for more info.

String _percent_sign(language: String) virtual const

Optional.

Returns percent sign used in the `language`.

bool _save_support_data(filename: String) virtual const

Optional.

Saves optional TextServer database (e.g. ICU break iterators and dictionaries)
to the file.

int _shaped_get_span_count(shaped: RID) virtual const

Required.

Returns number of text spans added using _shaped_text_add_string() or
_shaped_text_add_object().

Variant _shaped_get_span_embedded_object(shaped: RID, index: int) virtual
const

Required.

Returns text embedded object key.

Variant _shaped_get_span_meta(shaped: RID, index: int) virtual const

Required.

Returns text span metadata.

void _shaped_set_span_update_font(shaped: RID, index: int, fonts: Array[RID],
size: int, opentype_features: Dictionary) virtual

Required.

Changes text span font, font size, and OpenType features, without changing the
text.

bool _shaped_text_add_object(shaped: RID, key: Variant, size: Vector2,
inline_align: InlineAlignment, length: int, baseline: float) virtual

Required.

Adds inline object to the text buffer, `key` must be unique. In the text,
object is represented as `length` object replacement characters.

bool _shaped_text_add_string(shaped: RID, text: String, fonts: Array[RID],
size: int, opentype_features: Dictionary, language: String, meta: Variant)
virtual

Required.

Adds text span and font to draw it to the text buffer.

void _shaped_text_clear(shaped: RID) virtual

Required.

Clears text buffer (removes text and inline objects).

int _shaped_text_closest_character_pos(shaped: RID, pos: int) virtual const

Optional.

Returns composite character position closest to the `pos`.

void _shaped_text_draw(shaped: RID, canvas: RID, pos: Vector2, clip_l: float,
clip_r: float, color: Color) virtual const

Optional.

Draw shaped text into a canvas item at a given position, with `color`. `pos`
specifies the leftmost point of the baseline (for horizontal layout) or
topmost point of the baseline (for vertical layout).

void _shaped_text_draw_outline(shaped: RID, canvas: RID, pos: Vector2, clip_l:
float, clip_r: float, outline_size: int, color: Color) virtual const

Optional.

Draw the outline of the shaped text into a canvas item at a given position,
with `color`. `pos` specifies the leftmost point of the baseline (for
horizontal layout) or topmost point of the baseline (for vertical layout).

float _shaped_text_fit_to_width(shaped: RID, width: float,
justification_flags: BitField[JustificationFlag]) virtual

Optional.

Adjusts text width to fit to specified width, returns new text width.

float _shaped_text_get_ascent(shaped: RID) virtual const

Required.

Returns the text ascent (number of pixels above the baseline for horizontal
layout or to the left of baseline for vertical).

void _shaped_text_get_carets(shaped: RID, position: int, caret: `CaretInfo*`)
virtual const

Optional.

Returns shapes of the carets corresponding to the character offset `position`
in the text. Returned caret shape is 1 pixel wide rectangle.

PackedInt32Array _shaped_text_get_character_breaks(shaped: RID) virtual const

Optional.

Returns array of the composite character boundaries.

int _shaped_text_get_custom_ellipsis(shaped: RID) virtual const

Optional.

Returns ellipsis character used for text clipping.

String _shaped_text_get_custom_punctuation(shaped: RID) virtual const

Optional.

Returns custom punctuation character list, used for word breaking. If set to
empty string, server defaults are used.

float _shaped_text_get_descent(shaped: RID) virtual const

Required.

Returns the text descent (number of pixels below the baseline for horizontal
layout or to the right of baseline for vertical).

Direction _shaped_text_get_direction(shaped: RID) virtual const

Optional.

Returns direction of the text.

int _shaped_text_get_dominant_direction_in_range(shaped: RID, start: int, end:
int) virtual const

Optional.

Returns dominant direction of in the range of text.

int _shaped_text_get_ellipsis_glyph_count(shaped: RID) virtual const

Required.

Returns number of glyphs in the ellipsis.

`const Glyph*` _shaped_text_get_ellipsis_glyphs(shaped: RID) virtual const

Required.

Returns array of the glyphs in the ellipsis.

int _shaped_text_get_ellipsis_pos(shaped: RID) virtual const

Required.

Returns position of the ellipsis.

int _shaped_text_get_glyph_count(shaped: RID) virtual const

Required.

Returns number of glyphs in the buffer.

`const Glyph*` _shaped_text_get_glyphs(shaped: RID) virtual const

Required.

Returns an array of glyphs in the visual order.

Vector2 _shaped_text_get_grapheme_bounds(shaped: RID, pos: int) virtual const

Optional.

Returns composite character's bounds as offsets from the start of the line.

Direction _shaped_text_get_inferred_direction(shaped: RID) virtual const

Optional.

Returns direction of the text, inferred by the BiDi algorithm.

PackedInt32Array _shaped_text_get_line_breaks(shaped: RID, width: float,
start: int, break_flags: BitField[LineBreakFlag]) virtual const

Optional.

Breaks text to the lines and returns character ranges for each line.

PackedInt32Array _shaped_text_get_line_breaks_adv(shaped: RID, width:
PackedFloat32Array, start: int, once: bool, break_flags:
BitField[LineBreakFlag]) virtual const

Optional.

Breaks text to the lines and columns. Returns character ranges for each
segment.

int _shaped_text_get_object_glyph(shaped: RID, key: Variant) virtual const

Required.

Returns the glyph index of the inline object.

Vector2i _shaped_text_get_object_range(shaped: RID, key: Variant) virtual
const

Required.

Returns the character range of the inline object.

Rect2 _shaped_text_get_object_rect(shaped: RID, key: Variant) virtual const

Required.

Returns bounding rectangle of the inline object.

Array _shaped_text_get_objects(shaped: RID) virtual const

Required.

Returns array of inline objects.

Orientation _shaped_text_get_orientation(shaped: RID) virtual const

Optional.

Returns text orientation.

RID _shaped_text_get_parent(shaped: RID) virtual const

Required.

Returns the parent buffer from which the substring originates.

bool _shaped_text_get_preserve_control(shaped: RID) virtual const

Optional.

Returns `true` if text buffer is configured to display control characters.

bool _shaped_text_get_preserve_invalid(shaped: RID) virtual const

Optional.

Returns `true` if text buffer is configured to display hexadecimal codes in
place of invalid characters.

Vector2i _shaped_text_get_range(shaped: RID) virtual const

Required.

Returns substring buffer character range in the parent buffer.

PackedVector2Array _shaped_text_get_selection(shaped: RID, start: int, end:
int) virtual const

Optional.

Returns selection rectangles for the specified character range.

Vector2 _shaped_text_get_size(shaped: RID) virtual const

Required.

Returns size of the text.

int _shaped_text_get_spacing(shaped: RID, spacing: SpacingType) virtual const

Optional.

Returns extra spacing added between glyphs or lines in pixels.

int _shaped_text_get_trim_pos(shaped: RID) virtual const

Required.

Returns the position of the overrun trim.

float _shaped_text_get_underline_position(shaped: RID) virtual const

Required.

Returns pixel offset of the underline below the baseline.

float _shaped_text_get_underline_thickness(shaped: RID) virtual const

Required.

Returns thickness of the underline.

float _shaped_text_get_width(shaped: RID) virtual const

Required.

Returns width (for horizontal layout) or height (for vertical) of the text.

PackedInt32Array _shaped_text_get_word_breaks(shaped: RID, grapheme_flags:
BitField[GraphemeFlag], skip_grapheme_flags: BitField[GraphemeFlag]) virtual
const

Optional.

Breaks text into words and returns array of character ranges. Use
`grapheme_flags` to set what characters are used for breaking (see
GraphemeFlag).

int _shaped_text_hit_test_grapheme(shaped: RID, coord: float) virtual const

Optional.

Returns grapheme index at the specified pixel offset at the baseline, or `-1`
if none is found.

int _shaped_text_hit_test_position(shaped: RID, coord: float) virtual const

Optional.

Returns caret character offset at the specified pixel offset at the baseline.
This function always returns a valid position.

bool _shaped_text_is_ready(shaped: RID) virtual const

Required.

Returns `true` if buffer is successfully shaped.

int _shaped_text_next_character_pos(shaped: RID, pos: int) virtual const

Optional.

Returns composite character end position closest to the `pos`.

int _shaped_text_next_grapheme_pos(shaped: RID, pos: int) virtual const

Optional.

Returns grapheme end position closest to the `pos`.

void _shaped_text_overrun_trim_to_width(shaped: RID, width: float, trim_flags:
BitField[TextOverrunFlag]) virtual

Optional.

Trims text if it exceeds the given width.

int _shaped_text_prev_character_pos(shaped: RID, pos: int) virtual const

Optional.

Returns composite character start position closest to the `pos`.

int _shaped_text_prev_grapheme_pos(shaped: RID, pos: int) virtual const

Optional.

Returns grapheme start position closest to the `pos`.

bool _shaped_text_resize_object(shaped: RID, key: Variant, size: Vector2,
inline_align: InlineAlignment, baseline: float) virtual

Required.

Sets new size and alignment of embedded object.

void _shaped_text_set_bidi_override(shaped: RID, override: Array) virtual

Optional.

Overrides BiDi for the structured text.

void _shaped_text_set_custom_ellipsis(shaped: RID, char: int) virtual

Optional.

Sets ellipsis character used for text clipping.

void _shaped_text_set_custom_punctuation(shaped: RID, punct: String) virtual

Optional.

Sets custom punctuation character list, used for word breaking. If set to
empty string, server defaults are used.

void _shaped_text_set_direction(shaped: RID, direction: Direction) virtual

Optional.

Sets desired text direction. If set to TextServer.DIRECTION_AUTO, direction
will be detected based on the buffer contents and current locale.

void _shaped_text_set_orientation(shaped: RID, orientation: Orientation)
virtual

Optional.

Sets desired text orientation.

void _shaped_text_set_preserve_control(shaped: RID, enabled: bool) virtual

Optional.

If set to `true` text buffer will display control characters.

void _shaped_text_set_preserve_invalid(shaped: RID, enabled: bool) virtual

Optional.

If set to `true` text buffer will display invalid characters as hexadecimal
codes, otherwise nothing is displayed.

void _shaped_text_set_spacing(shaped: RID, spacing: SpacingType, value: int)
virtual

Optional.

Sets extra spacing added between glyphs or lines in pixels.

bool _shaped_text_shape(shaped: RID) virtual

Required.

Shapes buffer if it's not shaped. Returns `true` if the string is shaped
successfully.

`const Glyph*` _shaped_text_sort_logical(shaped: RID) virtual

Required.

Returns text glyphs in the logical order.

RID _shaped_text_substr(shaped: RID, start: int, length: int) virtual const

Required.

Returns text buffer for the substring of the text in the `shaped` text buffer
(including inline objects).

float _shaped_text_tab_align(shaped: RID, tab_stops: PackedFloat32Array)
virtual

Optional.

Aligns shaped text to the given tab-stops.

bool _shaped_text_update_breaks(shaped: RID) virtual

Optional.

Updates break points in the shaped text. This method is called by default
implementation of text breaking functions.

bool _shaped_text_update_justification_ops(shaped: RID) virtual

Optional.

Updates justification points in the shaped text. This method is called by
default implementation of text justification functions.

bool _spoof_check(string: String) virtual const

Optional.

Returns `true` if `string` is likely to be an attempt at confusing the reader.

PackedInt32Array _string_get_character_breaks(string: String, language:
String) virtual const

Optional.

Returns array of the composite character boundaries.

PackedInt32Array _string_get_word_breaks(string: String, language: String,
chars_per_line: int) virtual const

Optional.

Returns an array of the word break boundaries. Elements in the returned array
are the offsets of the start and end of words. Therefore the length of the
array is always even.

String _string_to_lower(string: String, language: String) virtual const

Optional.

Returns the string converted to lowercase.

String _string_to_title(string: String, language: String) virtual const

Optional.

Returns the string converted to title case.

String _string_to_upper(string: String, language: String) virtual const

Optional.

Returns the string converted to uppercase.

String _strip_diacritics(string: String) virtual const

Optional.

Strips diacritics from the string.

String _tag_to_name(tag: int) virtual const

Optional.

Converts OpenType tag to readable feature, variation, script, or language
name.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[BitField]: This value is an integer composed as a bitmask of the following flags.

