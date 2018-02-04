from django.contrib import admin

from core.models import GameObject, Positionable, Movable, Body, Spacecraft, Resource, SpacecraftPart


class GameObjectAdmin(admin.ModelAdmin):
    pass


class PositionableAdmin(admin.ModelAdmin):
    pass


class MovableAdmin(admin.ModelAdmin):
    pass


class BodyAdmin(admin.ModelAdmin):
    pass


class SpaceCraftAdmin(admin.ModelAdmin):
    pass


admin.site.register(GameObject, GameObjectAdmin)
admin.site.register(Positionable, PositionableAdmin)
admin.site.register(Movable, MovableAdmin)
admin.site.register(Body, BodyAdmin)
admin.site.register(Spacecraft, SpaceCraftAdmin)
admin.site.register(Resource)
admin.site.register(SpacecraftPart)