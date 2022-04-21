import csv
import tkinter as tk
from tkinter import *
import pandas as pd

root = tk.Tk()
root.title('Paszonator2000 Demo')
root.geometry("1000x900")
button_label_list = []
wybrane_pasze = []
wybrane_where_start = 21
count_wybrane = 0


# Function for creating captions and buttons after selecting the feed
def wybierzo(k, pasza_objetosciowa_w):
    global count, button_label_list, wybrane_pasze, wybrane_where_start, count_wybrane

    if pasza_objetosciowa_w[k] not in wybrane_pasze:
        if count_wybrane < 10:
            wybrane_pasze.append(pasza_objetosciowa_w[k])

            b = tk.Button(root, text="Usuń")
            l = tk.Label(root, text=pasza_objetosciowa_w[k])
            b['command'] = lambda l=l, b=b: (usun_obj(b, l, pasza_objetosciowa_w, k))
            button_label_list.append([b, l])
            button_label_list[-1][1].grid(row=wybrane_where_start, column=0)
            button_label_list[-1][0].grid(row=wybrane_where_start, column=1, sticky=W)
            wybrane_where_start += 1
            count_wybrane += 1
        else:
            l = tk.Label(root, text="Wybierz maksymalnie 10 pasz.", fg='red')
            l.grid(row=20, column=1, columnspan=2)


# Another function for creating captions and buttons after selecting the feed. This time from another file with different feed.
def wybierzt(k, pasza_tresciwa):
    global count, button_label_list, wybrane_pasze, wybrane_where_start, count_wybrane

    if (pasza_tresciwa[k] not in wybrane_pasze):
        if count_wybrane < 10:
            wybrane_pasze.append(pasza_tresciwa[k])

            b = tk.Button(root, text="Usuń")
            l = tk.Label(root, text=pasza_tresciwa[k])
            b['command'] = lambda l=l, b=b: (usun_tr(b, l, pasza_tresciwa, k))
            button_label_list.append([b, l])
            button_label_list[-1][1].grid(row=wybrane_where_start, column=0)
            button_label_list[-1][0].grid(row=wybrane_where_start, column=1, sticky=W)
            wybrane_where_start += 1
            count_wybrane += 1
        else:
            l = tk.Label(root, text="Wybierz maksymalnie 10 pasz.", fg='red')
            l.grid(row=20, column=1, columnspan=3)


# Function for deleting buttons and caprions after using a delete button.
def usun_tr(b, l, pasza_tresciwa, k):
    global count_wybrane
    b.destroy()
    l.destroy()
    wybrane_pasze.remove(pasza_tresciwa[k])
    count_wybrane -= 1


# Function for deleting buttons and caprions after using a delete button for the other type of feed.
def usun_obj(b, l, pasza_objetosciowa_u, k):
    global count_wybrane
    b.destroy()
    l.destroy()
    wybrane_pasze.remove(pasza_objetosciowa_u[k])
    count_wybrane -= 1


# Download the content of the barn type selection window
def display_selected(choice):
    zmiana_obory_d = StringVar()
    zmiana_obory_d.get()


# Function for calculating the energy demand
def obliczanie_zap():
    global zapotrzebowanie, masa1, wydajnosc1, bialko1, tluszcz1
    masa1 = float(masa.get())
    wydajnosc1 = float(wydajnosc.get())
    tluszcz1 = float(tluszcz.get())
    bialko1 = float(bialko.get())
    laktoza1 = 48
    zp = ((tluszcz1 * 10 * 9 + bialko1 * 10 * 4 + laktoza1 * 4) / 1700) * (
                0.4 + 0.15 * tluszcz1) * wydajnosc1  # living energy demand
    zb = (70 * masa1 ** 0.75) / 1700  # Production energy demand
    zapotrzebowanie = zp + zb  # Whole energy demand
    if zmiana_obory.get() == "Wolnostanowiskowa":
        zapotrzebowanie *= 1.1
    l = tk.Label(window_zap, text="Dane zostały zapisane.")
    l.grid(row=8, column=1, sticky=W, columnspan=2)
    l = tk.Label(root, text="Dane zostały zapisane.")
    l.grid(row=0, column=7, sticky=W, columnspan=2)


