import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_dataset(file_path):
    print("\n#### Question 1 ####\n")
    df = pd.read_csv(file_path)
    print(df)
    return df
    """
    - save the predict_mcdi.csv file located in the data/lab10 website on your local machine.
    - create a variable in your main function with the location of that file on your machine, and pass it into this
        function.
    - rename this function "load_dataset", and have it receive the file location as an input argument named "file_path"
    - have this function load the file indicated by "file_path  and create a pandas dataframe out of it
    - print the dataframe, and return it back to the main function, saved there as mcdi_df
    """


def subset_data_by_age(df, age):
    print("\n#### Question 2 ####\n")
    subset_df = df[df['Age'] == age]
    print(subset_df)
    return subset_df
    """
    - modify this function so it is named "subset_data_by_age"
    - have the function take two arguments, "df" and "age".
    - have this function create a new dataframe that is a subset of the full dataframe, but containing only the data
        for the age that is passed into the age variable.
    - print the new dataframe, and return it back to the main function
    - in the main function, call this function and pass it the full dataframe and the value 24 for age. receive the
        resulting dataframe back into your main function named "mcdi24_df"
    """


def get_mean(df, column_name):
    print("\n#### Question 3 ####\n")
    mean_value = df[[column_name]].mean()
    print(mean_value)
    return mean_value
    """
    - modify this function to have the name "get_mean".
    - have this function receive a dataframe and a column name as an input arguments,
    - have the function create a new dataframe containing the the mean value of the specified column.
    - print the resulting dataframe, and return it back to the main function.
    - call this function from main, pass it mcdi24_df and MCDIp, and call the variable it receives back mcdip24_mean
    """


def get_word_stats(df, word, statistic):
    print("\n#### Question 4 ####\n")
    filtered_df = df[df['Word'] == word].set_index('Age')[statistic]
    print(filtered_df)
    return filtered_df
    """
    - modify this function to have the name "get_word_stats"
    - have it receive three input arguments: df, word, statistic
    - have the function create a new dataframe which is the data only for the specified word and statistic, at each age
    - print the df and and return it to the main function as "word_stat"
    - call this function from main, and pass it a word and statistic of your choice
    for example, if the input word was "sock" and the statistic was "MCDIp", the resulting df would be:
        Age
        16    0.300209
        17    0.216117
        18    0.441177
        19    0.472561
        20    0.459854
        21    0.443350
        22    0.505000
        23    0.595420
        24    0.718696
        25    0.750751
        26    0.828729
        27    0.779487
        28    0.946048
        29    0.787879
        30    0.898305
Name: MCDIp, dtype: float64
    """


def get_corr_by_age(df, stat1, stat2):
    print("\n#### Question 5 ####\n")
    correlation_list = []
    for age in sorted(df['Age'].unique()):
        subset = df[df['Age'] == age]
        corr = subset[stat1].corr(subset[stat2])
        correlation_list.append({'Age': age, 'Correlation': corr})
    correlation_df = pd.DataFrame(correlation_list)
    print(correlation_df)
    return correlation_df
    """
    - rename this function "get_corr_by_age", and give it three input arguments: df, stat1 and stat2
    - have the function create a new dataframe that has the correlation of the two specified statistics separately for
        each age
    - print the resulting dataframe, and pass it back to the main function
    - call this function from main(), pass in the full dataframe, and the values "LogFreq" and "MCDIp".
    Your result should be:
                Age  Correlation
            1    16     0.212248
            3    17     0.206795
            5    18     0.184279
            7    19     0.167496
            9    20     0.163828
            11   21     0.130066
            13   22     0.164553
            15   23     0.162973
            17   24     0.129188
            19   25     0.122507
            21   26     0.160319
            23   27     0.144281
            25   28     0.113585
            27   29     0.159692
            29   30     0.131319
    """


