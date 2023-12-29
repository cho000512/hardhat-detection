from simple_image_download import simple_image_download as sim
response = sim.simple_image_download

keywords = ["construction worker jacket", "construction worker"]

for kw in keywords:
	response().download(kw, 100)