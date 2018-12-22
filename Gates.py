import numpy as np

def perceptron(weights,bias,x):
	# Dot product of weight with input
	# Then add it to the bias
	model = np.add(np.dot(weights,x),bias)
	print(model)
	# Sigmoid activation function = 1/((1+exp(-x))
	logit = 1/(1+np.exp(-model))
	print(logit)
	# Round off logit to nearest value 1 or 0 but only because those are the output values we care about.
	return np.round(logit)

# give inputs to perceptron function

def compute(gate,weightdict,inputs):
	# Take all the key values from particular gate in our weight dictionary
	weights = np.array([weightdict[gate][w] for w in weightdict[gate].keys()[::-1]])
	# calculate our perceptrons for each value in the input for each type of gate
	output = np.array([ perceptron(weights, weightdict['bias'][gate], val) for val in inputs])
	print(gate)
	return gate,output

def main():
	#Bias and weights based on optimal values found on the internet somewhere.
	#Gates in a list format
	Gates = {
		'and_gate':{
			'w1': -0.1,
			'w2': 0.2,
			'w3': 0.2			
		},
		'or_gate':{
			'w1': -0.1,
			'w2': 0.7,
			'w3': 0.7			
		},
		'not_gate':{
			'w0': 0.5,
			'w1': -0.7			
		},
		'nand_gate':{
			'w1': 0.6,
			'w2': -0.8,
			'w3': -0.8			
		},
		'nor_gate':{
			'w1': 0.5,
			'w2': -0.7,
			'w3': -0.7			
		},
		'bias':{
			'and_gate': -0.2,
			'or_gate': -0.1,
			'not_gate': 0.1,
			'nand_gate': 0.3,
			'nor_gate': 0.1
		}
		
	}
	inputs = np.array([
		[1,0,0],
		[1,0,1],
		[1,1,0],
		[1,1,1]
	])
	and_gate = compute('and_gate',Gates,inputs)
	or_gate = compute('or_gate',Gates,inputs)
	
	#diff inputs for not
	not_gate = compute('not_gate',Gates,[[1,0],[1,1]])
	nand_gate = compute('nand_gate',Gates,inputs)
	nor_gate = compute('nor_gate',Gates,inputs)

	def template(inputs, name, data):
        	print("Logic Gate: {}".format(name[6:].upper()))
        	print("X0\tX1\tX2\tY")
        	toPrint = ["{1}\t{2}\t{3}\t{0}".format(output, *datas) for datas, output in zip(inputs, data)]
        	for i in toPrint:
           		print(i)

	gate_list = [and_gate, or_gate, not_gate, nand_gate, nor_gate]
	for i in gate_list:
        	template(inputs, *i)

if __name__ == '__main__':
	main()
