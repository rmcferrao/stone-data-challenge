## Stone Data Challenge

This data science repository is organized in 4 main folders and some auxiliary archives. 
The `utils` folders holds two archives `ml_functions.py` and `process_data.py` that have some utilitary functions used in the notebooks. 
The `notebook` holds 3 jupyter notebooks, `01_exploratory` has the exploratory analysis, `02_dashboard` has a dashboard used to ease the analysis of the timeseries attributes (obs: if you want to use the dashboard you gonna have to run the top level main function in `process_data.py`. It generates two auxiliary archives that used to optimize the dashboard speed in looking for specific loans IDs). And, finally, `03_ml_models` have everything needed for a good implementation of ml models (Data pre processing, model training, model evaluation, score calculation and model prediction).
The `assets` has an `css` archived used to stylize the dashboard.
The `data` folder has two subfolders `processed` and `raw`. Please put the raw files in raw. The folder `processed` is used to store the processed filed for the dashboard.
