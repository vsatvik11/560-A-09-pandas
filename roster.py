
#https://goheels.com/sports/mens-basketball/roster
import pandas as pd
roster = ["Dixon", "Young", "Denis"]
player = {"Last Name": ["Dixon", "Young", "Denis"],
          "First Name": ["Derek", "Jaydon", "Denis"],
          "height": [83,72,73], 
          "weight": [240,180,180]}
data = pd.DataFrame(roster)
print(data)
