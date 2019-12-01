# This is the main function which takes input parameters as 2 files to be compared
def main(file2, file1):

    # Both files passed in as parameters from the main method are opened with read permissions
    # Both files are read into lists called data_one and data_two which split the text files by spaces and saves them all lowercase
    # Both lists are then saved to new lists, called sep_one and sep_two, which now hold sub-lists of size 5
    # The sub-lists are created with the method chunks(m, n)
    with open(file1, 'r', errors="ignore") as file_one:
        data_one = file_one.read().lower().split(' ')
    sep_one = []
    sep_one = list(chunks(data_one, 5))

    with open(file2, 'r', errors="ignore") as file_two:
        data_two = file_two.read().lower().split(' ')
    sep_two = []
    sep_two = list(chunks(data_two, 5))
        
    tempcount = 0
    tempcountscore = 0
    # finalarr is a final list which will hold all the maximum similarity values of
    # all sub-list comparisons
    finalarr = []

    # Similarity Checker Algorithm <- Start Here

    # Loop through sep_one to get the sub-lists
    for m in sep_one:
        # Initialize a temporary list to hold the similarity values of each sub-list comparison
        temparr = []
        # Loop through sep_two to get the sub-lists
        for n in sep_two:
            # Initialize a temporary counter to count the number of matched words
            # Initialize a temporary score count to store the mean similarity score of each sub-list comparison
            tempcount = 0
            tempcountscore = 0
            # Loop through sub-list m of sep_one to get the words
            for i in m:
                # Loop through sub-list n of sep_two to get the words
                for j in n:
                    # Condition to check if the words in sub-list n exist in sub-list m
                    if j in m:
                        # Condition to check if the word in sub-list m matches the word in sub-list n
                        if i == j:
                            # If the condition is met, then a match is found and the temporary counter is incremented
                            tempcount += 1
            # This temporary score count holds the mean similarity score between both sub-lists
            tempcountscore = tempcount / len(m)
            # The temporary score count is then appended to the temporary list
            temparr.append(tempcountscore)
        # The maximum similarity score in temparr is taken as the highest similarity score of
        # sub-list m compared to all sub-lists in sep_two and saved to k
        k = max(temparr)
        # k is then appended to the final list
        finalarr.append(k)
    # The total similarity value is found by calculating the mean value of all values in finalarr
    # the total similarity value is saved to similarity
    similarity = Avg(finalarr)
    if (similarity > 1):
        similarity = 1.0

    # Similarity Checker Algorithm <- End Here

    # The similarity score between each file is the return value of this function                
    return similarity

# This function takes 2 input parameters: m = List of words; n = size of desired sub-list
def chunks(m, n):
    for i in range(0, len(m), n):
        yield m[i:i + n]

# This function takes a list as input and returns the average value of the values in the input list
def Avg(arr):
    return sum(arr) / len(arr) 

# *Function to Run Program*
if __name__ == "__main__":
    # list1 contains the directory and name of original files
    list1 = ["evaluation/a.txt", "evaluation/b.txt", "evaluation/c.txt", "evaluation/d.txt", "evaluation/e.txt"]
    # list2 contains the directory and name of test files
    list2 = ["evaluation/1.txt", "evaluation/2.txt", "evaluation/3.txt", "evaluation/4.txt", "evaluation/5.txt", "evaluation/6.txt", "evaluation/7.txt", "evaluation/8.txt", "evaluation/9.txt", "evaluation/10.txt", "evaluation/11.txt", "evaluation/12.txt", "evaluation/13.txt", "evaluation/14.txt", "evaluation/15.txt", "evaluation/16.txt", "evaluation/17.txt", "evaluation/18.txt", "evaluation/19.txt", "evaluation/20.txt", "evaluation/21.txt", "evaluation/22.txt", "evaluation/23.txt", "evaluation/24.txt", "evaluation/25.txt", "evaluation/26.txt", "evaluation/27.txt", "evaluation/28.txt", "evaluation/29.txt", "evaluation/30.txt", "evaluation/31.txt", "evaluation/32.txt", "evaluation/33.txt", "evaluation/34.txt", "evaluation/35.txt", "evaluation/36.txt", "evaluation/37.txt", "evaluation/38.txt", "evaluation/39.txt", "evaluation/40.txt", "evaluation/41.txt", "evaluation/42.txt", "evaluation/43.txt", "evaluation/44.txt", "evaluation/45.txt", "evaluation/46.txt", "evaluation/47.txt", "evaluation/48.txt", "evaluation/49.txt", "evaluation/50.txt", "evaluation/51.txt", "evaluation/52.txt", "evaluation/53.txt", "evaluation/54.txt", "evaluation/55.txt", "evaluation/56.txt", "evaluation/57.txt", "evaluation/58.txt", "evaluation/59.txt", "evaluation/60.txt", "evaluation/61.txt", "evaluation/62.txt", "evaluation/63.txt", "evaluation/64.txt", "evaluation/65.txt", "evaluation/66.txt", "evaluation/67.txt", "evaluation/68.txt", "evaluation/69.txt", "evaluation/70.txt", "evaluation/71.txt", "evaluation/72.txt", "evaluation/73.txt", "evaluation/74.txt", "evaluation/75.txt", "evaluation/76.txt", "evaluation/77.txt", "evaluation/78.txt", "evaluation/79.txt", "evaluation/80.txt", "evaluation/81.txt", "evaluation/82.txt", "evaluation/83.txt", "evaluation/84.txt", "evaluation/85.txt", "evaluation/86.txt", "evaluation/87.txt", "evaluation/88.txt", "evaluation/89.txt", "evaluation/90.txt", "evaluation/91.txt", "evaluation/92.txt", "evaluation/93.txt", "evaluation/94.txt", "evaluation/95.txt", "evaluation/96.txt", "evaluation/97.txt", "evaluation/98.txt", "evaluation/99.txt", "evaluation/100.txt"]

    # h and g contain the list size of list1 and list2 respectively
    h = len(list1)
    g = len(list2)
    # f holds the open csv file with write permissions
    f = open("Similarity_Report.csv", "w")
    # Write the header row into the csv
    f.write(',a,b,c,d,e\n')
    # Loop through list of test files
    for i in range(g):
        # Write the row number into the first column of the csv
        f.write('{},'.format(i+1))
        # Loop through list of original files
        for j in range(h):
            # Write the similarity score to the csv
            f.writelines('{},'.format(main(list1[j], list2[i])))
        # After each test file is compared with each original file, a new line is written to the csv
        f.write('\n')
    # Close the csv file
    f.close()