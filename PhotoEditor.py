from tkinter import *
from PIL import ImageTk, Image, ImageOps, UnidentifiedImageError, ImageFilter, ImageEnhance
from tkinter import filedialog, messagebox
import numpy as np
import random

editor = Tk()
editor.title("21827943 A. Atahan Türk - 21828054 Yuşa Zorlu Photo Editor")
editor.geometry("1100x750")
editor.configure(bg="aquamarine3")

global myimage
myimage, grayscaled, mirrored, blurred, deblurred, rotated90, rotated180, rotated270, flipped, brighted, contred, cropped, original, \
satred, detected, reversedorg, rgbimage, noised = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None


def load_img():

    global openedfile
    openedfile = filedialog.askopenfilename(title ='Choose The Image To Load')
    try:
        global myimage
        myimage = Image.open(openedfile)
        img = myimage.resize((355, 355), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        inputCanvas.create_image(180, 180, image=img)
        inputCanvas.image=img
        outputCanvas.delete("all")
        outputCanvas.create_text(177,177,text="Edited Image", fill="aquamarine3", font=("Showcard Gothic",30))
        rgbreset()
        adjustreset()
        cropreset()
    except AttributeError:
        pass
    except UnidentifiedImageError:
        messagebox.showerror("Inappropriate File Type", "To apply a filter, you should upload a file which has an image file extension (.png, .jpg, .jpeg etc.)")


def reset_image():
    global myimage
    myimage = None
    outputCanvas.image = None
    inputCanvas.delete("all")
    inputCanvas.create_text(177,177,text="Input Image", fill="aquamarine3", font=("Showcard Gothic",30))
    outputCanvas.delete("all")
    outputCanvas.create_text(177,177,text="Edited Image", fill="aquamarine3", font=("Showcard Gothic",30))
    rgbreset()
    adjustreset()
    cropreset()


def save_image():
    global myimage, openedfile, grayscaled, mirrored, blurred, deblurred, rotated90, rotated180, rotated270, flipped, brighted, contred, satred, detected, reversedorg,\
        rgbedr, rgbimage, noised, noised1, cropped, cropped1, cropped2, original, original1,\
        flipped1,mirrored1, blurred1, deblurred1, rotated90_1, rotated180_1, rotated270_1, flipped1, brighted1, brighted2, contred1, contred2, satred1, satred2, detected1
    try:

        if myimage == None:
            messagebox.showerror("No Input Image", "To save an image, you should upload and edit an image first")
        elif outputCanvas.image == None:
            messagebox.showerror("No Input Image", "To save an image, you should edit the image first")
        else:
            file = filedialog.asksaveasfilename(defaultextension =".png",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])

        if outputCanvas.image == grayscaled1:
            grayscaled.save(file)
        if outputCanvas.image == mirrored1:
            mirrored.save(file)
        if outputCanvas.image == blurred1:
            blurred.save(file)
        if outputCanvas.image == deblurred1:
            deblurred.save(file)
        if outputCanvas.image == rotated90_1:
            rotated90.save(file)
        if outputCanvas.image == rotated180_1:
            rotated180.save(file)
        if outputCanvas.image == rotated270_1:
            rotated270.save(file)
        if outputCanvas.image == flipped1:
            flipped.save(file)
        if outputCanvas.image == brighted2:
            brighted1.save(file)
        if outputCanvas.image == contred2:
            contred1.save(file)
        if outputCanvas.image == satred2:
            satred1.save(file)
        if outputCanvas.image == detected1:
            detected.save(file)
        if outputCanvas.image == reversed1:
            reversedorg.save(file)
        if outputCanvas.image == rgbedr:
            rgbimage.save(file)
        if outputCanvas.image == noised1:
            noised.save(file)
        if outputCanvas.image == cropped2:
            cropped.save(file)
    except AttributeError:
        pass
    except ValueError:
        pass
    except UnboundLocalError:
        pass


