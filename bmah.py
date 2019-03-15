import requests
import lxml.html as lh
import datetime
import time

def create_file(location_server, server):
    file = open(location_server + "/" + server + ".csv", "a+")
    file.close()

def get_last_date_backup(lines):
    lastline = (len(lines) and lines[-1]) or ""
    return(lastline and len(lastline) > 8 and lastline[-8:]) or None

def get_info(server_name, date):
    
    url = "https://www.tradeskillmaster.com/black-market?realm=" + server_name
    tentativas = 0
    while True:
        if tentativas >= 50:
            print("esperando 1 mim...")
            time.sleep(60)
            tentativas = 0
            
        print((server_name, tentativas+1))
        page = requests.get(url)
        tentativas += 1
        doc = lh.fromstring(page.content)
        items = doc.xpath('//tr/td/a')
        if len(doc.xpath('//div[@class="empty"]')) == 1:
            break
        if len(items) > 0:
            break
        

    item_info = ""
    for item in items:
        item_id = item.get("data-item")
        item_name = item.get("title")
        item_info += "\n%s,%s,%s" %(item_id, item_name, date)
    print(item_info)
    print()
    return item_info

us_server = ['Azralon']
us_server = ['Aegwynn', 'Aerie-Peak', 'Agamaggan', 'Aggramar', 'Akama', 'Alexstrasza', 'Alleria', 'Altar-of-Storms', 'Alterac-Mountains', "AmanThul", 'Andorhal',
             'Anetheron', 'Antonidas', "Anubarak", 'Anvilmar', 'Arathor', 'Archimonde', 'Area-52', 'Argent-Dawn', 'Arthas', 'Arygos', 'Auchindoun', 'Azgalor',
             'Azjol-Nerub', 'Azralon', 'Azshara', 'Azuremyst', 'Baelgun', 'Balnazzar', 'Barthilas', 'Black-Dragonflight', 'Blackhand', 'Blackrock', 'Blackwater-Raiders',
             'Blackwing-Lair', "Blades-Edge", 'Bladefist', 'Bleeding-Hollow', 'Blood-Furnace', 'Bloodhoof', 'Bloodscalp', 'Bonechewer', 'Borean-Tundra',
             'Boulderfist', 'Bronzebeard', 'Burning-Blade', 'Burning-Legion', 'Caelestrasz', 'Cairne', 'Cenarion-Circle', 'Cenarius', "Chogall", 'Chromaggus',
             'Coilfang', 'Crushridge', 'Daggerspine', 'Dalaran', 'Dalvengyr', 'Dark-Iron', 'Darkspear', 'Darrowmere', "DathRemar", 'Dawnbringer', 'Deathwing',
             'Demon-Soul', 'Dentarg', 'Destromath', 'Dethecus', 'Detheroc', 'Doomhammer', 'Draenor', 'Dragonblight', 'Dragonmaw', "DrakTharon", "Drakthul",
             'Draka', 'Drakkari', 'Dreadmaul', 'Drenden', 'Dunemaul', 'Durotan', 'Duskwood', 'Earthen-Ring', 'Echo-Isles', 'Eitrigg', "EldreThalas", 'Elune',
             'Emerald-Dream', 'Eonar', 'Eredar', 'Executus', 'Exodar', 'Farstriders', 'Feathermoon', 'Fenris', 'Firetree', 'Fizzcrank', 'Frostmane', 'Frostmourne',
             'Frostwolf', 'Galakrond', 'Gallywix', 'Garithos', 'Garona', 'Garrosh', 'Ghostlands', 'Gilneas', 'Gnomeregan', 'Goldrinn', 'Gorefiend', 'Gorgonnash',
             'Greymane', 'Grizzly-Hills', "Guldan", 'Gundrak', 'Gurubashi', 'Hakkar', 'Haomarush', 'Hellscream', 'Hydraxis', 'Hyjal', 'Icecrown', 'Illidan',
             'Jaedenar', "JubeiThos", "Kaelthas", 'Kalecgos', 'Kargath', "KelThuzad", 'Khadgar', 'Khaz-Modan', "Khazgoroth", "Kiljaeden", 'Kilrogg', 'Kirin-Tor',
             'Korgath', 'Korialstrasz', 'Kul-Tiras', 'Laughing-Skull', 'Lethon', 'Lightbringer',
             "Lightnings-Blade", 'Lightninghoof', 'Llane', 'Lothar', 'Madoran', 'Maelstrom', 'Magtheridon', 'Maiev', "MalGanis", 'Malfurion', 'Malorne', 'Malygos',
             'Mannoroth', 'Medivh', 'Misha', "MokNathal", 'Moon-Guard', 'Moonrunner', "Mugthol", 'Muradin', 'Nagrand', 'Nathrezim', 'Nazgrel', 'Nazjatar', 'Nemesis',
             "Nerzhul", 'Nesingwary', 'Nordrassil', 'Norgannon', 'Onyxia', 'Perenolde', 'Proudmoore', "QuelThalas", "Queldorei", 'Ragnaros', 'Ravencrest', 'Ravenholdt',
             'Rexxar', 'Rivendare', 'Runetotem', 'Sargeras', 'Saurfang', 'Scarlet-Crusade', 'Scilla', "Senjin", 'Sentinels', 'Shadow-Council', 'Shadowmoon', 'Shadowsong',
             'Shandris', 'Shattered-Halls', 'Shattered-Hand', "Shuhalo", 'Silver-Hand', 'Silvermoon', 'Sisters-of-Elune', 'Skullcrusher', 'Skywall', 'Smolderthorn',
             'Spinebreaker', 'Spirestone', 'Staghelm', 'Steamwheedle-Cartel', 'Stonemaul', 'Stormrage', 'Stormreaver', 'Stormscale', 'Suramar', 'Tanaris', 'Terenas',
             'Terokkar', 'Thaurissan', 'The-Forgotten-Coast', 'The-Scryers', 'The-Underbog', 'The-Venture-Co', 'Thorium-Brotherhood', 'Thrall', 'Thunderhorn',
             'Thunderlord', 'Tichondrius', 'Tol-Barad', 'Tortheldrin', 'Trollbane', 'Turalyon', 'Twisting-Nether', 'Uldaman', 'Uldum', 'Undermine', 'Ursin', 'Uther',
             'Vashj', "Veknilash", 'Velen', 'Warsong', 'Whisperwind', 'Wildhammer', 'Windrunner', 'Winterhoof', 'Wyrmrest-Accord', 'Ysera', 'Ysondre', 'Zangarmarsh',
             "Zuljin", 'Zuluhed']

location_server = (("us", us_server),)
date = datetime.datetime.now().strftime("%Y%m%d")

for location_server, servers in location_server:
    for server in servers:
        server_name = "%s-%s" %(location_server, server)
        create_file(location_server, server)
        arq = open(location_server + "/" + server + ".csv", "r+")
        lines = arq.readlines()
        last_date_backup = get_last_date_backup(lines)

        if date != last_date_backup:
            item_info = get_info(server_name, date)

            if not lines:
                item_info = item_info[1:]
            arq.write(item_info)
        arq.close()
