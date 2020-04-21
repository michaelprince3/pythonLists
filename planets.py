planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.extend(["Neptune", "Uranus"])

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")

rocky_planets = planet_list[2:7]

planet_list.remove("Pluto")



print(planet_list)
print(rocky_planets)