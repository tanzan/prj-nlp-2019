def split_tags(string):
    return [tuple(i.split("/")) for i in string.split()]

def readTrainData(filename):
    data = []
    for line in open(filename):
        line = line.strip()
        #read in training or dev data with labels
        if len(line.split('\t')) == 7:
            (trendid, trendname, origsent, candsent, judge, origsenttag, candsenttag) = \
            line.split('\t')
        else:
            continue
        # ignoring the training data that has middle label 
        nYes = eval(judge)[0]            
        if nYes >= 3:
            amt_label = True
            data.append((split_tags(origsenttag), split_tags(candsenttag), amt_label))
        elif nYes <= 1:
            amt_label = False
            data.append((split_tags(origsenttag), split_tags(candsenttag), amt_label))
    return data

def readTestData(filename):
    data = []
    for line in open(filename):
        line = line.strip()
        #read in training or dev data with labels
        if len(line.split('\t')) == 7:
            (trendid, trendname, origsent, candsent, judge, origsenttag, candsenttag) = \
            line.split('\t')
        else:
            continue
        # ignoring the training data that has middle label 
        nYes = int(judge[0])
        if nYes >= 4:
            expert_label = True
        elif nYes <= 2:
            expert_label = False
        else:
            expert_label = None
        data.append((split_tags(origsenttag), split_tags(candsenttag), expert_label))
    return data

train_data = readTrainData("SemEval-PIT2015-py3/data/dev.data")
test_data = readTestData("SemEval-PIT2015-py3/data/test.data")