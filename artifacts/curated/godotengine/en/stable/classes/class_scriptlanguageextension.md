# ScriptLanguageExtension

Inherits: ScriptLanguage < Object

There is currently no description for this class. Please help us by
contributing one!

## Methods

void | _add_global_constant(name: StringName, value: Variant) virtual  
---|---  
void | _add_named_global_constant(name: StringName, value: Variant) virtual  
String | _auto_indent_code(code: String, from_line: int, to_line: int) virtual const  
bool | _can_inherit_from_file() virtual const  
bool | _can_make_function() virtual const  
Dictionary | _complete_code(code: String, path: String, owner: Object) virtual const  
Object | _create_script() virtual const  
Array[Dictionary] | _debug_get_current_stack_info() virtual  
String | _debug_get_error() virtual const  
Dictionary | _debug_get_globals(max_subitems: int, max_depth: int) virtual  
int | _debug_get_stack_level_count() virtual const  
String | _debug_get_stack_level_function(level: int) virtual const  
`void*` | _debug_get_stack_level_instance(level: int) virtual  
int | _debug_get_stack_level_line(level: int) virtual const  
Dictionary | _debug_get_stack_level_locals(level: int, max_subitems: int, max_depth: int) virtual  
Dictionary | _debug_get_stack_level_members(level: int, max_subitems: int, max_depth: int) virtual  
String | _debug_get_stack_level_source(level: int) virtual const  
String | _debug_parse_stack_level_expression(level: int, expression: String, max_subitems: int, max_depth: int) virtual  
int | _find_function(function: String, code: String) virtual const  
void | _finish() virtual  
void | _frame() virtual  
Array[Dictionary] | _get_built_in_templates(object: StringName) virtual const  
PackedStringArray | _get_comment_delimiters() virtual const  
PackedStringArray | _get_doc_comment_delimiters() virtual const  
String | _get_extension() virtual const  
Dictionary | _get_global_class_name(path: String) virtual const  
String | _get_name() virtual const  
Array[Dictionary] | _get_public_annotations() virtual const  
Dictionary | _get_public_constants() virtual const  
Array[Dictionary] | _get_public_functions() virtual const  
PackedStringArray | _get_recognized_extensions() virtual const  
PackedStringArray | _get_reserved_words() virtual const  
PackedStringArray | _get_string_delimiters() virtual const  
String | _get_type() virtual const  
bool | _handles_global_class_type(type: String) virtual const  
bool | _has_named_classes() virtual const  
void | _init() virtual  
bool | _is_control_flow_keyword(keyword: String) virtual const  
bool | _is_using_templates() virtual  
Dictionary | _lookup_code(code: String, symbol: String, path: String, owner: Object) virtual const  
String | _make_function(class_name: String, function_name: String, function_args: PackedStringArray) virtual const  
Script | _make_template(template: String, class_name: String, base_class_name: String) virtual const  
Error | _open_in_external_editor(script: Script, line: int, column: int) virtual  
bool | _overrides_external_editor() virtual  
ScriptNameCasing | _preferred_file_name_casing() virtual const  
int | _profiling_get_accumulated_data(info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: int) virtual  
int | _profiling_get_frame_data(info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: int) virtual  
void | _profiling_set_save_native_calls(enable: bool) virtual  
void | _profiling_start() virtual  
void | _profiling_stop() virtual  
void | _reload_all_scripts() virtual  
void | _reload_scripts(scripts: Array, soft_reload: bool) virtual  
void | _reload_tool_script(script: Script, soft_reload: bool) virtual  
void | _remove_named_global_constant(name: StringName) virtual  
bool | _supports_builtin_mode() virtual const  
bool | _supports_documentation() virtual const  
void | _thread_enter() virtual  
void | _thread_exit() virtual  
Dictionary | _validate(script: String, path: String, validate_functions: bool, validate_errors: bool, validate_warnings: bool, validate_safe_lines: bool) virtual const  
String | _validate_path(path: String) virtual const  
  
## Enumerations

enum LookupResultType:

LookupResultType LOOKUP_RESULT_SCRIPT_LOCATION = `0`

There is currently no description for this enum. Please help us by
contributing one!

LookupResultType LOOKUP_RESULT_CLASS = `1`

There is currently no description for this enum. Please help us by
contributing one!

LookupResultType LOOKUP_RESULT_CLASS_CONSTANT = `2`

There is currently no description for this enum. Please help us by
contributing one!

LookupResultType LOOKUP_RESULT_CLASS_PROPERTY = `3`

There is currently no description for this enum. Please help us by
contributing one!

LookupResultType LOOKUP_RESULT_CLASS_METHOD = `4`

There is currently no description for this enum. Please help us by
contributing one!

LookupResultType LOOKUP_RESULT_CLASS_SIGNAL = `5`

