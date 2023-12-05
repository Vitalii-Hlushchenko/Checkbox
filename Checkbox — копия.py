import tkinter as tk

class TriStateCheckbutton:
    def __init__(self, master, text="TriStateCheckbutton"):
        self.master = master
        self.state = tk.IntVar()
        self.checkbutton = tk.Checkbutton(master, variable=self.state)
        self.checkbutton.pack()
        self.label = tk.Label(master, text=text)
        self.label.pack()
        self.update_label()
        self.child_checkboxes = []

    def update_label(self):
        if hasattr(self, 'is_main') and self.is_main:
            child_states = [checkbox.get_state() for checkbox in self.child_checkboxes]

            if all(state == 1 for state in child_states):
                self.checkbutton.config(bg="green", tristatevalue=1)  
            elif any(state == 1 for state in child_states):
                self.checkbutton.config(bg="orange") 
            else:
                self.checkbutton.config(bg="red") 

    def set_state(self, new_state):
        self.state.set(new_state)
        self.update_label()

    def get_state(self):
        return self.state.get()

    def add_child_checkbox(self, child_checkbox):
        self.child_checkboxes.append(child_checkbox)
        
        child_checkbox.checkbutton.config(command=self.update_label)

    def toggle_child_checkboxes(self):
        
        new_state = self.get_state()
        for child_checkbox in self.child_checkboxes:
            child_checkbox.set_state(new_state)

        self.update_label()


root = tk.Tk()
root.title("TriStateCheckbutton Example")


main_checkbox = TriStateCheckbutton(root, text="Main checkbox")
main_checkbox.is_main = True  
main_checkbox.checkbutton.config(command=main_checkbox.toggle_child_checkboxes) 

child_checkbox1 = TriStateCheckbutton(root, text="Checkbox")
child_checkbox2 = TriStateCheckbutton(root, text="Checkbox")
child_checkbox3 = TriStateCheckbutton(root, text="Checkbox")

main_checkbox.add_child_checkbox(child_checkbox1)
main_checkbox.add_child_checkbox(child_checkbox2)
main_checkbox.add_child_checkbox(child_checkbox3)

root.mainloop()