def grayscale():
    global myimage
    global grayscaled, grayscaled1
    if myimage is None:
        messagebox.showerror("No Input Image", "To edit an image, you should upload an image first")
    elif myimage.mode == "L":
        messagebox.showerror("Wrong Input Image", "The image that you are trying to apply grayscale filter is already a grayscale image")
    else:
        grayscaled = myimage.copy()
        grayscaled = ImageOps.grayscale(grayscaled)
        grayscaled1 = grayscaled.resize((355, 355), Image.ANTIALIAS)
        grayscaled1 = ImageTk.PhotoImage(grayscaled1)
        outputCanvas.create_image(180,180,image=grayscaled1)
        outputCanvas.image = grayscaled1
        cropreset()
        adjustreset()
        rgbreset()


def flip():
    global myimage
    global flipped, flipped1
    if myimage is None:
        messagebox.showerror("No Input Image", "To edit an image, you should upload an image first")
    else:
        flipped = myimage.copy()
        flipped = ImageOps.mirror(flipped)
        flipped = flipped.rotate(180)
        flipped1 = flipped.resize((355, 355), Image.ANTIALIAS)
        flipped1 = ImageTk.PhotoImage(flipped1)
        outputCanvas.create_image(180,180,image=flipped1)
        outputCanvas.image = flipped1
        cropreset()
        adjustreset()
        rgbreset()


def mirror():
    global myimage
    global mirrored, mirrored1
    if myimage is None:
        messagebox.showerror("No Input Image", "To edit an image, you should upload an image first")
    else:
        mirrored = myimage.copy()
        mirrored = ImageOps.mirror(mirrored)
        mirrored1 = mirrored.resize((355, 355), Image.ANTIALIAS)
        mirrored1 = ImageTk.PhotoImage(mirrored1)
        outputCanvas.create_image(180,180,image=mirrored1)
        outputCanvas.image = mirrored1
        cropreset()
        adjustreset()
        rgbreset()


def rotate_90():
    global myimage
    global rotated90, rotated90_1
    if myimage is None:
        messagebox.showerror("No Input Image", "To edit an image, you should upload an image first")
    else:
        rotated90 = myimage.copy()
        rotated90 = rotated90.rotate(90,expand=True)
        rotated90_1 = rotated90.resize((355, 355), Image.ANTIALIAS)
        rotated90_1 = ImageTk.PhotoImage(rotated90_1)
        outputCanvas.create_image(180,180,image=rotated90_1)
        outputCanvas.image = rotated90_1
        cropreset()
        adjustreset()
        rgbreset()


def rotate_180():
    global myimage
    global rotated180, rotated180_1
    if myimage is None:
        messagebox.showerror("No Input Image", "To edit an image, you should upload an image first")
    else:
        rotated180 = myimage.copy()
        rotated180 = rotated180.rotate(180)
        rotated180_1 = rotated180.resize((355, 355), Image.ANTIALIAS)
        rotated180_1 = ImageTk.PhotoImage(rotated180_1)
        outputCanvas.create_image(180,180,image=rotated180_1)
        outputCanvas.image = rotated180_1
        cropreset()
        adjustreset()
        rgbreset()


def rotate_270():
    global myimage
    global rotated270, rotated270_1
    if myimage is None:
        messagebox.showerror("No Input Image", "To edit an image, you should upload an image first")
    else:
        rotated270 = myimage.copy()
        rotated270 = rotated270.rotate(270,expand=True)
        rotated270_1 = rotated270.resize((355, 355), Image.ANTIALIAS)
        rotated270_1 = ImageTk.PhotoImage(rotated270_1)
        outputCanvas.create_image(180,180,image=rotated270_1)
        outputCanvas.image = rotated270_1
        cropreset()
        adjustreset()
        rgbreset()


