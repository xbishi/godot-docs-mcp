# PhysicsServer3DExtension

Inherits: PhysicsServer3D < Object

Provides virtual methods that can be overridden to create custom
PhysicsServer3D implementations.

## Description

This class extends PhysicsServer3D by providing additional virtual methods
that can be overridden. When these methods are overridden, they will be called
instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of
PhysicsServer3D.

## Methods

void | _area_add_shape(area: RID, shape: RID, transform: Transform3D, disabled: bool) virtual  
---|---  
void | _area_attach_object_instance_id(area: RID, id: int) virtual  
void | _area_clear_shapes(area: RID) virtual  
RID | _area_create() virtual  
int | _area_get_collision_layer(area: RID) virtual const  
int | _area_get_collision_mask(area: RID) virtual const  
int | _area_get_object_instance_id(area: RID) virtual const  
Variant | _area_get_param(area: RID, param: AreaParameter) virtual const  
RID | _area_get_shape(area: RID, shape_idx: int) virtual const  
int | _area_get_shape_count(area: RID) virtual const  
Transform3D | _area_get_shape_transform(area: RID, shape_idx: int) virtual const  
RID | _area_get_space(area: RID) virtual const  
Transform3D | _area_get_transform(area: RID) virtual const  
void | _area_remove_shape(area: RID, shape_idx: int) virtual  
void | _area_set_area_monitor_callback(area: RID, callback: Callable) virtual  
void | _area_set_collision_layer(area: RID, layer: int) virtual  
void | _area_set_collision_mask(area: RID, mask: int) virtual  
void | _area_set_monitor_callback(area: RID, callback: Callable) virtual  
void | _area_set_monitorable(area: RID, monitorable: bool) virtual  
void | _area_set_param(area: RID, param: AreaParameter, value: Variant) virtual  
void | _area_set_ray_pickable(area: RID, enable: bool) virtual  
void | _area_set_shape(area: RID, shape_idx: int, shape: RID) virtual  
void | _area_set_shape_disabled(area: RID, shape_idx: int, disabled: bool) virtual  
void | _area_set_shape_transform(area: RID, shape_idx: int, transform: Transform3D) virtual  
void | _area_set_space(area: RID, space: RID) virtual  
void | _area_set_transform(area: RID, transform: Transform3D) virtual  
void | _body_add_collision_exception(body: RID, excepted_body: RID) virtual  
void | _body_add_constant_central_force(body: RID, force: Vector3) virtual  
void | _body_add_constant_force(body: RID, force: Vector3, position: Vector3) virtual  
void | _body_add_constant_torque(body: RID, torque: Vector3) virtual  
void | _body_add_shape(body: RID, shape: RID, transform: Transform3D, disabled: bool) virtual  
void | _body_apply_central_force(body: RID, force: Vector3) virtual  
void | _body_apply_central_impulse(body: RID, impulse: Vector3) virtual  
void | _body_apply_force(body: RID, force: Vector3, position: Vector3) virtual  
void | _body_apply_impulse(body: RID, impulse: Vector3, position: Vector3) virtual  
void | _body_apply_torque(body: RID, torque: Vector3) virtual  
void | _body_apply_torque_impulse(body: RID, impulse: Vector3) virtual  
void | _body_attach_object_instance_id(body: RID, id: int) virtual  
void | _body_clear_shapes(body: RID) virtual  
RID | _body_create() virtual  
Array[RID] | _body_get_collision_exceptions(body: RID) virtual const  
int | _body_get_collision_layer(body: RID) virtual const  
int | _body_get_collision_mask(body: RID) virtual const  
float | _body_get_collision_priority(body: RID) virtual const  
Vector3 | _body_get_constant_force(body: RID) virtual const  
Vector3 | _body_get_constant_torque(body: RID) virtual const  
float | _body_get_contacts_reported_depth_threshold(body: RID) virtual const  
PhysicsDirectBodyState3D | _body_get_direct_state(body: RID) virtual  
int | _body_get_max_contacts_reported(body: RID) virtual const  
BodyMode | _body_get_mode(body: RID) virtual const  
int | _body_get_object_instance_id(body: RID) virtual const  
Variant | _body_get_param(body: RID, param: BodyParameter) virtual const  
RID | _body_get_shape(body: RID, shape_idx: int) virtual const  
int | _body_get_shape_count(body: RID) virtual const  
Transform3D | _body_get_shape_transform(body: RID, shape_idx: int) virtual const  
RID | _body_get_space(body: RID) virtual const  
Variant | _body_get_state(body: RID, state: BodyState) virtual const  
int | _body_get_user_flags(body: RID) virtual const  
bool | _body_is_axis_locked(body: RID, axis: BodyAxis) virtual const  
bool | _body_is_continuous_collision_detection_enabled(body: RID) virtual const  
bool | _body_is_omitting_force_integration(body: RID) virtual const  
void | _body_remove_collision_exception(body: RID, excepted_body: RID) virtual  
void | _body_remove_shape(body: RID, shape_idx: int) virtual  
void | _body_reset_mass_properties(body: RID) virtual  
void | _body_set_axis_lock(body: RID, axis: BodyAxis, lock: bool) virtual  
void | _body_set_axis_velocity(body: RID, axis_velocity: Vector3) virtual  
void | _body_set_collision_layer(body: RID, layer: int) virtual  
void | _body_set_collision_mask(body: RID, mask: int) virtual  
void | _body_set_collision_priority(body: RID, priority: float) virtual  
void | _body_set_constant_force(body: RID, force: Vector3) virtual  
void | _body_set_constant_torque(body: RID, torque: Vector3) virtual  
void | _body_set_contacts_reported_depth_threshold(body: RID, threshold: float) virtual  
void | _body_set_enable_continuous_collision_detection(body: RID, enable: bool) virtual  
void | _body_set_force_integration_callback(body: RID, callable: Callable, userdata: Variant) virtual  
void | _body_set_max_contacts_reported(body: RID, amount: int) virtual  
void | _body_set_mode(body: RID, mode: BodyMode) virtual  
void | _body_set_omit_force_integration(body: RID, enable: bool) virtual  
void | _body_set_param(body: RID, param: BodyParameter, value: Variant) virtual  
void | _body_set_ray_pickable(body: RID, enable: bool) virtual  
void | _body_set_shape(body: RID, shape_idx: int, shape: RID) virtual  
void | _body_set_shape_disabled(body: RID, shape_idx: int, disabled: bool) virtual  
void | _body_set_shape_transform(body: RID, shape_idx: int, transform: Transform3D) virtual  
void | _body_set_space(body: RID, space: RID) virtual  
void | _body_set_state(body: RID, state: BodyState, value: Variant) virtual  
void | _body_set_state_sync_callback(body: RID, callable: Callable) virtual  
void | _body_set_user_flags(body: RID, flags: int) virtual  
bool | _body_test_motion(body: RID, from: Transform3D, motion: Vector3, margin: float, max_collisions: int, collide_separation_ray: bool, recovery_as_collision: bool, result: `PhysicsServer3DExtensionMotionResult*`) virtual const  
RID | _box_shape_create() virtual  
RID | _capsule_shape_create() virtual  
RID | _concave_polygon_shape_create() virtual  
float | _cone_twist_joint_get_param(joint: RID, param: ConeTwistJointParam) virtual const  
void | _cone_twist_joint_set_param(joint: RID, param: ConeTwistJointParam, value: float) virtual  
RID | _convex_polygon_shape_create() virtual  
RID | _custom_shape_create() virtual  
RID | _cylinder_shape_create() virtual  
void | _end_sync() virtual  
void | _finish() virtual  
void | _flush_queries() virtual  
void | _free_rid(rid: RID) virtual  
bool | _generic_6dof_joint_get_flag(joint: RID, axis: Axis, flag: G6DOFJointAxisFlag) virtual const  
float | _generic_6dof_joint_get_param(joint: RID, axis: Axis, param: G6DOFJointAxisParam) virtual const  
void | _generic_6dof_joint_set_flag(joint: RID, axis: Axis, flag: G6DOFJointAxisFlag, enable: bool) virtual  
void | _generic_6dof_joint_set_param(joint: RID, axis: Axis, param: G6DOFJointAxisParam, value: float) virtual  
int | _get_process_info(process_info: ProcessInfo) virtual  
RID | _heightmap_shape_create() virtual  
bool | _hinge_joint_get_flag(joint: RID, flag: HingeJointFlag) virtual const  
float | _hinge_joint_get_param(joint: RID, param: HingeJointParam) virtual const  
void | _hinge_joint_set_flag(joint: RID, flag: HingeJointFlag, enabled: bool) virtual  
void | _hinge_joint_set_param(joint: RID, param: HingeJointParam, value: float) virtual  
void | _init() virtual  
bool | _is_flushing_queries() virtual const  
void | _joint_clear(joint: RID) virtual  
RID | _joint_create() virtual  
void | _joint_disable_collisions_between_bodies(joint: RID, disable: bool) virtual  
int | _joint_get_solver_priority(joint: RID) virtual const  
JointType | _joint_get_type(joint: RID) virtual const  
bool | _joint_is_disabled_collisions_between_bodies(joint: RID) virtual const  
void | _joint_make_cone_twist(joint: RID, body_A: RID, local_ref_A: Transform3D, body_B: RID, local_ref_B: Transform3D) virtual  
void | _joint_make_generic_6dof(joint: RID, body_A: RID, local_ref_A: Transform3D, body_B: RID, local_ref_B: Transform3D) virtual  
void | _joint_make_hinge(joint: RID, body_A: RID, hinge_A: Transform3D, body_B: RID, hinge_B: Transform3D) virtual  
void | _joint_make_hinge_simple(joint: RID, body_A: RID, pivot_A: Vector3, axis_A: Vector3, body_B: RID, pivot_B: Vector3, axis_B: Vector3) virtual  
void | _joint_make_pin(joint: RID, body_A: RID, local_A: Vector3, body_B: RID, local_B: Vector3) virtual  
void | _joint_make_slider(joint: RID, body_A: RID, local_ref_A: Transform3D, body_B: RID, local_ref_B: Transform3D) virtual  
void | _joint_set_solver_priority(joint: RID, priority: int) virtual  
Vector3 | _pin_joint_get_local_a(joint: RID) virtual const  
Vector3 | _pin_joint_get_local_b(joint: RID) virtual const  
float | _pin_joint_get_param(joint: RID, param: PinJointParam) virtual const  
void | _pin_joint_set_local_a(joint: RID, local_A: Vector3) virtual  
void | _pin_joint_set_local_b(joint: RID, local_B: Vector3) virtual  
void | _pin_joint_set_param(joint: RID, param: PinJointParam, value: float) virtual  
RID | _separation_ray_shape_create() virtual  
void | _set_active(active: bool) virtual  
float | _shape_get_custom_solver_bias(shape: RID) virtual const  
Variant | _shape_get_data(shape: RID) virtual const  
float | _shape_get_margin(shape: RID) virtual const  
ShapeType | _shape_get_type(shape: RID) virtual const  
void | _shape_set_custom_solver_bias(shape: RID, bias: float) virtual  
void | _shape_set_data(shape: RID, data: Variant) virtual  
void | _shape_set_margin(shape: RID, margin: float) virtual  
float | _slider_joint_get_param(joint: RID, param: SliderJointParam) virtual const  
void | _slider_joint_set_param(joint: RID, param: SliderJointParam, value: float) virtual  
void | _soft_body_add_collision_exception(body: RID, body_b: RID) virtual  
RID | _soft_body_create() virtual  
AABB | _soft_body_get_bounds(body: RID) virtual const  
Array[RID] | _soft_body_get_collision_exceptions(body: RID) virtual const  
int | _soft_body_get_collision_layer(body: RID) virtual const  
int | _soft_body_get_collision_mask(body: RID) virtual const  
float | _soft_body_get_damping_coefficient(body: RID) virtual const  
float | _soft_body_get_drag_coefficient(body: RID) virtual const  
float | _soft_body_get_linear_stiffness(body: RID) virtual const  
Vector3 | _soft_body_get_point_global_position(body: RID, point_index: int) virtual const  
float | _soft_body_get_pressure_coefficient(body: RID) virtual const  
int | _soft_body_get_simulation_precision(body: RID) virtual const  
RID | _soft_body_get_space(body: RID) virtual const  
Variant | _soft_body_get_state(body: RID, state: BodyState) virtual const  
float | _soft_body_get_total_mass(body: RID) virtual const  
bool | _soft_body_is_point_pinned(body: RID, point_index: int) virtual const  
void | _soft_body_move_point(body: RID, point_index: int, global_position: Vector3) virtual  
void | _soft_body_pin_point(body: RID, point_index: int, pin: bool) virtual  
void | _soft_body_remove_all_pinned_points(body: RID) virtual  
void | _soft_body_remove_collision_exception(body: RID, body_b: RID) virtual  
void | _soft_body_set_collision_layer(body: RID, layer: int) virtual  
void | _soft_body_set_collision_mask(body: RID, mask: int) virtual  
void | _soft_body_set_damping_coefficient(body: RID, damping_coefficient: float) virtual  
void | _soft_body_set_drag_coefficient(body: RID, drag_coefficient: float) virtual  
void | _soft_body_set_linear_stiffness(body: RID, linear_stiffness: float) virtual  
void | _soft_body_set_mesh(body: RID, mesh: RID) virtual  
void | _soft_body_set_pressure_coefficient(body: RID, pressure_coefficient: float) virtual  
void | _soft_body_set_ray_pickable(body: RID, enable: bool) virtual  
void | _soft_body_set_simulation_precision(body: RID, simulation_precision: int) virtual  
void | _soft_body_set_space(body: RID, space: RID) virtual  
void | _soft_body_set_state(body: RID, state: BodyState, variant: Variant) virtual  
void | _soft_body_set_total_mass(body: RID, total_mass: float) virtual  
void | _soft_body_set_transform(body: RID, transform: Transform3D) virtual  
void | _soft_body_update_rendering_server(body: RID, rendering_server_handler: PhysicsServer3DRenderingServerHandler) virtual  
RID | _space_create() virtual  
int | _space_get_contact_count(space: RID) virtual const  
PackedVector3Array | _space_get_contacts(space: RID) virtual const  
PhysicsDirectSpaceState3D | _space_get_direct_state(space: RID) virtual  
float | _space_get_param(space: RID, param: SpaceParameter) virtual const  
bool | _space_is_active(space: RID) virtual const  
void | _space_set_active(space: RID, active: bool) virtual  
void | _space_set_debug_contacts(space: RID, max_contacts: int) virtual  
void | _space_set_param(space: RID, param: SpaceParameter, value: float) virtual  
RID | _sphere_shape_create() virtual  
void | _step(step: float) virtual  
void | _sync() virtual  
RID | _world_boundary_shape_create() virtual  
bool | body_test_motion_is_excluding_body(body: RID) const  
bool | body_test_motion_is_excluding_object(object: int) const  
  
