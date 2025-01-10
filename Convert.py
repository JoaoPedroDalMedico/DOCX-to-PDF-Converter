import os 
from tkinter import Tk, Label, Button, filedialog, messagebox, StringVar
from docx2pdf import convert

# Function select file
def select_file():
    # Open window to select file .docx
    file = filedialog.askopenfilename(title = " Select a file DOCX", filetypes= [("File DOCX", "*.docx")])
    if file:
        path_file.set(file)
        label_file["text"] = f"File selected: {os.path.basename(file)}"

# Function convert to PDF
def convert_to_pdf():
    # Check if a file was selected
    if not path_file.get():
        messagebox.showerror("Error", "Please, select a file .DOCX")
        return
    
    try:
        # Convert the selected file to PDF
        convert(path_file.get())
        messagebox.showinfo("Success", "File converted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initialize Tkinter
root = Tk()
root.title("DOCX to PDF Converter")
root.geometry("300x200")

# StringVar to store the file path
path_file = StringVar()

# Label to display the selected file
label_file = Label(root, text="No file selected")
label_file.pack(pady=20)

# Button to select file
button_select = Button(root, text="Select File", command=select_file)
button_select.pack(pady=10)

# Button to convert file
button_convert = Button(root, text="Convert to PDF", command=convert_to_pdf)
button_convert.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
