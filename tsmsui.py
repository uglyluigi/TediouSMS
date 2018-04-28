""" base_GUI_ui.py --

UI generated by GUI Builder Build 146 on 2018-04-23 10:26:02 from:
C:/Users/chris/Desktop/CYEN PROJ/base_GUI.ui
THIS IS AN AUTOGENERATED FILE AND SHOULD NOT BE EDITED.
The associated callback file should be modified instead.
"""

import Tkinter
import os # needed for relative image paths

# Using new-style classes: create empty base class object
# for compatibility with older python interps
#if sys.version_info < (2, 2):
#    class object:
#        pass

class Base_GUI(object):

	_images = [] # Holds image refs to prevent GC
	
	def __init__(self, root):

		# Widget Initialization
		self.sending_label = Tkinter.Label(root,
			font = "{MS Sans Serif} 14 bold",
			text = "Sending",
		)
		self.receiving_label = Tkinter.Label(root,
			font = "{MS Sans Serif} 14 bold",
			text = "Receiving",
		)
		self._button_2 = Tkinter.Button(root,
			font = "{MS Sans Serif} 14 bold",
			text = "SEND",
		)
		self._entry_1 = Tkinter.Entry(root,
			width = 0,
		)
		self._label_5 = Tkinter.Label(root,
			font = "{MS Sans Serif} 12",
			text = "Recipient IP Address",
		)
		self._label_6 = Tkinter.Label(root,
			font = "{MS Sans Serif} 12",
			text = "Your IP Address",
		)
		self._text_2 = Tkinter.Text(root,
			height = 0,
			width = 0,
		)
		self._text_3 = Tkinter.Text(root,
			height = 0,
			width = 0,
		)
		self._entry_2 = Tkinter.Entry(root,
			width = 0,
		)
		self._checkbutton_1 = Tkinter.Checkbutton(root,
			font = "{MS Sans Serif} 12 bold",
			text = "Listening on IP",
		)

		# widget commands


		self._button_2.configure(
			command = self._button_2_command
		)
		
		self._entry_1.configure(
			invalidcommand = self._entry_1_invalidcommand
		)
		
		self._entry_1.configure(
			validatecommand = self._entry_1_validatecommand
		)
		
		self._entry_1.configure(
			xscrollcommand = self._entry_1_xscrollcommand
		)
		
		self._text_2.configure(
			xscrollcommand = self._text_2_xscrollcommand
		)
		
		self._text_2.configure(
			yscrollcommand = self._text_2_yscrollcommand
		)
		
		self._text_3.configure(
			xscrollcommand = self._text_3_xscrollcommand
		)
		
		self._text_3.configure(
			yscrollcommand = self._text_3_yscrollcommand
		)
		
		self._entry_2.configure(
			invalidcommand = self._entry_2_invalidcommand
		)
		
		self._entry_2.configure(
			validatecommand = self._entry_2_validatecommand
		)
		
		self._entry_2.configure(
			xscrollcommand = self._entry_2_xscrollcommand
		)
		
		self._checkbutton_1.configure(
			command = self._checkbutton_1_command
		)


		# Geometry Management
		self.sending_label.grid(
			in_    = root,
			column = 1,
			row    = 1,
			columnspan = 1,
			ipadx = 0,
			ipady = 0,
			padx = 0,
			pady = 0,
			rowspan = 1,
			sticky = ""
		)
		self.receiving_label.grid(
			in_    = root,
			column = 2,
			row    = 1,
			columnspan = 1,
			ipadx = 0,
			ipady = 0,
			padx = 0,
			pady = 0,
			rowspan = 1,
			sticky = ""
		)
		self._button_2.grid(
			in_    = root,
			column = 1,
			row    = 3,
			columnspan = 1,
			ipadx = 0,
			ipady = 0,
			padx = 0,
			pady = 0,
			rowspan = 1,
			sticky = ""
		)
		self._entry_1.grid(
			in_    = root,
			column = 2,
			row    = 5,
			columnspan = 1,
			ipadx = 0,
			ipady = 0,
			padx = 0,
			pady = 0,
			rowspan = 1,
			sticky = "ew"
		)
		self._label_5.grid(
			in_    = root,
			column = 2,
			row    = 4,
			columnspan = 1,
			ipadx = 0,
			ipady = 0,
			padx = 0,
			pady = 0,
			rowspan = 1,
			sticky = ""
		)
		self._label_6.grid(
			in_    = root,
			column = 1,
			row    = 4,
			columnspan = 1,
			ipadx = 0,
			ipady = 0,
			padx = 0,
			pady = 0,
			rowspan = 1,
			sticky = ""
		)
		self._text_2.grid(
			in_    = root,
			column = 1,
			row    = 2,
			columnspan = 1,
			ipadx = 0,
			ipady = 0,
			padx = 0,
			pady = 0,
			rowspan = 1,
			sticky = "news"
		)
		self._text_3.grid(
			in_    = root,
			column = 2,
			row    = 2,
			columnspan = 1,
			ipadx = 0,
			ipady = 0,
			padx = 0,
			pady = 0,
			rowspan = 1,
			sticky = "news"
		)
		
		self._entry_2.grid(
			in_    = root,
			column = 1,
			row    = 5,
			columnspan = 1,
			ipadx = 0,
			ipady = 0,
			padx = 0,
			pady = 0,
			rowspan = 1,
			sticky = "ew"
		)
		
		self._checkbutton_1.grid(
			in_    = root,
			column = 2,
			row    = 3,
			columnspan = 1,
			ipadx = 0,
			ipady = 0,
			padx = 0,
			pady = 0,
			rowspan = 1,
			sticky = ""
		)


		# Resize Behavior
		root.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
		root.grid_rowconfigure(2, weight = 0, minsize = 133, pad = 0)
		root.grid_rowconfigure(3, weight = 0, minsize = 102, pad = 0)
		root.grid_rowconfigure(4, weight = 0, minsize = 21, pad = 0)
		root.grid_rowconfigure(5, weight = 0, minsize = 30, pad = 0)
		root.grid_rowconfigure(6, weight = 0, minsize = 2, pad = 0)
		root.grid_columnconfigure(1, weight = 0, minsize = 538, pad = 0)
		root.grid_columnconfigure(2, weight = 0, minsize = 538, pad = 0)




