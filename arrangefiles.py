import os

def move(folderName, files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

if __name__ == '__main__':

    files = os.listdir()
    files.remove('arrangefiles.py')
    #print(files)

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Videos')
    createIfNotExist('Music')
    createIfNotExist('Others')
    createIfNotExist('Adobe Files')
    createIfNotExist('PDFs')
    createIfNotExist('WebFiles')

    imgExts = [".png" , ".jpg", ".jpeg" , ".gif" , ".tiff" , ".eps" , ".raw", ".cr2","jpeg 2000",".exif",".bmp",".ppm",".pgm",".pbm",".pnm",".webp",".hdr",".heif",".ico"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docsExts = [".txt" , ".ppt", ".pptx" , ".odt" , ".xlsx" , ".xls", ".ods", ".dot", ".doc",".docx", ".wbk", ".docm", ".doxt", ".dotm", ".docb" , ".xlt", ".xlm", ".xlms", ".xltx", ".xltm", ".xlsb", ".xla", ".xlam", ".xll", ".xlw", ".pot", ".pps",".pptx",".pptm",".potx",".potm",".ppam",".ppsx",".ppsm",".sldx",".sldm",".accdb",".accde",".accdt",".accdt",".accdr",".pub",".xps"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docsExts]

    videoExts = [".mp4",".mkv", ".m4a", ".m4v", ".f4v", ".f4a", ".m4b", ".m4r", ".f4b", ".mov" , ".3gp", ".3gp2", ".3g2", ".3gpp", ".3gpp2", ".ogg", ".oga", ".ogv", ".ogx",".wmv", ".wma", ".asf*",".webm",".flv",".AVI",".OP1a", ".OP-Atom",".ts",".VOB"]
    video = [file for file in files if os.path.splitext(file)[1].lower() in videoExts]

    musicExts = [".3gp",".aa",".aac",".aax",".act",".aiff",".alac",".ape",".amr",".au",".awb",".dct",".dvf",".dss",".flac",".gsm",".iklax",".ivs",".m4a",".m4b",".m4p",".mmf",".mp3",".msv",".mpc",".ogg",".nmf",".nsf",".oga",".mogg",".opus",".ra",".raw",".rm",".rf64",".sln",".tta",".voc",".vox",".wav",".wma",".wv",".webm",".8svx",".cda"]
    music = [file for file in files if os.path.splitext(file)[1].lower() in musicExts]

    adobeExts = [".psd" ,".eps" ,".ai" ,".indd"]
    adobe = [file for file in files if os.path.splitext(file)[1].lower() in adobeExts]

    pdfExts = [".pdf"]
    pdf = [file for file in files if os.path.splitext(file)[1].lower() in pdfExts]


    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in videoExts) and (ext not in imgExts) and (ext not in docsExts) and (ext not in musicExts) and (ext not in adobeExts) and (ext not in pdfExts) and os.path.isfile(file):
            others.append(file)

    move("Images", images)
    move("Docs", docs)
    move("Videos", video)
    move("Music", music)
    move("Others", others)
    move("Adobe Files", adobe)
    move("PDFs", pdf)
