import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("data/Global Economy Indicators.csv")
df.columns=df.columns.str.strip()
df["Country"]=df["Country"].str.strip()

df1=df[df["Year"]==2021]
df2=df1.sort_values(by="Gross Domestic Product (GDP)", ascending=False)

liste=df2["Country"].head().tolist()
df3=df[df["Country"].isin(liste)]

df_us=df[df["Country"]=="United States"]
df_us1=df_us.sort_values(by="Year",ascending=True)
df_us1970 = df_us1.iloc[0]["Gross Domestic Product (GDP)"]
endeks=df_us1["Gross Domestic Product (GDP)"]/df_us1970*100
df_us1["Endeks"]=endeks

# ==================== SORU 1: BUYUME ENDEKSI ====================

for ulke in liste:
    tablo=df3[df3["Country"]==ulke]
    ztablo=tablo.sort_values(by="Year",ascending=True)
    ulke_1970=ztablo.iloc[0]["Gross Domestic Product (GDP)"]
    endeks1=ztablo["Gross Domestic Product (GDP)"]/ulke_1970*100
    print(endeks1.iloc[-1],ulke)
    plt.plot(ztablo["Year"],endeks1, label=ulke)

plt.title("En Büyük 5 Ekonominin Büyüme Endeksi (1970 = 100)")
plt.xlabel("YIL")
plt.ylabel("Endeks (1970 = 100, log ölçek)")
plt.legend()
plt.yscale("log")
plt.savefig("images/soru1_endeks.png")
plt.show()

# ==================== SORU 2: TARIMIN PAYI ====================

df3["Tarim_Payi"]=df3["Agriculture, hunting, forestry, fishing (ISIC A-B)"]/df3["Total Value Added"]*100

deger_1970 = []
deger_2021 = []

for ulke in liste:
    c = df3[df3["Country"] == ulke]
    a = c.sort_values(by="Year", ascending=True)
    deger_1970.append(a["Tarim_Payi"].iloc[0])
    deger_2021.append(a["Tarim_Payi"].iloc[-1])

x = np.arange(len(liste))
genislik = 0.35

plt.bar(x - genislik/2, deger_1970, genislik, label="1970")
plt.bar(x + genislik/2, deger_2021, genislik, label="2021")
plt.xticks(x, liste)
plt.title("Tarımın Toplam Katma Değer İçindeki Payı (%)")
plt.xlabel("Ülke")
plt.ylabel("Tarım Payı (%)")
plt.legend()
plt.savefig("images/soru2_tarim.png")
plt.show()

# ==================== SORU 3: KRIZ ETKISI ====================

for ulke in liste:
    df3_ulke=df[df["Country"]==ulke]

    deger_2008 = df3_ulke[df3_ulke["Year"]==2008]["Gross Domestic Product (GDP)"].iloc[0]
    deger_2009 = df3_ulke[df3_ulke["Year"]==2009]["Gross Domestic Product (GDP)"].iloc[0]
    deger_2019 = df3_ulke[df3_ulke["Year"]==2019]["Gross Domestic Product (GDP)"].iloc[0]
    deger_2020 = df3_ulke[df3_ulke["Year"]==2020]["Gross Domestic Product (GDP)"].iloc[0]

    degisim_2009 = (deger_2009 - deger_2008) / deger_2008 * 100
    degisim_2020 = (deger_2020 - deger_2019) / deger_2019 * 100

    print(ulke, "| 2008 krizi:", degisim_2009, "| 2020 krizi:", degisim_2020)

degisim_2008 = [-2.027027027027027, 11.11111111111111, 3.522504892367906, -8.847184986595174, 3.937007874015748]
degisim_2020 = [-1.4018691588785046, 2.797202797202797, -1.5625, 0.0, -6.315789473684211]

x = np.arange(len(liste))
genislik = 0.35

plt.bar(x - genislik/2, degisim_2008, genislik, label="2008 Krizi")
plt.bar(x + genislik/2, degisim_2020, genislik, label="2020 Krizi")
plt.xticks(x, liste)
plt.axhline(0, color="black", linewidth=0.8)
plt.title("Kriz Yıllarında GSYİH Yüzde Değişimi")
plt.xlabel("Ülke")
plt.ylabel("Yüzde Değişim (%)")
plt.legend()
plt.savefig("images/soru3_kriz.png")
plt.show()