import sys

# These are the list of all the already installed apps that were on the device
skipList = [
    "com.android.chrome","com.android.vending","com.google.ambient.streaming","com.google.android.accessibility.soundamplifier",
    "com.google.android.accessibility.switchaccess","com.google.android.aicore","com.google.android.apps.accessibility.voiceaccess","com.google.android.apps.aiwallpapers",
    "com.google.android.apps.camera.services","com.google.android.apps.carrier.carrierwifi","com.google.android.apps.docs","com.google.android.apps.dreamliner",
    "com.google.android.apps.emojiwallpaper","com.google.android.apps.maps","com.google.android.apps.messaging","com.google.android.apps.nbu.files",
    "com.google.android.apps.photos","com.google.android.apps.pixel.dcservice","com.google.android.apps.pixel.relationships","com.google.android.apps.pixel.support","com.google.android.apps.privacy.wildlife",
    "com.google.android.apps.recorder","com.google.android.apps.restore","com.google.android.apps.safetyhub","com.google.android.apps.scone","com.google.android.apps.setupwizard.searchselector",
    "com.google.android.apps.tachyon","com.google.android.apps.tips","com.google.android.apps.turbo","com.google.android.apps.wearables.maestro.companion",
    "com.google.android.apps.weather","com.google.android.apps.wellbeing","com.google.android.apps.work.clouddpc","com.google.android.apps.youtube.music",
    "com.google.android.as","com.google.android.as.oss","com.google.android.calculator","com.google.android.calendar","com.google.android.contactkeys",
    "com.google.android.contacts","com.google.android.deskclock","com.google.android.dialer","com.google.android.euicc","com.google.android.gm",
    "com.google.android.gms","com.google.android.GoogleCamera","com.google.android.googlequicksearchbox","com.google.android.marvin.talkback","com.google.android.youtube"
    "com.google.android.odad","com.google.android.partnersetup","com.google.android.projection.gearhead","com.google.android.safetycore","com.google.android.settings.intelligence",
    "com.google.android.soundpicker","com.google.android.tts","com.google.android.videos","com.google.android.webview","com.google.ar.core","com.google.assistant.hubui",
    "com.google.audio.hearing.visualization.accessibility.scribe","com.google.pixel.livewallpaper","helium314.keyboard","com.vagujhelyigergely.calculatorm3","org.secuso.privacyfriendlydicer"
    ]

with open("scripts/textLists/installedApks.txt","r") as f1:
    uapks = f1.read().splitlines()

for i in range(len(uapks)):
    uapks[i] = uapks[i].removesuffix(".apk")

with open("scripts/textLists/apklist.txt", "r") as f:
    apks = f.read().splitlines()

for apk in apks:
    apkPath=apk.split(":")[1].split("apk=")[0]
    apkName=apk.split("=")[-1]
    if apk.split("=")[-1] in skipList: 
        continue
    elif apk.split("=")[-1] in uapks: 
        continue
    else:
        print(f"{apkPath}apk {apkName}")

