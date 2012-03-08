Integration Application
=======================

Quick Start
-----------
Create a GUI for your steps in 3 simple steps:
1. Create custom classes inheriting ProcessStep
2. Use PreCondition, ExecuteStep and PostCondition
3. Prepare main

1. Create custom classes inheriting ProcessStep

For example: ## MySteps.py
	Class StepOne(ProcessStep):
		def __init(self, stepname, filename):
			self.stepname = stepname # stepname is mandatory and may not be changed. Additional parameters could be added.
			self.filename = filename

2. Use PreCondition, ExecuteStep and PostCondition
		def PreCondition(self):
			print "This function is automatically executed to check the necessary requirements to execute the step
			return 0 # On Success, return 0
			#return 1 # On Failure, return non-zero
		
		def ExecuteStep(self):
			print "This function is where the actual work is done."
			return 0 # On Success, return 0
			#return 1 # On Failure, return non-zero
			
		def PostCondition(self):
			print "Check whether the ExecuteStep worked as expected."
			return 0 # On Success, return 0
			#return 1 # On Failure, return non-zero

3.  Prepare main ##main.py
	from IntegrationApp import IntegrationApp
	from MySteps import StepOne
	
	if __name__ == "__main__":
    	process_steps = []
    	
    	# Instansiating object from Steps and add to process_steps
    	parsexls = StepOne("Parse", "suiv.xls")
    	process_steps.append(parsexls)
    	
    	parsecsv = StepOne("Fetch", "install.csv")
    	process_steps.append(parsecsv)

		# Start Application and call MainLoop
    	app = IntegrationApp(process_steps)
    	app.MainLoop()
