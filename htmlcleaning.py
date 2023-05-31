from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm
import os

directory_name = "path\\to\\repo\\reponame"


#loop through all files in directory = directory_name
for path, subdirs, files in tqdm(os.walk(directory_name)):
    for name in files:
        # select only html files if repo contains a mix of file types
        if name.__contains__(".html"):
            #create newpath which will be used as destination path for edited files
            newpath = path.replace("reponame", "new-reponame")

            # create newname which will be used to store edited files, =newpath + name
            newname = os.path.join(newpath, name)
            newname = newname.replace(".html", ".txt")

            #preprocess filepaths to cooperate with BeautifulSoup's file reader
            urlpath = "file:///" + os.path.join(path, name)
            urlpath = urlpath.replace("\\", "/")

            #open file in BeautifulSoup
            url = urlpath
            html = urlopen(url).read()
            soup = BeautifulSoup(html, features="html.parser")

            #######################################################################################################################################
            # Edit everything below to correct formatting. Currently outputs plain text with white space and repeated tokens from website removed #
            #######################################################################################################################################
            soup = BeautifulSoup("")

            if path.__contains__("coq-club-raw.tar"):
                rejects = ["mail", "thrd"]
                if any(name.__contains__(rej) for rej in rejects):
                    pass
                else:
                    #open file in BeautifulSoup
                    url = urlpath
                    html = urlopen(url).read()
                    soup = BeautifulSoup(html, features="html.parser")

                    soup = soup.main.extract()
                    for trash in soup(["li", "ul", "h1", "h2", "span"]):
                        trash.extract()

            elif path.__contains__("coq-zulip.tar"):
                newname = os.path.dirname(newname)
                if path.__contains__("zulip-archive"):
                    #open file in BeautifulSoup
                    url = urlpath
                    html = urlopen(url).read()
                    soup = BeautifulSoup(html, features="html.parser")

                    soup.head.decompose()

                    dates = soup.find_all("h4")
                    for name_date in dates:
                        date = name_date.find("a")
                        for date in name_date:
                            try:
                                date.decompose()
                            except:
                                pass

                    if os.path.exists(newname + ".txt"):
                        soup.h2.decompose()

            elif path.__contains__("leanprover-community.github.io-raw.tar"):
                newname = os.path.dirname(newname)

                # open file in BeautifulSoup
                url = urlpath
                html = urlopen(url).read()
                soup = BeautifulSoup(html, features="html.parser")

                soup = soup.article.extract()
                soup.hr.decompose()
                soup.header.decompose()

                if os.path.exists(newname + ".txt"):
                    soup.h2.decompose()

            elif path.__contains__("mail.haskell.org.tar"):
                newname = os.path.dirname(newname)

                rejects = ["author.html", "date.html", "subject.html", "thread.html"]
                if any(name == rej for rej in rejects):
                    pass
                else:
                    try:
                        # open file in BeautifulSoup
                        url = urlpath
                        html = urlopen(url).read()
                        soup = BeautifulSoup(html, features="html.parser")
                        # kill all script and style elements

                        soup = soup.pre.extract()
                    except:
                        pass

            if soup != BeautifulSoup(""):

                for script in soup(["script", "style"]):
                    script.extract()  # rip it out

                # get text
                text = soup.get_text()

                # break into lines and remove leading and trailing space, as well as junk text on each
                lines = []
                for line in text.splitlines():
                    if line.__contains__("Last updated: "):
                        pass
                    elif line.__contains__("Archive powered by "):
                        pass
                    else:
                        lines.append(line.strip())
                # break multi-headlines into a line each
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                # drop blank lines
                text = '\n'.join(chunk for chunk in chunks if chunk)
                
                
            # save edited text to newname (newpath + name)
            os.makedirs(newpath, exist_ok=True)
            txtfilewriter = open(newname, "w", encoding="utf-8")
            txtfilewriter.write(text)
            txtfilewriter.close()
