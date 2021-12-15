import json

print('╔╦╦╦═╦╗╔═╦═╦══╦═╗')
print('║║║║╩╣╚╣═╣║║║║║╩╣')
print('╚══╩═╩═╩═╩═╩╩╩╩═╝')

print()
print('Instructions:')
print()
print('1). Make sure that your resolution is of equal values on both axis.\n2). This script will only accept intergers as a value, so if your resolution is "128x128", make sure to only input "128" otherwise you will recieve an error.')
print()
input('Please press enter to continue...')
print()
RESOLUTION = int(input("Please enter your resolution: "))

values = [0.036, 0.060]
values1 = [0.092, 0.144]

scales = [
	values[0]/(RESOLUTION/16),
	values[1]/(RESOLUTION/16),
	values[0]/(RESOLUTION/16)
]

scales1 = [
	values1[0]/(RESOLUTION/16),
	values1[1]/(RESOLUTION/16),
	values1[0]/(RESOLUTION/16)
]


data = {
	'minecraft:render_offsets': {
		'main_hand': {
			'first_person': {'scale': scales},
			'third_person': {'scale': scales1}
		},
		'off_hand': {
			'first_person': {'scale': scales},
			'third_person': {'scale': scales1}
		}
	}
}

jstr = json.dumps(data, indent=4)
print(jstr)
