# PhysicsDirectSpaceState3DExtension

Inherits: PhysicsDirectSpaceState3D < Object

Provides virtual methods that can be overridden to create custom
PhysicsDirectSpaceState3D implementations.

## Description

This class extends PhysicsDirectSpaceState3D by providing additional virtual
methods that can be overridden. When these methods are overridden, they will
be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of
PhysicsDirectSpaceState3D.

## Methods

bool | _cast_motion(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, closest_safe: `float*`, closest_unsafe: `float*`, info: `PhysicsServer3DExtensionShapeRestInfo*`) virtual  
---|---  
bool | _collide_shape(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, results: `void*`, max_results: int, result_count: `int32_t*`) virtual  
Vector3 | _get_closest_point_to_object_volume(object: RID, point: Vector3) virtual const  
int | _intersect_point(position: Vector3, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, results: `PhysicsServer3DExtensionShapeResult*`, max_results: int) virtual  
bool | _intersect_ray(from: Vector3, to: Vector3, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, hit_from_inside: bool, hit_back_faces: bool, pick_ray: bool, result: `PhysicsServer3DExtensionRayResult*`) virtual  
int | _intersect_shape(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, result_count: `PhysicsServer3DExtensionShapeResult*`, max_results: int) virtual  
bool | _rest_info(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, rest_info: `PhysicsServer3DExtensionShapeRestInfo*`) virtual  
bool | is_body_excluded_from_query(body: RID) const  
  
## Method Descriptions

bool _cast_motion(shape_rid: RID, transform: Transform3D, motion: Vector3,
margin: float, collision_mask: int, collide_with_bodies: bool,
collide_with_areas: bool, closest_safe: `float*`, closest_unsafe: `float*`,
info: `PhysicsServer3DExtensionShapeRestInfo*`) virtual

There is currently no description for this method. Please help us by
contributing one!

bool _collide_shape(shape_rid: RID, transform: Transform3D, motion: Vector3,
margin: float, collision_mask: int, collide_with_bodies: bool,
collide_with_areas: bool, results: `void*`, max_results: int, result_count:
`int32_t*`) virtual

There is currently no description for this method. Please help us by
contributing one!

Vector3 _get_closest_point_to_object_volume(object: RID, point: Vector3)
virtual const

There is currently no description for this method. Please help us by
contributing one!

int _intersect_point(position: Vector3, collision_mask: int,
collide_with_bodies: bool, collide_with_areas: bool, results:
`PhysicsServer3DExtensionShapeResult*`, max_results: int) virtual

There is currently no description for this method. Please help us by
contributing one!

bool _intersect_ray(from: Vector3, to: Vector3, collision_mask: int,
collide_with_bodies: bool, collide_with_areas: bool, hit_from_inside: bool,
hit_back_faces: bool, pick_ray: bool, result:
`PhysicsServer3DExtensionRayResult*`) virtual

There is currently no description for this method. Please help us by
contributing one!

int _intersect_shape(shape_rid: RID, transform: Transform3D, motion: Vector3,
margin: float, collision_mask: int, collide_with_bodies: bool,
collide_with_areas: bool, result_count:
`PhysicsServer3DExtensionShapeResult*`, max_results: int) virtual

There is currently no description for this method. Please help us by
contributing one!

bool _rest_info(shape_rid: RID, transform: Transform3D, motion: Vector3,
margin: float, collision_mask: int, collide_with_bodies: bool,
collide_with_areas: bool, rest_info: `PhysicsServer3DExtensionShapeRestInfo*`)
virtual

There is currently no description for this method. Please help us by
contributing one!

bool is_body_excluded_from_query(body: RID) const

There is currently no description for this method. Please help us by
contributing one!

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[virtual]: This method should typically be overridden by the user to have any effect.
  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.