# Popup window where cow data is entered
def popup_window_zap():
    global window_zap, masa, wydajnosc, tluszcz, bialko, zmiana_obory
    window_zap = tk.Toplevel()

    l = tk.Label(window_zap, text="Masa ciała krowy (kg):")
    l.grid(row=2, column=0)
    masa = tk.Entry(window_zap, width=20)
    masa.grid(row=2, column=1)

    l = tk.Label(window_zap, text="Wydajność mleczna (kg/dzień):")
    l.grid(row=3, column=0)
    wydajnosc = tk.Entry(window_zap, width=20)
    wydajnosc.grid(row=3, column=1)

    l = tk.Label(window_zap, text="Zawartość tłuszczu w mleku (%):")
    l.grid(row=4, column=0)
    tluszcz = tk.Entry(window_zap, width=20)
    tluszcz.grid(row=4, column=1)

    l = tk.Label(window_zap, text="Zawartość białka w mleku (%)")
    l.grid(row=5, column=0)
    bialko = tk.Entry(window_zap, width=20)
    bialko.grid(row=5, column=1)

    l = tk.Label(window_zap, text="Rodzaj obory:")
    l.grid(row=6, column=0)
    obory = ["Wolnostanowiskowa", "Uwięziowa"]
    zmiana_obory = StringVar()
    zmiana_obory.set(obory[1])
    dropdown = OptionMenu(
        window_zap,
        zmiana_obory,
        *obory,
        command=display_selected
    )
    dropdown.grid(row=6, column=1, columnspan=2, sticky=W)

    l = tk.Label(window_zap, text=" ")
    l.grid(row=7, column=0)
    l = tk.Label(window_zap, text=" ")
    l.grid(row=8, column=0)

    b = tk.Button(window_zap, text="Oblicz zapotrzebowanie", command=obliczanie_zap)
    b.grid(row=8, column=0)

    l = tk.Label(window_zap, text=" ")
    l.grid(row=9, column=0)

    b = tk.Button(window_zap, text="Zamknij", command=window_zap.destroy)
    b.grid(row=10, column=2)


