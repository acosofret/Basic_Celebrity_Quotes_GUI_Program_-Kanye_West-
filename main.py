from tkinter import *
import requests

# We use tkinter for GUI


# We define a function that pulls random Kanye West quotes from a free REST API service (website below):
def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


# We set our GUI window (for more details check the tkinter documentation:
window = Tk() # GUI Window Object
window.title("Kanye Says...") # Window Title
window.config(padx=50, pady=50) # Window padding

canvas = Canvas(width=300, height=414) # Window Size (as a Canvas)
# the we add the image in which we want our quote text to be shown:
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
# and we add the text. ("Click on Kanye's face" is the default value - serving as instructions)
quote_text = canvas.create_text(150, 207, text=f"Click on Kanye's face", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0) # We format the Canvas

# Then we add a image showing Kanye's face as a button. Upon click this button it will trigger the get_quote function
# that will pull a new quote from the kanye.rest server and display it as the new text on the quote space.
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()