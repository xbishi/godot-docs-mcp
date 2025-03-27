# PhysicsDirectBodyState2DExtension

Inherits: PhysicsDirectBodyState2D < Object

Provides virtual methods that can be overridden to create custom
PhysicsDirectBodyState2D implementations.

## Description

This class extends PhysicsDirectBodyState2D by providing additional virtual
methods that can be overridden. When these methods are overridden, they will
be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of
PhysicsDirectBodyState2D.

## Methods

void | _add_constant_central_force(force: Vector2) virtual  
---|---  
void | _add_constant_force(force: Vector2, position: Vector2) virtual  
void | _add_constant_torque(torque: float) virtual  
void | _apply_central_force(force: Vector2) virtual  
void | _apply_central_impulse(impulse: Vector2) virtual  
void | _apply_force(force: Vector2, position: Vector2) virtual  
void | _apply_impulse(impulse: Vector2, position: Vector2) virtual  
void | _apply_torque(torque: float) virtual  
void | _apply_torque_impulse(impulse: float) virtual  
float | _get_angular_velocity() virtual const  
Vector2 | _get_center_of_mass() virtual const  
Vector2 | _get_center_of_mass_local() virtual const  
Vector2 | _get_constant_force() virtual const  
float | _get_constant_torque() virtual const  
RID | _get_contact_collider(contact_idx: int) virtual const  
int | _get_contact_collider_id(contact_idx: int) virtual const  
Object | _get_contact_collider_object(contact_idx: int) virtual const  
Vector2 | _get_contact_collider_position(contact_idx: int) virtual const  
int | _get_contact_collider_shape(contact_idx: int) virtual const  
Vector2 | _get_contact_collider_velocity_at_position(contact_idx: int) virtual const  
int | _get_contact_count() virtual const  
Vector2 | _get_contact_impulse(contact_idx: int) virtual const  
Vector2 | _get_contact_local_normal(contact_idx: int) virtual const  
Vector2 | _get_contact_local_position(contact_idx: int) virtual const  
int | _get_contact_local_shape(contact_idx: int) virtual const  
Vector2 | _get_contact_local_velocity_at_position(contact_idx: int) virtual const  
float | _get_inverse_inertia() virtual const  
float | _get_inverse_mass() virtual const  
Vector2 | _get_linear_velocity() virtual const  
PhysicsDirectSpaceState2D | _get_space_state() virtual  
float | _get_step() virtual const  
float | _get_total_angular_damp() virtual const  
Vector2 | _get_total_gravity() virtual const  
float | _get_total_linear_damp() virtual const  
Transform2D | _get_transform() virtual const  
Vector2 | _get_velocity_at_local_position(local_position: Vector2) virtual const  
void | _integrate_forces() virtual  
bool | _is_sleeping() virtual const  
void | _set_angular_velocity(velocity: float) virtual  
void | _set_constant_force(force: Vector2) virtual  
void | _set_constant_torque(torque: float) virtual  
void | _set_linear_velocity(velocity: Vector2) virtual  
void | _set_sleep_state(enabled: bool) virtual  
void | _set_transform(transform: Transform2D) virtual  
  
## Method Descriptions

void _add_constant_central_force(force: Vector2) virtual

Overridable version of PhysicsDirectBodyState2D.add_constant_central_force().

void _add_constant_force(force: Vector2, position: Vector2) virtual

Overridable version of PhysicsDirectBodyState2D.add_constant_force().

void _add_constant_torque(torque: float) virtual

Overridable version of PhysicsDirectBodyState2D.add_constant_torque().

void _apply_central_force(force: Vector2) virtual

Overridable version of PhysicsDirectBodyState2D.apply_central_force().

void _apply_central_impulse(impulse: Vector2) virtual

Overridable version of PhysicsDirectBodyState2D.apply_central_impulse().

void _apply_force(force: Vector2, position: Vector2) virtual

Overridable version of PhysicsDirectBodyState2D.apply_force().

void _apply_impulse(impulse: Vector2, position: Vector2) virtual

Overridable version of PhysicsDirectBodyState2D.apply_impulse().

void _apply_torque(torque: float) virtual

Overridable version of PhysicsDirectBodyState2D.apply_torque().

void _apply_torque_impulse(impulse: float) virtual

Overridable version of PhysicsDirectBodyState2D.apply_torque_impulse().

float _get_angular_velocity() virtual const

Implement to override the behavior of
PhysicsDirectBodyState2D.angular_velocity and its respective getter.

Vector2 _get_center_of_mass() virtual const

Implement to override the behavior of PhysicsDirectBodyState2D.center_of_mass
and its respective getter.

Vector2 _get_center_of_mass_local() virtual const

