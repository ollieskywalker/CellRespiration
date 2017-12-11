from Tkinter import *

import Tkinter

root = Tk()

glucoseImage = PhotoImage(file="glucose.png")
lacticAcidImage = PhotoImage(file="lac2.png")
ethonalImage =PhotoImage(file="ethanol.png")
blankImage = PhotoImage(file="Blank.png")
acetylImage = PhotoImage(file="acetylcoa.png")



frame = Frame(width="750")
frame.pack()

message = "Welcome to Cell Respiration in Python. This is an interactive application to help you learn the cell respiration process."
text = Message(frame, text=message, width=400)
text.config(bg='lightgreen', font=('times', 24, 'bold'))
text.pack(fill=X)

glucoseMolecule = ""


def next_slide():
	frame.destroy()
	glycolysisFrame = newFrame()

	message = "Glycolysis"
	text = Message(glycolysisFrame, text=message, width=400)
	text.config(text = message,bg="lightgreen", font=('times',24, 'bold'), justify=LEFT)
	text.pack(fill=X)
	#Glucose Image
	sideImage = Label(glycolysisFrame, image=glucoseImage).pack(side="right")
	#Label for entry field
	editTextName = Label(glycolysisFrame, text="Glucose Molecules").pack(side="left")
	#Text field to input molcules
	moleculesEntry = Entry(glycolysisFrame) 
	moleculesEntry.pack(side="left")

	glucoseMolecule = moleculesEntry
	#Text in list formate to show inputed molecules
	inputsLabel = Label(glycolysisFrame, text="Inputs: ") 
	inputsLabel.pack(side="left")
	#Text in list formate to show outputed molecules
	outputsLabel = Label(glycolysisFrame, text="Outputs: " + "\n" + "")
	outputsLabel.pack(side="left")	

	####################################
	def fermentation():
		frame.destroy()
		glycolysisFrame.destroy()
		secondFrame = newFrame()
		#secondtext is new title in the fermentation frame
		secondText = Message(secondFrame, text="Fermentation", width=400)
		secondText.config(text = "Fermentation",bg="lightgreen", font=('times',24, 'bold'), justify=LEFT)
		secondText.pack(fill=X)

		sideImage = Label(secondFrame, image=lacticAcidImage)
		sideImage.pack_forget()

		outputsLabel = Label(secondFrame, text="Outputs: " + "\n" + "")
		outputsLabel.pack(side="right")
		#Text in list formate to show outputed molecules
		inputsLabel = Label(secondFrame, text="Inputs: ")
		inputsLabel.pack(side="right")
		
		#Define functions for lactid acid fermentation and ethonal fermentation
		def lacticAcid():
			inputsLabel.config(text="Inputs: " + "\n" + "Pyruvate 2" + "\n NADH 2")
			outputsLabel.config(text="Outputs: " + "\n Lactate 2" + "\n" + "NAD+")
			sideImage.pack(side="right")
			sideImage.config(image=lacticAcidImage)
		def ethonal():
			inputsLabel.config(text="Inputs: " + "\n" + "Pyruvate 2" + "\n NADH 2")
			outputsLabel.config(text="Outputs: " + "\n Ethonal 2" + "\n" + "NAD+")
			sideImage.config(image=ethonalImage)
		#this function allows user to go back to original track
		def backPage():
			secondFrame.destroy()
			next_slide()
		#this layout will have two buttons asking if Eukaryote or Prokaryote
		eukaryoteButton = Button(secondFrame, text="Eukaryote", command=lacticAcid).pack(side="left")
		prokaryoteButton = Button(secondFrame, text="Prokaryote", command=ethonal).pack(side="left")
		backButton = Button(secondFrame,text="back", command=backPage).pack(side="left")

	####################################

	#Function to show outputs
	def showResult():
		inputsLabel.config(text="Inputs: " + "\n" + "Glucose " + moleculesEntry.get()+ "\n ATP " + str(2 * int(moleculesEntry.get()))+ "\n" + "2NAD+")
		outputsLabel.config(text="Outputs: " + "\n Pyruvate " + str(2 * int(moleculesEntry.get())) + "\n ATP " + str(4 * int(moleculesEntry.get())) + "\n" + "2NADH")
	#button to enter glucose
	enterGlucoseButton = Button(glycolysisFrame, text="enter", command=showResult).pack()

	########## Now we enter process to prime the pyruvate
	def primePyruvate():
		frame.destroy()
		glycolysisFrame.destroy()
		pyruvateFrame = newFrame()
		#text of pyruvate transition
		secondText = Message(pyruvateFrame, text="As we transition from cytoplasm to mitochondria, the pyruvate will be prepared for Kreb's cycle", width=400)
		secondText.config(bg="lightgreen", font=('times',24, 'bold'), justify=LEFT)
		secondText.pack(fill=X)

		#Labels to show input and output
		outputsLabel = Label(pyruvateFrame, text="Outputs: " + "\n" + "")
		outputsLabel.pack(side="right")

		inputsLabel = Label(pyruvateFrame, text="Inputs: ")
		inputsLabel.pack(side="right")

		def prime():
			outputsLabel.config(text="Outputs: " + "\n Acetyl-CoA 1" + "\n CO2 1"+ "\n NADH 2")
			inputsLabel.config(text="Inputs: " + "\n Pyruvate 1" + "\n NAD+ 2")		
			toKrebsButton = Button(pyruvateFrame, text="To kreb's cycle", command = toKrebs).pack(side="left")
		#Button to prime pyruvate
		primeButton = Button(pyruvateFrame, text="Prime!", command=prime)
		primeButton.pack(side="left")
		#transition to Kreb's cycle
		def toKrebs():
			pyruvateFrame.destroy()
			krebsFrame = newFrame()
			#title for kreb's cycle
			secondText = Message(krebsFrame, text="Kreb's cycle: Now the acetyl group is attatched to oxaloacetate forming citric acid. ", width=400)
			secondText.config(bg="lightgreen", font=('times',24, 'bold'), justify=LEFT)
			secondText.pack(fill=X)

			#Labels to show input and output
			outputsLabel = Label(krebsFrame, text="Outputs(x2 per glucose): " + "\n" + "")
			outputsLabel.pack(side="right")

			inputsLabel = Label(krebsFrame, text="Inputs(x2 per glucose): ")
			inputsLabel.pack(side="right")

			#create multiple buttons that will give functionality to program
			def oxidize():
				outputsLabel.config(text="Outputs(x2 per glucose): " + "\n CO2 2")
				inputsLabel.config(text="Inputs(x2 per glucose): " + "\n Acetyl-CoA 1")
				reduceButton = Button(krebsFrame, text="Reduce NAD+ and FAD", command=reduction).pack(side="left")

			def reduction():
				outputsLabel.config(text="Outputs(x2 per glucose): " + "\n CO2 2" + "\n NADH 3" + "\n FADH2 1")
				inputsLabel.config(text="Inputs(x2 per glucose): " + "\n Acetyl-CoA 1" + "\n NAD+ 3" + "\n FAD 1")
				atpButton = Button(krebsFrame, text="Get ATP!", command=getAtp).pack(side="left")
			def getAtp():
				outputsLabel.config(text="Outputs(x2 per glucose): " + "\n CO2 2" + "\n NADH 3" + "\n FADH2 1" + "\n ATP 1")
				inputsLabel.config(text="Inputs(x2 per glucose): " + "\n Acetyl-CoA 1" + "\n NAD+ 3" + "\n FAD 1" + "\n ADP 1")
				
				#lastStage stage of cell respiration; this will cover electron transport chain and chemiosmosis
				# op = oxidative phosphoralation
				def lastStage():
					krebsFrame.destroy()
					opFrame = newFrame()
					
					#Title for OP stage >:o
					secondText = Message(opFrame, text="Oxidative phosphorylation", width=400)
					secondText.config(bg="lightgreen", font=('times',24, 'bold'), justify=LEFT)
					secondText.pack(fill=X)

					#Labels to show input and output
					outputsLabel = Label(opFrame, text="Outputs(x1 per glucose): " + "\n" + "")
					outputsLabel.pack(side="right")

					inputsLabel = Label(opFrame, text="Inputs(x1 per glucose): ")
					inputsLabel.pack(side="right")

					#Start with electron transport chain
					def oxidizeOP():
						outputsLabel.config(text="Outputs(x1 per glucose): " + "\n NAD+ 10" + "\n FAD+ 2")
						inputsLabel.config(text="Inputs(x1 per glucose): " + "\n NADH 10" + "\n FADH2 2")
						secondText.config(text="Electron shuttles NADH and FADH2 are oxidized at the electron transport chain. Electrons flow through the chain, the are driven by the increasing electronegativity of the ETC",bg="lightgreen", font=('times',24, 'bold'), justify=LEFT)
						waterButton = Button(opFrame,text="H+ protons", command = pumpProtons).pack(side="left")

					def pumpProtons():
						secondText.config(text="As electrons move throught the chain, protons (H+) are pumped into the intermembrane space. Oxygen serves as terminal proton acceptor and aquires 4 electrons and 2 protons, thus, H2O is released as wate product",bg="lightgreen", font=('times',24, 'bold'), justify=LEFT)
						outputsLabel.config(text="Outputs(x1 per glucose): " + "\n NAD+ 10" + "\n FAD+ 2" + "\n H2O")
						inputsLabel.config(text="Inputs(x1 per glucose): " + "\n NADH 10" + "\n FADH2 2" + "\n O2")
						chemiosmosisButton = Button(opFrame, text="Chemiosmosis", command=chemiosmosis).pack(side="left")

					def chemiosmosis():
						secondText.config(text="H+ protons go through a protein channel called ATP Synthase which yields 34 ATP",bg="lightgreen", font=('times',24, 'bold'), justify=LEFT)
						outputsLabel.config(text="Outputs(x1 per glucose): " + "\n NAD+ 10" + "\n FAD+ 2" + "\n H2O" + "\n ATP 34")

					oxidizeOP = Button(opFrame, text="Oxidize NADH and FADH2 in electron transport chain", command=oxidizeOP).pack(side="left")

				toOxidativePhosphoration = Button(krebsFrame, text="Last Stage!", command=lastStage).pack(side="left")

			oxidizeButton = Button(krebsFrame, text="Oxidize carbon crom acetyl group", command=oxidize)
			oxidizeButton.pack(side="left")
			

		pyruvateImage = Label(pyruvateFrame, image=acetylImage).pack(side="right")

	continueButton = Button(glycolysisFrame, text="Continue with Oxygen", command=primePyruvate).pack()
	fermentationButton = Button(glycolysisFrame, text="Continue without Oxygen", command=fermentation).pack()


	
	#def lactidAcid():


def newFrame():
	newFrame = Frame(width="750")
	newFrame.pack()
	return newFrame

button = Button(frame, text="Start!", command=next_slide)
button.pack()

root.mainloop()
