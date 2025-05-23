# NoiseTexture2D

Inherits: Texture2D < Texture < Resource < RefCounted < Object

A 2D texture filled with noise generated by a Noise object.

## Description

Uses the FastNoiseLite library or other noise generators to fill the texture
data of your desired size. NoiseTexture2D can also generate normal map
textures.

The class uses Threads to generate the texture data internally, so
Texture2D.get_image() may return `null` if the generation process has not
completed yet. In that case, you need to wait for the texture to be generated
before accessing the image and the generated byte data:

    
    
    var texture = NoiseTexture2D.new()
    texture.noise = FastNoiseLite.new()
    await texture.changed
    var image = texture.get_image()
    var data = image.get_data()
    

## Properties

bool | as_normal_map | `false`  
---|---|---  
float | bump_strength | `8.0`  
Gradient | color_ramp  
bool | generate_mipmaps | `true`  
int | height | `512`  
bool | in_3d_space | `false`  
bool | invert | `false`  
Noise | noise  
bool | normalize | `true`  
bool | resource_local_to_scene | `false` (overrides Resource)  
bool | seamless | `false`  
float | seamless_blend_skirt | `0.1`  
int | width | `512`  
  
## Property Descriptions

bool as_normal_map = `false`

  * void set_as_normal_map(value: bool)

  * bool is_normal_map()

If `true`, the resulting texture contains a normal map created from the
original noise interpreted as a bump map.

float bump_strength = `8.0`

  * void set_bump_strength(value: float)

  * float get_bump_strength()

Strength of the bump maps used in this texture. A higher value will make the
bump maps appear larger while a lower value will make them appear softer.

Gradient color_ramp

  * void set_color_ramp(value: Gradient)

  * Gradient get_color_ramp()

A Gradient which is used to map the luminance of each pixel to a color value.

bool generate_mipmaps = `true`

  * void set_generate_mipmaps(value: bool)

  * bool is_generating_mipmaps()

Determines whether mipmaps are generated for this texture. Enabling this
results in less texture aliasing in the distance, at the cost of increasing
memory usage by roughly 33% and making the noise texture generation take
longer.

Note: generate_mipmaps requires mipmap filtering to be enabled on the material
using the NoiseTexture2D to have an effect.

int height = `512`

  * void set_height(value: int)

  * int get_height()

Height of the generated texture (in pixels).

bool in_3d_space = `false`

  * void set_in_3d_space(value: bool)

  * bool is_in_3d_space()

Determines whether the noise image is calculated in 3D space. May result in
reduced contrast.

bool invert = `false`

  * void set_invert(value: bool)

  * bool get_invert()

If `true`, inverts the noise texture. White becomes black, black becomes
white.

Noise noise

  * void set_noise(value: Noise)

  * Noise get_noise()

The instance of the Noise object.

bool normalize = `true`

  * void set_normalize(value: bool)

  * bool is_normalized()

If `true`, the noise image coming from the noise generator is normalized to
the range `0.0` to `1.0`.

Turning normalization off can affect the contrast and allows you to generate
non repeating tileable noise textures.

bool seamless = `false`

  * void set_seamless(value: bool)

  * bool get_seamless()

If `true`, a seamless texture is requested from the Noise resource.

Note: Seamless noise textures may take longer to generate and/or can have a
lower contrast compared to non-seamless noise depending on the used Noise
resource. This is because some implementations use higher dimensions for
generating seamless noise.

Note: The default FastNoiseLite implementation uses the fallback path for
seamless generation. If using a width or height lower than the default, you
may need to increase seamless_blend_skirt to make seamless blending more
effective.

float seamless_blend_skirt = `0.1`

  * void set_seamless_blend_skirt(value: float)

  * float get_seamless_blend_skirt()

Used for the default/fallback implementation of the seamless texture
generation. It determines the distance over which the seams are blended. High
values may result in less details and contrast. See Noise for further details.

Note: If using a width or height lower than the default, you may need to
increase seamless_blend_skirt to make seamless blending more effective.

int width = `512`

  * void set_width(value: int)

  * int get_width()

Width of the generated texture (in pixels).

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

