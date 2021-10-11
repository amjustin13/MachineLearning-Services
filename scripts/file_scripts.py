import os

def make_line_files(x_file_path, y_file_path):
	with open(x_file_path) as x_file:
		with open(y_file_path) as y_file:
			y_lines = y_file.readlines()
			x_lines = x_file.readlines()
			x_lines = [x_line.rstrip() for x_line in x_lines]
			y_lines = [y_line.rstrip() for y_line in y_lines]
			assert len(x_lines) == len(y_lines)
			for i in range(len(y_lines)):
				if y_lines[i] == "Amendment to a Long Form":
					y_lines[i] = -1
					x_lines[i] = -1
			x_lines = [line for line in x_lines if line != -1]
			y_lines = [line for line in y_lines if line != -1]
			
			assert len(x_lines) == len(y_lines)

			for i in range(len(x_lines)):
				f = open(f"data/{i}.txt", 'w')
				f.write(x_lines[i])
				f.close()
				
				f = open(f"labels/{i}.txt", 'w')
				f.write(y_lines[i])
				f.close()


def count_ds_labels(labels_file):
	with open(labels_file) as l_file:
		lines = l_file.readlines()
		lines = [line.rstrip() for line in lines]

		labels = {}
		for label in lines:
			if label in labels:
				labels[label] += 1
			else:
				labels[label] = 1
		print(labels)


def truncate_data(x_file_path, y_file_path):
	with open(x_file_path) as x_file:
		with open(y_file_path) as y_file:
			y_lines = y_file.readlines()
			x_lines = x_file.readlines()
			x_lines = [x_line.rstrip() for x_line in x_lines]
			y_lines = [y_line.rstrip() for y_line in y_lines]
			assert len(x_lines) == len(y_lines)

			labels_to_dirs = {	"Amendment to a Long Form": 	"Amendment_to_a_Long_Form", 
								"Certificate of Occupancy": 	"Certificate_of_Occupancy", 
								"Electrical Permit": 			"Electrical_Permit", 
								"Long Form/Alteration Permit": 	"Long_Form_Alteration_Permit", 
								"Electrical Fire Alarms": 		"Electrical_Fire_Alarms", 
								"Short Form Bldg Permit": 		"Short_Form_Bldg_Permit", 
								"Gas Permit": 					"Gas_Permit", 
								"Electrical Low Voltage": 		"Electrical_Low_Voltage", 
								"Erect/New Construction": 		"Erect_New_Construction", 
								"Electrical Temporary Service": "Electrical_Temporary_Service", 
								"Excavation Permit": 			"Excavation_Permit", 
								"Foundation Permit": 			"Foundation_Permit", 
								"Plumbing Permit": 				"Plumbing_Permit", 
								"Use of Premises": 				"Use_of_Premises"
							}
			labels_count = {	"Amendment to a Long Form": 	0, 
								"Certificate of Occupancy": 	0, 
								"Electrical Permit": 			0, 
								"Long Form/Alteration Permit": 	0, 
								"Electrical Fire Alarms": 		0, 
								"Short Form Bldg Permit": 		0, 
								"Gas Permit": 					0, 
								"Electrical Low Voltage": 		0, 
								"Erect/New Construction": 		0, 
								"Electrical Temporary Service": 0, 
								"Excavation Permit": 			0, 
								"Foundation Permit": 			0, 
								"Plumbing Permit": 				0, 
								"Use of Premises": 				0
							}

			labels_total = {	"Amendment to a Long Form": 	3933, 
								"Certificate of Occupancy": 	18447, 
								"Electrical Permit": 			108725, 
								"Long Form/Alteration Permit": 	34403, 
								"Electrical Fire Alarms": 		28342, 
								"Short Form Bldg Permit": 		139628, 
								"Gas Permit": 					51438, 
								"Electrical Low Voltage": 		42117, 
								"Erect/New Construction": 		2561, 
								"Electrical Temporary Service": 7134, 
								"Excavation Permit": 			10814, 
								"Foundation Permit": 			90, 
								"Plumbing Permit": 				69424, 
								"Use of Premises": 				1285
							}
				
			for i in range(len(x_lines)):
				dir_name = labels_to_dirs[y_lines[i]]
				count = labels_count[y_lines[i]]
				if count < 12000:
					cap = labels_total[y_lines[i]]*.8 if labels_total[y_lines[i]] < 10000 else 10000
					if count < cap:
						f = open(os.path.join("train", dir_name, f"{count}.txt"), 'w')
						f.write(x_lines[i])
						f.close()
					else:
						f = open(os.path.join("test", dir_name, f"{count - cap}.txt"), 'w')
						f.write(x_lines[i])
						f.close()
					labels_count[y_lines[i]] += 1


			


if __name__ == "__main__":
	# make_line_files("X_BostonDataSet.csv", "y_BostonDataSet.csv")
	# count_ds_labels("y_BostonDataSet.csv")
	truncate_data("X_BostonDataSet.csv", "y_BostonDataSet.csv")

