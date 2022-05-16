#
To obtain Scottish Postcode Directory files directly from the NRS website: https://www.nrscotland.gov.uk/statistics-and-data/geography/nrs-postcode-extract



Click the icon below to launch the repository with Binder:


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Gerald-Leung/SPD/HEAD)

If you run into any problems with the packages, use pip install <packagename> in terminal to fullfill the requirements (though this normally should not be needed).
  
The check_SPD.ipynb notebook provides documentation for the functionality of this simple process. The check_SPD.py script provides the actual functionality.
  
To run the script, open up terminal and type 
```
  python check_SPD.py --date <date of file/link>
```
It will then check the target website for any changes and if so, download the required CSV files. 
