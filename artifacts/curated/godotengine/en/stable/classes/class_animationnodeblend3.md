# AnimationNodeBlend3

Inherits: AnimationNodeSync < AnimationNode < Resource < RefCounted < Object

Blends two of three animations linearly inside of an AnimationNodeBlendTree.

## Description

A resource to add to an AnimationNodeBlendTree. Blends two animations out of
three linearly out of three based on the amount value.

This animation node has three inputs:

  * The base animation to blend with

  * A "-blend" animation to blend with when the blend amount is negative value

  * A "+blend" animation to blend with when the blend amount is positive value

In general, the blend value should be in the `[-1.0, 1.0]` range. Values
outside of this range can blend amplified animations, however,
AnimationNodeAdd3 works better for this purpose.

## Tutorials

  * Using AnimationTree

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

