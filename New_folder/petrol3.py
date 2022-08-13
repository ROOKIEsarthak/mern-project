import pickle
import random
import string
import math
import time

developerlogin = 0
adminlogin = 0
userlogin = 0
dp = dd = dg = 1
bp = bd = bg = 0
lp = []
ld = []

lg = []

a = time.asctime()
bz = a[:-13] + a[20:]
print(bz)
call1 = cald1 = 1
z1: str
z = c = 0
fdays1 = 0
fdays2 = []
fdayc = []
n = 0
z21 = 0
z1 = a[:-13] + a[20:]
k = []
kp = []
k1 = []
kd = []
k2 = []
kg = []
# These are for total amount of fuel sold to the customers #
# These are availab+le for only developer and owner #
sp = sd = sg = 0


class pump(object):
    tpc = f = az1 = az2 = tpc1 = s = 0

    # For no of vehicles in each fuel type "

    def totalday(self):

        import mysql.connector
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='PUMP',
                                           user='Sarthak',
                                           password='q1w2e3r4t5')
            cur = conn.cursor()
            print()
            cur.execute("SELECT SUM(total_coll) FROM COLLECTION")
            print()
            print()
            totalc1 = []
            for j in cur:
                tc1 = float(j[0])
                totalc1.append(tc1)
            print(" Total Collection till today is Rs", totalc1[0])

        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()
                print()

    def private(self):

        import mysql.connector
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='PUMP',
                                           user='Sarthak',
                                           password='q1w2e3r4t5')
            cur = conn.cursor()
            print()
            print("Enter 1 for vehicle types ")
            print("Enter 2 for vehicle no ")
            print("Enter 3 for Date")
            print("Enter 4 for Time")
            print("Enter 5 for Amount")
            print("Enter 6 for Quantity")
            print("\n")
            print("\n")
            gv = input("Enter your choice")
            print()
            if (gv == '1'):
                cur.execute("select distinct Fuel_type from collection;")
                print("Vehicles types in the list")
                print("\n")
                for i in cur:
                    print(i)
                gv1 = input("Enter the fuel type")
                cur.execute(
                    "select Vehicle_No,Fuel_type,total_coll,fuel_qty,date,time from collection where Fuel_type" + "=" + str(
                        gv1));
                print("\n")
                print("\n")
                print(
                    " Vehicle_no  |  Total Collection  |  Fuel Quantity  |          Date          |         Time       |       Fuel Type ")
                print(
                    " ----------     ----------------     -------------        -------------             ----------           -----------")
                for i3 in cur:
                    print("    ", str(i3[0]), "  ", "  ", float(i3[2]), "  ", "                ",
                          round(float((i3[3])), 3), "  ", "      ",
                          str(i3[4]), "       ", "   ", str(i3[5]), "          ", "   ", str(i3[1]))
                print("\n")

            if (gv == '2'):
                cur.execute("select Vehicle_no from collection;")
                print("Vehicles No's in the list")
                print("\n")
                for i in cur:
                    print(i)
                gv2 = input("Enter the vehicle no")
                cur.execute(
                    "select Vehicle_No,Fuel_type,total_coll,fuel_qty,date,time from collection where Vehicle_no" + "=" + str(
                        gv2));
                print("\n")
                print(
                    " Vehicle_no  |  Total Collection  |  Fuel Quantity  |          Date          |         Time       |       Fuel Type ")
                print(
                    " ----------     ----------------     -------------        -------------             ----------           -----------")
                for i3 in cur:
                    print("    ", str(i3[0]), "  ", "  ", float(i3[2]), "  ", "                ",
                          round(float((i3[3])), 3), "  ", "      ",
                          str(i3[4]), "       ", "   ", str(i3[5]), "          ", "   ", str(i3[1]))
                print("\n")
                print("\n")

            if (gv == "3"):
                cur.execute("Select distinct date from collection")
                print("\n")
                for i1 in cur:
                    print(i1)
                print("\n")
                ch3 = input("Enter the date from above list")
                cur.execute(
                    "select Vehicle_no,total_coll,Fuel_qty,date,time,Fuel_type from collection where date " + "=" + str(
                        ch3))
                print("\n")
                print(
                    " Vehicle_no  |  Total Collection  |  Fuel Quantity  |          Date          |         Time       |       Fuel Type ")
                print(
                    " ----------     ----------------     -------------        -------------             ----------           -----------")
                for i3 in cur:
                    print("    ", str(i3[0]), "  ", "  ", float(i3[1]), "  ", "                ",
                          round(float((i3[2])), 3), "  ", "      ",
                          str(i3[3]), "       ", "   ", str(i3[4]), "          ", "   ", str(i3[5]))
                print("\n")

            if (gv == "4"):
                cur.execute("Select time,date from collection")
                print(cur)
                for i1 in cur:
                    print(i1)
                ch3 = input("Enter the time from above list")
                cur.execute(
                    "select Vehicle_no,total_coll,Fuel_qty,date,time,Fuel_type,Station_id from collection where time " + "=" + str(
                        ch3))
                print(
                    " Vehicle_no  |  Total Collection  |  Fuel Quantity  |          Date          |         Time       |       Fuel Type      |      Station Id      ")
                print(
                    " ----------     ----------------     -------------        -------------             ----------           -----------           -------------     ")
                for i3 in cur:
                    print("    ", str(i3[0]), "  ", "  ", float(i3[1]), "  ", "                ",
                          round(float((i3[2])), 3), "  ", "      ",
                          str(i3[3]), "       ", "   ", str(i3[4]), "          ", "   ", str(i3[5]), "          ", "   ", str(i3[6]))
                print("\n")

            if (gv == "5"):
                cur.execute("Select total_coll from collection")
                for i1 in cur:
                    print(i1)
                ch3 = input("Enter the Amount from above list")
                cur.execute(
                    "select Vehicle_no,total_coll,Fuel_qty,date,time,Fuel_type from collection where total_coll " + "=" + str(
                        ch3))
                print("\n")
                print(
                    " Vehicle_no  |  Total Collection  |  Fuel Quantity  |          Date          |         Time       |       Fuel Type ")
                print(
                    " ----------     ----------------     -------------        -------------             ----------           -----------")
                for i3 in cur:
                    print("    ", str(i3[0]), "  ", "  ", float(i3[1]), "  ", "                ",
                          round(float((i3[2])), 3), "  ", "      ",
                          str(i3[3]), "       ", "   ", str(i3[4]), "          ", "   ", str(i3[5]))
                print("\n")

            if (gv == "6"):
                cur.execute("Select Fuel_qty from collection")
                for i1 in cur:
                    print(i1)
                ch3 = input("Enter the Fuel Quantity from above list")
                cur.execute(
                    "select Vehicle_no,total_coll,Fuel_qty,date,time,Fuel_type from collection where Fuel_qty " + "=" + str(
                        ch3))
                print(
                    " Vehicle_no  |  Total Collection  |  Fuel Quantity  |          Date          |         Time       |       Fuel Type ")
                print(
                    " ----------     ----------------     -------------        -------------             ----------           -----------")
                for i3 in cur:
                    print("    ", str(i3[0]), "  ", "  ", float(i3[1]), "  ", "                ",
                          round(float((i3[2])), 3), "  ", "      ",
                          str(i3[3]), "       ", "   ", str(i3[4]), "          ", "   ", str(i3[5]))
                print("\n")

        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()
                print()

    def petrol(self):

        self.ch = 0
        self.l = []
        print(" Select 1 for purchase in litres - : ")
        print(" Select 2 for purchase in amount - : ")

        self.ch = int(input(" Entre choice - :"))
        if self.ch == 1:
            self.petrol = 1000
            self.decamount = 71.37
            self.z = 0
            self.pq = int(input(" Enter the quantity of petrol u want - : "))
            self.pca = self.decamount * self.pq
            self.l.append(self.pca)
            self.vno1 = input(" Enter the vehicle number - : ")
            self.petrol1 = " Fuel Taken  =" + "  " + str(self.pq) + "Litres" + "  \n" + " Amount is  = " + str(
                self.pca) + "  \n" + " Vehicle no  =" + str(self.vno1) + "  \n" + " Time is " + time.asctime()
            time2 = time.asctime()
            t = time2[11:19]
            d = time2[:-13] + time2[20:]
            y = time2[20:25]
            coll = self.pca

            import mysql.connector
            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='PUMP',
                                               user='Sarthak',
                                               password='q1w2e3r4t5')
                ftype = "Petrol"
                s_id = "12345"
                cur = conn.cursor()
                ins = (
                    "INSERT INTO PETROL (Vehicle_No ,Pamt ,Pqty ,Time ,Date ,Collection ,Year ,station_id) VALUES (%(self.vno1)s ,%(self.pca)s ,%(self.pq)s ,%(t)s ,%(d)s,%(coll)s ,%(y)s ,%(s_id)s)")
                data = {
                    'self.vno1': self.vno1,
                    'self.pca': self.pca,
                    'self.pq': self.pq,
                    't': t,
                    'd': d,
                    'coll': coll,
                    'y': y,
                    's_id': s_id,
                }

                cur.execute(ins, data)
                ins1 = (
                    "INSERT INTO COLLECTION (total_coll ,Time ,date ,Fuel_type ,Fuel_qty ,station_id ,Vehicle_no) VALUES (%(coll)s ,%(t)s ,%(d)s ,%(ftype)s ,%(self.pq)s ,%(s_id)s ,%(self.vno1)s)")
                data1 = {
                    'coll': coll,
                    't': t,
                    'd': d,
                    'ftype': ftype,
                    'self.pq': self.pq,
                    's_id': s_id,
                    'self.vno1': self.vno1,
                }
                cur.execute(ins1, data1)
                conn.commit()

            except mysql.connector.Error as error:
                print("Failed to create table in MySQL: {}".format(error))
            finally:
                if (conn.is_connected()):
                    cur.close()
                    conn.close()
                    print("MySQL connection is closed")

            print("=" * 50)
            print('  ' * 18, '   Bill ', '  ' * 10)
            print("=" * 50)
            print('  ' * 13, 'Hindustan Petroleum', '  ' * 10)
            print("=" * 50)
            print(" You have been refilled ", self.pq, " litres of petrol  ")
            print(" You have recived ", (self.pq), "l of petrol of worth Rs", self.pca)

        if self.ch == 2:
            self.petrol = 1000
            self.decamount = 71.37
            self.z = 0
            self.p = float(input(" Enter the amount of which u want to buy petrol - : "))
            self.p1 = float(input(" Enter the amount given - : "))
            self.vno1 = input(" Enter the vehicle number - : ")

            if self.p1 >= self.p:
                self.n = self.p1 - self.p
                self.acfuel = (self.petrol * self.p) / self.decamount
            if self.p1 == self.p:
                self.acfuel = (self.petrol * self.p) / self.decamount
            if self.p1 < self.p:
                self.p = float(input(" Please enter the correct amount for refuelling - : "))
                self.p1 = float(input(" Enter the amount given - : "))
                if self.p1 >= self.p:
                    self.n = self.p1 - self.p
                    self.acfuel = (self.petrol * self.p) / self.decamount
                else:
                    print(" Jaao paise leke aao ")

            self.petrol1 = " Fuel taken  =" + "  " + str(
                self.acfuel / 1000) + "litres" + "\n" + " Amount is  = " + "  " + "Rs" + str(
                self.p) + "\n" + "Vehicle no  = " + str(self.vno1) + "\n" + "Time is " + time.asctime()
            self.l.append(self.p)
            q = round(self.acfuel / 1000, 3)
            coll = self.p
            time2 = time.asctime()
            t = time2[11:19]
            d = time2[:-13] + time2[20:]
            y = time2[20:25]

            ftype = "Petrol"
            s_id = "12345"
            import mysql.connector
            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='PUMP',
                                               user='Sarthak',
                                               password='q1w2e3r4t5')
                cur = conn.cursor()
                ins = (
                    "INSERT INTO PETROL (Vehicle_No ,Pamt ,Pqty ,Time ,Date ,Collection ,Year ,Station_id) VALUES (%(self.vno1)s ,%(self.p)s ,%(q)s ,%(t)s ,%(d)s, %(coll)s ,%(y)s ,%(s_id)s)")
                data = {
                    'self.vno1': self.vno1,
                    'self.p': self.p,
                    'q': q,
                    't': t,
                    'd': d,
                    'coll': coll,
                    'y': y,
                    's_id': '12345',
                }
                cur.execute(ins, data)
                ins1 = (
                    "INSERT INTO COLLECTION (total_coll ,Time ,date ,Fuel_type ,Fuel_qty ,station_id ,Vehicle_no) VALUES (%(coll)s ,%(t)s ,%(d)s ,%(ftype)s ,%(q)s ,%(s_id)s ,%(self.vno1)s)")
                data1 = {
                    'coll': coll,
                    't': t,
                    'd': d,
                    'ftype': ftype,
                    'q': q,
                    's_id': s_id,
                    'self.vno1': self.vno1,
                }
                cur.execute(ins1, data1)
                conn.commit()

            except mysql.connector.Error as error:
                print("Failed to create table in MySQL: {}".format(error))
            finally:
                if (conn.is_connected()):
                    cur.close()
                    conn.close()
                    print("MySQL connection is closed")

            print("=" * 50)
            print('  ' * 18, '   Bill ', '  ' * 10)
            print("=" * 50)
            print('  ' * 13, 'Hindustan Petroleum', '  ' * 10)
            print("=" * 50)
            print(" Amount returned is  ", self.n)
            print(" You have been refilled petrol of Rs", self.p)
            print(" You have recived ", round(self.acfuel / 1000, 3), "l of petrol ")
            print(" Your date of visit is    ", time.asctime())

    def deisel(self):

        self.ld = []
        self.decamount = 76.50
        self.deisel = 1000
        z11 = 0
        self.ch1 = 0
        print(" Select 1 for purchase in litres - : ")
        print(" Select 2 for purchase in amount - : ")
        self.ch1 = int(input("Entre choice"))
        if self.ch1 == 2:
            self.d = float(input(" Enter the amount of which u want to buy deisel - :"))
            self.d1 = float(input(" Enter the amount given - :"))
            self.vno2 = input(" Enter the vehicle number - : ")

            print(" Your date of visit is    ", time.asctime())

            if self.d1 >= self.d:
                self.n = self.d1 - self.d
                self.acqfuel = (self.deisel * self.d) / self.decamount
                print(" You have received ", (self.acqfuel / 1000), "litre of deisel ")
            if self.d1 == self.d:
                print(" You have been refilled deisel of Rs", self.d)
                self.acqfuel = (self.deisel * self.d) / self.decamount
                print(" You have recieved ", (self.acqfuel / 1000), "litre of deisel ")
            if self.d1 < self.d:
                self.d = float(input(" Please enter the correct amount for refuelling - : "))
                self.d1 = float(input(" Enter the amount given - :"))
                if self.d1 >= self.d:
                    self.n = self.d1 - self.d
                    self.acqfuel = (self.deisel * self.d) / self.decamount
                    print(" You have recived ", (self.acqfuel / 1000), "l of deisel ")
                    print(self.n, " amount returned ")
                    print(" You have been refilled deisel of Rs", self.d)
                else:
                    print(" Jaao paise leke aao ")
            self.deisel1 = " Fuel Taken  =" + "  " + str(
                self.acqfuel / 1000) + "litres" + "  \n" + " Amount is   =" + "Rs" + str(
                self.d) + "  \n" + " Vehicle no  =" + str(self.vno2) + "  \n" + " Time is " + time.asctime()
            self.ld.append(self.d)

            time3 = time.asctime()
            qd = round(self.acqfuel / 1000, 3)
            t = time3[11:19]
            d = time3[:-13] + time3[20:]
            y = time3[20:25]
            coll = self.d

            import mysql.connector
            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='PUMP',
                                               user='Sarthak',
                                               password='q1w2e3r4t5')
                cur = conn.cursor()
                ins = (
                    "INSERT INTO DIESEL (Vehicle_No ,Damt ,Dqty ,Time ,Date ,Collection ,Year ,Station_id) VALUES (%(self.vno2)s ,%(self.d)s ,%(qd)s ,%(t)s ,%(d)s, %(coll)s ,%(y)s ,%(s_id)s)")
                data = {
                    'self.vno2': self.vno2,
                    'self.d': self.d,
                    'qd': qd,
                    't': t,
                    'd': d,
                    'coll': coll,
                    'y': y,
                    's_id': '12345',
                }
                cur.execute(ins, data)
                ftype = "Diesel"
                s_id = "12345"
                ins1 = (
                    "INSERT INTO COLLECTION (total_coll ,Time ,date ,Fuel_type ,Fuel_qty ,station_id ,Vehicle_no) VALUES (%(coll)s ,%(t)s ,%(d)s ,%(ftype)s ,%(qd)s ,%(s_id)s ,%(self.vno2)s)")

                data1 = {
                    'coll': coll,
                    't': t,
                    'd': d,
                    'ftype': ftype,
                    'qd': qd,
                    's_id': s_id,
                    'self.vno2': self.vno2,
                }
                cur.execute(ins1, data1)
                conn.commit()

            except mysql.connector.Error as error:
                print("Failed to create table in MySQL: {}".format(error))
            finally:
                if (conn.is_connected()):
                    cur.close()
                    conn.close()
                    print("MySQL connection is closed")

            print("-" * 50)
            print('  ' * 18, '   Bill ', '  ' * 10)
            print("=" * 50)
            print('  ' * 13, 'Hindustan Petroleum', '  ' * 10)
            print("-" * 50)
            print(" Amount  returned is ", self.n)
            print(" You have been refilled deisel of Rs", self.d)
            print(" You have been refilled deisel of quantity", round(self.acqfuel / 1000, 2))
            print(" Your date of visit is - :  ", time.asctime())

        if self.ch1 == 1:
            self.dq = float(input(" Enter the quantity of which u want to buy deisel "))
            self.vno2 = input(" Enter the vehicle number ")

            self.dca = self.decamount * self.dq
            self.ld.append(self.dca)
            self.deisel1 = " Fuel taken  =" + "  " + str(self.dq) + "litres" + "  \n" + " Amount is   =" + "Rs" + str(
                self.dca) + "\n" + "Vehicle no  =" + str(self.vno2) + "  \n" + " Time is " + time.asctime()

            time3 = time.asctime()
            t = time3[11:19]
            d = time3[:-13] + time3[20:]
            y = time3[20:25]
            coll = self.dca

            import mysql.connector
            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='PUMP',
                                               user='Sarthak',
                                               password='q1w2e3r4t5')
                cur = conn.cursor()
                ins = (
                    "INSERT INTO DIESEL (Vehicle_No ,Damt ,Dqty ,Time ,Date ,Collection ,Year ,Station_id) VALUES (%(self.vno2)s ,%(self.dca)s ,%(self.dq)s ,%(t)s ,%(d)s, %(coll)s ,%(y)s ,%(s_id)s)")
                data = {
                    'self.vno2': self.vno2,
                    'self.dca': self.dca,
                    'self.dq': self.dq,
                    't': t,
                    'd': d,
                    'coll': coll,
                    'y': y,
                    's_id': '12345',
                }
                cur.execute(ins, data)
                ftype = "Diesel"
                s_id = "12345"
                ins1 = (
                    "INSERT INTO COLLECTION (total_coll ,Time ,date ,Fuel_type ,Fuel_qty ,station_id ,Vehicle_no) VALUES (%(coll)s ,%(t)s ,%(d)s ,%(ftype)s ,%(self.dq)s ,%(s_id)s ,%(self.vno2)s)")

                data1 = {
                    'coll': coll,
                    't': t,
                    'd': d,
                    'ftype': ftype,
                    'self.dq': self.dq,
                    's_id': s_id,
                    'self.vno2': self.vno2,
                }
                cur.execute(ins1, data1)
                conn.commit()

            except mysql.connector.Error as error:
                print("Failed to create table in MySQL: {}".format(error))
            finally:
                if (conn.is_connected()):
                    cur.close()
                    conn.close()
                    print("MySQL connection is closed")

            print("=" * 50)
            print('  ' * 18, '   Bill ', '  ' * 10)
            print("=" * 50)
            print('  ' * 13, 'Hindustan Petroleum', '  ' * 10)
            print("=" * 50)
            print(" You have recieved deisel of ", self.dq, "litres of worth Rs", self.dca)
            print("your date of visit is    ", time.asctime())

    def LPG(self):

        self.l2 = []
        self.decamount = 76.50
        self.gas = 1000
        print(" Select 1 for purchase in litres  - :")
        print(" Select 2 for purchase in amount - :")
        self.ch2 = int(input("Entre choice - :"))
        if self.ch2 == 2:
            self.l = float(input(" Enter the amount of which u want to buy L.P.G - :"))
            self.l1 = float(input(" Enter the amount given - :"))
            self.z2 = 0
            self.vno3 = input(" Enter the vehicle number - :")

            print("Your date of visit is - : ", time.asctime())

            if self.l1 > self.l:
                self.n = self.l1 - self.l
                self.acqdfuel = (self.gas * self.l) / self.decamount
            if self.l1 == self.l:
                self.acqdfuel = (self.gas * self.l) / self.decamount
            if self.l1 < self.l:
                self.l = float(input(" Please enter the correct amount for refuelling "))
                self.l1 = float(input(" Enter the amount given "))
                if self.l1 >= self.l:
                    self.n = self.l1 - self.l
                    self.acqdfuel = (self.gas * self.l) / self.decamount
                else:
                    print(" Jaao paise leke aao ")
            self.gas1 = " Fuel taken  =" + "  " + str(
                self.acqdfuel / 1000) + "litres" + " \n" + " Amount is   =" + "Rs" + str(
                self.l) + "  \n" + " Vehicle no  =" + str(self.vno3) + "  \n" + " Time is " + time.asctime()
            self.l2.append(self.l)

            time4 = time.asctime()
            qg = round(self.acqdfuel / 1000, 3)
            coll = self.l
            t = time4[11:19]
            d = time4[:-13] + time4[20:]
            y = time4[20:25]

            import mysql.connector
            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='PUMP',
                                               user='Sarthak',
                                               password='q1w2e3r4t5')
                cur = conn.cursor()
                ins = (
                    "INSERT INTO GAS (Vehicle_No ,Gamt ,Gqty ,Time ,Date ,Collection ,Year ,Station_id) VALUES (%(self.vno3)s ,%(self.l)s ,%(qg)s ,%(t)s ,%(d)s, %(coll)s ,%(y)s ,%(s_id)s)")
                data = {
                    'self.vno3': self.vno3,
                    'self.l': self.l,
                    'qg': qg,
                    't': t,
                    'd': d,
                    'coll': coll,
                    'y': y,
                    's_id': '12345',
                }
                cur.execute(ins, data)
                ftype = "LPG"
                s_id = "12345"
                ins1 = (
                    "INSERT INTO COLLECTION (total_coll ,Time ,date ,Fuel_type ,Fuel_qty ,station_id ,Vehicle_no) VALUES (%(coll)s ,%(t)s ,%(d)s ,%(ftype)s ,%(qg)s ,%(s_id)s ,%(self.vno3)s)")

                data1 = {
                    'coll': coll,
                    't': t,
                    'd': d,
                    'ftype': ftype,
                    'qg': qg,
                    's_id': s_id,
                    'self.vno3': self.vno3,
                }
                cur.execute(ins1, data1)
                conn.commit()

            except mysql.connector.Error as error:
                print("Failed to create table in MySQL: {}".format(error))
            finally:
                if (conn.is_connected()):
                    cur.close()
                    conn.close()
                    print("MySQL connection is closed")

            print("=" * 50)
            print('  ' * 18, '   Bill ', '  ' * 10)
            print("=" * 50)
            print('  ' * 13, 'Hindustan Petroleum', '  ' * 10)
            print("=" * 50)
            print(" You have been refilled L.P.G gas of ", round(self.acqdfuel / 1000, 2), "litres")
            print(" You have recived  L.P.G gas of worth Rs ", self.l)
            print(" Your date of visit is    ", time.asctime())

        if self.ch2 == 1:
            self.z2 = 0
            self.lq = float(input(" Enter the quantity of which u want to buy L.P.G "))
            self.vno3 = input(" Enter the vehicle number ")

            self.lca = self.decamount * self.lq
            self.l2.append(self.lca)
            self.gas1 = " Fuel taken  =" + "  " + str(self.lq) + "litres" + "  \n" + " Amount is   =" + "Rs" + str(
                self.lca) + "  \n" + " Vehicle no  =" + str(self.vno3) + "  \n" + " Time is " + time.asctime()

            time4 = time.asctime()
            coll = self.lca
            t = time4[11:19]
            d = time4[:-13] + time4[20:]
            y = time4[20:25]

            import mysql.connector
            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='PUMP',
                                               user='Sarthak',
                                               password='q1w2e3r4t5')
                cur = conn.cursor()
                ins = (
                    "INSERT INTO GAS (Vehicle_No ,Gamt ,Gqty ,Time ,Date ,Collection ,Year ,Station_id) VALUES (%(self.vno3)s ,%(self.lca)s ,%(self.lq)s ,%(t)s ,%(d)s, %(coll)s ,%(y)s ,%(s_id)s)")
                data = {
                    'self.vno3': self.vno3,
                    'self.lca': self.lca,
                    'self.lq': self.lq,
                    't': t,
                    'd': d,
                    'coll': coll,
                    'y': y,
                    's_id': '12345',
                }
                cur.execute(ins, data)
                ftype = "LPG"
                s_id = "12345"
                ins1 = (
                    "INSERT INTO COLLECTION (total_coll ,Time ,date ,Fuel_type ,Fuel_qty ,station_id ,Vehicle_no) VALUES (%(coll)s ,%(t)s ,%(d)s ,%(ftype)s ,%(self.lq)s ,%(s_id)s ,%(self.vno3)s)")

                data1 = {
                    'coll': coll,
                    't': t,
                    'd': d,
                    'ftype': ftype,
                    'self.lq': self.lq,
                    's_id': s_id,
                    'self.vno3': self.vno3,
                }
                cur.execute(ins1, data1)
                conn.commit()

            except mysql.connector.Error as error:
                print("Failed to create table in MySQL: {}".format(error))
            finally:
                if (conn.is_connected()):
                    cur.close()
                    conn.close()
                    print("MySQL connection is closed")

            print("=" * 50)
            print('  ' * 18, '   Bill ', '  ' * 10)
            print("=" * 50)
            print('  ' * 13, 'Hindustan Petroleum', '  ' * 10)
            print("=" * 50)
            print(" You have recieved ", self.lq, " litres of  LPG of worth Rs ", self.lca)
            print(" Your date of visit is    ", time.asctime())

    # '-'*5,"This is ONLY for the developer and owner of the pump ",'-'*5#

    def petroldetail(self):

        a = list()
        b = list()
        c = list()

        import mysql.connector
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='PUMP',
                                           user='Sarthak',
                                           password='q1w2e3r4t5')
            cur = conn.cursor()
            cur1 = conn.cursor()
            cur.execute("Select sum(pamt),sum(pqty),Vehicle_no from petrol;")
            print("\n")
            for i in cur:
                a.append(list(map(float, i)))
            print("Total Petrol Quantity ", float(a[0][1]), "litres sold of Amount ", float(a[0][0]))
            print("\n")
            print("\n")
            print("Enter 1 to search using Date ")
            print("Enter 2 to search using Vehicle No ")
            print("Enter 3 to search using Year ")
            print("Enter 4 to search using time ")
            print("Enter 5 to search using Amount of Fuel Bought ")
            print("Enter 6 to search using Quantity of Fuel Bought ")
            print("\n")
            print("\n")
            ch = input("Enter your choice")

            if (ch == "1"):
                print("Enter 1 if u have a date with u")
                print("Enter 2 to check a using a date in our database")
                ch1 = input("Enter your choice")
                print("\n")
                if (ch1 == "1"):
                    ch2 = input("Enter ur date ")
                    cur.execute(
                        "select Vehicle_no,Pamt,Pqty,date,time,Station_id from petrol where date " + "=" + str(ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):
                    cur.execute("Select distinct date from petrol")
                    print("\n")
                    for i1 in cur:
                        print(i1)
                    print("\n")
                    ch3 = input("Enter the date from above list")
                    cur.execute(
                        "select Vehicle_no,Pamt,Pqty,date,time,Station_id from petrol where date " + "=" + str(ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "2"):

                print("Enter 1 if u have a Vehicle No with u")
                print("Enter 2 to check a using Vehicle No in our database")
                print("\n")
                ch1 = input("Enter your choice")
                print("\n")

                if (ch1 == "1"):
                    ch2 = input("Enter ur Vehicle_no ")
                    cur.execute(
                        "Select Vehicle_no,Pamt,Pqty,date,time,Station_id from petrol where Vehicle_no " + "=" + str(
                            ch2))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):
                    cur.execute("Select distinct Vehicle_no from petrol")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the Vehicle_no from above list")
                    cur.execute(
                        "select Vehicle_no,Pamt,Pqty,date,time,Station_id from petrol where Vehicle_no " + "=" + str(
                            ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "3"):

                ch1 = "1"
                if (ch1 == "1"):
                    cur.execute("Select distinct Year from petrol")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the year from above list")
                    cur.execute(
                        "select Vehicle_no,Pamt,Pqty,date,time,Station_id from petrol where year " + "=" + str(ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "4"):

                print("Enter 1 if u have time details with u")
                print("Enter 2 to check time detials in our database")
                print("\n")
                ch1 = input("Enter your choice")
                print("\n")

                if (ch1 == "1"):
                    ch2 = input("Enter time ")
                    cur.execute(
                        "Select Vehicle_no,Pamt,Pqty,date,time,Station_id from petrol where time " + "=" + str(
                            ch2))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):
                    cur.execute("Select distinct time from petrol")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the time from above list")
                    cur.execute(
                        "select Vehicle_no,Pamt,Pqty,date,time,Station_id from petrol where time " + "=" + str(
                            ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "5"):

                print("Enter 1 if u have Amount details with u")
                print("Enter 2 to check Amount in our database")
                print("\n")
                ch1 = input("Enter your choice")
                print("\n")

                if (ch1 == "1"):
                    ch2 = input("Enter Amount ")
                    cur.execute(
                        "Select Vehicle_no,Pamt,Pqty,date,time,Station_id from petrol where pamt " + "=" + str(
                            ch2))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):
                    cur.execute("Select  pamt from petrol")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the Amount from above list")
                    cur.execute(
                        "select Vehicle_no,Pamt,Pqty,date,time,Station_id from petrol where pamt " + "=" + str(
                            ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "6"):

                print("Enter 1 if U have Fuel Quantity details with u")
                print("Enter 2 to check Fuel Quantity detials in our database")
                print("\n")
                ch1 = input("Enter your choice")
                print("\n")

                if (ch1 == "1"):
                    ch2 = input("Enter Fuel Quantity ")
                    cur.execute(
                        "Select Vehicle_no,Pamt,Pqty,date,time,Station_id from petrol where pqty " + "<=" + str(
                            ch2))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):

                    cur.execute("Select pqty from petrol")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the Fuel Quantity from above list")
                    cur.execute(
                        "select Vehicle_no,Pamt,Pqty,date,time,Station_id from petrol where pqty " + "<=" + str(
                            ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            print("\n")
            print("\n")
            conn.commit()

        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()
                print()

    def day(self):

        import mysql.connector
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='PUMP',
                                           user='Sarthak',
                                           password='q1w2e3r4t5')
            cur = conn.cursor()
            cur.execute("Select DISTINCT Date from collection")
            print("Date list")
            print()
            for i in cur:
                print(i)
            print()
            date1 = str(input("Enter the Date to be checked"))
            print()
            cur.execute("select sum(total_coll),date from collection where date" + "=" + str(date1));
            print()
            totalc = []
            for j in cur:
                tc = float(j[0])
                totalc.append(tc)
            print(" Total Collection  on ", date1, " is", totalc[0])
            conn.commit()

        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()
                print()

    def deiseldetail(self):

        dc = []
        dvl = []
        import mysql.connector
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='PUMP',
                                           user='Sarthak',
                                           password='q1w2e3r4t5')
            cur = conn.cursor()
            cur.execute("Select sum(damt),sum(dqty),Vehicle_no from diesel")
            print("\n")
            for i in cur:
                dc.append(list(map(float, i)))
            print("Total Petrol Quantity ", float(dc[0][1]), "litres sold of Amount Rs:", float(dc[0][0]))
            print("\n")
            print("\n")
            print("Enter 1 to search using Date ")
            print("Enter 2 to search using Vehicle No ")
            print("Enter 3 to search using Year ")
            print("Enter 4 to search using time ")
            print("Enter 5 to search using Amount of Fuel Bought ")
            print("Enter 6 to search using Quantity of Fuel Bought ")
            print("\n")
            print("\n")
            ch = input("Enter your choice")

            if (ch == "1"):
                print("Enter 1 if u have a date with u")
                print("Enter 2 to check a using a date in our database")
                ch1 = input("Enter your choice")
                print("\n")
                if (ch1 == "1"):
                    ch2 = input("Enter ur date ")
                    cur.execute(
                        "select Vehicle_no,damt,dqty,date,time,Station_id from diesel where date " + "=" + str(ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):
                    cur.execute("Select distinct date from diesel")
                    print("\n")
                    for i1 in cur:
                        print(i1)
                    print("\n")
                    ch3 = input("Enter the date from above list")
                    cur.execute(
                        "select Vehicle_no,damt,dqty,date,time,Station_id from diesel where date " + "=" + str(ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))
            if (ch == "2"):

                print("Enter 1 if u have a Vehicle No with u")
                print("Enter 2 to check a using Vehicle No in our database")
                print("\n")
                ch1 = input("Enter your choice")
                print("\n")

                if (ch1 == "1"):
                    ch2 = input("Enter ur Vehicle_no ")
                    cur.execute(
                        "Select Vehicle_no,damt,dqty,date,time,Station_id from diesel where Vehicle_no " + "=" + str(
                            ch2))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):
                    cur.execute("Select distinct Vehicle_no from diesel")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the Vehicle_no from above list")
                    cur.execute(
                        "select Vehicle_no,damt,dqty,date,time,Station_id from diesel where Vehicle_no " + "=" + str(
                            ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "3"):

                ch1 = "1"
                if (ch1 == "1"):
                    cur.execute("Select distinct Year from diesel")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the year from above list")
                    cur.execute(
                        "select Vehicle_no,damt,dqty,date,time,Station_id from diesel where year " + "=" + str(ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "4"):

                print("Enter 1 if u have time details with u")
                print("Enter 2 to check time detials in our database")
                print("\n")
                ch1 = input("Enter your choice")
                print("\n")

                if (ch1 == "1"):
                    ch2 = input("Enter time ")
                    cur.execute(
                        "Select Vehicle_no,damt,dqty,date,time,Station_id from diesel where time " + "=" + str(
                            ch2))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):
                    cur.execute("Select distinct time from diesel")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the time from above list")
                    cur.execute(
                        "select Vehicle_no,damt,dqty,date,time,Station_id from diesel where time " + "=" + str(
                            ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "5"):

                print("Enter 1 if u have Amount details with u")
                print("Enter 2 to check Amount in our database")
                print("\n")
                ch1 = input("Enter your choice")
                print("\n")

                if (ch1 == "1"):
                    ch2 = input("Enter Amount ")
                    cur.execute(
                        "Select Vehicle_no,damt,dqty,date,time,Station_id from diesel where damt " + "=" + str(
                            ch2))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):
                    cur.execute("Select  damt from diesel")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the Amount from above list")
                    cur.execute(
                        "select Vehicle_no,damt,dqty,date,time,Station_id from diesel where damt " + "=" + str(
                            ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "6"):

                print("Enter 1 if U have Fuel Quantity details with u")
                print("Enter 2 to check Fuel Quantity detials in our database")
                print("\n")
                ch1 = input("Enter your choice")
                print("\n")

                if (ch1 == "1"):
                    ch2 = input("Enter Fuel Quantity ")
                    cur.execute(
                        "Select Vehicle_no,damt,dqty,date,time,Station_id from diesel where dqty " + "<=" + str(
                            ch2))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):

                    cur.execute("Select dqty from diesel")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the Fuel Quantity from above list")
                    cur.execute(
                        "select Vehicle_no,damt,dqty,date,time,Station_id from diesel where dqty " + "<=" + str(
                            ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            print("\n")
            print("\n")
            conn.commit()


        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()
                print()

    def LPGdetail(self):

        lc = []
        import mysql.connector
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='PUMP',
                                           user='Sarthak',
                                           password='q1w2e3r4t5')
            cur = conn.cursor()
            cur.execute("Select sum(damt),sum(dqty),Vehicle_no from diesel")
            print("\n")
            for i in cur:
                lc.append(list(map(float, i)))
            print("Total Petrol Quantity ", float(lc[0][1]), "litres sold of Amount Rs:", float(lc[0][0]))
            print("\n")
            print("\n")
            print("Enter 1 to search using Date ")
            print("Enter 2 to search using Vehicle No ")
            print("Enter 3 to search using Year ")
            print("Enter 4 to search using time ")
            print("Enter 5 to search using Amount of Fuel Bought ")
            print("Enter 6 to search using Quantity of Fuel Bought ")
            print("\n")
            print("\n")
            ch = input("Enter your choice")

            if (ch == "1"):
                print("Enter 1 if u have a date with u")
                print("Enter 2 to check a using a date in our database")
                ch1 = input("Enter your choice")
                print("\n")
                if (ch1 == "1"):
                    ch2 = input("Enter ur date ")
                    cur.execute(
                        "select Vehicle_no,gamt,gqty,date,time,Station_id from gas where date " + "=" + str(ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):
                    cur.execute("Select distinct date from gas")
                    print("\n")
                    for i1 in cur:
                        print(i1)
                    print("\n")
                    ch3 = input("Enter the date from above list")
                    cur.execute(
                        "select Vehicle_no,gamt,gqty,date,time,Station_id from gas where date " + "=" + str(ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))
            if (ch == "2"):

                print("Enter 1 if u have a Vehicle No with u")
                print("Enter 2 to check a using Vehicle No in our database")
                print("\n")
                ch1 = input("Enter your choice")
                print("\n")

                if (ch1 == "1"):
                    ch2 = input("Enter ur Vehicle_no ")
                    cur.execute(
                        "Select Vehicle_no,gamt,gqty,date,time,Station_id from gas where Vehicle_no " + "=" + str(
                            ch2))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):
                    cur.execute("Select distinct Vehicle_no from gas")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the Vehicle_no from above list")
                    cur.execute(
                        "select Vehicle_no,gamt,gqty,date,time,Station_id from gas where Vehicle_no " + "=" + str(
                            ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "3"):

                ch1 = "1"
                if (ch1 == "1"):
                    cur.execute("Select distinct Year from gas")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the year from above list")
                    cur.execute(
                        "select Vehicle_no,gamt,gqty,date,time,Station_id from gas where year " + "=" + str(ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "4"):

                print("Enter 1 if u have time details with u")
                print("Enter 2 to check time detials in our database")
                print("\n")
                ch1 = input("Enter your choice")
                print("\n")

                if (ch1 == "1"):
                    ch2 = input("Enter time ")
                    cur.execute(
                        "Select Vehicle_no,gamt,gqty,date,time,Station_id from gas where time " + "=" + str(
                            ch2))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):
                    cur.execute("Select distinct time from gas")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the time from above list")
                    cur.execute(
                        "select Vehicle_no,gamt,gqty,date,time,Station_id from diesel where time " + "=" + str(
                            ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "5"):

                print("Enter 1 if u have Amount details with u")
                print("Enter 2 to check Amount in our database")
                print("\n")
                ch1 = input("Enter your choice")
                print("\n")

                if (ch1 == "1"):
                    ch2 = input("Enter Amount ")
                    cur.execute(
                        "Select Vehicle_no,gamt,gqty,date,time,Station_id from gas where gamt " + "=" + str(
                            ch2))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):
                    cur.execute("Select gamt from gas")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the Amount from above list")
                    cur.execute(
                        "select Vehicle_no,gamt,gqty,date,time,Station_id from gas where gamt " + "=" + str(
                            ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            if (ch == "6"):

                print("Enter 1 if U have Fuel Quantity details with u")
                print("Enter 2 to check Fuel Quantity detials in our database")
                print("\n")
                ch1 = input("Enter your choice")
                print("\n")

                if (ch1 == "1"):
                    ch2 = input("Enter Fuel Quantity ")
                    cur.execute(
                        "Select Vehicle_no,gamt,gqty,date,time,Station_id from gas where gqty " + "<=" + str(
                            ch2))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

                if (ch1 == "2"):

                    cur.execute("Select gqty from gas")
                    for i1 in cur:
                        print(i1)
                    ch3 = input("Enter the Fuel Quantity from above list")
                    cur.execute(
                        "select Vehicle_no,gamt,gqty,date,time,Station_id from gas where gqty " + "<=" + str(
                            ch3))
                    print("\n")
                    print(" Vehicle_no  |  Amount  |  Quantity  |        Date        |      Time     |  Station Id ")
                    for i2 in cur:
                        print("    ", str(i2[0]), "  ", "  ", float(i2[1]), "  ", "  ", float(i2[2]), "  ", "     ",
                              str(i2[3]), "  ", "   ", str(i2[4]), "  ", "   ", int(i2[5]))

            print("\n")
            print("\n")
            conn.commit()


        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()
                print()


def call():
    b = pump()

    print("\n")
    print("\n")
    print('=' * 20, " New Window ", '=' * 20)
    print("=" * 50)
    print(' *' * 15, ' Hindustan Petroleum ', ' *' * 16)
    print("=" * 50)
    print(" *" * 15, " Date ", z1, " *" * 18)
    print("\n")
    print("\n")
    print(' ' * 5, ' Todays rates are :- ', '  ' * 20)
    print("\n")
    print(' ' * 5, 'Petrol :-         |       Rs 76.50/litre')
    print(' ' * 5, 'Deisel :-         |       Rs 76.50/litre')
    print(' ' * 5, 'LPG   :-          |       Rs 76.50/litre')
    print("\n")
    print('=' * 50)
    print(" " * 5, "Choices are", " " * 20)
    print("\n")
    print(" " * 5, " 1   -:   For Petrol", " " * 20)
    print(" " * 5, " 2   -:   For Deisel", " " * 20)
    print(" " * 5, " 3   -:   For L.P.G ", " " * 20)
    print(" " * 5, " 4   -:   Petrol Details ", " " * 20)
    print(" " * 5, " 5   -:   Deisel Details ", " " * 20)
    print(" " * 5, " 6   -:   LPG  Details ", " " * 20)
    print(" " * 5, " 7   -:   Private Details ", " " * 20)
    print(" " * 5, " 8  -:   Total collection till  ", z1 + " " * 20)
    print(" " * 5, " 9  -:   Collection details on a particular Date ")





class login(pump):

    def adminlogin(self):
        import mysql.connector
        try:
            conn = mysql.connector.connect(host='localhost', database='PUMP', user='Sarthak', password='q1w2e3r4t5')
            cur = conn.cursor()
            sec1 = []
            adminid = input("Enter Admin ID")
            adminpass = input("Enter Admin Password")
            cur.execute("select adminid,pass from admin where pass " + "=" + str(adminpass))
            for i in cur:
                sec1.append(i)
            adid = sec1[0][0]
            adpass = sec1[0][1]
            if ((adminid == adid) and (adminpass == adpass)):
                print(" Login Successful ")
                while True:
                    print("\n")
                    print("\n")
                    try:
                        i = input("Press Y for menu ").upper()
                        if i == "Y":
                            login()
                            try:
                                c = float(input(" Enter your choice - : "))
                                if c == 1:
                                    c1.adminlogin()

                                if c == 2:
                                    c1.developerlogin()

                                if c == 3:
                                    c1.userlogin()

                                if c == 4:
                                    c1.signup()

                            except EOFError:
                                print(" Some thing went wrong U are directed to main menu ")
                        else:
                            b = pump()
                            print("\n")
                            print("\n")
                            print('=' * 20, " New Window ", '=' * 20)
                            print("=" * 50)
                            print(' *' * 15, ' Hindustan Petroleum ', ' *' * 16)
                            print("=" * 50)
                            print(" *" * 15, " Date ", z1, " *" * 18)
                            print("\n")
                            print("\n")
                            print(' ' * 5, ' Todays rates are :- ', '  ' * 20)
                            print("\n")
                            print(' ' * 5, 'Petrol :-         |       Rs 76.50/litre')
                            print(' ' * 5, 'Deisel :-         |       Rs 76.50/litre')
                            print(' ' * 5, 'LPG   :-          |       Rs 76.50/litre')
                            print("\n")
                            print('=' * 50)
                            print(" " * 5, "Choices are", " " * 20)
                            print("\n")
                            print(" " * 5, " 1   -:   For Petrol", " " * 20)
                            print(" " * 5, " 2   -:   For Deisel", " " * 20)
                            print(" " * 5, " 3   -:   For L.P.G ", " " * 20)
                            print(" " * 5, " 4   -:   Petrol Details ", " " * 20)
                            print(" " * 5, " 5   -:   Deisel Details ", " " * 20)
                            print(" " * 5, " 6   -:   LPG  Details ", " " * 20)
                            print(" " * 5, " 7   -:   Private Details ", " " * 20)
                            print(" " * 5, " 8   -:   Total collection till  ", z1 + " " * 20)
                            print(" " * 5, " 9   -:   Collection details on a particular Date ")
                    except:
                        call()
                    print("\n")
                    try:
                        c = float(input(" Enter your choice - : "))
                        if c == 1:
                            b.petrol()

                        if c == 2:
                            b.deisel()

                        if c == 3:
                            b.LPG()

                        if c == 4:
                            b.petroldetail()

                        if c == 5:
                            b.deiseldetail()

                        if c == 6:
                            b.LPGdetail()

                        if c == 7:
                            b.private()

                        if c == 8:
                            b.totalday()

                        if c == 9:
                            b.day()
                    except EOFError:
                        print(" Some thing went wrong U are directed to main menu ")
                        b = pump()


        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()
                print()

    def developerlogin(self):
        import mysql.connector
        try:
            conn = mysql.connector.connect(host='localhost', database='PUMP', user='Sarthak', password='q1w2e3r4t5')
            cur = conn.cursor()
            sec = []
            adminid = input("Enter Developer ID")
            adminpass = input("Enter Developer Password")
            cur.execute("select devID,pass from developer ")
            for i in cur:
                sec.append(i)
            adid = sec[0][0]
            adpass = sec[0][1]
            if ((adminid == adid) and (adminpass == adpass)):
                print(" Login Successful ")
                while True:
                    print("\n")
                    print("\n")
                    try:
                        i = input("Press Y for menu ").upper()
                        if i == "Y":
                            b = pump()
                            print("\n")
                            print("\n")
                            print('=' * 20, " New Window ", '=' * 20)
                            print("=" * 50)
                            print(' *' * 15, ' Hindustan Petroleum ', ' *' * 16)
                            print("=" * 50)
                            print(" *" * 15, " Date ", z1, " *" * 18)
                            print("\n")
                            print("\n")
                            print(' ' * 5, ' Todays rates are :- ', '  ' * 20)
                            print("\n")
                            print(' ' * 5, 'Petrol :-         |       Rs 76.50/litre')
                            print(' ' * 5, 'Deisel :-         |       Rs 76.50/litre')
                            print(' ' * 5, 'LPG   :-          |       Rs 76.50/litre')
                            print("\n")
                            print('=' * 50)
                            print(" " * 5, "Choices are", " " * 20)
                            print("\n")
                            print(" " * 5, " 1   -:   For Petrol", " " * 20)
                            print(" " * 5, " 2   -:   For Deisel", " " * 20)
                            print(" " * 5, " 3   -:   For L.P.G ", " " * 20)
                            print(" " * 5, " 4   -:   Petrol Details ", " " * 20)
                            print(" " * 5, " 5   -:   Deisel Details ", " " * 20)
                            print(" " * 5, " 6   -:   LPG  Details ", " " * 20)
                            print(" " * 5, " 7   -:   Private Details ", " " * 20)
                            print(" " * 5, " 8   -:   Total collection till  ", z1 + " " * 20)
                            print(" " * 5, " 9   -:   Collection details on a particular Date ")

                        else:
                            b = pump()
                            print("\n")
                            print("\n")
                            print('=' * 20, " New Window ", '=' * 20)
                            print("=" * 50)
                            print(' *' * 15, ' Hindustan Petroleum ', ' *' * 16)
                            print("=" * 50)
                            print(" *" * 15, " Date ", z1, " *" * 18)
                            print("\n")
                            print("\n")
                            print(' ' * 5, ' Todays rates are :- ', '  ' * 20)
                            print("\n")
                            print(' ' * 5, 'Petrol :-         |       Rs 76.50/litre')
                            print(' ' * 5, 'Deisel :-         |       Rs 76.50/litre')
                            print(' ' * 5, 'LPG   :-          |       Rs 76.50/litre')
                            print("\n")
                            print('=' * 50)
                            print(" " * 5, "Choices are", " " * 20)
                            print("\n")
                            print(" " * 5, " 1   -:   For Petrol", " " * 20)
                            print(" " * 5, " 2   -:   For Deisel", " " * 20)
                            print(" " * 5, " 3   -:   For L.P.G ", " " * 20)
                            print(" " * 5, " 4   -:   Petrol Details ", " " * 20)
                            print(" " * 5, " 5   -:   Deisel Details ", " " * 20)
                            print(" " * 5, " 6   -:   LPG  Details ", " " * 20)
                            print(" " * 5, " 7   -:   Private Details ", " " * 20)
                            print(" " * 5, " 8   -:   Total collection till  ", z1 + " " * 20)
                            print(" " * 5, " 9   -:   Collection details on a particular Date ")
                    except:
                        call()
                    print("\n")
                    try:
                        c = float(input(" Enter your choice - : "))
                        if c == 1:
                            b.petrol()

                        if c == 2:
                            b.deisel()

                        if c == 3:
                            b.LPG()

                        if c == 4:
                            b.petroldetail()

                        if c == 5:
                            b.deiseldetail()

                        if c == 6:
                            b.LPGdetail()

                        if c == 7:
                            b.private()

                        if c == 8:
                            b.totalday()

                        if c == 9:
                            b.day()
                    except EOFError:
                        print(" Some thing went wrong U are directed to main menu ")
                        b = pump()


        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()
                print()

    def userlogin(self):
        import mysql.connector
        try:
            conn = mysql.connector.connect(host='localhost', database='PUMP', user='Sarthak', password='q1w2e3r4t5')
            cur = conn.cursor()
            sec3 = []
            adminid = input("Enter User ID")
            adminpass = input("Enter User Password ")
            cur.execute("select userid,pass from user ")
            for i in cur:
                sec3.append(i)
            adid = sec3[0][0]
            adpass = sec3[0][1]
            if ((adminid == adid) and (adminpass == adpass)):
                print(" Login Successful ")
                while True:
                    print("\n")
                    print("\n")
                    try:
                        i = input("Press Y for menu ").upper()
                        if i == "Y":
                            b = pump()
                            print("\n")
                            print("\n")
                            print('=' * 20, " New Window ", '=' * 20)
                            print("=" * 50)
                            print(' *' * 15, ' Hindustan Petroleum ', ' *' * 16)
                            print("=" * 50)
                            print(" *" * 15, " Date ", z1, " *" * 18)
                            print("\n")
                            print("\n")
                            print(' ' * 5, ' Todays rates are :- ', '  ' * 20)
                            print("\n")
                            print(' ' * 5, 'Petrol :-         |       Rs 76.50/litre')
                            print(' ' * 5, 'Deisel :-         |       Rs 76.50/litre')
                            print(' ' * 5, 'LPG   :-          |       Rs 76.50/litre')
                            print("\n")
                            print('=' * 50)
                            print(" " * 5, "Choices are", " " * 20)
                            print("\n")
                            print(" " * 5, " 1   -:   For Petrol", " " * 20)
                            print(" " * 5, " 2   -:   For Deisel", " " * 20)
                            print(" " * 5, " 3   -:   For L.P.G ", " " * 20)
                            print(" " * 5, " 4   -:   Petrol Details ", " " * 20)
                            print(" " * 5, " 5   -:   Deisel Details ", " " * 20)
                            print(" " * 5, " 6   -:   LPG  Details ", " " * 20)
                            print(" " * 5, " 7   -:   Private Details ", " " * 20)
                            print(" " * 5, " 8   -:   Total collection till  ", z1 + " " * 20)
                            print(" " * 5, " 9   -:   Collection details on a particular Date ")

                        else:
                            b = pump()
                            print("\n")
                            print("\n")
                            print('=' * 20, " New Window ", '=' * 20)
                            print("=" * 50)
                            print(' *' * 15, ' Hindustan Petroleum ', ' *' * 16)
                            print("=" * 50)
                            print(" *" * 15, " Date ", z1, " *" * 18)
                            print("\n")
                            print("\n")
                            print(' ' * 5, ' Todays rates are :- ', '  ' * 20)
                            print("\n")
                            print(' ' * 5, 'Petrol :-         |       Rs 76.50/litre')
                            print(' ' * 5, 'Deisel :-         |       Rs 76.50/litre')
                            print(' ' * 5, 'LPG   :-          |       Rs 76.50/litre')
                            print("\n")
                            print('=' * 50)
                            print(" " * 5, "Choices are", " " * 20)
                            print("\n")
                            print(" " * 5, " 1   -:   For Petrol", " " * 20)
                            print(" " * 5, " 2   -:   For Deisel", " " * 20)
                            print(" " * 5, " 3   -:   For L.P.G ", " " * 20)
                            print(" " * 5, " 4   -:   Petrol Details ", " " * 20)
                            print(" " * 5, " 5   -:   Deisel Details ", " " * 20)
                            print(" " * 5, " 6   -:   LPG  Details ", " " * 20)
                            print(" " * 5, " 7   -:   Private Details ", " " * 20)
                            print(" " * 5, " 8   -:   Total collection till  ", z1 + " " * 20)
                            print(" " * 5, " 9   -:   Collection details on a particular Date ")
                    except:
                        call()
                    print("\n")
                    try:
                        c = float(input(" Enter your choice - : "))
                        if c == 1:
                            b.petrol()

                        if c == 2:
                            b.deisel()

                        if c == 3:
                            b.LPG()

                        if c == 4:
                            b.petroldetail()

                        if c == 5:
                            b.deiseldetail()

                        if c == 6:
                            b.LPGdetail()

                        if c == 7:
                            b.private()

                        if c == 8:
                            b.totalday()

                        if c == 9:
                            b.day()
                    except EOFError:
                        print(" Some thing went wrong U are directed to main menu ")
                        b = pump()


        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()
                print()

    def signup(self):
        import mysql.connector
        try:
            conn = mysql.connector.connect(host='localhost', database='PUMP', user='Sarthak', password='q1w2e3r4t5')
            cur = conn.cursor()
            print("Enter 1 to Create User Account ")
            print("\n")
            print("Enter 2 to Create Admin Account ")
            print("\n")
            print("Enter 3 to Create Developer Account ")
            print("\n")
            signch = int(input("Enter Your Choice "))
            uvl = ""
            usertime = time.asctime()

            if (signch == 1):

                fname = input("Enter First Name ")
                lname = input("Enter Last Name ")
                mobn = input("Enter Mob no ")
                add = input("Enter Address ")
                sex = input("Enter Sex ")
                aadharno = input("Enter Aadhar No ")
                mob1=mobn
                n = int(input("Enter the No of vehicles u have "))
                for i in range(n):
                    vnoi = input("Enter  Vehicle No ")
                    uvl =uvl +"||"+ vnoi
                mail = input("Enter ur mail id ")
                passchar = string.ascii_letters + string.digits + string.punctuation
                pass3 = ''.join(random.choice(passchar) for i in range(10))
                ins = (
                    "insert into user (First_name,Last_name,Mob_no,Address,Sex,Aadhar_no,Vehicles,Time,Mail,pass,userid) VALUES(%(fname)s,%(lname)s,%(mobn)s,%(add)s,%(sex)s,%(aadharno)s,%(uvl)s,%(usertime)s,%(mail)s,%(pass3)s,%(mob1)s)")
                data = {
                    'fname': fname,
                    'lname': lname,
                    'mobn': mobn,
                    'add': add,
                    'sex': sex,
                    'aadharno': aadharno,
                    'uvl': uvl,
                    'usertime': usertime,
                    'mail': mail,
                    'pass3': pass3,
                    'mob1': mob1,
                }
                cur.execute(ins, data)
                conn.commit()

                print("Sign in successful ")
                print("Your Id is ", mobn)
                print("Your Password is ",pass3)

            if (signch == 2):
                fname = input("Enter First Name ")
                lname = input("Enter Last Name ")
                mobn = input("Enter Mob no ")
                add = input("Enter Address ")
                sex = input("Enter Sex ")
                aadharno = input("Enter Station id No ")
                mail = input("Enter ur mail id ")
                adid=aadharno
                passchar = string.ascii_letters + string.digits + string.punctuation
                pass2 = ''.join(random.choice(passchar) for i in range(10))
                ins = (
                    "insert into admin (First_name,Last_name,Mob_no,Address,Sex,Station_id,Time,Mail,pass,adminId) VALUES(%(fname)s,%(lname)s,%(mobn)s,%(add)s,%(sex)s,%(aadharno)s,%(usertime)s,%(mail)s,%(pass2)s,%(adid)s)")
                data = {
                    'fname': fname,
                    'lname': lname,
                    'mobn': mobn,
                    'add': add,
                    'sex': sex,
                    'aadharno': aadharno,
                    'usertime': usertime,
                    'mail': mail,
                    'pass2': pass2,
                    'adid': adid,
                }
                cur.execute(ins, data)
                conn.commit()
                print("Sign in successful ")
                print("Your Id is ", adid)
                print("Your Password is ", pass2)
                conn.commit()

            if (signch == 3):
                fname = input("Enter First Name ")
                lname = input("Enter Last Name ")
                mobn = input("Enter Mob no ")
                add = input("Enter Address ")
                sex = input("Enter Sex ")
                mail = input("Enter ur mail id ")
                passchar = string.ascii_letters + string.digits + string.punctuation
                pass1 = ''.join(random.choice(passchar) for i in range(10))
                mob=mobn
                ins = (
                    "insert into developer (First_name,Last_name,Mob_no,Address,Sex,Time,Mail,pass,devID) VALUES(%(fname)s,%(lname)s,%(mobn)s,%(add)s,%(sex)s,%(usertime)s,%(mail)s,%(pass1)s,%(mob)s)")
                data = {
                    'fname': fname,
                    'lname': lname,
                    'mobn': mobn,
                    'add': add,
                    'sex': sex,
                    'usertime': usertime,
                    'mail': mail,
                    'pass1': pass1,
                    'mob': mob,
                }
                cur.execute(ins, data)
                conn.commit()
                print("Sign in successful ")
                print("Your Id is ", mobn)
                print(" Your Password is ", pass1)

                conn.commit()
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()
                print()

print("\n")
print("\n")
print('=' * 20, " Login Page ", '=' * 20)
print("=" * 50)
print(' *' * 15, ' Hindustan Petroleum ', ' *' * 16)
print("=" * 50)
print(" *" * 15, " Date ", z1, " *" * 18)
print("\n")
print("\n")
print("Enter 1 for Admin login ")
print("Enter 2 for Developer login ")
print("Enter 3 for User login ")
print("Enter 4 for Signup ")
print("\n")
print("\n")

try:
    c1=login()
    c = float(input(" Enter your choice - : "))

    if c == 1:
        c1.adminlogin()

    if c == 2:
        c1.developerlogin()

    if c == 3:
        c1.userlogin()

    if c == 4:
        c1.signup()

except EOFError:
    print(" Some thing went wrong U are directed to main menu ")

