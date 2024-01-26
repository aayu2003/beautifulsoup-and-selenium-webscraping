import cv2
import os
# Get the data directory path
data_dir = cv2.data.haarcascades

# List the XML files in the data directory
haarcascades = [f for f in os.listdir(data_dir) if f.endswith('.xml')]

# Print the list of available Haar cascades
print("Available Haar Cascades:")
for cascade in haarcascades:
    print(cascade)
