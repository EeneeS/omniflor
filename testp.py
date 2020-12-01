import soco
from time import sleep
from soco.discovery import by_name

# 2 pinnen hoog maken die relays aansturen voor het aanleggen van de boxen

# opstart-delay van het sonos systeem (300s / 5 min)
sleep(30)

ip_list = []
speaker_list = []

# kamer met daarbij juiste IP-adress krijgen.
for device in devices:
    # ip
    device_ip = device
    ip_list.append(device_ip)
    # naam
    device_name = device.player_name
    speaker_list.append(device_name)

# dictionary van alle speakers
all_speakers = dict(zip(speaker_list, ip_list))

# dictionary maken van alle slaves
slaves = dict(zip(speaker_list, ip_list))
del slaves[master_speaker]

# eventueel bestaande groepen verwijderen / wachtrij verwijderen
for device in devices:
    device.unjoin()
    sleep(0.01)
    device.clear_queue()

print("ALLE GROEPEN EN QUEUE VERWIJDERD")

# alle slaves in de groep van de master plaatsen
for speaker in slaves:
    slaves[speaker].join(all_speakers[master_speaker])
    sleep(0.01)

print("ALLE SPEAKERS ZIJN IN PARTYMODE")


# muziek van de master instellen die de slaves ook zullen spelen
all_speakers[master_speaker].play_uri(uri="http://icecast.vrtcdn.be/mnm-high.mp3",
                                      title="MNM", start=True, force_radio=False)

print("MUZIEK IS AAN HET SPELEN")
