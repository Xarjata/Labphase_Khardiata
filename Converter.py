import tkinter as tk

def fahrenheit_to_celsius(): 
    try:
      temp_celcius = float(ent_temperature.get())
      to_celcius = (temp_celcius-32) / 1.8

      lbl_result.config(text=f"{to_celcius:.2f} \N{DEGREE CELSIUS}")

    except ValueError: 
       lbl_result.config(text="Saisie invalide")


window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)
frm_entry = tk.Frame(master=window)

ent_temperature = tk.Entry(master=frm_entry, width=10)

lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}") 
    
frm_entry.grid(row=0, column=0, padx=10, pady= 10), btn_convert.grid(row=0, column=1, pady=10) 
ent_temperature.grid(row=0, column=0, padx=5, pady=5)
lbl_temp.grid(row=0, column=1, padx=5)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)


window.mainloop()