# Using NavigationRegions

NavigationRegions are the visual Node representation of a region of the
navigation map on the NavigationServer. Each NavigationRegion node holds a
resource for the navigation mesh data.

Both 2D and 3D version are available as NavigationRegion2D and
NavigationRegion3D respectively.

Individual NavigationRegions upload their 2D NavigationPolygon or 3D
NavigationMesh resource data to the NavigationServer. The NavigationServer map
turns this information into a combined navigation map for pathfinding.

To create a navigation region using the scene tree add a `NavigationRegion2D`
or `NavigationRegion3D` node to the scene. All regions require a navigation
mesh resource to function. See Using navigation meshes to learn how to create
and apply navigation meshes.

NavigationRegions will automatically push `global_transform` changes to the
region on the NavigationServer which makes them suitable for moving platforms.
The NavigationServer will attempt to connect the navigation meshes of
individual regions when they are close enough. For more details see Connecting
navigation meshes. To connect NavigationRegions over arbitrary distances see
Using NavigationLinks to learn how to create and use `NavigationLinks`.

Warning

While changing the transform of a NavigationRegion node does update the region
position on the NavigationServer, changing the scale does not. A navigation
mesh resource has no scale and needs to be fully updated when source geometry
changes scale.

Regions can be enabled / disabled and if disabled will not contribute to
future pathfinding queries.

Note

Existing paths will not be automatically updated when a region gets enabled /
disabled.

## Creating new navigation regions

New NavigationRegion nodes will automatically register to the default world
navigation map for their 2D/3D dimension.

The region RID can then be obtained from NavigationRegion Nodes with
`get_rid()`.

2D GDScript2D C#3D GDScript3D C#

    
    
    extends NavigationRegion2D
    
    var navigationserver_region_rid: RID = get_rid()
    
    
    
    public partial class MyNavigationRegion2D : NavigationRegion2D
    {
        public override void _Ready()
        {
            Rid navigationServerRegionRid = GetRid();
        }
    }
    
    
    
    extends NavigationRegion3D
    
    var navigationserver_region_rid: RID = get_rid()
    
    
    
    public partial class MyNavigationRegion3D : NavigationRegion3D
    {
        public override void _Ready()
        {
            Rid navigationServerRegionRid = GetRid();
        }
    }
    

New regions can also be created with the NavigationServer API and added to any
existing map.

If regions are created with the NavigationServer API directly they need to be
assigned a navigation map manually.

2D GDScript2D C#3D GDScript3D C#

    
    
    extends Node2D
    
    func _ready() -> void:
        var new_region_rid: RID = NavigationServer2D.region_create()
        var default_map_rid: RID = get_world_2d().get_navigation_map()
        NavigationServer2D.region_set_map(new_region_rid, default_map_rid)
    
    
    
    public partial class MyNode2D : Node2D
    {
        public override void _Ready()
        {
            Rid newRegionRid = NavigationServer2D.RegionCreate();
            Rid defaultMapRid = GetWorld2D().NavigationMap;
            NavigationServer2D.RegionSetMap(newRegionRid, defaultMapRid);
        }
    }
    
    
    
    extends Node3D
    
    func _ready() -> void:
        var new_region_rid: RID = NavigationServer3D.region_create()
        var default_map_rid: RID = get_world_3d().get_navigation_map()
        NavigationServer3D.region_set_map(new_region_rid, default_map_rid)
    
    
    
    public partial class MyNode3D : Node3D
    {
        public override void _Ready()
        {
            Rid newRegionRid = NavigationServer3D.RegionCreate();
            Rid defaultMapRid = GetWorld3D().NavigationMap;
            NavigationServer3D.RegionSetMap(newRegionRid, defaultMapRid);
        }
    }
    

Note

Navigation regions can only be assigned to a single navigation map. If an
existing region is assigned to a new navigation map it will leave the old map.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