There is currently no description for this enum. Please help us by
contributing one!

LookupResultType LOOKUP_RESULT_CLASS_ENUM = `6`

There is currently no description for this enum. Please help us by
contributing one!

LookupResultType LOOKUP_RESULT_CLASS_TBD_GLOBALSCOPE = `7`

Deprecated: This constant may be changed or removed in future versions.

LookupResultType LOOKUP_RESULT_CLASS_ANNOTATION = `8`

There is currently no description for this enum. Please help us by
contributing one!

LookupResultType LOOKUP_RESULT_LOCAL_CONSTANT = `9`

There is currently no description for this enum. Please help us by
contributing one!

LookupResultType LOOKUP_RESULT_LOCAL_VARIABLE = `10`

There is currently no description for this enum. Please help us by
contributing one!

LookupResultType LOOKUP_RESULT_MAX = `11`

There is currently no description for this enum. Please help us by
contributing one!

enum CodeCompletionLocation:

CodeCompletionLocation LOCATION_LOCAL = `0`

The option is local to the location of the code completion query - e.g. a
local variable. Subsequent value of location represent options from the outer
class, the exact value represent how far they are (in terms of inner classes).

CodeCompletionLocation LOCATION_PARENT_MASK = `256`

The option is from the containing class or a parent class, relative to the
location of the code completion query. Perform a bitwise OR with the class
depth (e.g. `0` for the local class, `1` for the parent, `2` for the
grandparent, etc.) to store the depth of an option in the class or a parent
class.

CodeCompletionLocation LOCATION_OTHER_USER_CODE = `512`

The option is from user code which is not local and not in a derived class
(e.g. Autoload Singletons).

CodeCompletionLocation LOCATION_OTHER = `1024`

The option is from other engine code, not covered by the other enum constants
- e.g. built-in classes.

enum CodeCompletionKind:

CodeCompletionKind CODE_COMPLETION_KIND_CLASS = `0`

There is currently no description for this enum. Please help us by
contributing one!

CodeCompletionKind CODE_COMPLETION_KIND_FUNCTION = `1`

There is currently no description for this enum. Please help us by
contributing one!

CodeCompletionKind CODE_COMPLETION_KIND_SIGNAL = `2`

There is currently no description for this enum. Please help us by
contributing one!

CodeCompletionKind CODE_COMPLETION_KIND_VARIABLE = `3`

There is currently no description for this enum. Please help us by
contributing one!

CodeCompletionKind CODE_COMPLETION_KIND_MEMBER = `4`

There is currently no description for this enum. Please help us by
contributing one!

CodeCompletionKind CODE_COMPLETION_KIND_ENUM = `5`

There is currently no description for this enum. Please help us by
contributing one!

CodeCompletionKind CODE_COMPLETION_KIND_CONSTANT = `6`

There is currently no description for this enum. Please help us by
contributing one!

CodeCompletionKind CODE_COMPLETION_KIND_NODE_PATH = `7`

There is currently no description for this enum. Please help us by
contributing one!

CodeCompletionKind CODE_COMPLETION_KIND_FILE_PATH = `8`

There is currently no description for this enum. Please help us by
contributing one!

CodeCompletionKind CODE_COMPLETION_KIND_PLAIN_TEXT = `9`

There is currently no description for this enum. Please help us by
contributing one!

CodeCompletionKind CODE_COMPLETION_KIND_MAX = `10`

There is currently no description for this enum. Please help us by
contributing one!

## Method Descriptions

void _add_global_constant(name: StringName, value: Variant) virtual

There is currently no description for this method. Please help us by
contributing one!

void _add_named_global_constant(name: StringName, value: Variant) virtual

There is currently no description for this method. Please help us by
contributing one!

String _auto_indent_code(code: String, from_line: int, to_line: int) virtual
const

There is currently no description for this method. Please help us by
contributing one!

bool _can_inherit_from_file() virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _can_make_function() virtual const

There is currently no description for this method. Please help us by
contributing one!

Dictionary _complete_code(code: String, path: String, owner: Object) virtual
const

There is currently no description for this method. Please help us by
contributing one!

Object _create_script() virtual const

There is currently no description for this method. Please help us by
contributing one!

Array[Dictionary] _debug_get_current_stack_info() virtual

There is currently no description for this method. Please help us by
contributing one!

String _debug_get_error() virtual const

There is currently no description for this method. Please help us by
contributing one!

Dictionary _debug_get_globals(max_subitems: int, max_depth: int) virtual

There is currently no description for this method. Please help us by
contributing one!

int _debug_get_stack_level_count() virtual const

There is currently no description for this method. Please help us by
contributing one!

