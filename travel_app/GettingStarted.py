#from datarel import datarel

from surprise import *
import os
import csv
import sys
import re

from surprise import Dataset
from surprise import Reader
from surprise import accuracy
class datarel:

    citiesId_to_name = {}
    name_to_citiesId = {}
    ratingsPath = r'C:\\Users\\acer\\Downloads\\Project_Work-20191225T172835Z-001\\Project_Work\\traverCity\\data\\ratings.csv'
    citiesPath = r'C:\\Users\\acer\\Downloads\\Project_Work-20191225T172835Z-001\\Project_Work\\traverCity\\data\\cities.csv'

    def loadCitiesLatest(self):


        #os.chdir(os.path.dirname(sys.argv[0]))

        ratingsDataset = 0
        self.citiesId_to_name = {}
        self.name_to_citiesId = {}

        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)

        ratingsDataset = Dataset.load_from_file(self.ratingsPath, reader=reader)

        with open(self.citiesPath, newline='', encoding='ISO-8859-1') as csvfile:
                citiesReader = csv.reader(csvfile)
                next(citiesReader)  #Skip header
                for row in citiesReader:
                    placeId = int(row[0])
                    city = row[1]
                    self.citiesId_to_name[placeId] = city
                    self.name_to_citiesId[city] = placeId

        return ratingsDataset

    def assignedrating(self, user):
        userRatings = []
        hitUser = False
        with open(self.ratingsPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                userID = int(row[0])
                if (user == userID):
                    placeId = int(row[1])
                    rating = float(row[2])
                    userRatings.append((placeId, rating))
                    hitUser = True
                if (hitUser and (user != userID)):
                    break

        return userRatings

#    def getPopularityRanks(self):
#        ratings = defaultdict(int)
#        rankings = defaultdict(int)
#        with open(self.ratingsPath, newline='') as csvfile:
#            ratingReader = csv.reader(csvfile)
#            next(ratingReader)
#            for row in ratingReader:
#                placeId = int(row[1])
#                ratings[placeId] += 1
#        rank = 1
#        for placeId, ratingCount in sorted(ratings.items(), key=lambda x: x[1], reverse=True):
#            rankings[placeId] = rank
#            rank += 1
#        return rankings

    def gettype(self):
        type = defaultdict(list)
        typeId = {}
        maxtypeId = 0
        with open(self.citiesPath, newline='', encoding='ISO-8859-1') as csvfile:
            citiesReader = csv.reader(csvfile)
            next(citiesReader)
            for row in citiesReader:
                placeId = int(row[0])
                typeList = row[3].split('|')
                typeIdlist = []
                print(typeList)
                for t in typeList:
                    if t in typeId:
                        tId = typeId[t]
                    else:
                        tId = maxtypeId
                        typeId[t] = tId
                        maxtypeId += 1
                    typeIdlist.append(tId)
                type[placeId] = typeIdlist

        for (placeId, typeIdlist) in type.items():
            bitfield = [0] * maxtypeId
            for tId in typeIdlist:
                bitfield[tId] = 1
            type[placeId] = bitfield

        return type

#    def getYears(self):
#        p = re.compile(r"(?:\((\d{4})\))?\s*$")
#        years = defaultdict(int)
#        with open(self.citiesPath, newline='', encoding='ISO-8859-1') as csvfile:
#            citiesReader = csv.reader(csvfile)
#            next(citiesReader)
#            for row in citiesReader:
#                placeId = int(row[0])
#                title = row[1]
#                m = p.search(title)
#                year = m.group(1)
#                if year:
#                    years[placeId] = int(year)
#        return years

#    def getMiseEnScene(self):
#        mes = defaultdict(list)
#        with open("LLVisualFeatures13K_Log.csv", newline='') as csvfile:
#            mesReader = csv.reader(csvfile)
#            next(mesReader)
#            for row in mesReader:
#                placeId = int(row[0])
#                avgShotLength = float(row[1])
#                meanColorVariance = float(row[2])
#                stddevColorVariance = float(row[3])
#                meanMotion = float(row[4])
#                stddevMotion = float(row[5])
#                meanLightingKey = float(row[6])
#                numShots = float(row[7])
#                mes[placeId] = [avgShotLength, meanColorVariance, stddevColorVariance,
#                   meanMotion, stddevMotion, meanLightingKey, numShots]
#        return mes

    def getcity(self, placeId):
        if placeId in self.citiesId_to_name:
            return self.citiesId_to_name[placeId]
        else:
            return ""

    def getplaceId(self, city):
        if city in self.name_to_citiesId:
            return self.name_to_citiesId[city]
        else:
            return 0

#    def getstate(self, placeId):
#        with open(self.citiesPath, newline='', encoding='ISO-8859-1') as csvfile:
#                citiesReader = csv.reader(csvfile)
#                next(citiesReader)  #Skip header line
#                for row in citiesReader:
#                    state = int(row[2])


from collections import defaultdict

def TestSet(testSubject, trainset):
    fill = trainset.global_mean

    anti_testset = []

    u = trainset.to_inner_uid(str(testSubject))

    user_items = set([j for (j, _) in trainset.ur[u]])
    anti_testset += [(trainset.to_raw_uid(u), trainset.to_raw_iid(i), fill) for
                             i in trainset.all_items() if
                             i not in user_items]
    return anti_testset


#testSubject = 2

#ml = datarel()

#print("Loading cities...")
#data = ml.loadCitiesLatest()
#print(data)

#Ratings = ml.assignedrating(testSubject)
#loved = []
#hated = []
#for ratings in Ratings:
#    if (float(ratings[1]) > 3.0):
#        loved.append(ratings)
#    if (float(ratings[1]) <= 3.0):
#        hated.append(ratings)

#print("\nUser ", testSubject, " loved these sites:")
#for ratings in loved:
#    print(ml.getcity(ratings[0]))
#print("\n...and negative value:")
#for ratings in hated:
#    print(ml.getcity(ratings[0]))

#print("\nBuilding model...")
#trainSet = data.build_full_trainset()

#algo = SVD()
#algo.fit(trainSet)

#print("Computing recommendations...")
#testSet = TestSet(testSubject, trainSet)
#predictions = algo.test(testSet)

#recommendations = []

#print ("\nWe recommend Cities:")
#for userID, placeId, actualRating, estimatedRating, _ in predictions:
#    intplaceId = int(placeId)
#    recommendations.append((intplaceId, estimatedRating))

#recommendations.sort(key=lambda x: x[1], reverse=True)

#for ratings in recommendations[:10]:
#   print(ml.getcity(ratings[0]))

def Get():
    testSubject = 2
    ml = datarel()

    print("Loading cities...")
    data = ml.loadCitiesLatest()
    #print(data)
    Ratings = ml.assignedrating(testSubject)
    loved = []
    hated = []
    for ratings in Ratings:
        if (float(ratings[1]) > 3.0):
            loved.append(ratings)
        if (float(ratings[1]) <= 3.0):
            hated.append(ratings)
    print("\nUser ", testSubject, " loved these sites:")
    for ratings in loved:
        print(ml.getcity(ratings[0]))
    print("\n...and negative value:")
    #for ratings in hated:
    #    print(ml.getcity(ratings[0]))

    print("\nBuilding model...")
    trainSet = data.build_full_trainset()

    algo = SVD()
    algo.fit(trainSet)

    print("Computing recommendations...")
    testSet = TestSet(testSubject, trainSet)
    predictions = algo.test(testSet)

    recommendations = []

    print ("\nWe recommend Cities:")
    for userID, placeId, actualRating, estimatedRating, _ in predictions:
        intplaceId = int(placeId)
        recommendations.append((intplaceId, estimatedRating))
    out = []
    recommendations.sort(key=lambda x: x[1], reverse=True)
    print("SDGFVXDVGBD")
   
    for ratings in recommendations[:10]:
        print(ml.getcity(ratings[0]))
        out.append(ml.getcity(ratings[0]))
    
    return out
Get()
