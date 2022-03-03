

def greet_with(name,location):
  print(f'Hello {name}, It looks like you\'re from {location}')

#positial argument example
greet_with("Anushan", "Toronto")
#positial argument gone wrong, will mix up name and locaiton in print statement 
greet_with("Toronto", "Anushan")

#using keyword arguments can ensure mapping of arguments are executed as intended

greet_with(location = "Toronto", name = "Anushan")