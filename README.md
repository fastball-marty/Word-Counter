# Custom Word Counter 
* Author(s): fastball-marty
* Published: 12.06.2023

## Description
This Github repository stores the code that counts the occurences of words in a .txt file, and it can be used for any body of text.

Link to website: <https://fastball-marty.github.io/Word-Counter>

Below are instructions on how to run this code on your machine, and how to count your own custom .txt file.

## Installation and Use

### 1. Install Dependencies

* Python:
  * Visit the official Python website: <https://www.python.org/downloads/>
  * Choose the appropriate version for your operating system (Windows, macOS, or Linux). The version number of python shouldn't matter, but I am using 3.11.6
  * Follow the installation instructions provided on the website.
  * During installation, make sure to check the option to add Python to your system's PATH.
  * Verify the installation by opening a command prompt or terminal and typing python --version or python3 --version. You should see the installed Python version.

* wordcounter.py
  * Within this repo: <https://github.com/fastball-marty/Word-Counter>
  * Navigate to the */src* subdirectory and click on the file *wordcounter.py*
  * Look for a "Download" button or a "Raw" button on the file page.
  * Right-click on the "Download" or "Raw" button and choose "Save As" to download the file to your computer.

### 2. Prepare .txt file
The wordcounter.py program requires your text to be stored as a .txt file. The tutorial below walks through how to create a .txt file:

<https://www.groovypost.com/howto/quickly-create-new-blank-text-file-windows-mac-linux/>

After you have created your .txt file and added the text you want to count, ensure **it is located in the same directory as wordcounter.py.** (For example, both files located on your Desktop.)

### 3. Navigate to the files
You will need a command line interface (CLI) to run this program. See the guides below on how to open up a CLI on your machine:

* Mac (terminal): <https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/2.14/mac/14.0>
* Windows (powershell): <https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started?view=powershell-7.4>
* Linux (terminal): <https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal>

Once your CLI is open, you will need to navigate to the directory where you stored the files using the cd command. For example, 

    cd Desktop/myFiles

will bring you to the Desktop directory, and then to the myFiles folder stored on your Desktop. Run the command

    ls 

and you will see all of the files located in your current directory. If you do not see both wordcounter.py and your .txt file, you are **not** in the correct directory.

Here is a simple tutorial on navigating the command line: <https://tutorials.codebar.io/command-line/introduction/tutorial.html#:~:text=The%20cd%20command%20allows%20you,command%20is%20cd%20your%2Ddirectory%20.&text=Now%20that%20we%20moved%20to,again%2C%20then%20cd%20into%20it.>

### 4. Run the program
Within your terminal and inside the correct directory, type the following line and press enter:

    python3 wordcounter.py

Alternatively, if you have an older version of python, enter:

    python wordcounter.py

The program should now be running. Enter the name of your file to count its words, and follow the additional prompts.

The results of wordcounter.py are stored in an automatically created file called *output.txt* in the same directory. **If a file named output.txt already exists in this directory, it will be overwritten.**
