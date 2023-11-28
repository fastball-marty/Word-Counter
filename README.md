# Custom Word Counter 
* Author(s): emmacarl7
* Published: 11.27.2023

## Description
This Github repository stores the code that counts the occurences of words in a .txt file, and it can be used for any body of text.

<https://github.com/emmacarl7/Word-Counter>

Below are instructions on how to run this code on your machine, and how to count your own custom .txt file.

## Installation and Use

### 1. Install Dependencies

* Python:
  * Visit the official Python website: <https://www.python.org/downloads/>
  * Choose the appropriate version for your operating system (Windows, macOS, or Linux).
  * Follow the installation instructions provided on the website.
  * During installation, make sure to check the option to add Python to your system's PATH.
  * Verify the installation by opening a command prompt or terminal and typing python --version or python3 --version. You should see the installed Python version.

* myapp.py
  * Within this repo: <https://github.com/emmacarl7/Word-Counter>
  * Click on the file 'myapp.py'
  * Look for a "Download" button or a "Raw" button on the file page.
  * Right-click on the "Download" or "Raw" button and choose "Save As" to download the file to your computer.

### 2. Prepare .txt file
The myapp.py program requires your text to be stored as a .txt file. The tutorial below walks through how to create a .txt file:

<https://www.groovypost.com/howto/quickly-create-new-blank-text-file-windows-mac-linux/>

After you have created your .txt file, ensure **it is located in the same directory as myapp.py.** (For example, both files located on your Desktop.)

### 3. Navigate to the files
You will need a command line interface to run this program. See the guides below on how to open up a terminal:

* Mac: <https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/2.14/mac/14.0>
* Windows: <https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started?view=powershell-7.4>
* Linux: <https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal>

Once your terminal is open, you will need to navigate to the directory where you stored the files. For example, 

    cd Desktop/myFiles

will bring you to the Desktop directory, and then to the myFiles folder stored on your Desktop. Run the command

    ls 

and you will see all of the files located in your current directory. If you do not see myapp.py and your .txt file, you are not in the correct directory.

Below is an example screenshot of the above steps from the Mac terminal:

![Termianl Tutorial](/assets/example.png)

### 4. Run the program
Within your terminal and inside the correct directory, type the following line and press enter:

    python3 myapp.py

Alternatively, if you have an older version of python, enter:

    python myapp.py

The program should now be running. Enter the name of your file to count its words.
