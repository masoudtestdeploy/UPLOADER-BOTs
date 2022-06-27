import json
import requests
import math
import urllib.parse as urlparse
import secrets
from seedrcc import Seedr
from seedr import SeedrAPI

# message.text[8:]
token = "eydhY2Nlc3NfdG9rZW4nOiAnOTc4ZWRjZWY5NGYwOWQ4ZGI2Njc0ZWE3N2M0MDAwOGIxNTU4NDJmZicsICdyZWZyZXNoX3Rva2VuJzogJzIzMjdiZWQ0OTUzNDYzMzYwNDFmM2MwM2JkODMyMGYyZDZiM2U4Y2QnfQ=="

def progressBar(progress):
    bars = int(float(progress)) // 5

    return f"{'▣'*bars}{(20-bars)*'▢'}"

def convertSize(byte):
    if byte == 0:
        return "0B"

    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(byte, 1024)))
    p = math.pow(1024, i)
    s = round(byte / p, 2)
    return "%s %s" % (s, size_name[i])

def urlEncode(url):
    return urlparse.quote(url, safe='/:&?=%')

def spaceBar(totalSpace, spaceUsed):
    bars = round((spaceUsed / totalSpace) * 20)

    return f"{'▣'*bars}{(20-bars)*'▢'}"

def account():
    account = Seedr(token=token)

    response = account.getSettings()

            #! On success
    if 'error' not in response:
        if response['result'] == True:
            text = f"<b>accountBtn</b>\n\nusername {response['account']['username']}\ntotalBandwidthUsed {convertSize(response['account']['bandwidth_used'])}\ncountry {response['country']}\n"
            #text += f"{language['inviteLink'][userLanguage]} seedr.cc/?r={response['account']['user_id']} \n{language['inviteRemaining'][userLanguage]} {response['account']['invites']} / {response['account']['max_invites']}\n{language['inviteAccepted'][userLanguage]} {response['account']['invites_accepted']} / {dbSql.getSetting(userId, 'totalRefer')}"

            text += f"\n\n{convertSize(response['account']['space_used'])} / {convertSize(response['account']['space_max'])}"
            text += f"\n{spaceBar(totalSpace=response['account']['space_max'], spaceUsed=response['account']['space_used'])}"

            return text
    else:
        return response

def active():
    account = Seedr(token=token)
    response = account.listContents()

    if 'error' not in response:
        if 'torrents' in response:
                #! If user has active torrents
            if response['torrents']:
                text = ''
                for i in response['torrents']:
                    text += f"<b>📂 {i['name']}</b>\n\n💾 {convertSize(i['size'])}, ⏰ {i['last_update']}\n\n"
                    text += f"Quality : {i['torrent_quality']}\nconnectedTo : {i['connected_to']}\ndownloadingFrom : {i['downloading_from']}\nseeders : {i['seeders']}\nleechers : {i['leechers']}\nuploadingTo : {i['uploading_to']}\n"

                    #! Show warnings if any
                    # if i['warnings'] != '[]':
                    #     warnings = i['warnings'].strip('[]').replace('"','').split(',')
                    #     for warning in warnings:
                    #         text += f"\n⚠️ {warning.capitalize()}"

                    text += f"\n{progressBar(i['progress'])}\n\n"

                #markup = telebot.types.InlineKeyboardMarkup()
                #markup.add(telebot.types.InlineKeyboardButton(text=language['refreshBtn'][userLanguage], callback_data='refreshActive'))

                return text

            #! If user don't have any active torrents
            else:
                return "noActiveTorrents"
    else:
        return response

