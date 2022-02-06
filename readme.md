### playtimecheck.py:

#### v0.10 
- checking if the process is currently running and saving to the dictionary as 'Hour: running' works.

#### v0.20 
- The option to hide the program has been added. Changed process decoding to utf-16 due to previously returned decoding error. A file with the .pyw extension has been added - hides the console while the program is running

#### v0.30
- Checking several consecutive programs simultaneously (chrome, notepad, ToDo) and saving the common dictionary to a .json file

#### v0.40
- changed way of saving data to .json file, instead of dictionaries with nested programs' run states
        in dictionaries with program names, now there are lists with program run states nested in the dictionaries
        program names. This will allow you to change the date format from string to datetime in the analysis.
#### v0.50
- Changed program state format in the list from string to boolean ['Chrome', 'Works'] to ['Chrome', True]
#### v0.51
- Clean unnecessary commands Switched to English
#### v0.60
- switched to **psutil** for cleaner code.

> ToDo:
      - change of coding in the line:
                16. output = subprocess.check_output (call) .decode ('utf-8')
        because the program running in python works fine and running directly from the .py file returns an encoding error
      - sending the file with the dictionary to the e-mail address.


### analysis.py:
        Module for analyzing data sent in a .json file.
        The data will be available in the form of tables and graphs.
#### v0.10
- first version
#### v0.20
        - reading data from a saved -json file
        - data conversion from dict to lists
        - convert date format from string to datetime
        - printout of the chart presenting the program status in the checked period
#### v0.30
        - reading a new .json file (several programs are checked simultaneously)
        - formatting the file and printing on the result screen
#### v0.40
        - thorough reconstruction of the file. The data in .json format contains the list dictionaries instead of the dictionaries of the dictionaries as before.
          The data read from the file is in string format, it requires conversion to datetime in order to perform operations related to dates.
#### v0.50
        - program main menu introduced with options to choose from
        - removed function of changing the string to boolean format in the program status list
        - separate function for string to datetime conversion
        - printing the usage status of three programs on one graph
#### v0.60
        - individual program analysis function added
        - Switched to English

> ToDo:
        - automatic program name selection from dictionary instead of manual typing