# Popup window, where feed doses are calculated and shown
def popup_window_dawki():
    global window_dawki, masa1, wydajnosc1, zapotrzebowanie
    window_dawki = tk.Toplevel()
    window_dawki.geometry('300x500')

    bialko2 = 0.7 * masa1 + 85 * wydajnosc1
    SM = 30 * masa1 + 100 * wydajnosc1

    ileJPM = 0
    ileBialka = 0
    ileWlokna = 0
    ileTluszczu = 0
    ileSM = 0
    ileNDF = 0
    ileBTJN = 0
    ileBTJE = 0
    D_bez_BTJ = {}
    D_z_BTJ = {}

    pasza_objetosciowa_df = pd.read_csv("pasza_objetosciowa.csv", header=0)
    pasza_tresciwa_df = pd.read_csv("pasza_tresciwa.csv", header=0)
    polaczone = pd.DataFrame()

    # Creating a dataframe for selected feeds
    for i in wybrane_pasze:
        dodaj = pasza_objetosciowa_df.loc[pasza_objetosciowa_df['nazwa'] == i]
        polaczone = pd.concat([dodaj, polaczone], ignore_index=True)
        dodaj = pasza_tresciwa_df.loc[pasza_tresciwa_df['nazwa'] == i]
        polaczone = pd.concat([dodaj, polaczone], ignore_index=True)
    polaczone['ilosc'] = 0

    # A loop that estimates which nutrient has the highest demand at the moment, add 5% of the best feed and so on.
    while not ((ileJPM > 0.9 * zapotrzebowanie) & (ileJPM < 1.5 * zapotrzebowanie)
               & (ileBialka > 0.9 * bialko2) & (ileBialka < 1.5 * bialko2)
               & (ileWlokna > 0.2 * SM)
               & (ileTluszczu > 0.02 * SM) & (ileTluszczu < 0.1 * SM)
               & (ileSM > 0.9 * SM) & (ileSM < 1.5 * SM)
               & (ileNDF > 0.28 * ileWlokna)
               & (ileBTJN > 0.9 * ileBTJE)
               & (ileBTJE > 0.9 * ileBTJN)):

        # We start at 0, and i later have to divide by ileBTJN and ileBTJE, so this if is preventing an error.
        if ileBTJE or ileBTJN == 0:
            # Here is the part that estimates which feed has the highest demand
            D_bez_BTJ['potrzeba_JPM'] = ileJPM / zapotrzebowanie
            D_bez_BTJ['potrzeba_bialka'] = ileBialka / bialko2
            D_bez_BTJ['potrzeba_wlokna'] = ileWlokna / (0.2 * SM)
            D_bez_BTJ['potrzeba_tluszczu'] = ileTluszczu / (0.03 * SM)
            D_bez_BTJ['potrzeba_SM'] = ileSM / SM
            D_bez_BTJ['potrzeba_NDF'] = ileNDF / (0.33 * 0.2 * SM)
            najpotrzebniejsze_bez_BTJ = min(D_bez_BTJ, key=D_bez_BTJ.get)

            # Here i check which feed suits the demand best and i add 5% of it to our final feed dose.
            if najpotrzebniejsze_bez_BTJ == 'potrzeba_JPM':
                polaczone = polaczone.sort_values(by="JPM%", ascending=False)
                polaczone = polaczone.reset_index(drop=True)
                ileJPM += 0.05 * pd.to_numeric(polaczone.at[0, 'JPM%']) / 100   # Adding 5% of the nutrients from the most needed feed to the final result of nutritional values.
                ileBialka += 0.05 * pd.to_numeric(polaczone.at[0, 'BO(g/kg)'])
                ileWlokna += 0.05 * pd.to_numeric(polaczone.at[0, 'WS(g/kg)'])
                ileTluszczu += 0.05 * pd.to_numeric(polaczone.at[0, 'TS(g/kg)'])
                ileSM += 0.05 * pd.to_numeric(polaczone.at[0, 'SM%']) * 10
                ileNDF += 0.05 * pd.to_numeric(polaczone.at[0, 'NDF(g/kg)'])
                ileBTJE += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJE(g/kg)'])
                ileBTJN += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJN(g/kg)'])
                polaczone.at[0, 'ilosc'] += 0.05    # Adding weight of the most needed feed to the final feed mix.

            elif najpotrzebniejsze_bez_BTJ == 'potrzeba_bialka':
                polaczone = polaczone.sort_values(by="BO(g/kg)", ascending=False)
                polaczone = polaczone.reset_index(drop=True)
                ileJPM += 0.05 * pd.to_numeric(polaczone.at[0, 'JPM%']) / 100
                ileBialka += 0.05 * pd.to_numeric(polaczone.at[0, 'BO(g/kg)'])
                ileWlokna += 0.05 * pd.to_numeric(polaczone.at[0, 'WS(g/kg)'])
                ileTluszczu += 0.05 * pd.to_numeric(polaczone.at[0, 'TS(g/kg)'])
                ileSM += 0.05 * pd.to_numeric(polaczone.at[0, 'SM%']) * 10
                ileNDF += 0.05 * pd.to_numeric(polaczone.at[0, 'NDF(g/kg)'])
                ileBTJE += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJE(g/kg)'])
                ileBTJN += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJN(g/kg)'])
                polaczone.at[0, 'ilosc'] += 0.05

            elif najpotrzebniejsze_bez_BTJ == 'potrzeba_wlokna':
                polaczone = polaczone.reset_index(drop=True)
                polaczone = polaczone.sort_values(by="WS(g/kg)", ascending=False)
                ileJPM += 0.05 * pd.to_numeric(polaczone.at[0, 'JPM%']) / 100
                ileBialka += 0.05 * pd.to_numeric(polaczone.at[0, 'BO(g/kg)'])
                ileWlokna += 0.05 * pd.to_numeric(polaczone.at[0, 'WS(g/kg)'])
                ileTluszczu += 0.05 * pd.to_numeric(polaczone.at[0, 'TS(g/kg)'])
                ileSM += 0.05 * pd.to_numeric(polaczone.at[0, 'SM%']) * 10
                ileNDF += 0.05 * pd.to_numeric(polaczone.at[0, 'NDF(g/kg)'])
                ileBTJE += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJE(g/kg)'])
                ileBTJN += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJN(g/kg)'])
                polaczone.at[0, 'ilosc'] += 0.05

            elif najpotrzebniejsze_bez_BTJ == 'potrzeba_tluszczu':
                polaczone = polaczone.sort_values(by="TS(g/kg)", ascending=False)
                polaczone = polaczone.reset_index(drop=True)
                ileJPM += 0.05 * pd.to_numeric(polaczone.at[0, 'JPM%']) / 100
                ileBialka += 0.05 * pd.to_numeric(polaczone.at[0, 'BO(g/kg)'])
                ileWlokna += 0.05 * pd.to_numeric(polaczone.at[0, 'WS(g/kg)'])
                ileTluszczu += 0.05 * pd.to_numeric(polaczone.at[0, 'TS(g/kg)'])
                ileSM += 0.05 * pd.to_numeric(polaczone.at[0, 'SM%']) * 10
                ileNDF += 0.05 * pd.to_numeric(polaczone.at[0, 'NDF(g/kg)'])
                ileBTJE += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJE(g/kg)'])
                ileBTJN += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJN(g/kg)'])
                polaczone.at[0, 'ilosc'] += 0.05

            elif najpotrzebniejsze_bez_BTJ == 'potrzeba_SM':
                polaczone = polaczone.sort_values(by="SM%", ascending=False)
                polaczone = polaczone.reset_index(drop=True)
                ileJPM += 0.05 * pd.to_numeric(polaczone.at[0, 'JPM%']) / 100
                ileBialka += 0.05 * pd.to_numeric(polaczone.at[0, 'BO(g/kg)'])
                ileWlokna += 0.05 * pd.to_numeric(polaczone.at[0, 'WS(g/kg)'])
                ileTluszczu += 0.05 * pd.to_numeric(polaczone.at[0, 'TS(g/kg)'])
                ileSM += 0.05 * pd.to_numeric(polaczone.at[0, 'SM%']) * 10
                ileNDF += 0.05 * pd.to_numeric(polaczone.at[0, 'NDF(g/kg)'])
                ileBTJE += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJE(g/kg)'])
                ileBTJN += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJN(g/kg)'])
                polaczone.at[0, 'ilosc'] += 0.05

            elif najpotrzebniejsze_bez_BTJ == 'potrzeba_NDF':
                polaczone = polaczone.sort_values(by="NDF(g/kg)", ascending=False)
                polaczone = polaczone.reset_index(drop=True)
                ileJPM += 0.05 * pd.to_numeric(polaczone.at[0, 'JPM%']) / 100
                ileBialka += 0.05 * pd.to_numeric(polaczone.at[0, 'BO(g/kg)'])
                ileWlokna += 0.05 * pd.to_numeric(polaczone.at[0, 'WS(g/kg)'])
                ileTluszczu += 0.05 * pd.to_numeric(polaczone.at[0, 'TS(g/kg)'])
                ileSM += 0.05 * pd.to_numeric(polaczone.at[0, 'SM%']) * 10
                ileNDF += 0.05 * pd.to_numeric(polaczone.at[0, 'NDF(g/kg)'])
                ileBTJE += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJE(g/kg)'])
                ileBTJN += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJN(g/kg)'])
                polaczone.at[0, 'ilosc'] += 0.05

        else:
            D_z_BTJ['potrzeba_JPM'] = ileJPM / zapotrzebowanie
            D_z_BTJ['potrzeba_bialka'] = ileBialka / bialko2
            D_z_BTJ['potrzeba_wlokna'] = ileWlokna / (0.2 * SM)
            D_z_BTJ['potrzeba_tluszczu'] = ileTluszczu / (0.03 * SM)
            D_z_BTJ['potrzeba_SM'] = ileSM / SM
            D_z_BTJ['potrzeba_NDF'] = ileNDF / (0.33 * 0.2 * SM)
            D_z_BTJ['potrzeba_BTJN'] = ileBTJN / ileBTJE
            D_z_BTJ['potrzeba_BTJE'] = ileBTJE / ileBTJN
            najpotrzebniejsze_z_BTJ = min(D_z_BTJ.items(), key=lambda x: x[1])

            if najpotrzebniejsze_z_BTJ == 'potrzeba_JPM':
                polaczone = polaczone.sort_values(by="JPM%", ascending=False)
                polaczone = polaczone.reset_index(drop=True)
                ileJPM += 0.05 * pd.to_numeric(polaczone.at[0, 'JPM%']) / 100
                ileBialka += 0.05 * pd.to_numeric(polaczone.at[0, 'BO(g/kg)'])
                ileWlokna += 0.05 * pd.to_numeric(polaczone.at[0, 'WS(g/kg)'])
                ileTluszczu += 0.05 * pd.to_numeric(polaczone.at[0, 'TS(g/kg)'])
                ileSM += 0.05 * pd.to_numeric(polaczone.at[0, 'SM%']) * 10
                ileNDF += 0.05 * pd.to_numeric(polaczone.at[0, 'NDF(g/kg)'])
                ileBTJE += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJE(g/kg)'])
                ileBTJN += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJN(g/kg)'])
                polaczone.at[0, 'ilosc'] += 0.05

            elif najpotrzebniejsze_z_BTJ == 'potrzeba_bialka':
                polaczone = polaczone.sort_values(by="BO(g/kg)", ascending=False)
                polaczone = polaczone.reset_index(drop=True)
                ileJPM += 0.05 * pd.to_numeric(polaczone.at[0, 'JPM%']) / 100
                ileBialka += 0.05 * pd.to_numeric(polaczone.at[0, 'BO(g/kg)'])
                ileWlokna += 0.05 * pd.to_numeric(polaczone.at[0, 'WS(g/kg)'])
                ileTluszczu += 0.05 * pd.to_numeric(polaczone.at[0, 'TS(g/kg)'])
                ileSM += 0.05 * pd.to_numeric(polaczone.at[0, 'SM%']) * 10
                ileNDF += 0.05 * pd.to_numeric(polaczone.at[0, 'NDF(g/kg)'])
                ileBTJE += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJE(g/kg)'])
                ileBTJN += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJN(g/kg)'])
                polaczone.at[0, 'ilosc'] += 0.05

            elif najpotrzebniejsze_z_BTJ == 'potrzeba_wlokna':
                polaczone = polaczone.sort_values(by="WS(g/kg)", ascending=False)
                polaczone = polaczone.reset_index(drop=True)
                ileJPM += 0.05 * pd.to_numeric(polaczone.at[0, 'JPM%']) / 100
                ileBialka += 0.05 * pd.to_numeric(polaczone.at[0, 'BO(g/kg)'])
                ileWlokna += 0.05 * pd.to_numeric(polaczone.at[0, 'WS(g/kg)'])
                ileTluszczu += 0.05 * pd.to_numeric(polaczone.at[0, 'TS(g/kg)'])
                ileSM += 0.05 * pd.to_numeric(polaczone.at[0, 'SM%']) * 10
                ileNDF += 0.05 * pd.to_numeric(polaczone.at[0, 'NDF(g/kg)'])
                ileBTJE += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJE(g/kg)'])
                ileBTJN += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJN(g/kg)'])
                polaczone.at[0, 'ilosc'] += 0.05

            elif najpotrzebniejsze_z_BTJ == 'potrzeba_tluszczu':
                polaczone = polaczone.sort_values(by="TS(g/kg)", ascending=False)
                polaczone = polaczone.reset_index(drop=True)
                ileJPM += 0.05 * pd.to_numeric(polaczone.at[0, 'JPM%']) / 100
                ileBialka += 0.05 * pd.to_numeric(polaczone.at[0, 'BO(g/kg)'])
                ileWlokna += 0.05 * pd.to_numeric(polaczone.at[0, 'WS(g/kg)'])
                ileTluszczu += 0.05 * pd.to_numeric(polaczone.at[0, 'TS(g/kg)'])
                ileSM += 0.05 * pd.to_numeric(polaczone.at[0, 'SM%']) * 10
                ileNDF += 0.05 * pd.to_numeric(polaczone.at[0, 'NDF(g/kg)'])
                ileBTJE += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJE(g/kg)'])
                ileBTJN += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJN(g/kg)'])
                polaczone.at[0, 'ilosc'] += 0.05

            elif najpotrzebniejsze_z_BTJ == 'potrzeba_SM':
                polaczone = polaczone.sort_values(by="SM%", ascending=False)
                polaczone = polaczone.reset_index(drop=True)
                ileJPM += 0.05 * pd.to_numeric(polaczone.at[0, 'JPM%']) / 100
                ileBialka += 0.05 * pd.to_numeric(polaczone.at[0, 'BO(g/kg)'])
                ileWlokna += 0.05 * pd.to_numeric(polaczone.at[0, 'WS(g/kg)'])
                ileTluszczu += 0.05 * pd.to_numeric(polaczone.at[0, 'TS(g/kg)'])
                ileSM += 0.05 * pd.to_numeric(polaczone.at[0, 'SM%']) * 10
                ileNDF += 0.05 * pd.to_numeric(polaczone.at[0, 'NDF(g/kg)'])
                ileBTJE += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJE(g/kg)'])
                ileBTJN += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJN(g/kg)'])
                polaczone.at[0, 'ilosc'] += 0.05

            elif najpotrzebniejsze_z_BTJ == 'potrzeba_NDF':
                polaczone = polaczone.sort_values(by="NDF(g/kg)", ascending=False)
                polaczone = polaczone.reset_index(drop=True)
                ileJPM += 0.05 * pd.to_numeric(polaczone.at[0, 'JPM%']) / 100
                ileBialka += 0.05 * pd.to_numeric(polaczone.at[0, 'BO(g/kg)'])
                ileWlokna += 0.05 * pd.to_numeric(polaczone.at[0, 'WS(g/kg)'])
                ileTluszczu += 0.05 * pd.to_numeric(polaczone.at[0, 'TS(g/kg)'])
                ileSM += 0.05 * pd.to_numeric(polaczone.at[0, 'SM%']) * 10
                ileNDF += 0.05 * pd.to_numeric(polaczone.at[0, 'NDF(g/kg)'])
                ileBTJE += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJE(g/kg)'])
                ileBTJN += 0.05 * pd.to_numeric(polaczone.at[0, 'BTJN(g/kg)'])
                polaczone.at[0, 'ilosc'] += 0.05

        # Here i prevent infinite running in case the user chose feeds that lack some nutrients.
        if ((ileJPM > 2 * zapotrzebowanie)
                | (ileBialka > 2 * bialko2)
                | (ileWlokna > 1 * SM)
                | (ileTluszczu > 0.2 * SM)
                | (ileSM > 2 * SM)
                | (ileNDF > 1 * SM)):
            break

    # Here i inform the user if the doses have been properly balanced.
    if ((ileJPM > 1.5 * zapotrzebowanie)
            | (ileBialka > 1.5 * bialko2)
            | (ileWlokna > 0.6 * SM)
            | (ileTluszczu > 0.07 * SM)
            | (ileSM > 1.5 * SM)
            | (ileNDF > 0.6 * SM)
            | (ileBTJN > 2 * ileBTJE)
            | (ileBTJE > 2 * ileBTJN)):
        if ileJPM > 1.5 * zapotrzebowanie:
            l = tk.Label(window_dawki, text="Za dużo energii.", fg='red')
            l.pack()
        if ileBialka > 1.5 * bialko2:
            l = tk.Label(window_dawki, text="Za dużo białka.", fg='red')
            l.pack()
        if ileWlokna > 0.6 * SM:
            l = tk.Label(window_dawki, text="Za dużo włókna.", fg='red')
            l.pack()
        if ileTluszczu > 0.07 * SM:
            l = tk.Label(window_dawki, text="Za dużo tłuszczu.", fg='red')
            l.pack()
        if ileSM > 1.5 * SM:
            l = tk.Label(window_dawki, text="Za dużo suchej masy.", fg='red')
            l.pack()
        if ileNDF > 0.6 * SM:
            l = tk.Label(window_dawki, text="Za dużo NDF.", fg='red')
            l.pack()
        if ileBTJN > 2 * ileBTJE:
            l = tk.Label(window_dawki, text="Za dużo BTJN.", fg='red')
            l.pack()
        if ileBTJE > 2 * ileBTJN:
            l = tk.Label(window_dawki, text="Za dużo BTJE.", fg='red')
            l.pack()
    else:
        l = tk.Label(window_dawki, text="Dawka dobrze zbilansowana.", fg='red')
        l.pack()

    # Presentation of the final results
    polaczone = polaczone.sort_values(by="ilosc", ascending=False)
    wyniki = polaczone[["nazwa", "ilosc"]]
    wyniki = wyniki.to_string(index=False, header=False)
    l = tk.Label(window_dawki, text="")
    l.pack()
    labelframe_wyniki = LabelFrame(window_dawki, text="Ilość pasz w kilogramach:")
    labelframe_wyniki.pack()
    l = tk.Label(labelframe_wyniki, text=wyniki)
    l.pack(anchor=W)
    l = tk.Label(window_dawki, text="")
    l.pack()
    labelframe_sklad = LabelFrame(window_dawki, text="Składniki pokarmowe w dawce:")
    labelframe_sklad.pack()
    l = tk.Label(labelframe_sklad, text=("Energia (JPM): " + str("%.2f" % ileJPM)
                                         + "\nBiałko (kg): " + str("%.2f" % (ileBialka / 1000))
                                         + "\nWlokno (kg): " + str("%.2f" % (ileWlokna / 1000))
                                         + "\nTłuszcz (kg): " + str("%.2f" % (ileTluszczu / 1000))
                                         + "\nSucha masa (kg): " + str("%.2f" % (ileSM / 1000))
                                         + "\nNDF (kg): " + str("%.2f" % (ileNDF / 1000))
                                         + "\nBTJN (kg): " + str("%.2f" % (ileBTJN / 1000))
                                         + "\nBTJE (kg): " + str("%.2f" % (ileBTJE / 1000))))
    l.pack()