def blur():
    global myimage
    global blurred, blurred1
    if myimage is None:
        messagebox.showerror("No Input Image", "To edit an image, you should upload an image first")
    else:
        if myimage.mode != "L" or myimage.mode != "RGB":
            myimage = myimage.convert("RGB")
        blurred = myimage.copy()
        blurred = blurred.filter(ImageFilter.GaussianBlur(5))
        blurred1 = blurred.resize((355, 355), Image.ANTIALIAS)
        blurred1 = ImageTk.PhotoImage(blurred1)
        outputCanvas.create_image(180,180,image=blurred1)
        outputCanvas.image = blurred1
        cropreset()
        adjustreset()
        rgbreset()


def deblur():
    global myimage
    global deblurred, deblurred1
    if myimage is None:
        messagebox.showerror("No Input Image", "To edit an image, you should upload an image first")
    else:
        if myimage.mode != "L" or myimage.mode != "RGB":
            myimage = myimage.convert("RGB")
        deblurred = myimage.copy()
        deblurred = deblurred.filter(ImageFilter.SHARPEN)
        deblurred = deblurred.filter(ImageFilter.SHARPEN)
        deblurred1 = deblurred.resize((355, 355), Image.ANTIALIAS)
        deblurred1 = ImageTk.PhotoImage(deblurred1)
        outputCanvas.create_image(180,180,image=deblurred1)
        outputCanvas.image = deblurred1
        cropreset()
        adjustreset()
        rgbreset()


def detect_edges():
    global myimage
    global detected, detected1
    if myimage is None:
        messagebox.showerror("No Input Image", "To edit an image, you should upload an image first")
    else:
        detected = myimage.copy()
        detected = detected.filter(ImageFilter.FIND_EDGES)
        detected1 = detected.resize((355, 355), Image.ANTIALIAS)
        detected1 = ImageTk.PhotoImage(detected1)
        outputCanvas.create_image(180,180,image=detected1)
        outputCanvas.image = detected1
        cropreset()
        adjustreset()
        rgbreset()


def reverse_colors():
    global myimage
    global reversedorg, reversed1
    if myimage is None:
        messagebox.showerror("No Input Image", "To edit an image, you should upload an image first")
    else:
        if myimage.mode != "L" or myimage.mode != "RGB":
            myimage = myimage.convert("RGB")
        reversedorg = myimage.copy()
        reversedorg = ImageOps.invert(reversedorg)
        reversed1 = reversedorg.resize((355, 355), Image.ANTIALIAS)
        reversed1 = ImageTk.PhotoImage(reversed1)
        outputCanvas.create_image(180,180,image=reversed1)
        outputCanvas.image = reversed1
        cropreset()
        adjustreset()
        rgbreset()


def addNoise():
    global myimage
    if myimage is None:
        messagebox.showerror("No Input Image", "To edit an image, you should upload an image first")
    else:
        if myimage.mode != "L" or myimage.mode != "RGB":
            myimage = myimage.convert("RGB")
        global noised, noised1
        noised = myimage.copy()
        pixelnoised = np.array(noised)
        x_lim, y_lim = noised.size
        ran_val_y = random.randint(2,2)
        for x in range(0, y_lim, ran_val_y):
            ran_val_x = random.randint(2, 2)
            for y in range(0, x_lim, ran_val_x):
                r = round(random.random()*255)
                if r > 255:
                    r = 255
                g = round(random.random()*255)
                if g>255:
                    g=255
                b = round(random.random()*255)
                if b>255:
                    b=255
                pixelnoised[x,y] = r,g,b
        noised = pixelnoised
        noised = Image.fromarray(noised)
        noised1 = noised.resize((355, 355), Image.ANTIALIAS)
        noised1 = ImageTk.PhotoImage(noised1)
        outputCanvas.create_image(180,180,image=noised1)
        outputCanvas.image = noised1
        cropreset()
        adjustreset()
        rgbreset()


