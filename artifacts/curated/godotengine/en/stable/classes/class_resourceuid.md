# ResourceUID

Inherits: Object

A singleton that manages the unique identifiers of all resources within a
project.

## Description

Resource UIDs (Unique IDentifiers) allow the engine to keep references between
resources intact, even if files are renamed or moved. They can be accessed
with `uid://`.

ResourceUID keeps track of all registered resource UIDs in a project,
generates new UIDs, and converts between their string and integer
representations.

## Methods

void | add_id(id: int, path: String)  
---|---  
int | create_id()  
String | get_id_path(id: int) const  
bool | has_id(id: int) const  
String | id_to_text(id: int) const  
void | remove_id(id: int)  
void | set_id(id: int, path: String)  
int | text_to_id(text_id: String) const  
  
## Constants

INVALID_ID = `-1`

The value to use for an invalid UID, for example if the resource could not be
loaded.

Its text representation is `uid://<invalid>`.

## Method Descriptions

void add_id(id: int, path: String)

Adds a new UID value which is mapped to the given resource path.

Fails with an error if the UID already exists, so be sure to check has_id()
beforehand, or use set_id() instead.

int create_id()

Generates a random resource UID which is guaranteed to be unique within the
list of currently loaded UIDs.

In order for this UID to be registered, you must call add_id() or set_id().

String get_id_path(id: int) const

Returns the path that the given UID value refers to.

Fails with an error if the UID does not exist, so be sure to check has_id()
beforehand.

bool has_id(id: int) const

Returns whether the given UID value is known to the cache.

String id_to_text(id: int) const

Converts the given UID to a `uid://` string value.

void remove_id(id: int)

Removes a loaded UID value from the cache.

Fails with an error if the UID does not exist, so be sure to check has_id()
beforehand.

void set_id(id: int, path: String)

Updates the resource path of an existing UID.

Fails with an error if the UID does not exist, so be sure to check has_id()
beforehand, or use add_id() instead.

int text_to_id(text_id: String) const

Extracts the UID value from the given `uid://` string.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

