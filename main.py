class ride:
	"""
	defines a single ride
	"""

	def __init__(self, id=0, data=[0,0,0,0,0,0]):
		self.id = id
		self.start_point = [int(data[0]), int(data[1])]
		self.end_point = [int(data[2]), int(data[3])]
		self.begin_time = int(data[4])
		self.finish_time = int(data[5])
		self.taken = False

class taken_ride: 
	"""
	this is the array of taken cars that should eventually be printed into a file.
	"""

	def __init__(self, car_id = 0, ride_id = 0):
		self.car = car_id
		self.ride = ride_id

class car: 
	"""
	car implemtation.
	"""
 
	def __init__(self, id=0):
		self.id = id
		self.location = [0, 0]
		self.ttl = 0

	def iterate():
		"""
		whenever a car picks up a ride, it gets a ttl of how far the ride is from the car.
		"""
		self.ttl = self.ttl - 1

def create_cars(number_of_cars):
	"""
	creates a list of cars.
	"""

	cars = []
	for i in range(number_of_cars):
		cars.append(car(i))

class simulation_data:
	"""
	this class holds the data of the board meta data
	"""

	def __init__(self, data=[0,0,0,0,0,0]):
		self.rows = int(data[0])
		self.cols = int(data[1])
		self.number_of_cars = int(data[2])
		self.number_of_rides = int(data[3])
		self.bonus = int(data[4])
		self.T = int(data[5])

class file_data:
    def __init__(self,r = [0,0,0,0,0,0],i = [[0,0,0,0,0,0]]):

    	# the meta data is of type : [rows, cols, num_of_cars, num_of_rides, bonus, number of steps]
        self.meta_data = r
        self.rides = i

def calc_distance(ab, xy): 
	"""
	calculate the distance between ab, and xy
	"""
	return abs(xy[0] - ab[0]) + abs(xy[1] - ab[1])

def parse_rides(data):
	"""
	data is a list of lists, should return a list of rides.
	"""
	rides = []

	for i in range(len(data)):
		rides.append(ride(i, data[i].split(" ")))

	return rides

def read_file(filepath) :
	"""
		- Reads a file and returns its number of lines.
	"""

	with open(filepath, 'r') as input_file:
		data = input_file.readlines()
		data = [x.strip() for x in data]
		return data 

def create_file_data(data):
	"""
		- create an instance of file_data for a given data_set
	"""

	# insert the first line into meta data.
	meta_data = data[0]

	# insert the rest of the data into rides 
	rides = data[1:]

	# return a new object of type file_data
	return file_data(meta_data, rides)

def take_ride(ride_id, car_id, car, rides, total_number_of_rides,  time) :
	"""
	insert into taken rides the ride_ide and car_id
	remove ride_id from rides (since it is taken)
	set the TTL for car
	"""

	for i in range(len(total_number_of_rides)):
		if rides[i].id = ride_id && not rides[i].taken:
			curr_ride = rides[i]
			rides[i].taken = True


	ride_score = calc_distance(curr_ride.start_point, curr_ride.end_point)
	car_score = calc_distance(curr_ride.start_point, car.location)
	t_score = curr_ride.begin_time - T - car_score
	car.ttl = ride_score + car_score + t_score



	# insert the id's into the taken car array
	return , taken_ride(car_id, ride_id)


#TODO : print into a file the content of taken_rides.
def parse_taken_rides(taken_rides, number_of_cars):
	"""
	print the taken rides into the following format : 
	
	NumberOfRides, RideNum, RideNum , ...
	"""

	output_lines = []

	# foreach car
	for i in range(number_of_cars):
		rides = []
		curr_car_counter = 0
		#foreach taken ride
		for j in range(taken_rides):
			#if the ride has car id 
			if taken_rides[j].car = i:
				#counter up and insert the ride id to a list
				curr_car_counter = curr_car_counter + 1
				rides.append[taken_rides[j].ride]

		if curr_car_counter != 0:
			output_lines.append(curr_car_counter, rides)

	return output_lines


def print_output(output_lines):
	"""
	get a list of [carid, [ride, ride, ride]]
	"""

	with open("output.txt", 'w') as outputfile : 
		for line in output_lines :
			outputfile.write(line[0])
			outputfile.write(line[" "])
			for ride in range(line[1:]):
				outputfile.write[line[ride]]
				outputfile.write(line[" "])
			outputfile.write(line["\n"])


if __name__ == "__main__":
    data = read_file("a_example.in")
    file_data = create_file_data(data)

    # create the simulation data.
    sd = simulation_data(file_data.meta_data.split(" "))

    # create the rides data - returns a slice of ride objects.
    open_rides = parse_rides(file_data.rides)
    taken_rides = []
    
    for i in range(sd.T):
