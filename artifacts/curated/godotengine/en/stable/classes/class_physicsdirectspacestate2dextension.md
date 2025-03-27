# PhysicsDirectSpaceState2DExtension

Inherits: PhysicsDirectSpaceState2D < Object

Provides virtual methods that can be overridden to create custom
PhysicsDirectSpaceState2D implementations.

## Description

This class extends PhysicsDirectSpaceState2D by providing additional virtual
methods that can be overridden. When these methods are overridden, they will
be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of
PhysicsDirectSpaceState2D.

## Methods

bool | _cast_motion(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, closest_safe: `float*`, closest_unsafe: `float*`) virtual  
---|---  
bool | _collide_shape(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, results: `void*`, max_results: int, result_count: `int32_t*`) virtual  
int | _intersect_point(position: Vector2, canvas_instance_id: int, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, results: `PhysicsServer2DExtensionShapeResult*`, max_results: int) virtual  
bool | _intersect_ray(from: Vector2, to: Vector2, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, hit_from_inside: bool, result: `PhysicsServer2DExtensionRayResult*`) virtual  
int | _intersect_shape(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, result: `PhysicsServer2DExtensionShapeResult*`, max_results: int) virtual  
bool | _rest_info(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, rest_info: `PhysicsServer2DExtensionShapeRestInfo*`) virtual  
bool | is_body_excluded_from_query(body: RID) const  
  
## Method Descriptions

bool _cast_motion(shape_rid: RID, transform: Transform2D, motion: Vector2,
margin: float, collision_mask: int, collide_with_bodies: bool,
collide_with_areas: bool, closest_safe: `float*`, closest_unsafe: `float*`)
virtual

There is currently no description for this method. Please help us by
contributing one!

bool _collide_shape(shape_rid: RID, transform: Transform2D, motion: Vector2,
margin: float, collision_mask: int, collide_with_bodies: bool,
collide_with_areas: bool, results: `void*`, max_results: int, result_count:
`int32_t*`) virtual

There is currently no description for this method. Please help us by
contributing one!

int _intersect_point(position: Vector2, canvas_instance_id: int,
collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool,
results: `PhysicsServer2DExtensionShapeResult*`, max_results: int) virtual

There is currently no description for this method. Please help us by
contributing one!

bool _intersect_ray(from: Vector2, to: Vector2, collision_mask: int,
collide_with_bodies: bool, collide_with_areas: bool, hit_from_inside: bool,
result: `PhysicsServer2DExtensionRayResult*`) virtual

There is currently no description for this method. Please help us by
contributing one!

int _intersect_shape(shape_rid: RID, transform: Transform2D, motion: Vector2,
margin: float, collision_mask: int, collide_with_bodies: bool,
collide_with_areas: bool, result: `PhysicsServer2DExtensionShapeResult*`,
max_results: int) virtual

There is currently no description for this method. Please help us by
contributing one!

bool _rest_info(shape_rid: RID, transform: Transform2D, motion: Vector2,
margin: float, collision_mask: int, collide_with_bodies: bool,
collide_with_areas: bool, rest_info: `PhysicsServer2DExtensionShapeRestInfo*`)
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

