import random

DeinName=input("Wie heißt du?\n")
BistDuMutig=input("Bist du mutig? Tippe 'Ja' oder 'Nein'.\n")




print(f"Dein Name lautet {DeinName}")
print(f"Bist du mutig? {BistDuMutig}")


Start=input(f"Du, {DeinName}, schlägst die Augen auf. Erschrocken stellst du fest, dass du dich in einem dir unbekannten Raum befindest. Was möchtest du tun? 1: Die Augen wieder schließen. 2: Aufstehen und dich in dem Raum umsehen.\n")
if (Start=="1"):
    print("Vielleicht bist du ja wieder zu Hause, wenn du die Augen noch einmal schließt und öffnest?")
    Augengeschlossen=input("Nein, es hat nicht geholfen. Du bist noch immer in dem dunklen Raum. Seufzend erhebst du dich und beginnst dich in dem Raum umzusehen Drücke 1, um fortzufahren.\n")
if (Start=="2" or Augengeschlossen =="1"):
    print("Du gehst einige Schritte und stellst fest, dass der Raum ein Fenster und eine weitere Tür hat. Du erkennst schcnell, dass sich das Fenster öffnen lässt.")
    Raum=input("Wohin durch möchtest du gehen? 1: Fenster. 2: Türe\n")
    if (Raum=="1"):
        print("Zunächst schaust du vorsichtig aus dem Fenster. Doch es ist zu dunkel, um die Höhe zwischen Fenster und Boden abschätzen zu können.")
        Fenster=input(f"Möchtest du wirklich aus dem Fenster springen?, {DeinName}? 1: ja. 2: nein\n")
        if (Fenster=="1"):
            Fensterklettern=random.randint(1,6)
            print(f"Du würfelst", {Fensterklettern})
            if(Fensterklettern<6):
                print(f"Das war leider keine gute Idee von dir {DeinName}. Die Distanz von Fenster und Boden war zu hoch... Ende. ")
            elif(Fensterklettern==6):
                print(f"Du landest ächzend auf deinen Füßen. Dir wird sofort bewusst, wie viel Glück du gerade gehabt hast. Doch das ist egal. Du willst nur weg von diesem unbekannten Haus. Du atmest einmal tief durch und läufst davon. Ende.")
        if (Fenster=="2"):
            NichtausdemFensterspringen=input(f"Du beschließt, dass dir ein Sprung ins Ungewisse zu riskant ist. Du entscheidest dich für die Türe. Drücke 1 um fortzufahren  ")
    if (Raum=="2" or NichtausdemFensterspringen=="1"):
        print("Vorsichtig öffnest du die Türe. In dem dunklen Flur erkennst du die Silhouetten einiger Möbel. Irgendwo hörst du das Ticken einer Uhr. Du durchquerst den Flur. Schließlich bleibst du vor einer Treppe stehen, die nach unten führt")
        Flur=input("Möchtest du die Treppe hinuntergehen oder dich weiter umschauen? 1: Treppe hinuntergehen. 2: Weiter umsehen\n")
        if (Flur=="1"):
            print("Du gehst die Treppe hinunter und gelangst in eine verlassene Bibliothek. Plötzlich hörst du schwere und kernige Schritte. Wer das nur sein könnte?")
            Bibliothek=input("Du bist hier also nicht alleine. Möchtest du auf die Person warten oder dich verstecken? 1: Warten. 2: Verstecken\n")
            if (Bibliothek=="1"):
                print("Mit aufgerissenen Augen stellst du fest, dass da ein kopfloser Ritter mit einem Schwert in der Hand auf dich zu kommt. Du versuchst zu entkommen, doch es ist zu spät. Der kopflose Ritter hat dich erwischt... Ende.")
            if (Bibliothek=="2" and BistDuMutig=="Ja"):
                print("In Windeseile versteckst du dich hinter einem Bücherregal. Du spähst hinter deiner Deckung hervor und erkennst schockiert, dass ein kopfloser Ritter mit einem Schwert in der Hand durch die Bibliothek stampft. Mutig wie du bist, gibst du keinen Laut von dir. Du wartest bis der schaurige Ritter verschwunden ist und kommst langsam hinter deinem Versteck hervor.")
                MutigInDerBibliothek= input("Der kopflose Ritter ist die Treppe hinaufgegangen. Um die Bibliothek nun zu verlassen drücke 1\n")
            else:
                print("In Windeseile versteckst du dich hinter einem Bücherregal. Du spähst hinter deiner Deckung hervor und erkennst schockiert, dass ein kopfloser Ritter mit einem Schwert in der Hand durch die Bibliothek stampft. Vor lauter Panik stößt du das Bücherregal um. Obwohl der Ritter keinen Kopf hat, scheint er dich bemerkt zu haben. Du versuchst vor ihm davon zu laufen, doch er ist unnatürlich schnell. Nach einer kurzen Verfolgungsjagd durch die Bibliothek hat er dich erwischt... Ende.")