l = Label(root, width=25, text='Wylicz zapotrzebowanie:', borderwidth=2, relief='ridge', anchor='w', bg='#A78755')
l.grid(row=0, column=0, sticky='W')
b = tk.Button(root, text="Wprowadź dane", command=popup_window_zap, width=50)
b.grid(row=0, column=2, columnspan=4, sticky=W)
l = Label(root, text=" ")
l.grid(row=2, column=0)
l = Label(root, text=" ")
l.grid(row=3, column=0)
l = Label(root, text=" ")
l.grid(row=4, column=0)
l = Label(root, text="Wybierz pasze objętościowe:", borderwidth=2, relief='ridge', anchor='w', bg='#A78755')
l.grid(row=5, column=0, sticky='W')
l = Label(root, width=25, text='Nazwa', relief='ridge', bg='#EBE0B9')
l.grid(row=6, column=0)
l = Label(root, width=10, text='SM (%)', relief='ridge', bg='#EBE0B9')
l.grid(row=6, column=1)
l = Label(root, width=10, text='BO (g/kg)', relief='ridge', bg='#EBE0B9')
l.grid(row=6, column=2)
l = Label(root, width=10, text='TS (g/kg)', relief='ridge', bg='#EBE0B9')
l.grid(row=6, column=3)
l = Label(root, width=10, text='WS (g/kg)', relief='ridge', bg='#EBE0B9')
l.grid(row=6, column=4)
l = Label(root, width=10, text='NDF (g/kg)', relief='ridge', bg='#EBE0B9')
l.grid(row=6, column=5)
l = Label(root, width=10, text='BTJN (g/kg)', relief='ridge', bg='#EBE0B9')
l.grid(row=6, column=6)
l = Label(root, width=10, text='BTJE (g/kg)', relief='ridge', bg='#EBE0B9')
l.grid(row=6, column=7)
l = Label(root, width=10, text='JPM (%)', relief='ridge', bg='#EBE0B9')
l.grid(row=6, column=8)

