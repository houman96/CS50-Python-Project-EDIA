#import needed library
import pandas as pd
import numpy as np

#read the Emergency Drug Instant Access (EDIA) CSV file
df = pd.read_csv("EDIA.csv")

#Ask the intern which disease and what drug he/she is going to used
disease = input("Please enter disease name: ").lower()
drug = input("Please enter drug name: ").lower()

#Find disease+drug
dose = df.loc[(df["Disease"] == disease) & (df["Drug"] == drug)]

#Tell the dosing
for dosing in dose['Dose']:
    print (dosing)
