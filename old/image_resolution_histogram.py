import os
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

# specify the folder path containing images
folder_path = r'C:\Users\m.mohseni\Desktop\V3_light\images'

# create an empty list to store image resolutions
resolutions = []

# iterate through each file in the folder
for filename in os.listdir(folder_path):
    # check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # open the image file
        with Image.open(os.path.join(folder_path, filename)) as img:
            # get the resolution of the image and append it to the list
            resolutions.append(img.size)

# create a list of x-values for the histogram
x_values = [r[0] for r in resolutions]

# plot the histogram using Seaborn
sns.histplot(x=x_values, kde=True , bins=100)
# plt.hist(x_values,bins=100)


# set the title and labels of the histogram
plt.title("Distribution of Image Resolutions")
plt.xlabel("Width")
plt.ylabel("Frequency")
plt.ylim(0, 250)
# show the histogram
sns.despine()
plt.show()