# Add a frame for a canvas.
frame_canvas_obj = tk.Frame(root, relief='ridge', borderwidth=2)
frame_canvas_obj.grid(row=7, column=0, sticky='nw', columnspan=14)
frame_canvas_obj.grid_rowconfigure(0, weight=1)
frame_canvas_obj.grid_columnconfigure(0, weight=1)

# Set grid_propagate to False to allow resizing later.
frame_canvas_obj.grid_propagate(False)

# Add a canvas in that frame.
canvas_obj = tk.Canvas(frame_canvas_obj)
canvas_obj.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas.
obj_sb = tk.Scrollbar(frame_canvas_obj, orient="vertical", command=canvas_obj.yview)
obj_sb.grid(row=0, column=1, sticky='ns')
canvas_obj.configure(yscrollcommand=obj_sb.set)

# Create a frame to contain the table.
frame_table_obj = tk.Frame(canvas_obj, highlightbackground="black", highlightthickness=1)
canvas_obj.create_window((0, 0), window=frame_table_obj, anchor='nw')

# A table which contains the feed data and creating a corresponding button for each feed
with open("pasza_objetosciowa.csv", newline="") as file:
    global button, pasza_objetosciowa
    reader_o = csv.reader(file)
    counter_o = 0
    i = 0
    for pasza_objetosciowa in reader_o:
        if counter_o != 0:
            for j in range(len(pasza_objetosciowa)):
                if j == 0:
                    l = Label(frame_table_obj, width=27, text=pasza_objetosciowa[j])
                    l.grid(row=i, column=j)

                    button = Button(frame_table_obj, text="Wybierz",
                                    command=lambda j=j, pasza_objetosciowa=pasza_objetosciowa: wybierzo(j,
                                                                                                        pasza_objetosciowa))
                    button.grid(row=i, column=9)
                else:
                    l = Label(frame_table_obj, width=12, text=pasza_objetosciowa[j])
                    l.grid(row=i, column=j)
            i += 1
        counter_o += 1

