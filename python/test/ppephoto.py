# ProcessPoolExecutor
import concurrent.futures
import time
from PIL import Image, ImageFilter

img_names = [
	'dan-cristian-padure-861NuwiTbBw-unsplash.jpg',
	'dan-cristian-padure-CAlbVYwhYgg-unsplash.jpg',
	'dan-cristian-padure-uFHc4Q-64Bs-unsplash.jpg',
	'dan-cristian-padure-ZIrEsi0jR6s-unsplash.jpg',
	'jene-stephaniuk-30tKlnFG5KE-unsplash.jpg',
	'pawel-czerwinski-arwTpnIUHdM-unsplash.jpg',
	'pawel-czerwinski-W_mfoOi1Elc-unsplash.jpg',
	'ralph-ravi-kayden-iZEG_9jaB40-unsplash.jpg',
	'solen-feyissa-uVc2mpXWUPQ-unsplash.jpg',
]

start = time.perf_counter()

size = (1200, 1200)
base = 'photos/'
out = 'out/'

def process_image(img_name):
	img = Image.open(base+img_name)
	img = img.filter(ImageFilter.GaussianBlur(15))
	img.thumbnail(size)
	img.save(out+img_name)
	print(f'{img_name} was processed...')

with concurrent.futures.ThreadPoolExecutor() as executor:
	executor.map(process_image, img_names)

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds')
