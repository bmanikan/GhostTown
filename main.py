import argparse
from utils import GhostTown
import cv2
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()

ap.add_argument('-i','--input', required=True, help='Input file name')
ap.add_argument('-o', '--output', required=True, help='output file name')

args = vars(ap.parse_args())

input_file = args['input']
output_file = args['output']

im = GhostTown(input_file)
image = im.background()

plt.figure(figsize=(20,10))
fig = plt.imshow(image)
fig.set_cmap('gray')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.savefig(output_file,bbox_inches='tight')