def brightness(hebelehubele):
    global myimage
    global brighted, brighted1, brighted2
    if myimage != None:
        if myimage.mode != "L" or myimage.mode != "RGB":
            myimage = myimage.convert("RGB")
        brighted = myimage.copy()
        myval = (varBright.get()/5)
        if myval == 0:
            myval = 0.1 #I think getting a completely dark image doesn't make any sense, so that's why I did this if statement
        brighted = ImageEnhance.Brightness(brighted)
        brighted1 = brighted.enhance(myval)
        brighted2 = brighted1.resize((355, 355), Image.ANTIALIAS)
        brighted2 = ImageTk.PhotoImage(brighted2)
        outputCanvas.create_image(180,180,image=brighted2)
        outputCanvas.image = brighted2
        cropreset()
        rgbreset()
    if outputCanvas.image == brighted2:
        scaleContrast.set(5)
        scaleSaturation.set(5)
    if myimage == None:
        scaleBright.set(5)


def contrast(hebelehubele):
    global myimage
    global contred, contred1, contred2
    if myimage != None:
        if myimage.mode != "L" or myimage.mode != "RGB":
            myimage = myimage.convert("RGB")
        contred = myimage.copy()
        myval = (varContrast.get()/5)
        if myval == 0:
            myval = 0.1 #Same logic with the brightness
        contred = ImageEnhance.Contrast(contred)
        contred1 = contred.enhance(myval)
        contred2 = contred1.resize((355, 355), Image.ANTIALIAS)
        contred2 = ImageTk.PhotoImage(contred2)
        outputCanvas.create_image(180,180,image=contred2)
        outputCanvas.image = contred2
        cropreset()
        rgbreset()
    if outputCanvas.image == contred2:
        scaleSaturation.set(5)
        scaleBright.set(5)
    if myimage == None:
        scaleContrast.set(5)


def saturation(hebelehubele):
    global myimage
    if myimage != None:
        if myimage.mode != "L" or myimage.mode != "RGB":
            myimage = myimage.convert("RGB")
        global satred, satred1, satred2
        satred = myimage.copy()
        myval = (varSaturation.get()/5)
        satred = ImageEnhance.Color(satred)
        satred1 = satred.enhance(myval)
        satred2 = satred1.resize((355, 355), Image.ANTIALIAS)
        satred2 = ImageTk.PhotoImage(satred2)
        outputCanvas.create_image(180,180,image=satred2)
        outputCanvas.image = satred2
        rgbreset()
        cropreset()
    if outputCanvas.image == satred2:
        scaleBright.set(5)
        scaleContrast.set(5)
    if myimage == None:
        scaleSaturation.set(5)


def rgb(hebelehubele):
    global myimage
    if myimage != None:
        if myimage.mode != "L" or myimage.mode != "RGB":
            myimage = myimage.convert("RGB")
        global rgbimage, rgbedr
        rgbimage = myimage.copy()
        pixel = np.array(rgbimage)
        x_lim, y_lim = rgbimage.size
        redscale = varRed.get()
        greenscale = varGreen.get()
        bluescale = varBlue.get()
        for x in range(0,y_lim):
            for y in range(0,x_lim):
                r,g,b = pixel[x,y]
                r = round(r * (redscale/5))
                if r>255:
                    r =255
                g = round(g * (greenscale/5))
                if g>255:
                    g =255
                b = round(b * (bluescale/5))
                if b>255:
                    b=255

                pixel[x,y] = r,g,b
        rgbimage = pixel
        rgbimage = Image.fromarray(rgbimage)
        rgbedr = rgbimage.resize((355, 355), Image.ANTIALIAS)
        rgbedr = ImageTk.PhotoImage(rgbedr)
        outputCanvas.create_image(180,180,image=rgbedr)
        outputCanvas.image = rgbedr
        adjustreset()
        cropreset()
    if myimage == None:
        scaleRed.set(5)
        scaleGreen.set(5)
        scaleBlue.set(5)


