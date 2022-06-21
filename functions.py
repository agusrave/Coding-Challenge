"""
Created on Mon Jun 20 13:30:21 2022

@author: Agustina Ravettino
"""

def pandas_function(results_file_name) :
    """Loads a file into a pandas dataframe and calculates and prints out the
            1. average file size
            2. the biggest file
            3. the smallest file
            4. histogram plot of file sizes
        param results_file_name: str results file name.
        return: result: json with results. 
    """
    import pandas as pd
    import json
    import numpy as np

    #Set dataframe columns
    colnames=['file_name','size_in_bytes']
    #Read file
    data=pd.read_csv(results_file_name,names=colnames, header=None,delim_whitespace=True)
    #Do calculations
    average= data.size_in_bytes.mean()
    #Generates mask for biggest and smallest files to allocate those file names
    mask_biggest= data.size_in_bytes ==data.size_in_bytes.max()
    biggest_ind=data[mask_biggest].index.values
    biggests=data.file_name[biggest_ind].values
    mask_smallest= data.size_in_bytes ==data.size_in_bytes.min()
    smallest_ind=data[mask_smallest].index.values
    smallests=data.file_name[smallest_ind].values
    #Generate a simple histogram plot
    ax = data.plot.hist(bins=10, alpha=0.8)

    #Print out results
    print( "The average file size in bytes is: ", round(average,2), 
          "\nThe biggest file/s is/are: ", biggests, 
          "\nThe smallest file/s is/are: ", smallests
         )    
    biggests_str= np.array2string(biggests, precision=2, separator=',',
                      suppress_small=True)
    smallests_str= np.array2string(smallests, precision=2, separator=',',
                      suppress_small=True)
    result = {
    "AverageFileSizeInBytes": average,
    "Biggest(s)File(s)": biggests_str,
    "Smallest(s)File(s)": smallests_str
    }
    
    result = json.dumps(result)

    return result


def unzip_file(directory):
    """function to unzip file"""
    with ZipFile(directory, 'r') as zipObj:
    # Extract all the contents of zip file in current directory
        zipObj.extractall()






