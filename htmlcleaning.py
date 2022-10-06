from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm
import os

directory_name = "D:\\stability-files\\archives"


#loop through all files in directory = directory_name
for path, subdirs, files in tqdm(os.walk(directory_name)):
    for name in files:
        if name.__contains__(".html"):
            #create newpath which will be used as destination path for edited files
            newpath = path.replace("archives", "edited-archives")

            # create newname which will be used to store edited files, =newpath + name
            newname = os.path.join(newpath, name)

            #preprocess filepaths to cooperate with BeautifulSoup's file reader
            urlpath = "file:///" + os.path.join(path, name)
            urlpath = urlpath.replace("\\", "/")

            #open file in BeautifulSoup
            url = urlpath
            html = urlopen(url).read()
            soup = BeautifulSoup(html, features="html.parser")

            ######################################################################################################
            # Edit everything below to correct formatting. Currently outputs plain text with white space removed #
            ######################################################################################################

            # get text
            text = soup.get_text()

            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)


            # save edited text to newname (newpath + name)
            os.makedirs(newpath, exist_ok=True)
            txtfilewriter = open(newname, "w", encoding="utf-8")
            txtfilewriter.write(text)
            txtfilewriter.close()