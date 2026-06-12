from pyscript import web, when, display, document

clicks = 0
totalClicks = 0
doubleStore = False
quadStore = False
octoStore = False
sexdecuStore = False
duotringtupleStore = False
quattorsexagintupleStore = False
centupleStore = False
bg_music_unmuted = False

def update_display():
    document.getElementById("clickCount").innerText = clicks
    document.getElementById("totalCount").innerText = totalClicks

update_display()

@when ("click", "#buyingDuo")
def buyingDuo(event):
    global clicks, doubleStore
    if not doubleStore:
        if clicks >= 25:
            clicks -= 25
            doubleStore = True
            update_display()
            document.getElementById("buyingDuo").innerText = "Sold Out"

@when ("click", "#buyingQuad")
def buyingQuad(event):
    global clicks, quadStore
    if not quadStore:
        if clicks >= 100:
            clicks -= 100
            quadStore = True
            update_display()
            document.getElementById("buyingQuad").innerText = "Sold Out"

@when ("click", "#buyingOcto")
def buyingOcto(event):
    global clicks, octoStore
    if not octoStore:
        if clicks >= 400:
            clicks -= 400
            octoStore = True
            update_display()
            document.getElementById("buyingOcto").innerText = "Sold Out"

@when ("click", "#buyingSexdecu")
def buyingSexdecu(event):
    global clicks, sexdecuStore
    if not sexdecuStore:
        if clicks >= 1600:
            clicks -= 1600
            sexdecuStore = True
            update_display()
            document.getElementById("buyingSexdecu").innerText = "Sold Out"

@when ("click", "#buyingDuotringtuple")
def buyingDuoTring(event):
    global clicks, duotringtupleStore
    if not duotringtupleStore:
        if clicks >= 6400:
            clicks -= 6400
            duotringtupleStore = True
            update_display()
            document.getElementById("buyingDuotringtuple").innerText = "Sold Out"

@when ("click", "#buyingQuattorsexagintuple")
def buyingQuattorsexagin(event):
    global clicks, quattorsexagintupleStore
    if not quattorsexagintupleStore:
        if clicks >= 25600:
            clicks -= 25600
            quattorsexagintupleStore = True
            update_display()
            document.getElementById("buyingQuattorsexagintuple").innerText = "Sold Out"

@when ("click", "#buyingCentuple")
def buyingCentuple(event):
    global clicks, centupleStore
    if not centupleStore:
        if clicks >= 40000:
            clicks -= 40000
            centupleStore = True
            update_display()
            document.getElementById("buyingCentuple").innerText = "Sold Out"

@when ("click", "#clicking")
def clicking(event):
    global clicks, totalClicks, bg_music_unmuted
    if centupleStore:
        clicks += 100
        totalClicks += 100
    elif quattorsexagintupleStore:
        clicks += 64
        totalClicks += 64
    elif duotringtupleStore:
        clicks += 32
        totalClicks += 32
    elif sexdecuStore:
        clicks += 16
        totalClicks += 16
    elif octoStore:
        clicks += 8
        totalClicks += 8
    elif quadStore:
        clicks += 4
        totalClicks += 4
    elif doubleStore:
        clicks += 2
        totalClicks += 2
    else:
        clicks += 1
        totalClicks += 1
    update_display()

    
    if not bg_music_unmuted:
        bg = document.getElementById("bgMusic")
        if bg:
            bg.muted = False
            bg.volume = 0.1
            bg.play().catch(lambda e: print("bg play error:", e))
            bg_music_unmuted = True
        else:
            print("bgMusic element not found!")

    audio = document.getElementById("splatSound")
    audio.volume = 0.3
    audio.currentTime = 0
    audio.play()