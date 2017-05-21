Senior Design Scripts
Katie Biegel and Ashton Krajnovich

Description of files in this folder:
gridxy_40x40 - file that contains the grid information or x/y locations of the grid
gaussdata_40x40 - file that contains the background data used for testing the scripts (x/y location and data value)
images folder - folder that plots output to from the pathing function

Scripts:
testing_reading_control: accepts grid and data file and computes variance map
	- DO NOT EDIT

testing_pathing: controls pathing over the grid, creates weighting map
	- this script also outputs figures, to create figures: edit outlined sections of code
	- ONLY EDIT TO OUPUT FIGURES

testing_comborun: overall running script, this is where you will run the code from
	- calls outside functions like pathing and batch file creation
	- EDIT VARIABLES AT THE TOP OF THE SCRIPT

testing_alltogethernow: batchrun function
	- runs sgems script creation and computes the variance maps
	- ONLY EDIT FOR LOCATIONS OF OUTPUTS

sgems_script_WRTIE_revised: creates SGeMS scripts
	- EDIT LINES 49 AND 50 TO SPECIFY GRID SIZE