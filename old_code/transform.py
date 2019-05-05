import math

def rotate_vec(vec, angle):
	vec_angle = math.atan(vec.y / vec.x)
	new_angle = vec_angle + angle
	
	
