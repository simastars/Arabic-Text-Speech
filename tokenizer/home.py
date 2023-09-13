from tk import *

class GridExample(Frame):
        def __init__(self,master):
            Frame.__init__(self,master)
            self.grid()
            top_text=Label(self,text="This text appears on top left")
            top_text.grid() # Default position 0, 0
            bottom_text=Label(self,text="This text appears on bottom left")
            bottom_text.grid() # Default position 1, 0
            right_text=Label(self,text="This text appears on the right and spans both rows",
            wraplength=100)
            # Position is 0,1
            # Rowspan means actual position is [0-1],1
            right_text.grid(row=0,column=1,rowspan=2)
        # Spawn Window
if __name__=="__main__":
    root=Tk()
    grid_frame=GridExample(root)
    grid_frame.mainloop()