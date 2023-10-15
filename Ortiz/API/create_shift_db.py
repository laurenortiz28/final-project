import sqlite3
conn = sqlite3.connect('shiftspot.db')
c=conn.cursor()

try:
    c.execute("DROP TABLE shift;")
except:
    print ("Error")
c.execute("""
          CREATE TABLE shift(
          sft_id INTEGER,
          cafe_id INTEGER,
          employee_id INTEGER,
          shift_id TEXT,
          day_of_week TEXT
)""")
many_shift = [
                (1,1,3765,'morning','monday'),
                (2,1,3765,'off','tuesday'),
                (3,1,3765,'morning','wednesday'),
                (4,1,3765,'morning','thursday'),
                (5,1,3765,'off','friday'),
                (6,1,3765,'off','saturday'),
                (105,1,3765,'morning','sunday'),
                (106,1,8921,'morning','monday'),
                (7,1,8921,'morning','tuesday'),
                (8,1,8921,'off','wednesday'),
                (9,1,8921,'morning','thursday'),
                (10,1,8921,'off','friday'),
                (110,1,8921,'morning','saturday'),
                (111,1,8921,'morning','sunday'),
                (11,1,4532,'off','monday'),
                (12,1,4532,'morning','tuesday'),
                (13,1,4532,'off','wednesday'),
                (14,1,4532,'morning','thursday'),
                (15,1,4532,'off','friday'),
                (150,1,4532,'morning','saturday'),
                (115,1,4532,'off','sunday'),
                (16,1,6189,'morning','monday'),
                (17,1,6189,'off','tuesday'),
                (18,1,6189,'morning','wednesday',),
                (19,1,6189,'off','thursday'),
                (20,1,6189,'morning','friday'),
                (221,1,6189,'off','saturday'),
                (222,1,6189,'morning','sunday'),
                (21,1,1274,'off','monday'),
                (22,1,1274,'off','tuesday'),
                (23,1,1274,'morning','wednesday'),
                (24,1,1274,'morning','thursday'),
                (25,1,1274,'off','friday'),
                (250,1,1274,'morning','saturday'),
                (260,1,1274,'morning','sunday'),
                (26,1,9408,'off','monday'),
                (27,1,9408,'noon','tuesday'),
                (28,1,9408,'off','wednesday'),
                (29,1,9408,'noon','thursday'),
                (30,1,9408,'off','friday'),
                (130,1,9408,'morning','saturday'),
                (131,1,9408,'morning','sunday'),
                (31,1,5632,'off','monday'),
                (32,1,5632,'noon','tuesday'),
                (33,1,5632,'noon','wednesday'),
                (34,1,5632,'off','thursday'),
                (35,1,5632,'noon','friday'),
                (350,1,5632,'morning','saturday'),
                (360,1,5632,'off','sunday'),
                (36,1,7196,'noon','monday'),
                (37,1,7196,'noon','tuesday'),
                (38,1,7196,'noon','wednesday'),
                (39,1,7196,'off','thursday'),
                (40,1,7196,'off','friday'),
                (140,1,7196,'morning','saturday'),
                (141,1,7196,'morning','sunday'),
                (41,1,3850,'noon','monday'),
                (42,1,3850,'noon','tuesday'),
                (43,1,3850,'noon','wednesday'),
                (44,1,3850,'noon','thursday'),
                (45,1,3850,'noon','friday'),
                (145,1,3850,'off','saturday'),
                (150,1,3850,'off','sunday'),
                (46,1,2467,'off','monday'),
                (47,1,2467,'noon','tuesday'),
                (48,1,2467,'off','wednesday'),
                (49,1,2467,'noon','thursday'),
                (50,1,2467,'noon','friday'),
                (500,1,2467,'off','saturday'),
                (501,1,2467,'morning','sunday'),
                (51,2,8013,'morning','monday'),
                (52,2,8013,'off','tuesday'),
                (53,2,8013,'off','wednesday'),
                (54,2,8013,'morning','thursday'),
                (55,2,8013,'morning','friday'),
                (155,1,8013,'off','saturday'),
                (156,1,8013,'morning','sunday'),
                (56,2,5724,'morning','monday'),
                (57,2,5724,'off','tuesday'),
                (58,2,5724,'off','wednesday'),
                (59,2,5724,'morning','thursday'),
                (60,2,5724,'morning','friday'),
                (501,1,5724,'off','saturday'),
                (503,1,5724,'off','sunday'),
                (61,2,1398,'morning','monday'),
                (62,2,1398,'off','tuesday'),
                (63,2,1398,'morning','wednesday'),
                (64,2,1398,'morning','thursday'),
                (65,2,1398,'off','friday'),
                (505,1,1398,'morning','saturday'),
                (509,1,1398,'off','sunday'),
                (66,2,6247,'morning','monday'),
                (67,2,6247,'off','tuesday'),
                (68,2,6247,'morning', 'wednesday'),
                (69,2,6247,'off','thursday'),
                (73,2,9754,'morning','wednesday'),
                (74,2,9754,'morning','thursday'),
                (75,2,9754,'morning','friday'),
                (514,1,9754,'off','saturday'),
                (519,1,9754,'off','sunday'),
                (76,2,3021,'noon','monday'),
                (77,2,3021,'noon','tuesday'),
                (78,2,3021,'off','wednesday'),
                (79,2,3021,'noon','thursday'),
                (80,2,3021,'off','friday'),
                (520,1,3021,'morning','saturday'),
                (506,1,3021,'morning','sunday'),
                (81,2,3820,'off','monday'),
                (82,2,3820,'noon','tuesday'),
                (83,2,3820,'noon','wednesday'),
                (84,2,3820,'off','thursday'),
                (85,2,3820,'noon','friday'),
                (350,1,3820,'off','saturday'),
                (205,1,3820,'morning','sunday'),
                (86,2,2123,'off','monday'),
                (87,2,2123,'noon','tuesday'),
                (88,2,2123,'noon','wednesday'),
                (89,2,2123,'off','thursday'),
                (90,2,2123,'off','friday'),
                (895,1,2123,'morning','saturday'),
                (905,1,2123,'morning','sunday'),
                (91,2,8561,'noon','monday'),
                (92,2,8561,'off','tuesday'),
                (93,2,8561,'noon','wednesday'),
                (94,2,8561,'noon','thursday'),
                (95,2,8561,'off','friday'),
                (785,1,8561,'morning','saturday'),
                (985,1,8561,'morning','sunday'),
                (96,2,1244,'noon','monday'),
                (97,2,1244,'noon','tuesday'),
                (98,2,1244,'noon','wednesday'),
                (99,2,1244,'off','thursday'),
                (100,2,1244,'noon','friday'),
                (596,1,1244,'off','saturday'),
                (542,1,1244,'morning','sunday')
             ]
c.executemany("INSERT INTO shift VALUES (?,?,?,?,?)", many_shift)
conn.commit()
conn.close()