Implement to override the behavior of
PhysicsDirectBodyState2D.center_of_mass_local and its respective getter.

Vector2 _get_constant_force() virtual const

Overridable version of PhysicsDirectBodyState2D.get_constant_force().

float _get_constant_torque() virtual const

Overridable version of PhysicsDirectBodyState2D.get_constant_torque().

RID _get_contact_collider(contact_idx: int) virtual const

Overridable version of PhysicsDirectBodyState2D.get_contact_collider().

int _get_contact_collider_id(contact_idx: int) virtual const

Overridable version of PhysicsDirectBodyState2D.get_contact_collider_id().

Object _get_contact_collider_object(contact_idx: int) virtual const

Overridable version of PhysicsDirectBodyState2D.get_contact_collider_object().

Vector2 _get_contact_collider_position(contact_idx: int) virtual const

Overridable version of
PhysicsDirectBodyState2D.get_contact_collider_position().

int _get_contact_collider_shape(contact_idx: int) virtual const

Overridable version of PhysicsDirectBodyState2D.get_contact_collider_shape().

Vector2 _get_contact_collider_velocity_at_position(contact_idx: int) virtual
const

Overridable version of
PhysicsDirectBodyState2D.get_contact_collider_velocity_at_position().

int _get_contact_count() virtual const

Overridable version of PhysicsDirectBodyState2D.get_contact_count().

Vector2 _get_contact_impulse(contact_idx: int) virtual const

Overridable version of PhysicsDirectBodyState2D.get_contact_impulse().

Vector2 _get_contact_local_normal(contact_idx: int) virtual const

Overridable version of PhysicsDirectBodyState2D.get_contact_local_normal().

Vector2 _get_contact_local_position(contact_idx: int) virtual const

Overridable version of PhysicsDirectBodyState2D.get_contact_local_position().

int _get_contact_local_shape(contact_idx: int) virtual const

Overridable version of PhysicsDirectBodyState2D.get_contact_local_shape().

Vector2 _get_contact_local_velocity_at_position(contact_idx: int) virtual
const

Overridable version of
PhysicsDirectBodyState2D.get_contact_local_velocity_at_position().

float _get_inverse_inertia() virtual const

Implement to override the behavior of PhysicsDirectBodyState2D.inverse_inertia
and its respective getter.

float _get_inverse_mass() virtual const

Implement to override the behavior of PhysicsDirectBodyState2D.inverse_mass
and its respective getter.

Vector2 _get_linear_velocity() virtual const

Implement to override the behavior of PhysicsDirectBodyState2D.linear_velocity
and its respective getter.

PhysicsDirectSpaceState2D _get_space_state() virtual

Overridable version of PhysicsDirectBodyState2D.get_space_state().

float _get_step() virtual const

Implement to override the behavior of PhysicsDirectBodyState2D.step and its
respective getter.

float _get_total_angular_damp() virtual const

Implement to override the behavior of
PhysicsDirectBodyState2D.total_angular_damp and its respective getter.

Vector2 _get_total_gravity() virtual const

Implement to override the behavior of PhysicsDirectBodyState2D.total_gravity
and its respective getter.

float _get_total_linear_damp() virtual const

Implement to override the behavior of
PhysicsDirectBodyState2D.total_linear_damp and its respective getter.

Transform2D _get_transform() virtual const

Implement to override the behavior of PhysicsDirectBodyState2D.transform and
its respective getter.

Vector2 _get_velocity_at_local_position(local_position: Vector2) virtual const

Overridable version of
PhysicsDirectBodyState2D.get_velocity_at_local_position().

void _integrate_forces() virtual

Overridable version of PhysicsDirectBodyState2D.integrate_forces().

bool _is_sleeping() virtual const

Implement to override the behavior of PhysicsDirectBodyState2D.sleeping and
its respective getter.

void _set_angular_velocity(velocity: float) virtual

Implement to override the behavior of
PhysicsDirectBodyState2D.angular_velocity and its respective setter.

void _set_constant_force(force: Vector2) virtual

Overridable version of PhysicsDirectBodyState2D.set_constant_force().

void _set_constant_torque(torque: float) virtual

Overridable version of PhysicsDirectBodyState2D.set_constant_torque().

void _set_linear_velocity(velocity: Vector2) virtual

Implement to override the behavior of PhysicsDirectBodyState2D.linear_velocity
and its respective setter.

void _set_sleep_state(enabled: bool) virtual

Implement to override the behavior of PhysicsDirectBodyState2D.sleeping and
its respective setter.

void _set_transform(transform: Transform2D) virtual

Implement to override the behavior of PhysicsDirectBodyState2D.transform and
its respective setter.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