## Method Descriptions

void _area_add_shape(area: RID, shape: RID, transform: Transform3D, disabled:
bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_attach_object_instance_id(area: RID, id: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_clear_shapes(area: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

RID _area_create() virtual

There is currently no description for this method. Please help us by
contributing one!

int _area_get_collision_layer(area: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _area_get_collision_mask(area: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _area_get_object_instance_id(area: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Variant _area_get_param(area: RID, param: AreaParameter) virtual const

There is currently no description for this method. Please help us by
contributing one!

RID _area_get_shape(area: RID, shape_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _area_get_shape_count(area: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Transform3D _area_get_shape_transform(area: RID, shape_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

RID _area_get_space(area: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Transform3D _area_get_transform(area: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

void _area_remove_shape(area: RID, shape_idx: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_set_area_monitor_callback(area: RID, callback: Callable) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_set_collision_layer(area: RID, layer: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_set_collision_mask(area: RID, mask: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_set_monitor_callback(area: RID, callback: Callable) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_set_monitorable(area: RID, monitorable: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_set_param(area: RID, param: AreaParameter, value: Variant) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_set_ray_pickable(area: RID, enable: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_set_shape(area: RID, shape_idx: int, shape: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_set_shape_disabled(area: RID, shape_idx: int, disabled: bool)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_set_shape_transform(area: RID, shape_idx: int, transform:
Transform3D) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_set_space(area: RID, space: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

void _area_set_transform(area: RID, transform: Transform3D) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_add_collision_exception(body: RID, excepted_body: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_add_constant_central_force(body: RID, force: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_add_constant_force(body: RID, force: Vector3, position: Vector3)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_add_constant_torque(body: RID, torque: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_add_shape(body: RID, shape: RID, transform: Transform3D, disabled:
bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_apply_central_force(body: RID, force: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_apply_central_impulse(body: RID, impulse: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_apply_force(body: RID, force: Vector3, position: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_apply_impulse(body: RID, impulse: Vector3, position: Vector3)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_apply_torque(body: RID, torque: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_apply_torque_impulse(body: RID, impulse: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_attach_object_instance_id(body: RID, id: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_clear_shapes(body: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

RID _body_create() virtual

There is currently no description for this method. Please help us by
contributing one!

Array[RID] _body_get_collision_exceptions(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _body_get_collision_layer(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _body_get_collision_mask(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

float _body_get_collision_priority(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _body_get_constant_force(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _body_get_constant_torque(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

float _body_get_contacts_reported_depth_threshold(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

PhysicsDirectBodyState3D _body_get_direct_state(body: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

int _body_get_max_contacts_reported(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

BodyMode _body_get_mode(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _body_get_object_instance_id(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Variant _body_get_param(body: RID, param: BodyParameter) virtual const

There is currently no description for this method. Please help us by
contributing one!

RID _body_get_shape(body: RID, shape_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _body_get_shape_count(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Transform3D _body_get_shape_transform(body: RID, shape_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

RID _body_get_space(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Variant _body_get_state(body: RID, state: BodyState) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _body_get_user_flags(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _body_is_axis_locked(body: RID, axis: BodyAxis) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _body_is_continuous_collision_detection_enabled(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _body_is_omitting_force_integration(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

void _body_remove_collision_exception(body: RID, excepted_body: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_remove_shape(body: RID, shape_idx: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_reset_mass_properties(body: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_axis_lock(body: RID, axis: BodyAxis, lock: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_axis_velocity(body: RID, axis_velocity: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_collision_layer(body: RID, layer: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_collision_mask(body: RID, mask: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_collision_priority(body: RID, priority: float) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_constant_force(body: RID, force: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_constant_torque(body: RID, torque: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_contacts_reported_depth_threshold(body: RID, threshold: float)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_enable_continuous_collision_detection(body: RID, enable: bool)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_force_integration_callback(body: RID, callable: Callable,
userdata: Variant) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_max_contacts_reported(body: RID, amount: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_mode(body: RID, mode: BodyMode) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_omit_force_integration(body: RID, enable: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_param(body: RID, param: BodyParameter, value: Variant) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_ray_pickable(body: RID, enable: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_shape(body: RID, shape_idx: int, shape: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_shape_disabled(body: RID, shape_idx: int, disabled: bool)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_shape_transform(body: RID, shape_idx: int, transform:
Transform3D) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_space(body: RID, space: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_state(body: RID, state: BodyState, value: Variant) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_state_sync_callback(body: RID, callable: Callable) virtual

There is currently no description for this method. Please help us by
contributing one!

void _body_set_user_flags(body: RID, flags: int) virtual

There is currently no description for this method. Please help us by
contributing one!

bool _body_test_motion(body: RID, from: Transform3D, motion: Vector3, margin:
float, max_collisions: int, collide_separation_ray: bool,
recovery_as_collision: bool, result: `PhysicsServer3DExtensionMotionResult*`)
virtual const

There is currently no description for this method. Please help us by
contributing one!

RID _box_shape_create() virtual

There is currently no description for this method. Please help us by
contributing one!

RID _capsule_shape_create() virtual

There is currently no description for this method. Please help us by
contributing one!

RID _concave_polygon_shape_create() virtual

There is currently no description for this method. Please help us by
contributing one!

float _cone_twist_joint_get_param(joint: RID, param: ConeTwistJointParam)
virtual const

There is currently no description for this method. Please help us by
contributing one!

void _cone_twist_joint_set_param(joint: RID, param: ConeTwistJointParam,
value: float) virtual

There is currently no description for this method. Please help us by
contributing one!

RID _convex_polygon_shape_create() virtual

There is currently no description for this method. Please help us by
contributing one!

RID _custom_shape_create() virtual

There is currently no description for this method. Please help us by
contributing one!

RID _cylinder_shape_create() virtual

There is currently no description for this method. Please help us by
contributing one!

void _end_sync() virtual

There is currently no description for this method. Please help us by
contributing one!

void _finish() virtual

There is currently no description for this method. Please help us by
contributing one!

void _flush_queries() virtual

There is currently no description for this method. Please help us by
contributing one!

void _free_rid(rid: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

bool _generic_6dof_joint_get_flag(joint: RID, axis: Axis, flag:
G6DOFJointAxisFlag) virtual const

There is currently no description for this method. Please help us by
contributing one!

float _generic_6dof_joint_get_param(joint: RID, axis: Axis, param:
G6DOFJointAxisParam) virtual const

There is currently no description for this method. Please help us by
contributing one!

void _generic_6dof_joint_set_flag(joint: RID, axis: Axis, flag:
G6DOFJointAxisFlag, enable: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _generic_6dof_joint_set_param(joint: RID, axis: Axis, param:
G6DOFJointAxisParam, value: float) virtual

There is currently no description for this method. Please help us by
contributing one!

int _get_process_info(process_info: ProcessInfo) virtual

There is currently no description for this method. Please help us by
contributing one!

RID _heightmap_shape_create() virtual

There is currently no description for this method. Please help us by
contributing one!

bool _hinge_joint_get_flag(joint: RID, flag: HingeJointFlag) virtual const

There is currently no description for this method. Please help us by
contributing one!

float _hinge_joint_get_param(joint: RID, param: HingeJointParam) virtual const

There is currently no description for this method. Please help us by
contributing one!

void _hinge_joint_set_flag(joint: RID, flag: HingeJointFlag, enabled: bool)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _hinge_joint_set_param(joint: RID, param: HingeJointParam, value: float)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _init() virtual

There is currently no description for this method. Please help us by
contributing one!

bool _is_flushing_queries() virtual const

There is currently no description for this method. Please help us by
contributing one!

void _joint_clear(joint: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

RID _joint_create() virtual

There is currently no description for this method. Please help us by
contributing one!

void _joint_disable_collisions_between_bodies(joint: RID, disable: bool)
virtual

There is currently no description for this method. Please help us by
contributing one!

int _joint_get_solver_priority(joint: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

JointType _joint_get_type(joint: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _joint_is_disabled_collisions_between_bodies(joint: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

void _joint_make_cone_twist(joint: RID, body_A: RID, local_ref_A: Transform3D,
body_B: RID, local_ref_B: Transform3D) virtual

There is currently no description for this method. Please help us by
contributing one!

void _joint_make_generic_6dof(joint: RID, body_A: RID, local_ref_A:
Transform3D, body_B: RID, local_ref_B: Transform3D) virtual

There is currently no description for this method. Please help us by
contributing one!

void _joint_make_hinge(joint: RID, body_A: RID, hinge_A: Transform3D, body_B:
RID, hinge_B: Transform3D) virtual

There is currently no description for this method. Please help us by
contributing one!

void _joint_make_hinge_simple(joint: RID, body_A: RID, pivot_A: Vector3,
axis_A: Vector3, body_B: RID, pivot_B: Vector3, axis_B: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _joint_make_pin(joint: RID, body_A: RID, local_A: Vector3, body_B: RID,
local_B: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _joint_make_slider(joint: RID, body_A: RID, local_ref_A: Transform3D,
body_B: RID, local_ref_B: Transform3D) virtual

There is currently no description for this method. Please help us by
contributing one!

void _joint_set_solver_priority(joint: RID, priority: int) virtual

There is currently no description for this method. Please help us by
contributing one!

Vector3 _pin_joint_get_local_a(joint: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _pin_joint_get_local_b(joint: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

float _pin_joint_get_param(joint: RID, param: PinJointParam) virtual const

There is currently no description for this method. Please help us by
contributing one!

void _pin_joint_set_local_a(joint: RID, local_A: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _pin_joint_set_local_b(joint: RID, local_B: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _pin_joint_set_param(joint: RID, param: PinJointParam, value: float)
virtual

There is currently no description for this method. Please help us by
contributing one!

RID _separation_ray_shape_create() virtual

There is currently no description for this method. Please help us by
contributing one!

void _set_active(active: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

float _shape_get_custom_solver_bias(shape: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Variant _shape_get_data(shape: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

float _shape_get_margin(shape: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

ShapeType _shape_get_type(shape: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

void _shape_set_custom_solver_bias(shape: RID, bias: float) virtual

There is currently no description for this method. Please help us by
contributing one!

void _shape_set_data(shape: RID, data: Variant) virtual

There is currently no description for this method. Please help us by
contributing one!

void _shape_set_margin(shape: RID, margin: float) virtual

There is currently no description for this method. Please help us by
contributing one!

float _slider_joint_get_param(joint: RID, param: SliderJointParam) virtual
const

There is currently no description for this method. Please help us by
contributing one!

void _slider_joint_set_param(joint: RID, param: SliderJointParam, value:
float) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_add_collision_exception(body: RID, body_b: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

RID _soft_body_create() virtual

There is currently no description for this method. Please help us by
contributing one!

AABB _soft_body_get_bounds(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Array[RID] _soft_body_get_collision_exceptions(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _soft_body_get_collision_layer(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _soft_body_get_collision_mask(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

float _soft_body_get_damping_coefficient(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

float _soft_body_get_drag_coefficient(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

float _soft_body_get_linear_stiffness(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _soft_body_get_point_global_position(body: RID, point_index: int)
virtual const

There is currently no description for this method. Please help us by
contributing one!

float _soft_body_get_pressure_coefficient(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _soft_body_get_simulation_precision(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

RID _soft_body_get_space(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

Variant _soft_body_get_state(body: RID, state: BodyState) virtual const

There is currently no description for this method. Please help us by
contributing one!

float _soft_body_get_total_mass(body: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _soft_body_is_point_pinned(body: RID, point_index: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_move_point(body: RID, point_index: int, global_position:
Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_pin_point(body: RID, point_index: int, pin: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_remove_all_pinned_points(body: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_remove_collision_exception(body: RID, body_b: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_collision_layer(body: RID, layer: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_collision_mask(body: RID, mask: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_damping_coefficient(body: RID, damping_coefficient: float)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_drag_coefficient(body: RID, drag_coefficient: float)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_linear_stiffness(body: RID, linear_stiffness: float)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_mesh(body: RID, mesh: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_pressure_coefficient(body: RID, pressure_coefficient:
float) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_ray_pickable(body: RID, enable: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_simulation_precision(body: RID, simulation_precision: int)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_space(body: RID, space: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_state(body: RID, state: BodyState, variant: Variant)
virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_total_mass(body: RID, total_mass: float) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_set_transform(body: RID, transform: Transform3D) virtual

There is currently no description for this method. Please help us by
contributing one!

void _soft_body_update_rendering_server(body: RID, rendering_server_handler:
PhysicsServer3DRenderingServerHandler) virtual

There is currently no description for this method. Please help us by
contributing one!

RID _space_create() virtual

There is currently no description for this method. Please help us by
contributing one!

int _space_get_contact_count(space: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

PackedVector3Array _space_get_contacts(space: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

PhysicsDirectSpaceState3D _space_get_direct_state(space: RID) virtual

There is currently no description for this method. Please help us by
contributing one!

float _space_get_param(space: RID, param: SpaceParameter) virtual const

There is currently no description for this method. Please help us by
contributing one!

bool _space_is_active(space: RID) virtual const

There is currently no description for this method. Please help us by
contributing one!

void _space_set_active(space: RID, active: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _space_set_debug_contacts(space: RID, max_contacts: int) virtual

There is currently no description for this method. Please help us by
contributing one!

void _space_set_param(space: RID, param: SpaceParameter, value: float) virtual

There is currently no description for this method. Please help us by
contributing one!

RID _sphere_shape_create() virtual

There is currently no description for this method. Please help us by
contributing one!

void _step(step: float) virtual

There is currently no description for this method. Please help us by
contributing one!

void _sync() virtual

There is currently no description for this method. Please help us by
contributing one!

RID _world_boundary_shape_create() virtual

There is currently no description for this method. Please help us by
contributing one!

bool body_test_motion_is_excluding_body(body: RID) const

There is currently no description for this method. Please help us by
contributing one!

bool body_test_motion_is_excluding_object(object: int) const

There is currently no description for this method. Please help us by
contributing one!

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

