import tkinter as tk
from tkinter import ttk, TclError
from tkinter import filedialog
from PIL import Image,ImageTk


class UserProfile:
    def __init__(self) :
        self.root = tk.Tk()
        self.root.title("Card Generator")
        self.root.geometry('1500x1000')
        #Input Frame
        self.Title_frame = tk.Frame(self.root)
        self.Title_frame.pack(pady=10)
        self.Title_frame.configure(bg="#192F44")

        # self.title_label =tk.Label(self.Title_frame,text="User Profile Form",background="#192F44",fg="white",font=('Calibri',30))
        # self.title_label.grid(row=0,column=0,padx=10,pady=20,sticky="NS",ipadx=600,ipady=20)
        
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)
        self.input_frame.configure(bg="#20283E")

        name_label1 = tk.Label(self.input_frame, text="First Name :")
        name_label1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.name_entry1 = tk.Entry(self.input_frame)
        self.name_entry1.grid(row=1, column=1, padx=10, pady=7,ipadx=50)

        name_label2 = tk.Label(self.input_frame, text="Last Name :")
        name_label2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.name_entry2 = tk.Entry(self.input_frame)
        self.name_entry2.grid(row=2, column=1, padx=10, pady=7,ipadx=50)

        
        self.mobile_label = tk.Label(self.input_frame, text="Mobile Number :")
        self.mobile_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.name_entry3 = tk.Entry(self.input_frame)
        self.name_entry3.grid(row=3, column=1, padx=10, pady=7,ipadx=50)

        # self.profile_photo_label = tk.Label(self.input_frame, text="Profile Photo")
        # self.profile_photo_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # self.name_label5 = tk.Label(self.input_frame, text="No File Selected")
        # self.name_label5.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # self.photo_button = tk.Button(self.input_frame,text="Select Photo",command=self.browse_image)
        # self.photo_button.grid(row=5,column=0,padx=10,pady=10,sticky="w",columnspan=2,ipadx=130)

        self.gender_label = tk.Label(self.input_frame, text="Do you work?")
        self.gender_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        self.Gender_var =tk.StringVar()

        self.Male_Radio = tk.Radiobutton(self.input_frame,text="",variable=self.Gender_var,value="")
        self.Male_Radio.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        # self.Female_Radio = tk.Radiobutton(self.input_frame,text="Female",variable=self.Gender_var,value="Female")
        # self.Female_Radio.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        # self.height_label = tk.Label(self.input_frame, text="Height(cm):")
        # self.height_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")
        self.name_entry7 = tk.Entry(self.input_frame)
        self.name_entry7.grid(row=8, column=1, padx=10, pady=7,ipadx=50)

        self.image_display = tk.Label(self.input_frame)
        self.image_display.grid(row=9,column=0,columnspan=2,pady=10) 

        self.Submit_frame = tk.Frame(self.root)
        self.Submit_frame.pack(pady=10)
        self.Submit_frame.configure(bg="#20283E")

        self.Submit_button = tk.Button(self.Submit_frame,text="Submit",command=self.submit_form)
        self.Submit_button.grid(row=1,column=0,padx=10,pady=10,sticky="w")

        self.output_label = tk.Label(self.root, text="", font=('Calibri', 14))
        self.output_label.pack(pady=10)

        # Image display in the output window
        image_display_output = tk.Label(self.root)
        image_display_output.pack(pady=10)

        self.path_label = tk.Label(self.root, text="", font=('Calibri', 14))
        self.path_label.pack(pady=10)

    def browse_image(self):
            self.file_path =filedialog.askopenfilenames()
            if self.file_path:
                self.name_label5.config(text=self.file_path)

    def load_and_display(self): 
         self.image = Image.open(self.file_path)
         self.photo = ImageTk.PhotoImage(self.image)
         self.photo_button.config(image =self.photo)
         self.photo_button.config.image = self.photo
         self.image_display.config(image = self.photo)
         self.image_display.image = self.photo
    def submit_form(self):
        self.first_name = self.name_entry1.get()
        self.last_name = self.name_entry2.get()
        self.mobile_number = self.name_entry3.get()
        self.gender = self.Gender_var.get()  # Use Gender_var.get() to get the selected gender
        self.height = self.name_entry7.get()
        self.select_photo_path = self.name_label5.cget("text")

        # Display input details on the output window
        self.output_label.config(text=f"First Name: {self.first_name}\nLast Name: {self.last_name}\nMobile Number: {self.mobile_number}\nGender: {self.gender}\nHeight: {self.height}\nProfile Photo Path: {self.select_photo_path}")

        # Display the image in the output window
        if self.select_photo_path:
            image = Image.open(self.select_photo_path)
            image = image.resize((100, 100), Image.BICUBIC)  # Use Image.BICUBIC as the resampling filter
            photo = ImageTk.PhotoImage(image)
            self.image_display.config(image=photo)
            self.image_display.image = photo

            # Display the image path
            self.path_label.config(text=f"Image Path: {self.select_photo_path}")


    def run(self):
        self.root.mainloop()

    
if __name__ == "__main__":
    app=UserProfile()
    app.run()