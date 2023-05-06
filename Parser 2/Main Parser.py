import re
data = """19/02/2023, 09:35 - Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more.
19/02/2023, 09:35 - Purujit Padhy created group "POMKER"
19/02/2023, 09:35 - Purujit Padhy added you
19/02/2023, 09:36 - Vimanyu: 19/02 
Vimanyu +100
Puru -40
Shrey -60
19/02/2023, 22:33 - Vimanyu: 19/02
Vimanyu -15
Nihar -255
Shaurya +140
Aman +130
19/02/2023, 22:35 - (Not) Aman Gupta: 01/02
aman +10
vimanyu -55
puru +0
shaurya +45
19/02/2023, 22:48 - Somin Ranjan, King Semen: Ok
19/02/2023, 22:48 - (Not) Aman Gupta: Bruh
19/02/2023, 22:49 - Somin Ranjan, King Semen: <Media omitted>
20/02/2023, 00:28 - You're now an admin
21/02/2023, 00:00 - You added Nihar Malik
21/02/2023, 00:01 - Vimanyu: 21/02
Vimanyu +0
Shaurya -105
Aman +190
Nihar -10
Puru -75
21/02/2023, 00:01 - (Not) Aman Gupta: 02/02
Puru +90
Shaurya +115
Aman -100
Grug -105
21/02/2023, 00:26 - Somin Ranjan, King Semen: null
23/02/2023, 00:08 - Vimanyu: You deleted this message
23/02/2023, 00:09 - Vimanyu: 23/02
Vimanyu +35
Puru +70
Semen -120
Aman -200
Shaurya+215
24/02/2023, 08:27 - You changed this group's icon
24/02/2023, 19:32 - Nihar Malik: null
25/02/2023, 13:30 - Vimanyu: 25/02
Vimanyu -105
Shaurya +110
Puru -5
Aman +0
25/02/2023, 23:39 - Vimanyu: 25/02
Vimanyu +0
Puru -85
Shaurya +15
Aman +70
26/02/2023, 12:16 - Vimanyu: 18/02 
Puru +200
Aman -200
Vimanyu +95
Shaurya -95
26/02/2023, 12:17 - Vimanyu: 24/02
Vimanyu -200
Shaurya +65
Nihar +45
Aman +90
26/02/2023, 21:29 - Vimanyu: You deleted this message
26/02/2023, 21:30 - Vimanyu: 26/02
Vimanyu -145
Shaurya +130
Aman +5
27/02/2023, 19:55 - Vimanyu: 27/02
Vimanyu -95
Shaurya +30
Nihar +115
Aman -50
01/03/2023, 20:19 - Vimanyu: 01/03
Vimanyu +150
Aman -200
Puru -35
Nihar +10
Shaurya +75
02/03/2023, 23:25 - You added Samarth Khandelwal
03/03/2023, 00:02 - Vimanyu: 03/03
Shaurya +460
Nihar -130
Samarth -200
Aman -200
Vimanyu +70
04/03/2023, 00:43 - Purujit Padhy: 04/03
Shaurya -40
Vimanyu +5
Puru -60
Shrey -200
Aman +295
04/03/2023, 02:35 - (Not) Aman Gupta changed this group's icon
05/03/2023, 21:21 - Shaurya Mehta: 05/03
Shaurya +150
Vimanyu -135
Aman -15
10/03/2023, 00:55 - Vimanyu: 10/03
Vimanyu +240
Nihar -180
Aman +225
Shaurya -285
10/03/2023, 16:26 - Purujit Padhy: 09/03
Shaurya -300
Puru +190
Aman +110
10/03/2023, 16:28 - Purujit Padhy: 08/03
Vimanyu -200
Puru +70
Shaurya +35
Aman +95
10/03/2023, 16:41 - Vimanyu: 10/03
Vimanyu -20
Aman +140
Shaurya -120
10/03/2023, 21:46 - Vimanyu: 10/03 
Vimanyu -200
Puru +30
Aman +470
Shaurya -300
10/03/2023, 21:50 - Vimanyu: 10/03
Aman -200
Shaurya +175
Puru +75
Shrey -50
10/03/2023, 23:45 - Vimanyu: 10/03
Nihar -80
Vimanyu -200
Shaurya +280
11/03/2023, 00:33 - Vimanyu: 11/03
Nihar -5
Aman +65
Shaurya +140
Puru -200
11/03/2023, 18:44 - Vimanyu: 11/03
Nihar -200
Vimanyu +325
Shaurya +75
Aman -200
12/03/2023, 01:03 - Vimanyu: You deleted this message
12/03/2023, 01:05 - Vimanyu: 12/03
Vimanyu -245
Puru -40
Shaurya -200
Aman -200
Nihar +685
12/03/2023, 22:27 - Vimanyu: 12/03
Vimanyu +70
Shaurya -55
Aman +55
Puru -70
14/03/2023, 17:00 - Vimanyu: 14/03
Vimanyu -25
Aman +20
Nihar + 175
Shaurya +30
Puru -200
15/03/2023, 16:44 - Vimanyu: 15/03
Vimanyu +110
Nihar -45
Shaurya -65
15/03/2023, 16:44 - (Not) Aman Gupta: Bhosdike bula to leta
16/03/2023, 21:49 - Vimanyu: 16/03
Vimanyu -85
Aman +30
Shaurya +200
Puru -80
Nihar -65
17/03/2023, 23:27 - Shaurya Mehta: null
17/03/2023, 23:43 - Nihar Malik: This message was deleted
17/03/2023, 23:54 - Nihar Malik: 17/03
Aman +10
Puru -30
Nihar -200
Shaurya +220
18/03/2023, 15:13 - Vimanyu: 18/03
Vimanyu -35
Shaurya +165
Aman -130
23/03/2023, 00:09 - Nihar Malik: 22/03
Vimanyu -200
Nihar +195
Shaurya +20
Aman -15
24/03/2023, 00:21 - Nihar Malik: 23/03
Shaurya +130
Nihar +70
Aman -200
26/03/2023, 14:37 - Vimanyu: 26/03
Vimanyu +80
Aman -200
Shaurya +110
Puru -45
Nihar +55
28/03/2023, 00:57 - (Not) Aman Gupta: 28/03
Vimanyu -45
Aman +335
Shaurya+210
Nihar -10
Puru -500
28/03/2023, 17:26 - Nihar Malik: 28/03
Aman -200
Shaurya -160
Nihar +360
05/04/2023, 23:38 - (Not) Aman Gupta: 05/04
Aman +62.5
Puru -100
Shaurya +37.5
08/04/2023, 22:08 - Nihar Malik: 08/04
Aman -50
Shaurya -90
Puru -200
Nihar +340
09/04/2023, 22:10 - Nihar Malik: 09/04
Aman +160
Shaurya +35
Nihar +5
Puru -200
11/04/2023, 00:31 - Nihar Malik: 10/04
Aman -185
Vimanyu -200
Shaurya +75
Nihar +310
13/04/2023, 01:15 - Nihar Malik: 13/04
Aman +80
Nihar +40
Shaurya -120
21/04/2023, 23:12 - Nihar Malik: 21/04 
Shaurya -300
Nihar -125
Vimanyu +425
23/04/2023, 01:48 - Vimanyu: 23/04
Nihar -200
Vimanyu +120
Shaurya +80
06/05/2023, 23:40 - Nihar Malik: This message was deleted
06/05/2023, 23:41 - Nihar Malik: 6/5
Nihar +585
Vimanyu -300
Aman -100
Shaurya -200
Somin +15
07/05/2023, 00:34 - Somin Ranjan, King Semen: It should be +40 for me
"""
# regex bullshit
x = re.findall(r"(\n[a-zA-Z]*( )?[+-].*)", data, re.MULTILINE)
# print (x)
info = [];

# Discard two elements, idfk why regex returns three junk elemtnts, and elements after two relevant ones, per line
for i in x:
    info.append(i[0][1:])

print(info)

#for a in info:
#    if (a.startswith("Vimanyu") or a.startswith("vimanyu")):
#        print (a)

# Make dictionary and add shit up

accounts = {}
total = 0;
for term in info:
    p = -1
    try:
        p = term.rindex('+')
    except:
        p = term.rindex('-')
    amt = term[p:]

    name = term[0: p - 1];
    name = name.lower()
    if (not name in accounts.keys()):
        accounts[name] = 0.0;
#s    print(name, amt)
    amt = amt.replace(' ', '');
    accounts[name] += float(amt)

    total += float(amt);

print(accounts);
print(total)
