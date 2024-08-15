import os
from fasthtml.common import Script, Link, Style

texts = [
    """
## A new generation of coders


The Apollo 11 mission was the first manned mission to land on the Moon. 

It was the fifth human spaceflight of Project Apollo and the third human voyage to the Moon or Moon orbit. Launched on July 16, 1969, it carried Commander Neil Armstrong, Command Module Pilot Michael Collins, and Lunar Module Pilot Edwin "Buzz" Aldrin. The mission was the culmination of the Apollo program and a national goal set in 1961 by President John F. Kennedy. Kennedy's goal was accomplished on the Apollo 11 mission when Armstrong and Aldrin landed their Lunar Module (LM) on the Moon on July 20, 1969, and walked on its surface.
""",
    """
Apollo 13 was the seventh crewed mission in the Apollo space program and the third meant to land on the Moon. The craft was launched from Kennedy Space Center on April 11, 1970, but the lunar landing was aborted after an oxygen tank in the service module (SM) failed two days into the mission. The crew instead looped around the Moon and returned safely to Earth on April 17. The mission was commanded by Jim Lovell with Jack Swigert as command module pilot and Fred Haise as lunar module pilot. Swigert was a late replacement for the original CM pilot Ken Mattingly, who was grounded by the flight surgeon after exposure to German measles.
Apollo 13 was the seventh crewed mission in the Apollo space program and the third meant to land on the Moon. The craft was launched from Kennedy Space Center on April 11, 1970, but the lunar landing was aborted after an oxygen tank in the service module (SM) failed two days into the mission. The crew instead looped around the Moon and returned safely to Earth on April 17. The mission was commanded by Jim Lovell with Jack Swigert as command module pilot and Fred Haise as lunar module pilot. Swigert was a late replacement for the original CM pilot Ken Mattingly, who was grounded by the flight surgeon after exposure to German measles.
Apollo 13 was the seventh crewed mission in the Apollo space program and the third meant to land on the Moon. The craft was launched from Kennedy Space Center on April 11, 1970, but the lunar landing was aborted after an oxygen tank in the service module (SM) failed two days into the mission. The crew instead looped around the Moon and returned safely to Earth on April 17. The mission was commanded by Jim Lovell with Jack Swigert as command module pilot and Fred Haise as lunar module pilot. Swigert was a late replacement for the original CM pilot Ken Mattingly, who was grounded by the flight surgeon after exposure to German measles.
Apollo 13 was the seventh crewed mission in the Apollo space program and the third meant to land on the Moon. The craft was launched from Kennedy Space Center on April 11, 1970, but the lunar landing was aborted after an oxygen tank in the service module (SM) failed two days into the mission. The crew instead looped around the Moon and returned safely to Earth on April 17. The mission was commanded by Jim Lovell with Jack Swigert as command module pilot and Fred Haise as lunar module pilot. Swigert was a late replacement for the original CM pilot Ken Mattingly, who was grounded by the flight surgeon after exposure to German measles.

""",
]

texts2 = [
    # text on geothermal energy
    """
## Geothermal energy

Geothermal energy is thermal energy generated and stored in the Earth. Thermal energy is the energy that determines the temperature of matter. The geothermal energy of the Earth's crust originates from the original formation of the planet and from radioactive decay of materials (in currently uncertain but possibly roughly equal proportions). The geothermal gradient, which is the difference in temperature between the core of the planet and its surface, drives a continuous conduction of thermal energy in the form of heat from the core to the surface. The adjective geothermal originates from the Greek roots γη (ge), meaning earth, and θερμος (thermos), meaning hot.
Geothermal energy is thermal energy generated and stored in the Earth. Thermal energy is the energy that determines the temperature of matter. The geothermal energy of the Earth's crust originates from the original formation of the planet and from radioactive decay of materials (in currently uncertain but possibly roughly equal proportions). The geothermal gradient, which is the difference in temperature between the core of the planet and its surface, drives a continuous conduction of thermal energy in the form of heat from the core to the surface. The adjective geothermal originates from the Greek roots γη (ge), meaning earth, and θερμος (thermos), meaning hot.
Geothermal energy is thermal energy generated and stored in the Earth. Thermal energy is the energy that determines the temperature of matter. The geothermal energy of the Earth's crust originates from the original formation of the planet and from radioactive decay of materials (in currently uncertain but possibly roughly equal proportions). The geothermal gradient, which is the difference in temperature between the core of the planet and its surface, drives a continuous conduction of thermal energy in the form of heat from the core to the surface. The adjective geothermal originates from the Greek roots γη (ge), meaning earth, and θερμος (thermos), meaning hot.
Geothermal energy is thermal energy generated and stored in the Earth. Thermal energy is the energy that determines the temperature of matter. The geothermal energy of the Earth's crust originates from the original formation of the planet and from radioactive decay of materials (in currently uncertain but possibly roughly equal proportions). The geothermal gradient, which is the difference in temperature between the core of the planet and its surface, drives a continuous conduction of thermal energy in the form of heat from the core to the surface. The adjective geothermal originates from the Greek roots γη (ge), meaning earth, and θερμος (thermos), meaning hot.
Geothermal energy is thermal energy generated and stored in the Earth. Thermal energy is the energy that determines the temperature of matter. The geothermal energy of the Earth's crust originates from the original formation of the planet and from radioactive decay of materials (in currently uncertain but possibly roughly equal proportions). The geothermal gradient, which is the difference in temperature between the core of the planet and its surface, drives a continuous conduction of thermal energy in the form of heat from the core to the surface. The adjective geothermal originates from the Greek roots γη (ge), meaning earth, and θερμος (thermos), meaning hot.

""",
    # text on solar energy
    """
## Solar energy

Solar energy is radiant light and heat from the Sun that is harnessed using a range of ever-evolving technologies such as solar heating, photovoltaics, solar thermal energy, solar architecture, molten salt power plants, and artificial photosynthesis. It is an essential source of renewable energy and its technologies are broadly characterized as either passive solar or active solar depending on how they capture and distribute solar energy or convert it into solar power. Active solar techniques include the use of photovoltaic systems, concentrated solar power, and solar water heating to harness the energy. Passive solar techniques include orienting a building to the Sun, selecting materials with favorable thermal mass or light dispersing properties, and designing spaces that naturally circulate air.
""",
]

debug = os.environ.get("DEBUG", "false").lower() == "true"
tailwind = (Script(src="https://cdn.tailwindcss.com?plugins=typography"),)
daisyui = (
    Link(
        href="https://cdn.jsdelivr.net/npm/daisyui@4.12.x/dist/full.min.css",
        rel="stylesheet",
        type="text/css",
    ),
)
hide_scrollbar = Style(
    """
    /* Hide scrollbars for all elements */
    * {
        scrollbar-width: none; /* Firefox */
        -ms-overflow-style: none;  /* Internet Explorer 10+ */
    }
    
    *::-webkit-scrollbar {
        display: none; /* Safari and Chrome */
    }
    """
)
# email = None
