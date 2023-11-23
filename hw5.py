import csv
fn = open('athlete_events_2000-2016_cl.csv', 'r', encoding='utf-8-sig') 
data = list(csv.reader(fn, delimiter = ','))
fn.close()

fn = open('athlete_events_mock.csv', 'r', encoding='utf-8-sig') 
data_mock = list(csv.reader(fn, delimiter = ','))
fn.close()

def convert_to_dict(data):
    athletes_by_Year_NOC = {}
    for i in range(1,len(data)):
        year = data[i][9]
        country = data[i][7]
        person = {}
        for j in range(len(data[0])):
            person[data[0][j]] = data[i][j]
        if year not in athletes_by_Year_NOC:
            athletes_by_Year_NOC[year] = {}
        if country not in athletes_by_Year_NOC[year]:
            athletes_by_Year_NOC[year][country] = []
        athletes_by_Year_NOC[year][country].append(person)
    return athletes_by_Year_NOC


def get_medals_by_team(athletes_by_Year_NOC, year):
    
    medals = {}
    noc = athletes_by_Year_NOC[year]
    for i in noc:
        gold = 0
        silver = 0
        bronze = 0
        for j in noc[i]:
            if j['Medal'] == 'Gold':gold += 1
            if j['Medal'] == 'Silver':silver += 1
            if j['Medal'] == 'Bronze':bronze += 1
        medals[i] = (gold, silver, bronze)
    return medals


def get_top_five(medals):
    topfive = []
    score_country = {}
    for country in medals:
        if medals[country] not in score_country:
            score_country[medals[country]] = []
        score_country[medals[country]].append(country)
    number = 0
    top = sorted(score_country)[::-1]
    for score in top:
        if number >=5:
            break
        wait = []
        for j in score_country[score]:
            wait.append((j, score[0], score[1], score[2]))
        wait.sort()
        topfive += wait
        number += len(score_country[score])
    return topfive

def get_medals_trend(athletes_by_Year_NOC, NOC, start, end):
    trend = []
    for i in range(start, end+1):
        if str(i) in athletes_by_Year_NOC:
            by_year = get_medals_by_team(athletes_by_Year_NOC, str(i))
            if NOC in by_year:
                by_country = by_year[NOC]
                trend.append((str(i), by_country[0], by_country[1], by_country[2]))
    return trend

def get_sports(athletes_by_Year_NOC, NOC, year):
    sports = set()
    if str(year) in athletes_by_Year_NOC:
        by_year = athletes_by_Year_NOC[str(year)]
        if NOC in by_year:
            by_country = by_year[NOC]
            for i in range(len(by_country)):
                if by_country[i]['Medal'] != 'NA':
                    sports.add(by_country[i]['Sport'])
    return sports

def get_common_sports(athletes_by_Year_NOC, NOCs, year):
    sports = set()
    get = False
    for i in NOCs:
        if not get:
            sports = get_sports(athletes_by_Year_NOC, i, year)
            get = True
        sports = sports & get_sports(athletes_by_Year_NOC, i, year)
    return sports

d = convert_to_dict(data)
print(get_common_sports(d, {'THA','VIE'}, '2008'))
print(get_common_sports(d, {'THA','VIE','DEN'}, '2008'))
print(get_common_sports(d, {'THA','XXX'}, '2008'))