import random, math
import numpy as np
import pandas as pd
def generate_data(n):
    data = []
    for i in range(n):
        m = random.randint(0,100)
        a = random.randint(0,100)
        ass = random.randint(0,50)
        pi = (m*0.6 + ass*0.4) * math.log(a+1)
        data.append((f"S{i+1}", m, a, ass, pi))
    return data
def classify_students(data):
    d = {}
    for s in data:
        id, m, a, _, _ = s
        if m < 40 or a < 50:
            d[id] = "At Risk"
        elif m <= 70:
            d[id] = "Average"
        elif m <= 90:
            d[id] = "Good"
        else:
            d[id] = "Top Performer"
    return d
def analyze_data(data):
    df = pd.DataFrame(data, columns=["ID","Marks","Att","Assign","PI"])
    marks = df["Marks"].values
    att = df["Att"].values
    mean = sum(marks)/len(marks)
    median = np.median(marks)
    std = np.std(marks)
    corr = np.corrcoef(marks, att)[0][1]
    mn, mx = min(marks), max(marks)
    df["Norm"] = [(x-mn)/(mx-mn) for x in marks]
    risk = sum(1 for x in att if x < 50)
    top = sum(1 for x in marks if x > 90)
    if std < 15 and risk <= 3 and top >= 2:
        insight = "Stable Academic System"
    elif risk > 3:
        insight = "Critical Attention Required"
    else:
        insight = "Moderate Performance"
    return df, (mean, std, max(marks)), insight
last_digit=1
n = max(10,last_digit)
data = generate_data(n)
print("\nData:\n", pd.DataFrame(data))
print("\nClassification:\n", classify_students(data))
df, summary, insight = analyze_data(data)
print("\nFinal DataFrame:\n", df)
print("\nSummary (mean, std, max):", summary)
print("\nInsight:", insight)