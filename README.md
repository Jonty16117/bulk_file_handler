# Bulk File Handler
A Python script to dealing with large number of files with just few commands

## Getting Started
To use bulk file handler on your local machine, just clone or download from [Bulk File Handler](link "Click here to clone or download").

## Prerequisites
You need to have **Python3** installed on your system. Any version previous to Pytho3 **will not work**.

## Installing
To set up this python script there are following options available(choose any that suits you): 

***1. Running `main.py` file directly (for windows/macOS/linux):***  
Just edit the `main.py` file using the defined functions withe the required methods. But this becomes hard if you want to edit again and again.

***2. Install the script (for macOS/linux systems only):***  
To install the script, run the `installer.sh` shell script file using the following command inside terminal:  

`./installer.sh` 

## Usage
General command syntax in terminal:  
`main <method name>`

Using **Bulk File Handler** is a piece of cake. Just follow any of the above installing steps use it in two basic steps. 

***1. Selecting files:***  
Select the files on which you want to perform the actions. The selection of files can be done by filtering our the files based on your conditions iteratively. e.g. you can first select files that have string "abc" in their name, then filter those with size less than "10000" bytes, then filter out with those that are created in date between "2010-12-10" and "2015-10-11", and so on. Basically you can select files on the following bases:  
1. By String ("can also be used with any RegEx in place of String")
2. By Date
3. By Size
4. By File type

example commands:  

`main filterFilesListByString`    
`main filterFilesListBySize`  
`main showSelectedFiles`   
`main renameSelectedFiles`    ...etc.

***2. Applying operations:***  
After seleting the files you now have the list of files on which you can perform any of the following actions:  
1. Move
2. Copy/Paste
3. Rename
4. Delete

## Built With  
- ***Python3***  
- ***Libraries used***  
	- [os](https://docs.python.org/3/library/os.html)  
	- [re](https://docs.python.org/3/howto/regex.html)  
	- [datetime](https://docs.python.org/3/library/datetime.html)  
	- [time](https://docs.python.org/3/library/time.html)  
	- [math](https://docs.python.org/3/library/math.html)  
	- [shutil](https://docs.python.org/3/library/shutil.html)  
	- [sys](https://docs.python.org/3/library/sys.html)  

## Contributing
Please feel free to pull requests, fork, and submit issues (if any).  

## Versioning  
This is the first build. Further versions will be released if added more funtionalities.

## Author  
- ***Jonty***  
See also the list of [CONTRIBUTORS](https://github.com/Jonty16117/bulk_file_handler/blob/master/CONTRIBUTORS.md) who participated in this project.

## License  
This project is licensed under the GPL v3.0 License - see the LICENSE.md file for details

