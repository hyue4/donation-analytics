import sys
from scipy import stats

def main():
    itcont = sys.argv[1]
    percentile = sys.argv[2]
    output = sys.argv[3]
    data = []
    indexes = [0, 7, 10, 13, 14, 15]
    donors = {}
    recipents = {}
    ret_indexes = [0, 2, 3]
    with open(percentile) as f:
        percentile = f.readlines()
    percentile = int(percentile[0]) / 100
    with open(output, 'w+') as out:
        with open(itcont) as f:
            for line in f:
                # first we split the lines into arrays
                tmp = line.split('|')
                # now we get the relevent index
                cur = [tmp[i] for i in indexes]
                # if other_id skip
                if(cur[5] != ''):
                    next 
                # truncate the zip and year
                cur[2] = cur[2][0:5]
                cur[3] = cur[3][4:]
                # if this is a repeat donor add the line to the donor
                donor = cur[1] + cur[2]
                if donors.get(donor):
                    # cur recipet
                    rec = cur[0] + cur[2]
                    year = cur[3]
                    # if the recipet has recieved donations before
                    if recipents.get(rec):
                        # if the recipet has recieved donations before in this year
                        if recipents[rec].get(year):
                            recipents[rec][year].append(int(cur[4]))
                        # if different year, make new year record and append donation
                        else:
                            recipents[rec][year] = []
                            recipents[rec][year].append(int(cur[4]))
                    # if the recipet has not recieved a donation before
                    else:
                        recipents[rec] = {}
                        recipents[rec][year] = []
                        recipents[rec][year].append(int(cur[4]))
                    ret = [cur[i] for i in ret_indexes]
                    # calculate percentile
                    # total for that year
                    total = sum(recipents[rec][year])
                    # number of contributions for that year
                    contributions = len(recipents[rec][year])
                    perc = int(round(stats.scoreatpercentile(recipents[rec][year], percentile)))
                    ret = ret + [str(perc), str(total), str(contributions)]
                    out.write('|'.join(ret) + '\n')
                    print(ret)
                # if not mark as repeat
                else:
                    donors[donor] = True

main()
    