# Update table frames idle tasks to let tkinter calculate buttons sizes.
frame_table_obj.update_idletasks()

# Resize the canvas frame to show exactly how much options i want.
frame_canvas_obj.config(width=990, height=155)

# Set the canvas scrolling region.
canvas_obj.config(scrollregion=canvas_obj.bbox("all"))

l = Label(root, text=" ")
l.grid(row=9, column=0)
l = Label(root, text=" ")
l.grid(row=10, column=0)
l = Label(root, text="Wybierz pasze treściwe:", borderwidth=2, relief='ridge', anchor='w', bg='#A78755')
l.grid(row=11, column=0, sticky='W')
l = Label(root, width=25, text='Nazwa', relief='ridge', bg='#EBE0B9')
l.grid(row=12, column=0)
l = Label(root, width=10, text='SM (%)', relief='ridge', bg='#EBE0B9')
l.grid(row=12, column=1)
l = Label(root, width=10, text='BO (g/kg)', relief='ridge', bg='#EBE0B9')
l.grid(row=12, column=2)
l = Label(root, width=10, text='TS (g/kg)', relief='ridge', bg='#EBE0B9')
l.grid(row=12, column=3)
l = Label(root, width=10, text='WS (g/kg)', relief='ridge', bg='#EBE0B9')
l.grid(row=12, column=4)
l = Label(root, width=10, text='NDF (g/kg)', relief='ridge', bg='#EBE0B9')
l.grid(row=12, column=5)
l = Label(root, width=10, text='BTJN (g/kg)', relief='ridge', bg='#EBE0B9')
l.grid(row=12, column=6)
l = Label(root, width=10, text='BTJE (g/kg)', relief='ridge', bg='#EBE0B9')
l.grid(row=12, column=7)
l = Label(root, width=10, text='JPM (%)', relief='ridge', bg='#EBE0B9')
l.grid(row=12, column=8)

