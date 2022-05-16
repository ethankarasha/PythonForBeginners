the_string = "North Dakota"

print(the_string.rjust(17))

print(the_string.rjust(17, "*"))

center_plus = the_string.center(16, "+")

print(center_plus)

print(the_string.lstrip("orthN"))

print(center_plus.rstrip("+"))

print(center_plus.strip("+"))

print(the_string.replace("North", "South"))