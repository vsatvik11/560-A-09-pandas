
#https://goheels.com/sports/mens-basketball/roster
import pandas as pd
roster = ["Dixon", "Young", "Denis", "Davis", "trimble", "Wilson", "Powell", "Veesaar", "Stevenson", "Holbrook"]
player = {"Last Name": ["Dixon", "Young", "Denis", "Davis", "trimble", "Wilson", "Powell", "Veesaar", "Stevenson", "Holbrook"],
          "First Name": ["Derek", "Jaydon", "Isaiah", "Elijah", "Seth", "Caleb", "Jonathan", "Henri", "Jarin", "John"],
          "height": [77,76,76, 75, 75, 82, 78, 84, 82, 80], 
          "weight": [200,200,180, 205, 200, 215, 190, 225, 215, 230]}
data = pd.DataFrame(player)

#bmi = weight inkg/height in meters squared
data["bmi"] = (data["weight"]/2.205/((data["height"]/39.37)**2)).round(2)
print(data)
data.to_csv("bmi.csv")