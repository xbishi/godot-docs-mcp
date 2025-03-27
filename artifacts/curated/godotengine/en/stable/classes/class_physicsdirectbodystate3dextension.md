# PhysicsDirectBodyState3DExtension

Inherits: PhysicsDirectBodyState3D < Object

Provides virtual methods that can be overridden to create custom
PhysicsDirectBodyState3D implementations.

## Description

This class extends PhysicsDirectBodyState3D by providing additional virtual
methods that can be overridden. When these methods are overridden, they will
be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of
PhysicsDirectBodyState3D.

## Methods

void | _add_constant_central_force(force: Vector3) virtual  
---|---  
void | _add_constant_force(force: Vector3, position: Vector3) virtual  
void | _add_constant_torque(torque: Vector3) virtual  
void | _apply_central_force(force: Vector3) virtual  
void | _apply_central_impulse(impulse: Vector3) virtual  
void | _apply_force(force: Vector3, position: Vector3) virtual  
void | _apply_impulse(impulse: Vector3, position: Vector3) virtual  
void | _apply_torque(torque: Vector3) virtual  
void | _apply_torque_impulse(impulse: Vector3) virtual  
Vector3 | _get_angular_velocity() virtual const  
Vector3 | _get_center_of_mass() virtual const  
Vector3 | _get_center_of_mass_local() virtual const  
Vector3 | _get_constant_force() virtual const  
Vector3 | _get_constant_torque() virtual const  
RID | _get_contact_collider(contact_idx: int) virtual const  
int | _get_contact_collider_id(contact_idx: int) virtual const  
Object | _get_contact_collider_object(contact_idx: int) virtual const  
Vector3 | _get_contact_collider_position(contact_idx: int) virtual const  
int | _get_contact_collider_shape(contact_idx: int) virtual const  
Vector3 | _get_contact_collider_velocity_at_position(contact_idx: int) virtual const  
int | _get_contact_count() virtual const  
Vector3 | _get_contact_impulse(contact_idx: int) virtual const  
Vector3 | _get_contact_local_normal(contact_idx: int) virtual const  
Vector3 | _get_contact_local_position(contact_idx: int) virtual const  
int | _get_contact_local_shape(contact_idx: int) virtual const  
Vector3 | _get_contact_local_velocity_at_position(contact_idx: int) virtual const  
Vector3 | _get_inverse_inertia() virtual const  
Basis | _get_inverse_inertia_tensor() virtual const  
float | _get_inverse_mass() virtual const  
Vector3 | _get_linear_velocity() virtual const  
Basis | _get_principal_inertia_axes() virtual const  
PhysicsDirectSpaceState3D | _get_space_state() virtual  
float | _get_step() virtual const  
float | _get_total_angular_damp() virtual const  
Vector3 | _get_total_gravity() virtual const  
float | _get_total_linear_damp() virtual const  
Transform3D | _get_transform() virtual const  
Vector3 | _get_velocity_at_local_position(local_position: Vector3) virtual const  
void | _integrate_forces() virtual  
bool | _is_sleeping() virtual const  
void | _set_angular_velocity(velocity: Vector3) virtual  
void | _set_constant_force(force: Vector3) virtual  
void | _set_constant_torque(torque: Vector3) virtual  
void | _set_linear_velocity(velocity: Vector3) virtual  
void | _set_sleep_state(enabled: bool) virtual  
void | _set_transform(transform: Transform3D) virtual  
  
## Method Descriptions

void _add_constant_central_force(force: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _add_constant_force(force: Vector3, position: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _add_constant_torque(torque: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _apply_central_force(force: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _apply_central_impulse(impulse: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _apply_force(force: Vector3, position: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _apply_impulse(impulse: Vector3, position: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _apply_torque(torque: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _apply_torque_impulse(impulse: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_angular_velocity() virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_center_of_mass() virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_center_of_mass_local() virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_constant_force() virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_constant_torque() virtual const

There is currently no description for this method. Please help us by
contributing one!

RID _get_contact_collider(contact_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _get_contact_collider_id(contact_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

Object _get_contact_collider_object(contact_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_contact_collider_position(contact_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _get_contact_collider_shape(contact_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_contact_collider_velocity_at_position(contact_idx: int) virtual
const

There is currently no description for this method. Please help us by
contributing one!

int _get_contact_count() virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_contact_impulse(contact_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_contact_local_normal(contact_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_contact_local_position(contact_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

int _get_contact_local_shape(contact_idx: int) virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_contact_local_velocity_at_position(contact_idx: int) virtual
const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_inverse_inertia() virtual const

There is currently no description for this method. Please help us by
contributing one!

Basis _get_inverse_inertia_tensor() virtual const

There is currently no description for this method. Please help us by
contributing one!

float _get_inverse_mass() virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_linear_velocity() virtual const

There is currently no description for this method. Please help us by
contributing one!

Basis _get_principal_inertia_axes() virtual const

There is currently no description for this method. Please help us by
contributing one!

PhysicsDirectSpaceState3D _get_space_state() virtual

There is currently no description for this method. Please help us by
contributing one!

float _get_step() virtual const

There is currently no description for this method. Please help us by
contributing one!

float _get_total_angular_damp() virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_total_gravity() virtual const

There is currently no description for this method. Please help us by
contributing one!

float _get_total_linear_damp() virtual const

There is currently no description for this method. Please help us by
contributing one!

Transform3D _get_transform() virtual const

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_velocity_at_local_position(local_position: Vector3) virtual const

There is currently no description for this method. Please help us by
contributing one!

void _integrate_forces() virtual

There is currently no description for this method. Please help us by
contributing one!

bool _is_sleeping() virtual const

There is currently no description for this method. Please help us by
contributing one!

void _set_angular_velocity(velocity: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _set_constant_force(force: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _set_constant_torque(torque: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _set_linear_velocity(velocity: Vector3) virtual

There is currently no description for this method. Please help us by
contributing one!

void _set_sleep_state(enabled: bool) virtual

There is currently no description for this method. Please help us by
contributing one!

void _set_transform(transform: Transform3D) virtual

There is currently no description for this method. Please help us by
contributing one!

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.
  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