def addTorrent(magnetLink=None, torrentFile=None, wishlistId=None):
    account = Seedr(token=token)


    response = account.addTorrent(
        magnetLink=magnetLink,
        torrentFile=torrentFile,
        wishlistId=wishlistId
    )

    if 'result' in response:
                #! If torrent added successfully
        if 'user_torrent_id' in response:            
            return active()

                #! If no enough space
        elif response['result'] in ['not_enough_space_added_to_wishlist', 'not_enough_space_wishlist_full']:
            return "not_enough_space_added_to_wishlist / not_enough_space_wishlist_full"
                #! Invalid magnet link
        elif response['result'] == 'parsing_error':
            return "parsing_error"
                #! If parallel downloads exceeds
        elif response['result'] == 'queue_full_added_to_wishlist':
            return "queue_full_added_to_wishlist"
                #! If the torrent is already downloading
        elif response == {'result': True}:
            return "alreadyDownloading"
                #! If no torrent is passed
        elif 'error' in response and response['error'] == 'no_torrent_passed':
            return "no_torrent_passed"

        else:
            return "unknownError"
    else:
        return response

def deleteFolder(Folder_id):
    account = Seedr(token=token)
    response = account.deleteFolder(Folder_id)
    if 'error' not in response:
         #! If folder is deleted successfully
        if response['result'] == True:
            return "deletedSuccessfully"
    else:
        return response

def fileLink(file_id):

    account = Seedr(token=token)
    response = account.fetchFile(file_id)

    if 'error' not in response:
                #! If download link found
        if 'url' in response:
            encodedUrl = urlEncode(response['url'])
            text = f"🖹 <b>{response['name']}</b>\n\n"
            text += f"🔗 <code>{encodedUrl}</code>\n\n"
            return text
    else:
        return response

def folders():

    account = Seedr(token=token)
    response = account.listContents()
    if 'error' not in response:
        #! If user has files
        if response['folders']:
            text = ''
            for i in response['folders']:
                text += f"<b>📂 {i['fullname']}</b>\n\n💾 {convertSize(i['size'])}B, ⏰ {i['last_update']}"
                text += f"\n\nfiles : /getFiles_{i['id']}\nlink: /getLink_{i['id']}\ndelete : /delete_{i['id']}\n\n"
            return text
                #! If user has no files
        else:
            return "noFiles"
    else:
        return response

def getFiles(id):
    account = Seedr(token=token)
    response = account.listContents(folderId=id)
    if 'error' not in response:
        #! If success
        if 'name' in response:
            text = f"<b>📁 {response['name']}</b>\n\n"
            for folder in response['folders']:
                text += f"🖿 {folder['name']} <b>[ {convertSize(folder['size'])}]</b>\n\n"
                text += f"files : /getFiles_{folder['id']}\n"
                text += f"link : /getLink_{folder['id']}\n"
                text += f"delete : /delete_{folder['id']}\n\n"
            for file in response['files']:
                text += f"<code>{'🎬' if file['play_video'] == True else '🎵' if file['play_audio'] == True else '📄'} {file['name']}</code> <b>[{convertSize(file['size'])}]</b>\n\n"
                text += f"link : /fileLink_{'v' if file['play_video'] == True else 'a' if file['play_audio'] == True else 'u'}{file['folder_file_id']}\n"
                text += f"delete : /remove_{file['folder_file_id']}\n\n"
            return text
    else:
        return response

def getLink(folderId):

    seedr = SeedrAPI(email="masoudakhoondi1@gmail.com", password="12345678")

    Get_File_link = seedr.get_file(folderId)["url"]
    Get_File_name = seedr.get_file(folderId)["name"]
    text = f"🖿 <code>{Get_File_name}</code>\n\n🔗 <code>{Get_File_link}</code>"
    return text

def removeFile(fileid):
    account = Seedr(token=token)
    response = account.deleteFile(fileid)
    if 'error' not in response:
        #! If file removed successfully
        if response['result'] == True:
            return "removedSuccessfully"
    else:
        return response

def wishlist():
    account = Seedr(token=token)
    response = account.getSettings()
    #! On success
    if 'error' not in response:
        text = ''
        # Seedr Wishlist
        if response['result'] is True:
            if response['account']['wishlist']:
                for wish in response['account']['wishlist']:
                    text += f"⭐ <b>{wish['title']}</b>\n\nAdd: /addTorrent_{wish['id']}\nRemove: /removeWL_{wish['id']}\n\n"
        if text:
            return text
        else:
            return "noWishlist"
    else:
        return response

#print(wishlist())
