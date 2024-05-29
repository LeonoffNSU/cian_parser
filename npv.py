import pandas as pd


df = pd.read_excel('Продажи.xlsx')
df['payment'] = df['payment'].astype(int)

PI = 0.6 * df['price']
for month in range(1, 13):
    I_month = round(df['payment'] / 1.0042 ** month, 2)
    PI += I_month

for month in range(1, 25):
    I_month = round(df['payment'] / ((1.0042 ** 12) * (1.0033 ** month)), 2)
    PI += I_month

df['PI'] = PI

price_year1 = df['price'] * 1.0192934
price_year2 = price_year1 * 1.0192934
price_year3 = price_year2 * 1.0192934
price_year4 = price_year3 * 1.0192934
price_year5 = price_year4 * 1.0192934
price_year6 = price_year5 * 1.0192934
price_year7 = price_year6 * 1.0192934
price_year8 = price_year7 * 1.0192934
price_year9 = price_year8 * 1.0192934
price_year10 = price_year9 * 1.0192934
price_year11 = price_year10 * 1.0192934
price_year12 = price_year11 * 1.0192934
price_year13 = price_year12 * 1.0192934
price_year14 = price_year13 * 1.0192934
price_year15 = price_year14 * 1.0192934

r1_year = ((price_year1 - df['price']) + df['potential_rental_cost'] * 12) / df['price']
r2_year = ((price_year2 - price_year1) + df['potential_rental_cost'] * 12) / price_year1
r3_year = ((price_year3 - price_year2) + df['potential_rental_cost'] * 12) / price_year2
r4_year = ((price_year4 - price_year3) + df['potential_rental_cost'] * 12) / price_year3
r5_year = ((price_year5 - price_year4) + df['potential_rental_cost'] * 12) / price_year4
r6_year = ((price_year6 - price_year5) + df['potential_rental_cost'] * 12) / price_year5
r7_year = ((price_year7 - price_year6) + df['potential_rental_cost'] * 12) / price_year6
r8_year = ((price_year8 - price_year7) + df['potential_rental_cost'] * 12) / price_year7
r9_year = ((price_year9 - price_year8) + df['potential_rental_cost'] * 12) / price_year8
r10_year = ((price_year10 - price_year9) + df['potential_rental_cost'] * 12) / price_year9
r11_year = ((price_year11 - price_year10) + df['potential_rental_cost'] * 12) / price_year10
r12_year = ((price_year12 - price_year11) + df['potential_rental_cost'] * 12) / price_year11
r13_year = ((price_year13 - price_year12) + df['potential_rental_cost'] * 12) / price_year12
r14_year = ((price_year14 - price_year13) + df['potential_rental_cost'] * 12) / price_year13
r15_year = ((price_year15 - price_year14) + df['potential_rental_cost'] * 12) / price_year14

PV = 0 * df['price']
multiplier1 = (1 + r1_year / 12) ** 12
multiplier2 = multiplier1 * ((1 + r2_year / 12) ** 12)
multiplier3 = multiplier2 * ((1 + r3_year / 12) ** 12)
multiplier4 = multiplier3 * ((1 + r4_year / 12) ** 12)
multiplier5 = multiplier4 * ((1 + r5_year / 12) ** 12)
multiplier6 = multiplier5 * ((1 + r6_year / 12) ** 12)
multiplier7 = multiplier6 * ((1 + r7_year / 12) ** 12)
multiplier8 = multiplier7 * ((1 + r8_year / 12) ** 12)
multiplier9 = multiplier8 * ((1 + r9_year / 12) ** 12)
multiplier10 = multiplier9 * ((1 + r10_year / 12) ** 12)
multiplier11 = multiplier10 * ((1 + r11_year / 12) ** 12)
multiplier12 = multiplier11 * ((1 + r12_year / 12) ** 12)
multiplier13 = multiplier12 * ((1 + r13_year / 12) ** 12)
multiplier14 = multiplier13 * ((1 + r14_year / 12) ** 12)
multiplier15 = multiplier14 * ((1 + r15_year / 12) ** 12)

# ладно, пусть будет 15 циклов (копировать - вставить)
for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (1 + r1_year / 12) ** month, 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r2_year / 12) ** month) * multiplier1), 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r3_year / 12) ** month) * multiplier2), 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r4_year / 12) ** month) * multiplier3), 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r5_year / 12) ** month) * multiplier4), 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r6_year / 12) ** month) * multiplier5), 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r7_year / 12) ** month) * multiplier6), 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r8_year / 12) ** month) * multiplier7), 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r9_year / 12) ** month) * multiplier8), 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r10_year / 12) ** month) * multiplier9), 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r11_year / 12) ** month) * multiplier10), 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r12_year / 12) ** month) * multiplier11), 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r13_year / 12) ** month) * multiplier12), 2)
    PV += C_month

for month in range(1, 13):
    C_month = round(df['potential_rental_cost'] / (((1 + r14_year / 12) ** month) * multiplier13), 2)
    PV += C_month

for month in range(1, 12):  # до 179-го слагаемого, в 180-м нужно добавить future value
    C_month = round(df['potential_rental_cost'] / (((1 + r15_year / 12) ** month) * multiplier14), 2)
    PV += C_month

last_term = round((df['potential_rental_cost'] + price_year15) / (((1 + r15_year / 12) ** 12) * multiplier14), 2)
PV += last_term
df['PV'] = PV
df['NPV'] = df['PV'] - df['PI']

with pd.ExcelWriter('NPV.xlsx') as writer:
    df.to_excel(writer, sheet_name='Данные', index=False)