String _debug_get_stack_level_function(level: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

`void*` _debug_get_stack_level_instance(level: int) virtual

There is currently no description for this method. Please help us by
contributing one!

int _debug_get_stack_level_line(level: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

Dictionary _debug_get_stack_level_locals(level: int, max_subitems: int,
max_depth: int) virtual

There is currently no description for this method. Please help us by
contributing one!

Dictionary _debug_get_stack_level_members(level: int, max_subitems: int,
max_depth: int) virtual

There is currently no description for this method. Please help us by
contributing one!

String _debug_get_stack_level_source(level: int) virtual const

Returns the source associated with a given debug stack position.

String _debug_parse_stack_level_expression(level: int, expression: String,
max_subitems: int, max_depth: int) virtual

There is currently no description for this method. Please help us by
contributing one!

int _find_function(function: String, code: String) virtual const

Returns the line where the function is defined in the code, or `-1` if the
function is not present.

void _finish() virtual

There is currently no description for this method. Please help us by
contributing one!

void _frame() virtual

There is currently no description for this method. Please help us by
contributing one!

Array[Dictionary] _get_built_in_templates(object: StringName) virtual const

There is currently no description for this method. Please help us by
contributing one!

PackedStringArray _get_comment_delimiters() virtual const

There is currently no description for this method. Please help us by
contributing one!

PackedStringArray _get_doc_comment_delimiters() virtual const

There is currently no description for this method. Please help us by
contributing one!

String _get_extension() virtual const

There is currently no description for this method. Please help us by
contributing one!

Dictionary _get_global_class_name(path: String) virtual const

There is currently no description for this method. Please help us by
contributing one!

String _get_name() virtual const

There is currently no description for this method. Please help us by
contributing one!

Array[Dictionary] _get_public_annotations() virtual const

There is currently no description for this method. Please help us by
contributing one!

Dictionary _get_public_constants() virtual const

There is currently no description for this method. Please help us by
contributing one!

Array[Dictionary] _get_public_functions() virtual const

There is currently no description for this method. Please help us by
contributing one!

PackedStringArray _get_recognized_extensions() virtual const

There is currently no description for this method. Please help us by
contributing one!

PackedStringArray _get_reserved_words() virtual const

There is currently no description for this method. Please help us by
contributing one!

PackedStringArray _get_string_delimiters() virtual const

There is currently no description for this method. Please help us by
contributing one!

String _get_type() virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _handles_global_class_type(type: String) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _has_named_classes() virtual const

Deprecated: This method is not called by the engine.

void _init() virtual

There is currently no description for this method. Please help us by
contributing one!

bool _is_control_flow_keyword(keyword: String) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _is_using_templates() virtual

There is currently no description for this method. Please help us by
contributing one!

Dictionary _lookup_code(code: String, symbol: String, path: String, owner:
Object) virtual const

There is currently no description for this method. Please help us by
contributing one!

String _make_function(class_name: String, function_name: String,
function_args: PackedStringArray) virtual const

There is currently no description for this method. Please help us by
contributing one!

Script _make_template(template: String, class_name: String, base_class_name:
String) virtual const

There is currently no description for this method. Please help us by
contributing one!

Error _open_in_external_editor(script: Script, line: int, column: int) virtual

There is currently no description for this method. Please help us by
contributing one!

bool _overrides_external_editor() virtual

There is currently no description for this method. Please help us by
contributing one!

ScriptNameCasing _preferred_file_name_casing() virtual const

There is currently no description for this method. Please help us by
contributing one!

int _profiling_get_accumulated_data(info_array:
`ScriptLanguageExtensionProfilingInfo*`, info_max: int) virtual

There is currently no description for this method. Please help us by
contributing one!

int _profiling_get_frame_data(info_array:
`ScriptLanguageExtensionProfilingInfo*`, info_max: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _profiling_set_save_native_calls(enable: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _profiling_start() virtual

There is currently no description for this method. Please help us by
contributing one!

void _profiling_stop() virtual

There is currently no description for this method. Please help us by
contributing one!

void _reload_all_scripts() virtual

There is currently no description for this method. Please help us by
contributing one!

void _reload_scripts(scripts: Array, soft_reload: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _reload_tool_script(script: Script, soft_reload: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _remove_named_global_constant(name: StringName) virtual

There is currently no description for this method. Please help us by
contributing one!

bool _supports_builtin_mode() virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _supports_documentation() virtual const

There is currently no description for this method. Please help us by
contributing one!

void _thread_enter() virtual

There is currently no description for this method. Please help us by
contributing one!

void _thread_exit() virtual

There is currently no description for this method. Please help us by
contributing one!

Dictionary _validate(script: String, path: String, validate_functions: bool,
validate_errors: bool, validate_warnings: bool, validate_safe_lines: bool)
virtual const

There is currently no description for this method. Please help us by
contributing one!

String _validate_path(path: String) virtual const

There is currently no description for this method. Please help us by
contributing one!

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

