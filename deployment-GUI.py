import tkinter as tk
import pickle
import numpy as np
from tkinter import messagebox


# Load pre-trained model

model = pickle.load(open("XGBoost",'rb'))  


# Create GUI window
window = tk.Tk()
window.title("House Price Predictor")
window.iconbitmap('winter_house.ico') # set icon the program 
window['bg'] = '#181818' # set bacgraund color
frame= tk.Frame(window, bg= '#303030')
frame.grid()
window= tk.LabelFrame(frame,text='User Information', bg= '#181818',foreground="orange")
window.grid(row=0,column=0)

# Create input labels
sqft_living_label = tk.Label(window, text="Sqft Living:",background='#181818',foreground="white")
sqft_living_label.grid(row=1, column=0)
grade_label = tk.Label(window, text="Grade:",background='#181818',foreground="white")
grade_label.grid(row=2, column=0)

long_label = tk.Label(window, text="longitude:",background='#181818',foreground="white")
long_label.grid(row=3, column=0)
lat_label = tk.Label(window, text="latitude:",background='#181818',foreground="white")
lat_label.grid(row=4, column=0)

bathrooms_label = tk.Label(window, text="Bathrooms:",background='#181818',foreground="white")
bathrooms_label.grid(row=5, column=0)
view_label = tk.Label(window, text="View:",background='#181818',foreground="white")
view_label.grid(row=6, column=0)
sqft_basement_label = tk.Label(window, text="Sqft Basement:",background='#181818',foreground="white")
sqft_basement_label.grid(row=7, column=0)
bedrooms_label = tk.Label(window, text="Bedrooms:",background='#181818',foreground="white")
bedrooms_label.grid(row=8, column=0)

# Create input fields
sqft_living_entry = tk.Entry(window)
sqft_living_entry.grid(row=1, column=1)
grade_entry = tk.Entry(window)
grade_entry.grid(row=2, column=1)
long_entry = tk.Entry(window)
long_entry.grid(row=3, column=1)
lat_entry = tk.Entry(window)
lat_entry.grid(row=4, column=1)
bathrooms_entry = tk.Entry(window)
bathrooms_entry.grid(row=5, column=1)
view_entry = tk.Entry(window)
view_entry.grid(row=6, column=1)
sqft_basement_entry = tk.Entry(window)
sqft_basement_entry.grid(row=7, column=1)
bedrooms_entry = tk.Entry(window)
bedrooms_entry.grid(row=8, column=1)

# Create function to predict price based on input values
def predict_price():
    # Get input values
    sqft_living = float(sqft_living_entry.get())
    grade = float(grade_entry.get())
    long = float(long_entry.get())
    lat = float(lat_entry.get())
    bathrooms = float(bathrooms_entry.get())
    view = float(view_entry.get())
    sqft_basement = float(sqft_basement_entry.get())
    bedrooms = float(bedrooms_entry.get())

    # Create feature vector
    features = [[sqft_living, grade, long, lat, bathrooms, view, sqft_basement, bedrooms]]
    X=np.array(features)
    # Predict price using pre-trained model
    predicted_price = model.predict(X)[0]
    print(f"Predicted Price: ${predicted_price:,.2f}")
    # Update output label with predicted price

    messagebox.showinfo(title='prediction',message=f"Predicted Price: ${predicted_price:,.2f}") #Result window

    #for loop to make a distance between label and entry box equal
for widget in window.winfo_children():
    widget.grid_configure(padx=18,pady=5)


# Make prediction button
button=tk.Button(frame ,text='Enter data',command=predict_price,background='black',foreground="orange")
button.grid(row=9 ,column=0,sticky='news',padx=18,pady=10)
# make a button to stop prediction proccess 
button2=tk.Button(frame ,text='stop',command=frame.quit,background='black',foreground="orange")
button2.grid(row=10 ,column=0,sticky='news',padx=18,pady=10)




import tkinter as tk

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip = None
        self.id = None
        self.x = self.y = 0

    def showtip(self):
        "Display tooltip"
        self.id = self.widget.after(500, self.show)
        
    def hidetip(self):
        "Hide tooltip"
        if self.tip:
            self.tip.destroy()
            self.tip = None

    def show(self):
        "Create tooltip"
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tip = tk.Toplevel(self.widget)
        self.tip.wm_overrideredirect(True)
        self.tip.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tip, text=self.text, justify='left', background="#ffffff", relief='solid', borderwidth=1)
        label.pack(ipadx=1)

    def __del__(self):
        "Destructor"
        if self.id:
            self.widget.after_cancel(self.id)

# Example usage:

# Create a tooltip for the button
tip = Tooltip(sqft_living_label, "What is the size of the living area in square feet.")
sqft_living_label.bind("<Enter>", lambda event: tip.showtip())
sqft_living_label.bind("<Leave>", lambda event: tip.hidetip())

tip1 = Tooltip(grade_label, "What is the Grade rank from (1-13)")
grade_label.bind("<Enter>", lambda event: tip1.showtip())
grade_label.bind("<Leave>", lambda event: tip1.hidetip())

tip2 = Tooltip(long_label, "What is the longitude:")
long_label.bind("<Enter>", lambda event: tip2.showtip())
long_label.bind("<Leave>", lambda event: tip2.hidetip())

tip3 = Tooltip(lat_label, "What is the latitude:")
lat_label.bind("<Enter>", lambda event: tip3.showtip())
lat_label.bind("<Leave>", lambda event: tip3.hidetip())

tip4 = Tooltip(bathrooms_label, "How many bathrooms are in the house.")
bathrooms_label.bind("<Enter>", lambda event: tip4.showtip())
bathrooms_label.bind("<Leave>", lambda event: tip4.hidetip())

tip5 = Tooltip(view_entry, "What is the view rank, from (0-4).")
view_label.bind("<Enter>", lambda event: tip5.showtip())
view_label.bind("<Leave>", lambda event: tip5.hidetip())

tip6 = Tooltip(sqft_basement_label, "What is the size of the basement in the house?")
sqft_basement_label.bind("<Enter>", lambda event: tip6.showtip())
sqft_basement_label.bind("<Leave>", lambda event: tip6.hidetip())

tip7 = Tooltip(bathrooms_label, "How many bedrooms are in the house.")
bedrooms_label.bind("<Enter>", lambda event: tip7.showtip())
bedrooms_label.bind("<Leave>", lambda event: tip7.hidetip())


window.mainloop()