def crop(hebelehubele):
    global myimage
    outputCanvas.delete("all")
    outputCanvas.create_text(177,177,text="Edited Image", fill="aquamarine3", font=("Showcard Gothic",30))
    if myimage != None:
        global cropped, cropped1, cropped2
        cropped = myimage.copy()
        (originalx,originaly) = cropped.size
        ratiox, ratioy = originalx/355, originaly/355
        cropped1 = cropped.resize((355, 355), Image.ANTIALIAS)
        (left,upper,right,bottom) = (scaleX_start.get(),scaleY_start.get(),scaleX_end.get(),scaleY_end.get())
        cropped1 = cropped1.crop((left,upper,right,bottom))
        cropped2 = ImageTk.PhotoImage(cropped1)
        outputCanvas.create_image(180,180,image=cropped2)
        outputCanvas.image = cropped2
        cropped = cropped.crop((left*ratiox,upper*ratioy,right*ratiox,bottom*ratioy))
        adjustreset()
        rgbreset()
    if myimage == None:
        scaleX_start.set(0)
        scaleX_end.set(355)
        scaleY_start.set(0)
        scaleY_end.set(355)


def originalimage():
    global myimage
    if myimage is None:
        messagebox.showerror("No Input Image", "To edit an image, you should upload an image first")
    else:
        global original, original1
        original = myimage.copy()
        original1 = original.resize((355, 355), Image.ANTIALIAS)
        original1 = ImageTk.PhotoImage(original1)
        outputCanvas.create_image(180,180,image=original1)
        outputCanvas.image = original1
        cropreset()
        adjustreset()
        rgbreset()


def cropreset():
    varX_start.set(0)
    varX_end.set(355)
    varY_start.set(0)
    varY_end.set(355)


def adjustreset():
    varBright.set(5)
    varContrast.set(5)
    varSaturation.set(5)


def rgbreset():
    varRed.set(5)
    varGreen.set(5)
    varBlue.set(5)


grayscaled1, mirrored1, rotated90_1, rotated180_1, rotated270_1, blurred1, deblurred1,noised1, original1,\
    flipped1, brighted1, brighted2, contred1, contred2, satred1, satred2, detected1, cropped1, cropped2,\
    reversed1, rgbedr= None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None


titleLabel = Label(editor, text=" 21827943 - 21828054 Photo Editor ", font=("Showcard Gothic", 25), fg="aquamarine4", bg="aquamarine2", relief=RAISED, bd=5, pady=10, padx=264)
titleLabel.place(x=0, y=0)

menubar = Menu(editor)
editor.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Load and Show Image", command=load_img)
fileMenu.add_command(label="Save Image", command=save_image)
fileMenu.add_command(label="Reset Image", command=reset_image)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)
inputCanvas = Canvas(editor, width="350", height="350", relief=RIDGE, bd=3, bg="aquamarine1")
inputCanvas.create_text(177,177,text="Input Image", fill="aquamarine3", font=("Showcard Gothic",30))
inputCanvas.place(x=190, y = 100)
outputCanvas = Canvas(editor, width="350", height="350", relief=RIDGE, bd=3, bg="aquamarine1")
outputCanvas.create_text(177,177,text="Edited Image", fill="aquamarine3", font=("Showcard Gothic",30))
outputCanvas.place(x=555, y = 100)
outputCanvas.image = None

filterFrame = LabelFrame(editor, text="Filters", font=("Arial Black",12), padx=10, pady=10,bg="aquamarine4",fg="aquamarine1")
filterFrame.place(x=7,y=150)
gsButton = Button(filterFrame, text="Grayscale", command=grayscale, font=("Showcard Gothic", 12), width=13,bg="aquamarine4", fg="mediumspringgreen",relief=RAISED, bd=3)
gsButton.grid(row=0,column=0)
blurButton = Button(filterFrame, text="Blur", font=("Showcard Gothic", 12), width=13, command=blur,bg="aquamarine4", fg="mediumspringgreen",relief=RAISED, bd=3)
blurButton.grid(row=1,column=0)
deblurButton = Button(filterFrame, text="Deblur", font=("Showcard Gothic", 12), width=13, command=deblur,bg="aquamarine4", fg="mediumspringgreen",relief=RAISED, bd=3)
deblurButton.grid(row=2,column=0)
negativeButton = Button(filterFrame, text="Reverse Colours", font=("Showcard Gothic", 13), width=13, command=reverse_colors,bg="aquamarine4", fg="mediumspringgreen",relief=RAISED, bd=3)
negativeButton.grid(row=3, column=0)
addnoiseButton = Button(filterFrame, text="Add Noise", font=("Showcard Gothic", 12), width=13, command=addNoise,bg="aquamarine4", fg="mediumspringgreen",relief=RAISED, bd=3)
addnoiseButton.grid(row=7,column=0)
detectedgesButton = Button(filterFrame, text="Detect Edges", font=("Showcard Gothic", 12), width=13, command=detect_edges,bg="aquamarine4", fg="mediumspringgreen",relief=RAISED, bd=3)
detectedgesButton.grid(row=8,column=0)

