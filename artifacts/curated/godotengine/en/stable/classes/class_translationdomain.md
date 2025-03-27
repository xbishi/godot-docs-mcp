# TranslationDomain

Inherits: RefCounted < Object

A self-contained collection of Translation resources.

## Description

TranslationDomain is a self-contained collection of Translation resources.
Translations can be added to or removed from it.

If you're working with the main translation domain, it is more convenient to
use the wrap methods on TranslationServer.

## Properties

bool | pseudolocalization_accents_enabled | `true`  
---|---|---  
bool | pseudolocalization_double_vowels_enabled | `false`  
bool | pseudolocalization_enabled | `false`  
float | pseudolocalization_expansion_ratio | `0.0`  
bool | pseudolocalization_fake_bidi_enabled | `false`  
bool | pseudolocalization_override_enabled | `false`  
String | pseudolocalization_prefix | `"["`  
bool | pseudolocalization_skip_placeholders_enabled | `true`  
String | pseudolocalization_suffix | `"]"`  
  
## Methods

void | add_translation(translation: Translation)  
---|---  
void | clear()  
Translation | get_translation_object(locale: String) const  
StringName | pseudolocalize(message: StringName) const  
void | remove_translation(translation: Translation)  
StringName | translate(message: StringName, context: StringName = &"") const  
StringName | translate_plural(message: StringName, message_plural: StringName, n: int, context: StringName = &"") const  
  
## Property Descriptions

bool pseudolocalization_accents_enabled = `true`

  * void set_pseudolocalization_accents_enabled(value: bool)

  * bool is_pseudolocalization_accents_enabled()

Replace all characters with their accented variants during pseudolocalization.

Note: Updating this property does not automatically update texts in the scene
tree. Please propagate the MainLoop.NOTIFICATION_TRANSLATION_CHANGED
notification manually after you have finished modifying pseudolocalization
related options.

bool pseudolocalization_double_vowels_enabled = `false`

  * void set_pseudolocalization_double_vowels_enabled(value: bool)

  * bool is_pseudolocalization_double_vowels_enabled()

Double vowels in strings during pseudolocalization to simulate the lengthening
of text due to localization.

Note: Updating this property does not automatically update texts in the scene
tree. Please propagate the MainLoop.NOTIFICATION_TRANSLATION_CHANGED
notification manually after you have finished modifying pseudolocalization
related options.

bool pseudolocalization_enabled = `false`

  * void set_pseudolocalization_enabled(value: bool)

  * bool is_pseudolocalization_enabled()

If `true`, enables pseudolocalization for the project. This can be used to
spot untranslatable strings or layout issues that may occur once the project
is localized to languages that have longer strings than the source language.

Note: Updating this property does not automatically update texts in the scene
tree. Please propagate the MainLoop.NOTIFICATION_TRANSLATION_CHANGED
notification manually after you have finished modifying pseudolocalization
related options.

float pseudolocalization_expansion_ratio = `0.0`

  * void set_pseudolocalization_expansion_ratio(value: float)

  * float get_pseudolocalization_expansion_ratio()

The expansion ratio to use during pseudolocalization. A value of `0.3` is
sufficient for most practical purposes, and will increase the length of each
string by 30%.

Note: Updating this property does not automatically update texts in the scene
tree. Please propagate the MainLoop.NOTIFICATION_TRANSLATION_CHANGED
notification manually after you have finished modifying pseudolocalization
related options.

bool pseudolocalization_fake_bidi_enabled = `false`

  * void set_pseudolocalization_fake_bidi_enabled(value: bool)

  * bool is_pseudolocalization_fake_bidi_enabled()

If `true`, emulate bidirectional (right-to-left) text when pseudolocalization
is enabled. This can be used to spot issues with RTL layout and UI mirroring
that will crop up if the project is localized to RTL languages such as Arabic
or Hebrew.

Note: Updating this property does not automatically update texts in the scene
tree. Please propagate the MainLoop.NOTIFICATION_TRANSLATION_CHANGED
notification manually after you have finished modifying pseudolocalization
related options.

bool pseudolocalization_override_enabled = `false`

  * void set_pseudolocalization_override_enabled(value: bool)

  * bool is_pseudolocalization_override_enabled()

Replace all characters in the string with `*`. Useful for finding non-
localizable strings.

Note: Updating this property does not automatically update texts in the scene
tree. Please propagate the MainLoop.NOTIFICATION_TRANSLATION_CHANGED
notification manually after you have finished modifying pseudolocalization
related options.

String pseudolocalization_prefix = `"["`

  * void set_pseudolocalization_prefix(value: String)

  * String get_pseudolocalization_prefix()

Prefix that will be prepended to the pseudolocalized string.

Note: Updating this property does not automatically update texts in the scene
tree. Please propagate the MainLoop.NOTIFICATION_TRANSLATION_CHANGED
notification manually after you have finished modifying pseudolocalization
related options.

bool pseudolocalization_skip_placeholders_enabled = `true`

  * void set_pseudolocalization_skip_placeholders_enabled(value: bool)

  * bool is_pseudolocalization_skip_placeholders_enabled()

Skip placeholders for string formatting like `%s` or `%f` during
pseudolocalization. Useful to identify strings which need additional control
characters to display correctly.

Note: Updating this property does not automatically update texts in the scene
tree. Please propagate the MainLoop.NOTIFICATION_TRANSLATION_CHANGED
notification manually after you have finished modifying pseudolocalization
related options.

String pseudolocalization_suffix = `"]"`

  * void set_pseudolocalization_suffix(value: String)

  * String get_pseudolocalization_suffix()

Suffix that will be appended to the pseudolocalized string.

Note: Updating this property does not automatically update texts in the scene
tree. Please propagate the MainLoop.NOTIFICATION_TRANSLATION_CHANGED
notification manually after you have finished modifying pseudolocalization
related options.

## Method Descriptions

void add_translation(translation: Translation)

Adds a translation.

void clear()

Removes all translations.

Translation get_translation_object(locale: String) const

Returns the Translation instance that best matches `locale`. Returns `null` if
there are no matches.

StringName pseudolocalize(message: StringName) const

Returns the pseudolocalized string based on the `message` passed in.

void remove_translation(translation: Translation)

Removes the given translation.

StringName translate(message: StringName, context: StringName = &"") const

Returns the current locale's translation for the given message and context.

StringName translate_plural(message: StringName, message_plural: StringName,
n: int, context: StringName = &"") const

Returns the current locale's translation for the given message, plural message
and context.

The number `n` is the number or quantity of the plural object. It will be used
to guide the translation system to fetch the correct plural form for the
selected language.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

