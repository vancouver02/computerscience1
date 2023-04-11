import math

# creted a function here to calculate the volume of a prism
def volume_prism(length,width,height):
    volume_of_prism = length*width*height
    return volume_of_prism
#this function calculates the depth of a cylinder
def find_length(radius,volume):
    depth_of_cylinder = math.pi* radius**2 * height
    return depth_of_cylinder

# variables created that takes the input of the length,width, and height, as well as the radius of the cylinder
length = float(input("Length of rectangular prism (m) ==> "))
print(length)

width = float(input("Width of rectangular prism (m) ==> "))
print(width)

height = float(input("Height of rectangular prism (m) ==> "))
print(height)

radius_of_cylinder = float(input("Radius of cylinder (m) ==> "))
print(radius_of_cylinder)

# computing the total amount of water needed to fill the rectangular prism 70 times a day for 3 months
volume = volume_prism(length,width,height)*70*30

# finding the height of the cylinder needed to hold the computed amount of water
height_cylinder = height(radius_of_cylinder, volume)

print("Lake with {:.2f} will lose {:.2f} depth in three months.").format(radius_of_cylinder,height_cylinder)