editFrame = LabelFrame(editor, text="Editing Tools", font=("Arial Black",12), padx=10, pady=10,bg="aquamarine4",fg="aquamarine1")
editFrame.place(x=920,y=150)
mirrorButton = Button(editFrame, text="Mirror", command=mirror, font=("Showcard Gothic", 12), width=13,bg="aquamarine4", fg="mediumspringgreen",relief=RAISED, bd=3)
mirrorButton.grid(row=0,column=0)
rotate90Button = Button(editFrame, text="Rotate 90", font=("Showcard Gothic", 12), width=13, command=rotate_90,bg="aquamarine4", fg="mediumspringgreen",relief=RAISED, bd=3)
rotate90Button.grid(row=1,column=0)
rotate180Button = Button(editFrame, text="Rotate 180", font=("Showcard Gothic", 12), width=13, command=rotate_180,bg="aquamarine4", fg="mediumspringgreen",relief=RAISED, bd=3)
rotate180Button.grid(row=2,column=0)
rotate270Button = Button(editFrame, text="Rotate 270", font=("Showcard Gothic", 12), width=13, command=rotate_270,bg="aquamarine4", fg="mediumspringgreen",relief=RAISED, bd=3)
rotate270Button.grid(row=3,column=0)
originalButton = Button(editFrame, text="Original", font=("Showcard Gothic", 12), width=13,bg="aquamarine4", fg="mediumspringgreen",relief=RAISED, bd=3, command=originalimage)
originalButton.grid(row=5,column=0)
flipButton = Button(editFrame,text="Flip", font=("Showcard Gothic", 12), width=13, command=flip,bg="aquamarine4", fg="mediumspringgreen",relief=RAISED, bd=3)
flipButton.grid(row=4,column=0)

adjustFrame = LabelFrame(editor, text="Adjust", font=("Arial Black", 12),padx=10, pady=10,bg="mediumturquoise")
adjustFrame.place(x=750, y= 500)
brightlabel = Label(adjustFrame, text="Brightness", font=("Showcard Gothic",12),fg="white", bg="mediumturquoise")
brightlabel.grid(row=1,column=0)
varBright = IntVar()
scaleBright = Scale(adjustFrame, from_=0, to=10, variable=varBright, orient=HORIZONTAL, length=300, showvalue=0, troughcolor="#69EAFF", bg="white",command=brightness)
scaleBright.grid(row=0,column=0)
scaleBright.set(5)
contrastlabel = Label(adjustFrame, text="Contrast", font=("Showcard Gothic",12),fg="black", bg="mediumturquoise")
contrastlabel.grid(row=3,column=0)
varContrast = IntVar()
scaleContrast = Scale(adjustFrame, from_=0, to=10, variable=varContrast, orient=HORIZONTAL, length=300, showvalue=0, troughcolor="#69EAFF", bg="black", command=contrast)
scaleContrast.grid(row=2,column=0)
scaleContrast.set(5)
saturationLabel = Label(adjustFrame, text="Saturation", font=("Showcard Gothic", 12),fg="gray35", bg="mediumturquoise")
saturationLabel.grid(row=5,column=0)
varSaturation = IntVar()
scaleSaturation = Scale(adjustFrame, from_=0, to=10, variable=varSaturation, orient=HORIZONTAL,length=300, showvalue=0, troughcolor="#69EAFF", bg="gray35", command=saturation)
scaleSaturation.grid(row=4,column=0)
scaleSaturation.set(5)

