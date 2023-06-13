import os
from PIL import Image, ImageDraw

PICSIZE = tuple((190, 140))

cwd = os.getcwd()
print(cwd)
source = []
back = ["idle.png", "hovered.png", "pressed.png"]
# Iterate directory
for file in  os.listdir(cwd):

    print("file :", file)

    if file.endswith('.png'):
        if file not in back:
            source.append(file)


print(source)


# https://pythonexamples.org/pillow-image-overlay/

for bak in back:
    base_img = Image.open(bak)
    base_img = base_img.convert('RGBA')

    for overlay in source:
        overlay_img = Image.open(overlay)

        # Convert the overlay image to RGBA mode
        overlay_img = overlay_img.convert('RGBA')

        # Define the position where the overlay image will be pasted
        position = (0, 0)


        newim = Image.new('RGBA', PICSIZE, (0, 0, 0, 0))

        # Overlay the image over base image
        #base_img.paste(overlay_img, position, overlay_img)
        newim.paste(base_img, position, base_img)
        newim.paste(overlay_img, position, overlay_img)

        # Save the resulting image
        #base_img.save(f'{overlay}_{bak}.png')
        #newim.save(f'{overlay}_{bak}.png')

        no_ext_fikename_overlay = overlay[:-4]


        print(f"  bak {bak} ; overlay {overlay} ; no_ext_fikename_overlay  {no_ext_fikename_overlay}  ")

        #newim.save(f'{no_ext_fikename_overlay}_{bak}.png')
        newim.save(f'{no_ext_fikename_overlay}_{bak}')

