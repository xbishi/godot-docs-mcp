# TranslationServer

Inherits: Object

The server responsible for language translations.

## Description

The translation server is the API backend that manages all language
translations.

Translations are stored in TranslationDomains, which can be accessed by name.
The most commonly used translation domain is the main translation domain. It
always exists and can be accessed using an empty StringName. The translation
server provides wrapper methods for accessing the main translation domain
directly, without having to fetch the translation domain first. Custom
translation domains are mainly for advanced usages like editor plugins. Names
starting with `godot.` are reserved for engine internals.

## Tutorials

  * Internationalizing games

  * Locales

## Properties

bool | pseudolocalization_enabled | `false`  
---|---|---  
  
## Methods

void | add_translation(translation: Translation)  
---|---  
void | clear()  
int | compare_locales(locale_a: String, locale_b: String) const  
PackedStringArray | get_all_countries() const  
PackedStringArray | get_all_languages() const  
PackedStringArray | get_all_scripts() const  
String | get_country_name(country: String) const  
String | get_language_name(language: String) const  
PackedStringArray | get_loaded_locales() const  
String | get_locale() const  
String | get_locale_name(locale: String) const  
TranslationDomain | get_or_add_domain(domain: StringName)  
String | get_script_name(script: String) const  
String | get_tool_locale()  
Translation | get_translation_object(locale: String)  
bool | has_domain(domain: StringName) const  
StringName | pseudolocalize(message: StringName) const  
void | reload_pseudolocalization()  
void | remove_domain(domain: StringName)  
void | remove_translation(translation: Translation)  
void | set_locale(locale: String)  
String | standardize_locale(locale: String, add_defaults: bool = false) const  
StringName | translate(message: StringName, context: StringName = &"") const  
StringName | translate_plural(message: StringName, plural_message: StringName, n: int, context: StringName = &"") const  
  
## Property Descriptions

bool pseudolocalization_enabled = `false`

  * void set_pseudolocalization_enabled(value: bool)

  * bool is_pseudolocalization_enabled()

If `true`, enables the use of pseudolocalization on the main translation
domain. See
ProjectSettings.internationalization/pseudolocalization/use_pseudolocalization
for details.

## Method Descriptions

void add_translation(translation: Translation)

Adds a translation to the main translation domain.

void clear()

Removes all translations from the main translation domain.

int compare_locales(locale_a: String, locale_b: String) const

Compares two locales and returns a similarity score between `0` (no match) and
`10` (full match).

PackedStringArray get_all_countries() const

Returns an array of known country codes.

PackedStringArray get_all_languages() const

Returns array of known language codes.

PackedStringArray get_all_scripts() const

Returns an array of known script codes.

String get_country_name(country: String) const

Returns a readable country name for the `country` code.

String get_language_name(language: String) const

Returns a readable language name for the `language` code.

PackedStringArray get_loaded_locales() const

Returns an array of all loaded locales of the project.

String get_locale() const

Returns the current locale of the project.

See also OS.get_locale() and OS.get_locale_language() to query the locale of
the user system.

String get_locale_name(locale: String) const

Returns a locale's language and its variant (e.g. `"en_US"` would return
`"English (United States)"`).

TranslationDomain get_or_add_domain(domain: StringName)

Returns the translation domain with the specified name. An empty translation
domain will be created and added if it does not exist.

String get_script_name(script: String) const

Returns a readable script name for the `script` code.

String get_tool_locale()

Returns the current locale of the editor.

Note: When called from an exported project returns the same value as
get_locale().

Translation get_translation_object(locale: String)

Returns the Translation instance that best matches `locale` in the main
translation domain. Returns `null` if there are no matches.

bool has_domain(domain: StringName) const

Returns `true` if a translation domain with the specified name exists.

StringName pseudolocalize(message: StringName) const

Returns the pseudolocalized string based on the `message` passed in.

Note: This method always uses the main translation domain.

void reload_pseudolocalization()

Reparses the pseudolocalization options and reloads the translation for the
main translation domain.

void remove_domain(domain: StringName)

Removes the translation domain with the specified name.

Note: Trying to remove the main translation domain is an error.

void remove_translation(translation: Translation)

Removes the given translation from the main translation domain.

void set_locale(locale: String)

Sets the locale of the project. The `locale` string will be standardized to
match known locales (e.g. `en-US` would be matched to `en_US`).

If translations have been loaded beforehand for the new locale, they will be
applied.

String standardize_locale(locale: String, add_defaults: bool = false) const

Returns a `locale` string standardized to match known locales (e.g. `en-US`
would be matched to `en_US`). If `add_defaults` is `true`, the locale may have
a default script or country added.

StringName translate(message: StringName, context: StringName = &"") const

Returns the current locale's translation for the given message and context.

Note: This method always uses the main translation domain.

StringName translate_plural(message: StringName, plural_message: StringName,
n: int, context: StringName = &"") const

Returns the current locale's translation for the given message, plural message
and context.

The number `n` is the number or quantity of the plural object. It will be used
to guide the translation system to fetch the correct plural form for the
selected language.

Note: This method always uses the main translation domain.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

