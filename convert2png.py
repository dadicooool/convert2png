try:
    from PIL import Image
except ImportError:
    print("Pïllow needed. Install with 'pip install pillow' from shell")

import os

def cleanslash(stringin):
    if stringin.endswith("/"):
        stringout = stringin[:-1]
    elif stringin.endswith("\\"):
        stringout = stringin[:-1]
    else:
        stringout = stringin
    return stringout

def convert():
    jpglist = []
    webplist = []
    totallist = []
    input_path = input("JPG/WebP directory path: ")
    input_path = cleanslash(input_path)
    if input_path == "":
        input_path = "/"
    output_path = input("PNG directory path (leave blank for 'input_path'/output): ")
    output_path = output_path.replace("\\", "/")
    output_path = cleanslash(output_path)
    if output_path == "":
        output_path = input_path + "/output"
        print("Output folder set to: " + output_path)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for filename in os.listdir(input_path):
        ext = os.path.splitext(filename)[1]
        ext = ext.lower()
        if ext == ".jpg" or ext == ".jpeg":
            jpglist.append(filename)
        elif ext == ".webp":
            webplist.append(filename)
    print("Total files: " + str(len(jpglist) + len(webplist)) + " (" + str(len(jpglist)) + " JPG, " + str(len(webplist)) + " WebP)")
    i = 1
    totallist = jpglist + webplist
    for filename in totallist:
        current_img = Image.open(input_path + '/' + filename)
        print(f"Processing: " + str(i) + "/" + str(len(totallist)), end="\r")
        current_img.save(output_path + '/' + os.path.splitext(filename)[0] + '.png', 'PNG')
        i += 1
    print("\nDone.")
        
    

while True:
    convert()
    loop = input("1 to continue\n2 to exit\n")
    if loop == "1":
        convert()
    else:
        exit()
