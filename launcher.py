from arm_characterization.data_logger import main as armDataLogger
from arm_characterization.data_analyzer import main as armDataAnalyzer

from drive_characterization.data_logger import main as driveDataLogger
from drive_characterization.data_analyzer import main as driveDataAnalyzer

import tkinter
from tkinter import *

gui = tkinter.Tk()

if __name__ == "__main__":
    Label(gui, text='Robot Characterization Launcher',
        font=("Helvetica", 22),
        padx=10, pady=10).grid(row=0, column=0, sticky=E+W)

    def _wrapWindowFunc(toWrap):
        def wrapped():
            gui.withdraw()
            newWindow = Toplevel()
            toWrap(newWindow)
            newWindow.wait_window()
            gui.deiconify()
        return wrapped
        

    row = 1
    def _makeButtons(parentFrame, mechanismName, dataLoggerFunc, dataAnalyzerFunc):
        global row
        
        Label(parentFrame, text=f"{mechanismName}:",
            anchor=W, pady=5).grid(row=row, column=0, sticky=E+W)
        row += 1

        frame = Frame(parentFrame, bd=2, relief=GROOVE)
        frame.grid(row=row, column=0, sticky=E+W)
        frame.columnconfigure(0, weight=1)
        row += 1

        Button(frame, text=f"{mechanismName} Data Logger",
            command=dataLoggerFunc).grid(row=1, column=0, sticky=E+W)
        Button(frame, text=f"{mechanismName} Data Analyzer",
            command=_wrapWindowFunc(dataAnalyzerFunc)).grid(row=2, column=0, sticky=E+W)

    _makeButtons(gui, "Arm", armDataLogger, armDataAnalyzer)
    _makeButtons(gui, "Drivetrain", driveDataLogger, driveDataAnalyzer)
    
    gui.title("RobotPy Robot Characterization Launcher")
    gui.mainloop()

