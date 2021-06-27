import csv
import bilisearch
import time
def start(author):
    with open ('res.csv','w') as csvfile:
        csvwriter = csv.writer(csvfile)
        headline = []
        headline.append('TIME')
        headline = headline + author
        csvwriter.writerow(headline)
        csvfile.close()
        while True:
            with open ('res.csv','a') as csvfile:
                csvwriter = csv.writer(csvfile)
                nowtime = str(time.asctime( time.localtime(time.time())))
                fannumber = []
                fannumber.append(nowtime)
                for x in author:
                    fannumber.append ( str( bilisearch.get_fannum(x) ) )
                csvwriter.writerow(fannumber)
                csvfile.close()
                time.sleep(300)