import csv
import math 

#Stole from Bart for this reading function
def read_file (file_name):
    with open(file_name, "r") as f:
        rows = csv.reader(f)
        data = []
        for row in rows:
            c = int(row[0])
            fs = [int(f) for f in row[1:]]
            data.append((c, fs))
    return data

def display_file(file):
    for c,fs in file:
        print(c,fs)

def training (train_file):
    train_data= read_file(train_file)
    total_instance=0

    #fine how many instances and features per instance
    for c,fs in train_data:
        total_instance+=1
        total_feature=0
        for f in fs:
            total_feature+=1
    N=[0]*2
    F=[[0]*total_feature for  _ in range (2)]
    
    for c,fs in train_data:
        N[c]+=1
        index=0
        for f in fs:
            if f == 1:
                F[c][index]+=1
                #print(F[0][5],F[1][5])
            index+=1
    return N,F

def compute_prob (target,train_file,test_instance): #target =0 for normal, 1 for abnormal hear
    N,F = training(train_file)
    L =[0]*2
    L[target]=math.log(N[target]+0.5)- math.log (N[0]+N[1]+0.5)
    index =0
    for fs in test_instance:
        s = F[target][index]
        if fs == 0:
            s=N[target]-s
        L[target]=L[target]+math.log(s+0.5)-math.log(N[target]+0.5)
        index+=1
    return L[target]

def classify_instance(train_file,test_instance):
    #print(compute_prob(1,train_file,test_instance),"  ",compute_prob(0,train_file,test_instance))
    if compute_prob(1,train_file,test_instance) > compute_prob(0,train_file,test_instance):
        return 1
    return 0



def main():
    print("Choose 1 to 4\n")
    print("1:spect-itg \n")
    print("2:spect-org\n")
    print("3:spect-resplit\n")
    print("4:spect-resplit-itg\n")
    choice = int(input())
    if choice == 1:
        total_instance =0
        total_correct=0
        total_positive=0
        total_positive_correct=0
        total_negative=0
        total_negative_correct=0

        test_data = read_file("spect-itg.test.csv")
        for c,f in test_data:
            total_instance+=1
            if c == 0:
                total_negative+=1
            if c== 1:
                total_positive+=1
            if classify_instance("spect-itg.train.csv",f) == c:
                total_correct+=1
                if c == 0:
                    total_negative_correct+=1
                if c== 1:
                    total_positive_correct+=1
        print ("spec-itg: ",total_correct,"/",total_instance)
        print ("true negative: ",total_negative_correct,"/",total_negative)
        print ("true positive: ",total_positive_correct,"/",total_positive)

    elif choice == 2:
        total_instance =0
        total_correct=0
        total_positive=0
        total_positive_correct=0
        total_negative=0
        total_negative_correct=0

        test_data = read_file("spect-orig.test.csv")
        for c,f in test_data:
            total_instance+=1
            if c == 0:
                total_negative+=1
            if c== 1:
                total_positive+=1
            if classify_instance("spect-orig.train.csv",f) == c:
                total_correct+=1
                if c == 0:
                    total_negative_correct+=1
                if c== 1:
                    total_positive_correct+=1
        print ("spect-org: ",total_correct,"/",total_instance)
        print ("true negative: ",total_negative_correct,"/",total_negative)
        print ("true positive: ",total_positive_correct,"/",total_positive)

    elif choice == 3:
        total_instance =0
        total_correct=0
        total_positive=0
        total_positive_correct=0
        total_negative=0
        total_negative_correct=0

        test_data = read_file("spect-resplit.test.csv")
        for c,f in test_data:
            total_instance+=1
            if c == 0:
                total_negative+=1
            if c== 1:
                total_positive+=1
            if classify_instance("spect-resplit.train.csv",f) == c:
                total_correct+=1
                if c == 0:
                    total_negative_correct+=1
                if c== 1:
                    total_positive_correct+=1
        print ("spect-resplit: ",total_correct,"/",total_instance)
        print ("true negative: ",total_negative_correct,"/",total_negative)
        print ("true positive: ",total_positive_correct,"/",total_positive)

    elif choice == 4:
        total_instance =0
        total_correct=0
        total_positive=0
        total_positive_correct=0
        total_negative=0
        total_negative_correct=0

        test_data = read_file("spect-resplit-itg.test.csv")
        for c,f in test_data:
            total_instance+=1
            if c == 0:
                total_negative+=1
            if c== 1:
                total_positive+=1
            if classify_instance("spect-resplit-itg.train.csv",f) == c:
                total_correct+=1
                if c == 0:
                    total_negative_correct+=1
                if c== 1:
                    total_positive_correct+=1
        print ("resplit-itg: ",total_correct,"/",total_instance)
        print ("true negative: ",total_negative_correct,"/",total_negative)
        print ("true positive: ",total_positive_correct,"/",total_positive)


main()
#training("spect-orig.train.csv")
#compute_prob(1,"spect-orig.train.csv","spect-orig.test.csv")

