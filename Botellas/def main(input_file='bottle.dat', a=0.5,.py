def main(input_file='bottle.dat', a=0.5, dx=0.1, dy=0.1, 
         timesteps=200, image_interval=4000):
	versions = ['py','cyt']
	input_files = ['bottle.dat', 'bottle_medium.dat', 'bottle_large.dat']
	timestepsS = ['100', '200', '500', '1000', '2000']
	for version in versions:
		for input_file in input_files:
			for timesteps in timestepsS:
				if version == 'py':      	
					#print("Using pure Python") 	
					# Initialise the temperature field
					field, field0 = init_fields(input_file)

					#print("Heat equation solver")
					#print("Diffusion constant: {}".format(a))
					#print("Input file: {}".format(input_file))
					#print("Parameters")
					#print("----------")
					#print("  nx={} ny={} dx={} dy={}".format(field.shape[0], field.shape[1],
												dx, dy))
					#print("  time steps={}  image interval={}".format(timesteps,
															image_interval))

					# Plot/save initial field
					write_field(field, 0)
					# Iterate
					t0 = time.time()
					iterate(field, field0, a, dx, dy, timesteps, image_interval)
					t1 = time.time()
					# Plot/save final field
					write_field(field, timesteps)

					#print("Simulation finished in {0} s".format(t1-t0))
				if version == 'cyt':    	
				# Initialise the temperature field
					field, field0 = init_fields_cyt(input_file)

					#print("Heat equation solver")
					#print("Diffusion constant: {}".format(a))
					#print("Input file: {}".format(input_file))
					#print("Parameters")
					#print("----------")
					#print("  nx={} ny={} dx={} dy={}".format(field.shape[0], field.shape[1],
													dx, dy))
					#print("  time steps={}  image interval={}".format(timesteps,
																image_interval))

					# Plot/save initial field
					write_field_cyt(field, 0)
					# Iterate
					t0 = time.time()
					iterate_cyt(field, field0, a, dx, dy, timesteps, image_interval)
					t1 = time.time()
					# Plot/save final field
					write_field_cyt(field, timesteps)

					#print("Simulation finished in {0} s".format(t1-t0))
