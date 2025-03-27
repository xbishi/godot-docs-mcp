# SkeletonModification2DStackHolder

Experimental: This class may be changed or removed in future versions.

Inherits: SkeletonModification2D < Resource < RefCounted < Object

A modification that holds and executes a SkeletonModificationStack2D.

## Description

This SkeletonModification2D holds a reference to a
SkeletonModificationStack2D, allowing you to use multiple modification stacks
on a single Skeleton2D.

Note: The modifications in the held SkeletonModificationStack2D will only be
executed if their execution mode matches the execution mode of the
SkeletonModification2DStackHolder.

## Methods

SkeletonModificationStack2D | get_held_modification_stack() const  
---|---  
void | set_held_modification_stack(held_modification_stack: SkeletonModificationStack2D)  
  
## Method Descriptions

SkeletonModificationStack2D get_held_modification_stack() const

Returns the SkeletonModificationStack2D that this modification is holding.

void set_held_modification_stack(held_modification_stack:
SkeletonModificationStack2D)

Sets the SkeletonModificationStack2D that this modification is holding. This
modification stack will then be executed when this modification is executed.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[const]: This method has no side effects. It doesn't modify any of the instance's member variables.
  *[void]: No return value.