def qplot_word_stats(df):
    print("\n#### Question 6 ####\n")
    words = ['sock', 'dog', 'milk', 'car']
    for word in words:
        word_data = get_word_stats(df, word, 'MCDIp')
        plt.plot(word_data.index, word_data.values, marker='o', label=word)

    plt.xlabel('Age (months)')
    plt.ylabel('MCDIp')
    plt.title('MCDIp Scores by Age for Selected Words')
    plt.legend()
    plt.show()
    """
    - create a list with four words on it that are in the MCDI dataset
    - create a loop that loops over the list, and each time calls your get_word_stats() function, passing it
        the full dataframe, the word, and the statistic "MCDIp".
    - use the resulting dataframes to create a line plot with four lines, showing the values of MCDIp for each word
        at each age
    - don't forget to label your figure, the axes, and include a legend.
    """


def plot_means_by_age(df):
    print("\n#### Question 7 ####\n")
    ages = [18, 24, 30]
    means = []
    for age in ages:
        subset = subset_data_by_age(df, age)
        mean_val = get_mean(subset, 'MCDIp')
        means.append(mean_val)

    plt.bar(ages, means)
    plt.xlabel('Age (months)')
    plt.ylabel('Mean MCDIp')
    plt.title('Average MCDIp Scores at Different Ages')
    plt.show()
    """
    - create a list with three ages that are in the MCDI dataset.
    - create a bar plot with the average MCDIp score at three different ages.
    - use your subset_data_by_age() and get_mean() functions to accomplish this
    - label your figure and axes!
    """


def plot_histograms(df):
    print("\n#### Question 8 ####\n")
    subset = subset_data_by_age(df, 24)
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].hist(subset['MCDIp'])
    axs[0].set_title('MCDIp')
    axs[1].hist(subset['LogFreq'])
    axs[1].set_title('LogFreq')
    axs[2].hist(subset['ProKWo'])
    axs[2].set_title('ProKWo')
    plt.suptitle("Histograms at 24 Months")
    plt.show()
    """
    - create a figure with three subplots
    - the three subplots should all be histograms, containing the values of MCDIp, LogFreq, and
        ProKWo at 24 months
    - label your figure, subplots, and axes!
    """


def plot_scatterplots(df):
    print("\n#### Question 9 ####\n")
    subset = subset_data_by_age(df, 24)
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    axs[0].scatter(subset['LogFreq'], subset['MCDIp'])
    axs[0].set_title('LogFreq vs MCDIp')
    axs[1].scatter(subset['ProKWo'], subset['MCDIp'])
    axs[1].set_title('ProKWo vs MCDIp')
    plt.suptitle("Scatterplots at 24 Months")
    plt.show()
    """
    - create a figure with two subplots
    - the two subplots should be scatterplots of LogFreq x MCDIp at 24 months, and ProKWo x MCDIp
        at 24 months
    - label your figure, subplots, and axes
    """


def plot_custom(df):
    print("\n#### Question 10 ####\n")
    grouped = df.groupby('Lexical_Class')['MCDIp'].mean()
    grouped.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Average MCDIp by Lexical Class")
    plt.ylabel("MCDIp")
    plt.xlabel("Lexical Class")
    plt.show()
    """
    - create one more figure of your choice using the MCDIp dataset, different from the others we
    have made so far
    """

def main():
    file_path = "data/predict_mcdi.csv"
    mcdi_df = load_dataset(file_path)
    mcdi24_df = subset_data_by_age(mcdi_df, 24)
    mcdip24_mean = get_mean(mcdi24_df, 'MCDIp')
    word_stat = get_word_stats(mcdi_df, 'sock', 'MCDIp')
    corr_df = get_corr_by_age(mcdi_df, 'LogFreq', 'MCDIp')
    plot_word_stats(mcdi_df)
    plot_means_by_age(mcdi_df)
    plot_histograms(mcdi_df)
    plot_scatterplots(mcdi_df)
    plot_custom(mcdi_df)

if __name__ == "__main__":
    main()