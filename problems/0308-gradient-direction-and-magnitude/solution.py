import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:

	mag = np.sqrt(sum([i**2 for i in gradient]))
	n = len(gradient)
	
	if mag == 0:
		dire = [0] * n
		desc = [0] * n
		
	else:
		dire = [i/mag for i in gradient]
		desc = [-i for i in dire]

	return {
		'magnitude':mag,
		'direction': dire,
		'descent_direction':desc

	}
	
print(gradient_direction_magnitude([0.0, 0.0]))