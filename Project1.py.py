name = "Daniel Lee"

Student_ID = "C02759269"
#https://abcnews.go.com/US/mendocino-complex-fire-now-largest-california-history/story?id=57073385


CA_WILDFIRE_LARGEST_IN_HISTORY = '''
      Fire name, cause                Date              County            Acres     Death

--------------------------------------------------------------------------------------------

1. MENDOCINO COMPLEX (unknown)      July 2018       Mendocino/Lake       283,800      0
2. THOMAS (Under investigation)     Dec. 2017    Ventura/Santa Barbara   281.893      1
3. CEDAR (Human-related)            Oct. 2003          San Diego         273,246      15
4. RUSH (Lightning)                 Aug. 2012          Lassen            271,911      0
5. RIM (Human-related)              Aug. 2013          Tuolumne          257,314      0
6. ZACA (Human-related)             July 2007          Santa Barbara     240,207      0
7. MATILIJA (Undetermined)          Sept. 1932         Ventura           220,000      0
8. WITCH (Power lines)              Oct. 2007          San Diego         197,990      2
9. KLAMATH (Lightning)              June 2008          Siskiyou          192,038      2
10. MARBLE CONE (Lightning)         July 1977          Monterey          177,866      0

'''


CA_WILDFIRE_LARGEST_IN_HISTORY_tuple = (('Fire name, cause', 'Date', 'County', 'Acres', 'Death'),
                      ('MENDOCINO COMPLEX (unknown)', 'July 2018', 'Mendocino/Lake', 283800, 0),
                      ('THOMAS (Under investigation)', 'Dec. 2017', 'Ventura/Santa Barbara', 281893, 1),
                      ('CEDAR (Human-related)', 'Oct. 2003', 'San Diego', 273246, 15),
                      ('RUSH (Lightning)','Aug. 2012', 'Lassen', 271911, 0),
                      ('RIM (Human-related)', 'Aug. 2013', 'Tuolumne', 257314, 0),
                      ('ZACA (Human-related)', 'July 2007', 'Santa Barbara', 240207, 0),
                      ('MATILIJA (Undetermined)', 'Sept. 1932', 'Ventura', 220000, 0),
                      ('WITCH (Power lines)', 'Oct. 2007', 'San Diego', 197990, 2),
                      ('KLAMATH (Lightning)', 'June 2008', 'Siskiyou', 192038, 2),
                      ('MARBLE CONE (Lightning)', 'July 1977', 'Monterey', 177866, 0)
                     )


print(CA_WILDFIRE_LARGEST_IN_HISTORY_tuple)
print(type(CA_WILDFIRE_LARGEST_IN_HISTORY_tuple))

CA_WILDFIRE_LARGEST_IN_HISTORY_list = []
for i in CA_WILDFIRE_LARGEST_IN_HISTORY_tuple:
    CA_WILDFIRE_LARGEST_IN_HISTORY_list.append(i)


class CA_WILDFIRE_LARGEST_IN_HISTORY():
    def __init__(self, FireNameCause: str, Date: str, County: int,
                 Acres: int, Death: int):
        self.FireNameCause = contractName
        self.Date = Date
        self.County = County
        self.Acres = Acres
        self.Death = Death
