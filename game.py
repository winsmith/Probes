from engine import ProbesEngine
from game_object import Body, Position, Vector, SpaceCraft

game_engine = ProbesEngine()

earth_mass = 5.972e24
earth = Body(Position(1, 2, 3), Vector(0, 0, 0), earth_mass)

moon_mass = 7.34767309e22
moon_position = Position(3e20, 0, 0)
moon = Body(moon_position, Vector(0, earth.orbital_velocity(moon_position), 0), moon_mass)

voyager_position = Position(4e20, 0, 0)
voyager = SpaceCraft(voyager_position, Vector(0, earth.orbital_velocity(voyager_position), 0))
