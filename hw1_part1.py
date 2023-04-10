
width = input("Width of box ==> ")
print(width)

height = input("Height of box ==> ")
print(height)

frame_character = input("Enter frame character")
print(frame_character)

height_width = height +'x'+ width

print()
print("Box: ")

print(frame_character*int(width))
print(frame_character,height_width+" "*(int(width)-int(len(height_width))-3)+frame_character)
print(frame_character+" "*(int(width)-2)+frame_character+"\n")*(int(height)-3)+frame_character*int(width)












