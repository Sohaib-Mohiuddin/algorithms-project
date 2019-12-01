def main(file2, file1):
    with open(file1, 'r', errors="ignore") as file_one:
        data_one = file_one.read().lower().split(' ')
    sep_one = []
    sep_one = list(chunks(data_one, 5))

    with open(file2, 'r', errors="ignore") as file_two:
        data_two = file_two.read().lower().split(' ')
    sep_two = []
    sep_two = list(chunks(data_two, 5))
        
    tempcount = 0
    tempcountmax = 0
    finalarr = []

    # Similarity Checker Algorithm <- Start Here
    for m in sep_one:
        temparr = []
        for n in sep_two:
            tempcount = 0
            tempcountmax = 0
            for i in m:
                for j in n:
                    if j in m:
                        if i == j:
                            tempcount += 1
            tempcountmax = tempcount / len(m)
            temparr.append(tempcountmax)
        k = max(temparr)
        finalarr.append(k)
    similarity = Avg(finalarr)
    if (similarity > 1):
        similarity = 1.0
    # Similarity Checker Algorithm <- End Here
                            
    return similarity

def chunks(m, n):
    for i in range(0, len(m), n):
        yield m[i:i + n]

def Avg(arr):
    return sum(arr) / len(arr) 


if __name__ == "__main__":
    list1 = ["evaluation/a.txt", "evaluation/b.txt", "evaluation/c.txt", "evaluation/d.txt", "evaluation/e.txt"]
    list2 = ["evaluation/1.txt", "evaluation/2.txt", "evaluation/3.txt", "evaluation/4.txt", "evaluation/5.txt", "evaluation/6.txt", "evaluation/7.txt", "evaluation/8.txt", "evaluation/9.txt", "evaluation/10.txt", "evaluation/11.txt", "evaluation/12.txt", "evaluation/13.txt", "evaluation/14.txt", "evaluation/15.txt", "evaluation/16.txt", "evaluation/17.txt", "evaluation/18.txt", "evaluation/19.txt", "evaluation/20.txt", "evaluation/21.txt", "evaluation/22.txt", "evaluation/23.txt", "evaluation/24.txt", "evaluation/25.txt", "evaluation/26.txt", "evaluation/27.txt", "evaluation/28.txt", "evaluation/29.txt", "evaluation/30.txt", "evaluation/31.txt", "evaluation/32.txt", "evaluation/33.txt", "evaluation/34.txt", "evaluation/35.txt", "evaluation/36.txt", "evaluation/37.txt", "evaluation/38.txt", "evaluation/39.txt", "evaluation/40.txt", "evaluation/41.txt", "evaluation/42.txt", "evaluation/43.txt", "evaluation/44.txt", "evaluation/45.txt", "evaluation/46.txt", "evaluation/47.txt", "evaluation/48.txt", "evaluation/49.txt", "evaluation/50.txt", "evaluation/51.txt", "evaluation/52.txt", "evaluation/53.txt", "evaluation/54.txt", "evaluation/55.txt", "evaluation/56.txt", "evaluation/57.txt", "evaluation/58.txt", "evaluation/59.txt", "evaluation/60.txt", "evaluation/61.txt", "evaluation/62.txt", "evaluation/63.txt", "evaluation/64.txt", "evaluation/65.txt", "evaluation/66.txt", "evaluation/67.txt", "evaluation/68.txt", "evaluation/69.txt", "evaluation/70.txt", "evaluation/71.txt", "evaluation/72.txt", "evaluation/73.txt", "evaluation/74.txt", "evaluation/75.txt", "evaluation/76.txt", "evaluation/77.txt", "evaluation/78.txt", "evaluation/79.txt", "evaluation/80.txt", "evaluation/81.txt", "evaluation/82.txt", "evaluation/83.txt", "evaluation/84.txt", "evaluation/85.txt", "evaluation/86.txt", "evaluation/87.txt", "evaluation/88.txt", "evaluation/89.txt", "evaluation/90.txt", "evaluation/91.txt", "evaluation/92.txt", "evaluation/93.txt", "evaluation/94.txt", "evaluation/95.txt", "evaluation/96.txt", "evaluation/97.txt", "evaluation/98.txt", "evaluation/99.txt", "evaluation/100.txt"]

    h = len(list1)
    g = len(list2)
    arr = []
    f = open("Similarity_Report.csv", "w")
    f.write(',a,b,c,d,e\n')
    for i in range(g):
        f.write('{},'.format(i+1))
        for j in range(h):
            f.writelines('{},'.format(main(list1[j], list2[i])))
        f.write('\n')
    f.close()