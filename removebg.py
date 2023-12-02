# import required modules
from rembg import remove
from PIL import Image

# get the image
input_path = 'pic.png'

# output file
output_path = 'pic_output.png'

# process the image
input = Image.open(input_path)

# remove the background from the image
output = remove(input)

# save the removed image
output.save(output_path)