# Add a frame for a canvas.
frame_canvas_tr = tk.Frame(root, relief='ridge', borderwidth=2)
frame_canvas_tr.grid(row=13, column=0, sticky='nw', columnspan=14)
frame_canvas_tr.grid_rowconfigure(0, weight=1)
frame_canvas_tr.grid_columnconfigure(0, weight=1)

# Set grid_propagate to False to allow manual resizing.
frame_canvas_tr.grid_propagate(False)

# Add a canvas in that frame.
canvas_tr = tk.Canvas(frame_canvas_tr)
canvas_tr.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas.
tr_sb = tk.Scrollbar(frame_canvas_tr, orient="vertical", command=canvas_tr.yview)
tr_sb.grid(row=0, column=1, sticky='ns')
canvas_tr.configure(yscrollcommand=tr_sb.set)

# Create a frame to contain the table.
frame_table_tr = tk.Frame(canvas_tr, highlightbackground="black", highlightthickness=1)
canvas_tr.create_window((0, 0), window=frame_table_tr, anchor='nw')

# A table which contains the feed data and creating a corresponding button for each feed. This time for the other type of feeds.
with open("pasza_tresciwa.csv", newline="") as file:
    reader_t = csv.reader(file)
    counter_t = 0
    i = 0
    for pasza_tresciwa in reader_t:
        if counter_t != 0:
            for j in range(len(pasza_tresciwa)):
                if j == 0:
                    l = Label(frame_table_tr, width=27, text=pasza_tresciwa[j])
                    l.grid(row=i, column=j)

                    b = Button(frame_table_tr, text="Wybierz",
                               command=lambda j=j, pasza_tresciwa=pasza_tresciwa: wybierzt(j, pasza_tresciwa))
                    b.grid(row=i, column=9)
                else:
                    l = Label(frame_table_tr, width=12, text=pasza_tresciwa[j])
                    l.grid(row=i, column=j)
            i += 1
        counter_t += 1

# Update table frames idle tasks to let tkinter calculate buttons sizes.
frame_table_tr.update_idletasks()

# Resize the canvas frame to show exactly how much options i want.
frame_canvas_tr.config(width=990, height=155)

# Set the canvas scrolling region.
canvas_tr.config(scrollregion=canvas_tr.bbox("all"))

l = Label(root, text=" ")
l.grid(row=18, column=0)
l = Label(root, text=" ")
l.grid(row=19, column=0)
l = Label(root, width=25, text="Wybrane pasze", borderwidth=2, relief='ridge', anchor='w', bg='#A78755')
l.grid(row=20, column=0, sticky='W')
b = Button(root, text="OBLICZ DAWKĘ PASZOWĄ", command=popup_window_dawki, width=50)
b.grid(row=20, column=5, columnspan=6, sticky=W)

root.mainloop()
