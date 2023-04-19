import pandas as pd



def Assignment(Dataframe, Column): #function that takes 2 arguments, the dataframe name and the number of the column
    Dataframe.dropna(how="all", inplace=True) # this step is unnecessary since pandas doesnt include rows with
                                              #entirley no data
    Dataframe.fillna("NA", inplace=True) #fills null values with string "NA"
    Dataframe.drop_duplicates(inplace=True) #drop duplicates
    dfU=Dataframe.iloc[:,Column].unique() #create and array with all the unique values in a given column 
                                          #to slice based on the value of the column
    for i in dfU:
        if i != "NA" :
            SlicedFrame=Dataframe.loc[Dataframe.iloc[:,Column] == i]
            filename = r'Assignment_{}.csv'.format(int(i))
            #Just insert the location where you want the CSV file to be imported to and the files will be there
            SlicedFrame.to_csv(filename, index=False)
        else :
            SlicedFrame=Dataframe.loc[Dataframe.iloc[:,Column] == i]
            filename = r'output/Assignment_NA.csv'
            SlicedFrame.to_csv(filename, index=False)

def DoubleCheck(Dataframe, Column):    
    df_new=Dataframe.copy()
    Dataframe.fillna("NA", inplace=True) #fills null values with string "NA"
    Dataframe.drop_duplicates(inplace=True) #drop duplicates
    UniqueCount=df_new.iloc[:,Column].nunique()
    print(f'the number of documents downloaded to the location should be {UniqueCount}')

def main():
    user_input = input("Enter the column number that is used to split files: ")
    url = "https://raw.githubusercontent.com/haithamabbas1/Data-Assigment/main/datafile.csv"
    df = pd.read_csv(url) #Import the provided data
    if user_input.isdigit() and int(user_input) < len(df.columns) and int(user_input) >= 0:
        Assignment(df, int(user_input))
        DoubleCheck(df, int(user_input))
    else:
        print("Please enter a valid number")

if __name__ == "__main__":
    main()