rgbFrame = LabelFrame(editor, text="RGB Values", font=("Arial Black", 12),padx=10, pady=10,bg="mediumturquoise")
rgbFrame.place(x=385, y=500)
redLabel = Label(rgbFrame, text="RED", font=("Showcard Gothic",13),fg="red", bg="mediumturquoise")
redLabel.grid(row=1,column=0)
varRed = IntVar()
scaleRed = Scale(rgbFrame, from_=0, to=10, variable=varRed, orient= HORIZONTAL, length=300,showvalue=0,troughcolor="red",bg="white", command=rgb)
scaleRed.grid(row=0,column=0)
scaleRed.set(5)
greenLabel = Label(rgbFrame, text="GREEN", font=("Showcard Gothic",13),fg="green3", bg="mediumturquoise")
greenLabel.grid(row=3,column=0)
varGreen = IntVar()
scaleGreen = Scale(rgbFrame, from_=0, to=10, variable=varGreen, orient= HORIZONTAL, length=300,showvalue=0,troughcolor="green3",bg="white",command=rgb)
scaleGreen.grid(row=2,column=0)
scaleGreen.set(5)
blueLabel = Label(rgbFrame, text="BLUE", font=("Showcard Gothic",13),fg="blue", bg="mediumturquoise")
blueLabel.grid(row=5,column=0)
varBlue = IntVar()
scaleBlue = Scale(rgbFrame, from_=0, to=10, variable=varBlue, orient= HORIZONTAL, length=300,showvalue=0,troughcolor="blue",bg="white", command=rgb)
scaleBlue.grid(row=4,column=0)
scaleBlue.set(5)

cropFrame = LabelFrame(editor, text="Crop", font=("Arial Black", 12),padx=10, pady=10,bg="mediumturquoise")
cropFrame.place(x=20, y= 480)
xStartLabel = Label(cropFrame, text="X Dimension Start",font=("Showcard Gothic",13),bg="mediumturquoise",fg="dodgerblue4")
xStartLabel.grid(row=0,column=0)
varX_start = IntVar()
scaleX_start = Scale(cropFrame, from_=0, to=355,variable=varX_start,orient=HORIZONTAL,length=300,showvalue=0,command=crop, bg="dodgerblue4", troughcolor="white")
scaleX_start.grid(row=1,column=0)
scaleX_start.set(0)
xEndLabel = Label(cropFrame, text="X Dimension End",font=("Showcard Gothic",13),bg="mediumturquoise",fg="dodgerblue4")
xEndLabel.grid(row=2,column=0)
varX_end = IntVar()
scaleX_end = Scale(cropFrame, from_=0, to=355,variable=varX_end,orient=HORIZONTAL,length=300,showvalue=0,command=crop, bg="dodgerblue4", troughcolor="white")
scaleX_end.grid(row=3,column=0)
scaleX_end.set(355)
yStartLabel = Label(cropFrame, text="Y Dimension Start",font=("Showcard Gothic",13),bg="mediumturquoise",fg="dodgerblue4")
yStartLabel.grid(row=4,column=0)
varY_start = IntVar()
scaleY_start = Scale(cropFrame, from_=0, to=355,variable=varY_start,orient=HORIZONTAL,length=300,showvalue=0,command=crop, bg="dodgerblue4", troughcolor="white")
scaleY_start.grid(row=5,column=0)
scaleY_start.set(0)
yEndLabel = Label(cropFrame, text="Y Dimension End",font=("Showcard Gothic",13),bg="mediumturquoise",fg="dodgerblue4")
yEndLabel.grid(row=6,column=0)
varY_end = IntVar()
scaleY_end = Scale(cropFrame, from_=0, to=355,variable=varY_end,orient=HORIZONTAL,length=300,showvalue=0,command=crop, bg="dodgerblue4", troughcolor="white")
scaleY_end.grid(row=7,column=0)
scaleY_end.set(355)



editor.mainloop()
