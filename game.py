from engine import ProbesEngine
from game_object import Body, Position, Vector, SpaceCraft, Planetoid

game_engine = ProbesEngine()

earth_mass = 5.972e24
earth = Planetoid(Position(1, 2, 3), Vector(0, 0, 0), earth_mass, "Earth")
game_engine.game_objects.append(earth)

moon_mass = 7.34767309e22
moon_position = Position(3e20, 0, 0)
moon = Planetoid(moon_position, Vector(0, earth.orbital_velocity(moon_position), 0), moon_mass, "Moon")
game_engine.game_objects.append(moon)

voyager_position = Position(4e20, 0, 0)
voyager = SpaceCraft(voyager_position, Vector(0, earth.orbital_velocity(voyager_position), 0), "Voyager")
game_engine.game_objects.append(voyager)

game_engine.run()

