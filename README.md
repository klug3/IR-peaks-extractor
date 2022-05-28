# IR-peaks-extractor:
Read FTIR peaks from xlsx file and write to new txt.

## Installation:
1. Install python 3.10
2. Create virtual environment (e.g. py -3.10 -m venv .venv)
3. Activate venv: ./.venv/Scripts/activate
4. Install required packages from requirements.txt file (python -m pip install -r requirements.txt)
4. Configure IR_peaks_extractor.py as needed:
    - By default, xlsx file name is peaks.xlsx and must be located in project directory.
    - By default, script is looking for compounds names starting "TM_" and deletes other columns.
    - By default, script writes output file as "FTIR_data.txt".
5. Run IR_peaks_extractor.py

## Requirements:
- Python version: 3.10 (any 3.x should work as well)
- pandas, xlrd, openpyxl

## Notes:
- Project requires pandas for such simple task just becase it was not optimised for anything and anyone but me ;)
- It is not a general purpose tool but a usefull script to automatize basic and time consuming task. 