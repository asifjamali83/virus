# -*- coding: utf-8 -*- 
#INI CUMA SC ISENG ISENG JH#
#WALAU ISENG GW BUAT PKE OTAK#
from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#------------------Ini pembatas jah hiraukan-----------------#
print ("\n\n --- GURU IS HERE ---\n")
achink = LINE("")
achink.log("Auth Token : " + str(achink.authToken))
achink.log("Timeline Token : " + str(achink.tl.channelAccessToken))
#======================================================#

#=============================================================#0
waitOpen = codecs.open("Mbk2.json","r","utf-8")
settingsOpen = codecs.open("Mbk.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
stickers1Open = codecs.open("sticker1.json","r","utf-8")
stickers2Open = codecs.open("sticker2.json","r","utf-8")
wait = json.load(waitOpen)
images = json.load(imagesOpen)
settings = json.load(settingsOpen)
stickers = json.load(stickersOpen)
stickers1 = json.load(stickers1Open)
stickers2 = json.load(stickers2Open)
#==============================================================================#
achinkMID = achink.profile.mid
achinkProfile = achink.getProfile()
achinkSettings = achink.getSettings()
#==============================================================================#
achinkPoll = OEPoll(achink)
achinkMID = achink.getProfile().mid
admin = [achinkMID]
loop = asyncio.get_event_loop()
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10']
mc = {"wr":{}}
unsendchat = {}
msgdikirim = {}
msg_image={}
msg_video={}
msg_sticker={}
wbanlist = []
msg_dict = {}
temp_flood = {}
#=================================
temptag = {
    "stealtag": False,
}
sets = {
    'autoCancel':{"on":False,"members":10},
	"changeGroupPicture":{},
    "pict": True,
    "sti2": True,
    "tagsticker": False,
    "Sticker": False,
    "autoJoinTicket": False,
    "image": {
        "name": "",
    },
    "addSticker": {
        "name": "",
        "status": False,
    },
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "tag": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "lv": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "wc": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "add": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "join2": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
        }
    },
    "ilstpict": {},
}
chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

anyun = {
    "addTikel": {
        "name": "",
        "status": False
        },
}
nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}
tes = {
    "Message": {},
    "msg": {},
}

tes2 = {
    "Message2": {},
    "msg2": {},
}
tagadd = {
    "tagss": False,
    "tags": False,
    "tag": "THANKS FOR REMEMBERING ME😜",
    "add": "тниq fσя α∂∂ιиg мє αѕ fяιєи∂",
    "wctext": "ωєℓ¢σмє",
    "lv": "",
    "b": "",
    "m": "",
}
apalo = {
    "blacklist":{},
    "Talkblacklist": {},
    "talkban": True,
    "Talkwblacklist": False,
    "Talkdblacklist": False,
}
temp = {"te": "#FFFFFF","t": "#6600CC"}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

ProfileMe = {
    "coverId": "",
    "statusMessage": "",
    "PictureMe": "",
    "NameMe": "",
}
peler = { 
    "receivercount": 0,
    "sendcount": 0
}
hoho = {
    "savefile": False,
    "namefile": "",
}

user1 = achinkMID
user2 = ""

setTime = {}
setTime = rfuSet['setTime']

contact = achink.getProfile() 
backup = achink.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()
Start = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

settings["myProfile"]["displayName"] = achinkProfile.displayName
settings["myProfile"]["statusMessage"] = achinkProfile.statusMessage
settings["myProfile"]["pictureStatus"] = achinkProfile.pictureStatus
cont = achink.getContact(achinkMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = achink.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

ProfileMe["statusMessage"] = achinkProfile.statusMessage
ProfileMe["pictureStatus"] = achinkProfile.pictureStatus
coverId = achink.getProfileDetail()["result"]["objectId"]
ProfileMe["coverId"] = coverId
#=====================================================================
with open("Mbk.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("Mbk2.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
#==============================================================================#

simple = {
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "setsticker":False,
    "stkid":"52114135",
    "stkpkgid":"11539",
    "stkver":"1"
}
#================================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Ma '
        achink.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    achink.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    achink.sendMessage(to, '', annda, 13)
def cloneProfile(mid):
    contact = achink.getContact(mid)
    if contact.videoProfile == None:
        achink.cloneContactProfile(mid)
    else:
        profile = achink.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        achink.updateProfile(profile)
        pict = achink.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = achink.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = achink.getProfileDetail(mid)['result']['objectId']
    achink.updateProfileCoverById(coverId)
def backupProfile():
    profile = achink.getContact(achinkMID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = achink.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def restoreProfile():
    profile = achink.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        achink.updateProfileAttribute(8, profile.pictureStatus)
        achink.updateProfile(profile)
    else:
        achink.updateProfile(profile)
        pict = achink.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = achink.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    achink.updateProfileCoverById(coverId)
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        achink.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@GuruTags' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@GuruTags'+wait["GROUP"]['AR']['P'][msg.to]
    NAME = achink.getGroup(msg.to).name
    sd = achink.waktunjir()
    achink.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',NAME),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@GuruTags'))
def anulurk(to, wait):
    moneys = {}
    for a in wait["setTime"][to].items():
        moneys[a[1]] = [a[0]] if a[1] is not None else idnya
    sort = sorted(moneys)
    sort = sort[0:]
    k = len(sort)//100
    for a in range(k+1):
        if a == 0:no= a;msgas = '╭「 Lurkers 」─'
        else:no = a*100;msgas = '├「 Lurkers 」─'
        h = []
        for i in sort[a*100 : (a+1)*100]:
            h.append(moneys[i][0])
            no+=1
            a = '{}'.format(humanize.naturaltime(datetime.fromtimestamp(i/1000)))
            if no == len(sort):msgas+='\n│{}. @GuruTags\n╰    「 {} 」'.format(no,a)
            else:msgas+='\n│{}. @GuruTags\n│    「 {} 」'.format(no,a)
        mentions(to, msgas, h)
def ClonerV2(to):
    try:
        contact = achink.getContact(to)
        profile = achink.profile
        profileName = achink.profile
        profileStatus = achink.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        achink.updateProfile(profileName)
        achink.updateProfile(profileStatus)
        profile.pictureStatus = achink.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if achink.getProfileCoverId(to) is not None:
            achink.updateProfileCoverById(achink.getProfileCoverId(to))
        achink.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return achink.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        achink.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
def changeVideoAndPictureProfile(path, path2):
    try:
        files = {'file': open(path, 'rb')}
        data = {'params':achink.genOBSParams({'oid': mid,'ver': '2.0','type':'video','cat': 'vp.mp4'})}
        r_vp = achink.server.postContent(achink.server.LINE_OBS_DOMAIN + '/talk/vp/upload.nhn',data=data, files=files)
        if r_vp.status_code != 201:
            raise Exception('update profile video picture failure.')
        achink.updateProfilePicture(path2, 'vp')
    except Exception as e:
        print(str(e))
def sendMentionFooter(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@GuruTag"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        NAME = "{}".format(achink.getContact(achinkMID).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(achink.getContact(achinkMID).pictureStatus)
        ticket = "http://nav.cx/11S41K2"
        achink.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': NAME, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        achink.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@GuruTag"
    if mids == []:
        raise Exception("Invalid mids")
    if "@GuruTags" in text:
        if text.count("@GuruTags") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@GuruTags")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    achink.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(achink.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + achink.getContact("u6e4534dd63e82642f29205d2c993c642").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = achink.genOBSParams({'oid': achinkMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = achink.server.postContent('{}/talk/vp/upload.nhn'.format(str(achink.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        achink.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("")
#=====================================================================#
#          Def tamplate/flex/carousel/liff
#======================================================================#
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = achink.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = achink.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = achink.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def bcTemplate2(friend, data):
    xyz = LiffChatContext(friend)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = achink.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendCarousel(to, data):
    data = json.dumps(data)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = achink.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=data, headers=headers)
def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = achink.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)
def sendflex(to, data):
    n1 = LiffChatContext(to)
    n2 = LiffContext(chat=n1)
    view = LiffViewRequest('1602687308-GXq4Vvk9', n2)
    token = achink.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

uagent = {
    "User-Agent": "Mozilla\t5.0"
}
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def infomeme():
    helpMessage2 = """
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.👿.👿.👿
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.
"""
    return helpMessage2
def postFlex(self, to, data='', altText=''):
        self.allowLiff()
        token = self.issueLiffView(to)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        anu = {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Guru bots",
                                "wrap": True,
                                "color": "#000000",
                                "size" : "sm"
                            }
                        ]
                    }
                }
        altText = altText if altText else '%s sent a messages' % self.profile.displayName
        data = data if data else anu
        data = {
            'messages': [{'type': 'flex', 'altText' : altText, 'contents' : data}]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res
def sendFlex(self, to, data):
        token = self.issueLiffView(to)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [data]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res
def postFlex(self, to, data):
        token = self.issueLiffView(to)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [data]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res
#=========================================================================
def slyric(to,text):
        try:
            r = requests.get("https://api.genius.com/search?q="+text+"&access_token=2j351ColWKXXVxq1PdUNXDYECI2x4zClLyyAJJkrIeX8K7AQ0F-HTmWfG6tNVszO")
            data = r.json()
            hits = data["response"]["hits"][0]["result"]["api_path"]
            title= "\nTitle: "+data["response"]["hits"][0]["result"]["title"].strip()
            oleh = "\nArtis: "+data["response"]["hits"][0]["result"]["primary_artist"]["name"].strip()
            g = data["response"]["hits"][0]["result"]['song_art_image_thumbnail_url']
            r1 = requests.get("https://api.genius.com"+hits+"?&access_token=2j351ColWKXXVxq1PdUNXDYECI2x4zClLyyAJJkrIeX8K7AQ0F-HTmWfG6tNVszO")
            data1 = r1.json()
            path = data1["response"]["song"]["path"]
            release = data1["response"]["song"]["release_date"]
            page_url = "http://genius.com" + path
            page = requests.get(page_url)
            html = BeautifulSoup(page.text, "html.parser")
            [h.extract() for h in html('script')]
            lyrics = html.find("div", class_="lyrics").get_text().strip()
            pesan = " 「 Lyric 」"+title+oleh+'\n'+lyrics
            k = len(pesan)//10000
            for aa in range(k+1):
                achink.sendMessage(to,'{}'.format(pesan[aa*10000 : (aa+1)*10000]))
        except:
            achink.sendMessage(to,"「 404 」\nStatus: Error\nReason: I'cant found lyric {}".format(text))
#===================================================================
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd

#==============================================================================
    
def NOTIFIED_READ_MESSAGE(op):
    try:
        if read['readPoint'][op.param1]:
            if op.param2 in read['readMember'][op.param1]:
                pass
            else:
                read['readMember'][op.param1][op.param2] = True
                read['ROM'][op.param1] = op.param2
        else:
            pass
    except:
        pass
def logError(text):
    achink.log("[ ELLOR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType,mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@G"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        achink.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        achink.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        group = achink.getGroup(to)
        mids = [mem.mid for mem in group.members]
        jml = len(mids)
        arrData = ""
        if mid[0] == mids[0]:
            textx = ""
        else:
            textx = ""
        arr = []
        for i in mid:
            no = mids.index(i) + 1
            textx += "{}.".format(str(no))
            mention = "@G\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
        if no == jml:
            textx += ""
            textx += ""
        achink.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        achink.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d month" % (months)
    if weeks != 0: text += " %02d weeks" % (weeks)
    if days != 0: text += " %02d days" % (days)
    if hours !=  0: text +=  " %02d hours" % (hours)
    if mins != 0: text += " %02d mins" % (mins)
    if secs != 0: text += " %02d sec" % (secs)
    if text[0] == " ":
            text = text[1:]
    return text
#===============================================================
def restartBot():
    print ("RESETBOT..")
    python = sys.executable
    os.execl(python, python, *sys.argv)
#================================================================
def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output video.mp3 {}'.format(link))
    try:
        achink.sendAudio(to, 'video.mp3')
        time.sleep(2)
        os.remove('video.mp3')
    except Exception as e:
        achink.sendMessage(to, "Error")

def fileYtMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output FileYoutube.mp4 {}'.format(link))
    try:
        achink.sendFile(to, "FileYoutube.mp4")
        time.sleep(2)
        os.remove('FileYoutube.mp4')
    except Exception as e:
        achink.sendMessage(to, ' 「 ERROR 」')
    
def fileYtMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output FileYoutube.mp3 {}'.format(link))
    try:
        achink.sendFile(to, 'FileYoutube.mp3')
        time.sleep(2)
        os.remove('FileYoutube.mp3')
    except Exception as e:
        achink.sendMessage(to, ' 「 ERROR 」')
#=====================================================================
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    achink.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': achink.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + achink.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    achink.sendMessage(to, '', contentMetadata, 7)
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            achink.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
#=====================================================
def tagdia(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@Gbots "
        if mids == []:
            raise Exception("Invalid mids")
        if "@GuruTags" in text:
            if text.count("@GuruTags") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@GuruTags")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        achink.sendMessage(to, textx, {'MSG_SENDER_NAME': achink.getContact(ps).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + achink.getContact(ps).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#============================================================================================
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''  
    rmv = len(key + cmd) + 1
    return text[rmv:]
#============================================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('Mbk.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('Mbk2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers1
        f = codecs.open('sticker1.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers2
        f = codecs.open('sticker2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#==================================================================================
#        def add&block
#==================================================================================
async def achinkBot(op):
    try:
        if settings["restartPoint"] != None:
            achink.sendMessage(settings["restartPoint"], 'Sukses restart')
            settings["restartPoint"] = None
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
              if op.param2 in admin:
                  return
              achink.findAndAddContactsByMid(op.param1)
              achink.sendMessage(op.param1,"{}".format(tagadd["add"]))
              msgSticker = sets["messageSticker"]["listSticker"]["add"]
              if msgSticker != None:
                  sid = msgSticker["STKID"]
                  spkg = msgSticker["STKPKGID"]
                  sver = msgSticker["STKVER"]
                  sendSticker(op.param1, sver, spkg, sid)
              print ("[ 5 ] AUTO ADD")
        if op.type == 5:
            if settings["autoblock"] == True:
              if op.param2 in admin:
                  return
              achink.sendMessage(op.param1,tagadd["b"])
              achink.blockContact(op.param1)
              print ("[ 5 ] AUTO BLOCK")
        if op.type == 13:
            if achinkMID in op.param3:
                G = achink.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if sets["autoCancel"]["on"] == True:
                        if len(G.members) <= sets["autoCancel"]["members"]:
                            achink.acceptGroupInvitation(op.param1)
                        else:
                            achink.leaveGroup(op.param1)
                    else:
                        achink.acceptGroupInvitation(op.param1)
                elif sets["autoCancel"]["on"] == True:
                    if len(G.members) <= sets["autoCancel"]["members"]:
                        achink.acceptGroupInvitation(op.param1)
                        achink.leaveGroup(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in apalo["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    achink.acceptGroupInvitation(op.param1, matched_list)
                    achink.leaveGroup(op.param1, matched_list)
                    print ("[ 17 ] LEAVE GROUP")
        if op.type == 15:
          if settings["Leave"] == True:
            if op.param2 in admin:
                return
            ginfo = achink.getGroup(op.param1)
            contact = achink.getContact(op.param2)
            name = contact.displayName
            pp = contact.pictureStatus
            s = name #+ " " + tagadd["lv"]
            e = tagadd["lv"]
            data = {
                         "type": "flex",
                                    "altText": "member ",
                                    "contents": {
                                    "styles": {
                                    "header": {
                                    "backgroundColor":"#0000CD"
                                    },
                                    "body": {
                                    "backgroundColor": "#FFFFFF"
                                    },
                                    "footer": {
                                    "backgroundColor": "#0000CD"
                                    }
                                    },
           "type": "bubble",
           "header": {
           "type": "box",
           "layout": "horizontal",
           "contents": [
                              {
                              "type": "button",
                              "style": "secondary",
                              "color": "#FFFFFF",
                              "height": "sm",
                              "gravity": "center",
                              "flex": 1,
                              "action": {
                              "type": "uri",
                              "label": "😊😊😊😊",
                              "uri": "http://nav.cx/11S41K2"
                          }
                     },
                ]
           },
           "body": {
           "type": "box",
           "layout": "horizontal",
           "spacing": "md",
           "contents": [
                              {
                               "type": "box",
                               "layout": "vertical",
                               "flex": 0,
                               "contents": [
                                                   {
                                                    "type": "image",
                                                    "url": "https://profile.line-scdn.net/" + str(pp),
                                                    "size": "lg",
                                                    "gravity": "bottom"
                                                   }
                                              ]
                                        }, 
                                  {
                                 "type": "separator",
                                 "color": "#000000"
                             },
                         {
                         "type": "box",
                         "layout": "vertical",
                         "flex": 2,
                         "contents": [
                                            {
                                             "type": "text",
                                             "text":"whats wrong {}".format(s),
                                             "color": "#000000",
                                             "size": "sm",
                                             "weight": "bold",
                                             "flex": 3,
                                             "wrap": True,
                                             "gravity": "top"
                                             },{
                                             "type": "text",
                                             "text": "left...?",
                                             "color": "#000000",
                                             "size": "sm",
                                             "weight": "bold",
                                             "flex": 3,
                                             "wrap": True,
                                             "gravity": "top"},{
                                             "type": "text",
                                             "text": e,
                                             "color": "#000000",
                                             "size": "sm",
                                             "weight": "bold",
                                             "flex": 3,
                                             "wrap": True,
                                             "gravity": "top"
                                           }
                                      ]
                                 }
                             ]
                         },
                         "footer": {
                         "type": "box",
                         "layout": "horizontal",
                         "contents": [
                                            {
                                             "type": "button",
                                             "style": "secondary",
                                             "color": "#FFFFFF",
                                             "height": "sm",
                                             "gravity": "center",
                                             "flex": 1,
                                             "action": {
                                             "type": "uri",
                                             "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                             "uri": "http://nav.cx/11S41K2",
                                             }
                                         },
                                     {
                                    "type": "spacer",
                                    "size": "sm",
                                 }
                             ],
                        "flex": 0
                    }
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 15:
          if settings["lv"] == True:
              ginfo = achink.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["lv"]
              if msg != None:
                  contact = achink.getContact(achinkMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' Kirim stiker','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["Welcome"] == True:
            if op.param2 in admin:
                return
            g = achink.getGroup(op.param1)
            contact = achink.getContact(op.param2)
            gname = g.name
            name = contact.displayName
            cover = achink.getProfileCoverURL(op.param2)
            pp = contact.pictureStatus
            a = "welcome to group  {}".format(gname)
            m = "member name  : {}\n\n".format(name)
            s = tagadd["wctext"]
            data = {
                         "type": "flex",
                                    "altText": "welcome",
                                    "contents": {
                                    "styles": {
                                    "header": {
                                    "backgroundColor":"#0000CD"
                                    },
                                    "body": {
                                    "backgroundColor": "#FFFFFF"
                                    },
                                    "footer": {
                                    "backgroundColor": "#0000CD"
                                    }
                                    },
           "type": "bubble",
           "header": {
           "type": "box",
           "layout": "horizontal",
           "contents": [
                              {
                              "type": "button",
                              "style": "secondary",
                              "color": "#FFFFFF",
                              "height": "sm",
                              "gravity": "center",
                              "flex": 1,
                              "action": {
                              "type": "uri",
                              "label": "◦•●◉✿ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 ✿◉●•◦",
                              "uri": "http://nav.cx/11S41K2"
                          }
                     },
                ]
           },
           "body": {
           "type": "box",
           "layout": "horizontal",
           "spacing": "md",
           "contents": [
                              {
                               "type": "box",
                               "layout": "vertical",
                               "flex": 0,
                               "contents": [
                                                   {
                                                    "type": "image",
                                                    "url": "https://profile.line-scdn.net/" + str(pp),
                                                    "size": "lg",
                                                    "gravity": "bottom"
                                                   }
                                              ]
                                        }, 
                                  {
                                 "type": "separator",
                                 "color": "#000000"
                             },
                         {
                         "type": "box",
                         "layout": "vertical",
                         "flex": 2,
                         "contents": [
                                            {
                                             "type": "text",
                                             "text":"Hello {}".format(name),
                                             "color": "#000000",
                                             "size": "sm",
                                             "weight": "bold",
                                             "flex": 3,
                                             "wrap": True,
                                             "gravity": "top"
                                             },{
                                             "type": "text",
                                             "text": a,
                                             "color": "#000000",
                                             "size": "sm",
                                             "weight": "bold",
                                             "flex": 3,
                                             "wrap": True,
                                             "gravity": "top"},{
                                             "type": "text",
                                             "text": s,
                                             "color": "#000000",
                                             "size": "sm",
                                             "weight": "bold",
                                             "flex": 3,
                                             "wrap": True,
                                             "gravity": "top"
                                           }
                                      ]
                                 }
                             ]
                         },
                         "footer": {
                         "type": "box",
                         "layout": "horizontal",
                         "contents": [
                                            {
                                             "type": "button",
                                             "style": "secondary",
                                             "color": "#FFFFFF",
                                             "height": "sm",
                                             "gravity": "center",
                                             "flex": 1,
                                             "action": {
                                             "type": "uri",
                                             "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                             "uri": "http://nav.cx/11S41K2",
                                             }
                                         },
                                     {
                                    "type": "spacer",
                                    "size": "sm",
                                 }
                             ],
                        "flex": 0
                    }
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["Wc"] == True:
            if op.param2 in admin:
                return
            ginfo = achink.getGroup(op.param1)
            contact = achink.getContact(op.param2)
            cover = achink.getProfileCoverURL(op.param2)
            names = contact.displayName
            status = contact.statusMessage
            pp = contact.pictureStatus
            data = {
                            "type": "flex",
                                    "altText": "NEWS FLASH",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#0000CD"
                                        },
                                        "body": {
                                        "backgroundColor": "#000000"
                                        },
                                        "footer": {
                                          "backgroundColor": "#0000CD"
                                        }
                                        },
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "◦•●◉✿ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 ✿◉●•◦",
                                    "uri": "http://nav.cx/11S41K2"
      }
      },
    ]
  },
  "hero": {
    "type": "image",
    "url": cover,
    "size": "full",
    "aspectRatio": "16:9",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://nav.cx/11S41K2"
    }
  },
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "contents": [
          {
            "type": "image",
           # "type": "image",
                                                    "url": "https://profile.line-scdn.net/" + str(pp),
                                                 #   "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    #"aspectMode": "cover",
                                                  #  "gravity": "bottom",
                                                    "size": "lg",
                                               #     "aspectRatio": "1:1",
          #  "aspectMode": "cover",
           # "aspectRatio": "4:3",
         #   "size": "sm",
            "gravity": "bottom"
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#FFFFFF"
                                            }, {
       #   }
    #    ]
     # },
    #  {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
                                                    "text":"NAME : {}".format(names),
                                                    "color": "#FFFFFF",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                    },{
                                                    "type": "text",
                                                    "text": status,
                                                    "color": "#FFFFFF",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                    "uri": "http://nav.cx/11S41K2",
       # "type": "button",
        #"action": {
         # "type": "uri",
          #"label": "KELUARGA",
        #  "uri": "http://nav.cx/11S41K2",
        }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["wcsti2"] == True:
              ginfo = achink.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["wc"]
              if msg != None:
                  contact = achink.getContact(achinkMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+'Kirim stiker','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
        if op.type == 25:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.to not in unsendchat:
                unsendchat[msg.to] = {}
            if msg_id not in unsendchat[msg.to]:
                unsendchat[msg.to][msg_id] = msg_id
            msgdikirim[msg_id] = {"text":text}
            to = msg.to
            isValid = True
            cmd = command(text)
            setkey = settings['keyCommand'].title()
            if settings['setKey'] == False: setkey = ''
            if isValid != False:
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    try:
                        if msg.to not in wait['Unsend']:
                            wait['Unsend'][msg.to] = {'B':[]}
                        if msg._from not in [achinkMID]:
                            return
                        wait['Unsend'][msg.to]['B'].append(msg.id)
                    except:pass
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != achinkMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and sender not in achinkMID:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if achinkMID in mention["M"]:
                                if to not in wait['ROM']:
                                    wait['ROM'][to] = {}
                                if msg._from not in wait['ROM'][to]:
                                    wait['ROM'][to][msg._from] = {}
                                if 'msg.id' not in wait['ROM'][to][msg._from]:
                                    wait['ROM'][to][msg._from]['msg.id'] = []
                                if 'waktu' not in wait['ROM'][to][msg._from]:
                                    wait['ROM'][to][msg._from]['waktu'] = []
                                wait['ROM'][to][msg._from]['msg.id'].append(msg.id)
                                wait['ROM'][to][msg._from]['waktu'].append(msg.createdTime)
                                autoresponuy(to,msg,wait)
                                break
                if msg._from not in achinkMID:
                  if apalo["talkban"] == True:
                    if msg._from in apalo["Talkblacklist"]:
                        achink.sendMention(to, "I said the fuck up @GuruTags:)","",[msg._from])
                        achink.kickoutFromGroup(msg.to, [msg._from])
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    if settings["notag"] == True:
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if achinkMID in mention["M"]:
                               achink.sendMention(to, "I said the fuck up @GuruTags:)","",[msg._from])
                               achink.kickoutFromGroup(msg.to, [msg._from])
                               break

                if 'MENTION' in msg.contentMetadata.keys() != None:
                    if temptag["stealtag"] == True:
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if achinkMID in mention["M"]:                      	
                                contact = achink.getContact(sender)
                                LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                                LINKVIDEO = "https://os.line.naver.jp/os/p/" + sender + "/vp"
                                data = {
                         "type": "flex",
                                    "altText": "respon tag",
                                    "contents": {
                                    "styles": {
                                    "header": {
                                    "backgroundColor":"#0000CD"
                                    },
                                    "body": {
                                    "backgroundColor": "#FFFFFF"
                                    },
                                    "footer": {
                                    "backgroundColor": "#0000CD"
                                    }
                                    },
           "type": "bubble",
           "header": {
           "type": "box",
           "layout": "horizontal",
           "contents": [
                              {
                              "type": "button",
                              "style": "secondary",
                              "color": "#FFFFFF",
                              "height": "sm",
                              "gravity": "center",
                              "flex": 1,
                              "action": {
                              "type": "uri",
                              "label": "RESPON TAG",
                              "uri": "http://nav.cx/11S41K2"
                          }
                     },
                ]
           },
           "body": {
           "type": "box",
           "layout": "horizontal",
           "spacing": "md",
           "contents": [
                              {
                               "type": "box",
                               "layout": "vertical",
                               "flex": 0,
                               "contents": [
                                                   {
                                                    "type": "image",
                                                    "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                                    "size": "lg",
                                                    "gravity": "bottom"
                                                   }
                                              ]
                                        }, 
                                  {
                                 "type": "separator",
                                 "color": "#000000"
                             },
                         {
                         "type": "box",
                         "layout": "vertical",
                         "flex": 2,
                         "contents": [
                                            {
                                             "type": "text",
                                             "text": "Hello {}".format(contact.displayName),
                                             "color": "#000000",
                                             "size": "sm",
                                             "weight": "bold",
                                             "flex": 3,
                                             "wrap": True,
                                             "gravity": "top"
                                             },{
                                             "type": "text",
                                             "text": "miss",
                                             "color": "#000000",
                                             "size": "sm",
                                             "weight": "bold",
                                             "flex": 3,
                                             "wrap": True,
                                             "gravity": "top"},{
                                             "type": "text",
                                             "text": "the trend is hot",
                                             "color": "#000000",
                                             "size": "sm",
                                             "weight": "bold",
                                             "flex": 3,
                                             "wrap": True,
                                             "gravity": "top"
                                           }
                                      ]
                                 }
                             ]
                         },
                         "footer": {
                         "type": "box",
                         "layout": "horizontal",
                         "contents": [
                                            {
                                             "type": "button",
                                             "style": "secondary",
                                             "color": "#FFFFFF",
                                             "height": "sm",
                                             "gravity": "center",
                                             "flex": 1,
                                             "action": {
                                             "type": "uri",
                                             "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                             "uri": "http://nav.cx/11S41K2",
                                             }
                                         },
                                     {
                                    "type": "spacer",
                                    "size": "sm",
                                 }
                             ],
                        "flex": 0
                    }
                }
            }
                                sendTemplate(to, data)
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    if msg.toType == 0:
                        if settings["autoRead"] == True:
                            achink.sendChatChecked(to, msg_id)
                    if msg.toType == 2:
                        if settings["autoRead1"] == True:
                            achink.sendChatChecked(to, msg_id)
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in clientMID:
                            try:
                                achink.kickoutFromGroup(msg.to,[sender])
                            except Exception as e:
                                 print(e)
                if msg.contentType == 4:
                    if norak["detectTemplate"] == True:
                        data = {
                            "type": "text",
                            "text": "Yeah, you know, that's template 🤔",
                            "sentBy": {
                                "label": "Detect Template",
                                "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),
                                "linkUrl": "https://line.me/ti/p/~" + achink.profile.userid
                            }
                        }
                        sendTemplate(to, data)
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != achinkMID: to = sender
                else: to = receiver
                if msg._from not in achinkMID:
                  if apalo["talkban"] == True:
                    if msg._from in apalo["Talkblacklist"]:
                        achink.sendMention(to, "Sorry u are banned from messaging @GuruTags :)","",[msg._from])
                        achink.kickoutFromGroup(msg.to, [msg._from])
                if msg.contentType == 13:
                  if apalo["Talkwblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          achink.sendMessage(msg.to,"Already available")
                          apalo["Talkwblacklist"] = False
                      else:
                          apalo["Talkblacklist"][msg.contentMetadata["mid"]] = True
                          apalo["Talkwblacklist"] = False
                          achink.sendMessage(msg.to,"Add this account to blacklist.")
                  if apalo["Talkdblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          del apalo["Talkblacklist"][msg.contentMetadata["mid"]]
                          achink.sendMessage(msg.to,"Add this account to white list")
                          apalo["Talkdblacklist"] = False
                      else:
                          apalo["Talkdblacklist"] = False
                          achink.sendMessage(msg.to,"Not in the Blacklist")
                if msg.contentType == 16:
                    if msg.toType in [2,1,0]:
                        print ("AutoLikeCommat")
                        try:
                            if settings["autolike"] == True:
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                if purl[1] not in wait['postId']:
                                    achink.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                    am = "『 ℓιкє ∂σиє』"
                                    data = {
                                           "type": "text",
                                           "text": "{}".format(str(am)),
                                           "sentBy": {
                                           "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                           "iconUrl": "https://drive.google.com/uc?export=download&id=1P9ldomhjBihks3JSWi0lDAM-wHbh4BmN",
                                           "uri": "http://nav.cx/11S41K2"
                                         }
                                     }
                                    sendTemplate(to, data)
                                if settings["com"] == True:
                                    achink.createComment(purl[0], purl[1], settings["commet"])  
                                    wait['postId'].append(purl[1])
                                else:
                                    pass
                        except Exception as e:
                                if settings["autolike"] == True:
                                    purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                                    if purl[1] not in wait['postId']:
                                        achink.likePost(msg._from, purl[1], random.choice([1001,1002,1003,1004,1005]))
                                    if settings["com"] == True:
                                        achink.createComment(msg._from, purl[1], settings["commet"])
                                        am = "『 LIKE DONE 』"
                                        data = {
                                           "type": "text",
                                           "text": "{}".format(str(am)),
                                           "sentBy": {
                                           "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                           "iconUrl": "https://raw.githubusercontent.com/achinkmaulana/png/master/1552389695781.jpg",
                                           "uri": "http://nav.cx/11S41K2"
                                          }
                                       }
                                        sendTemplate(to, data)
                                        wait['postId'].append(purl[1])
                                    else:pass
#================================================================================================
        if op.type == 25:
            print("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != achink.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "sp" or text.lower() == "speed":
                    start = time.time()
                    achink.sendMessage("testing...")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = "speed : %.3f sec" % (took)
                    data = {
                                           "type": "text",
                                           "text": "{}".format(str(a)),
                                           "sentBy": {
                                           "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                           "iconUrl": "https://drive.google.com/uc?export=download&id=1P9ldomhjBihks3JSWi0lDAM-wHbh4BmN",
                                           "uri": "http://nav.cx/11S41K2"
                                         }
                                     }
                    sendTemplate(to, data)
                elif "setname " in text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = achink.getProfile()
                        profile_A.displayName = string
                        achink.updateProfile(profile_A)
                        achink.sendMessage(msg.to,"Updated name to :\n" + string)
                elif "setbio " in msg.text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = achink.getProfile()
                        profile_A.statusMessage = string
                        achink.updateProfile(profile_A)
                        achink.sendMessage(msg.to,"Succes Update :\n" + string)
                elif msg.text.lower().startswith("block "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = achink.getContact(ls)
                                    achink.blockContact(ls)
                                achink.generateReplyMessage(msg.id)
                                achink.sendReplyMessage(msg.id, to, "Sukses menabahkan  " + str(contact.displayName) + " ke Blocklist")
                elif text.lower() == "gantipotogroup":
                    if msg.toType == 2:
                        if to not in sets["changeGroupPicture"]:
                            sets["changeGroupPicture"].append(to)
                        achink.sendMessage(to, "send pic.....")
                elif msg.text.lower().startswith("picc "):
                                query = removeCmd("poto", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "sendImage",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif text.lower() == 'gcreator' or text.lower() == "gc":
                    group = achink.getGroup(to)
                    cg = group.creator
                    c = cg.mid
                    name = cg.displayName
                    pp = cg.pictureStatus
                    data = {
                                  "type": "flex",
                                    "altText": "MENU HELP",
                                    "contents": {
                                    "styles": {
                                    "header": {
                                    "backgroundColor":"#0000CD"
                                     },
                                     "body": {
                                     "backgroundColor": "#000000"
                                      },
                                      "footer": {
                                      "backgroundColor": "#0000CD"
                                    }
                                },
    "type": "bubble",
    "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
                       {
                       "type": "button",
                       "style": "secondary",
                       "color": "#FFFFFF",
                       "height": "sm",
                       "gravity": "center",
                       "flex": 1,
                       "action": {
                       "type": "uri",
                       "label": "◦•●◉✿ 𝐆𝐑𝐎𝐔𝐏 𝐂𝐑𝐄𝐀𝐓𝐎𝐑 ✿◉●•◦",
                       "uri": "http://nav.cx/11S41K2"
                  }
           },
       ]
  },
  "body": {
  "type": "box",
  "layout": "horizontal",
  "spacing": "md",
  "contents": [
                    {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "contents": [
                                       {
                                        "type": "image",
                                        "url": "https://profile.line-scdn.net/" + str(pp),
                                        "size": "lg",
                                        "gravity": "bottom"
                                     }
                                 ]
                            }, 
                        {
                       "type": "separator",
                       "color": "#FFFFFF"
                   }, 
               {
              "type": "box",
              "layout": "vertical",
              "flex": 2,
              "contents": [
                                  {
                                    "type": "text",
                                    "text":"INFO OF GCREATOR",
                                    "color": "#FFFFFF",
                                    "size": "sm",
                                    "weight": "bold",
                                    "flex": 1,
                                    "wrap": True,
                                    "gravity": "top"
                                   },
                                   {
                                    "type": "separator",
                                    "color": "#FFFFFF"
                                    }, 
                                    {
                                     "type": "text",
                                     "text": name,
                                     "color": "#FFFFFF",
                                     "size": "sm",
                                     "weight": "bold",
                                     "flex": 6,
                                     "wrap": True,
                                     "gravity": "top"
                                 }
                             ]
                         }
                      ]
                   },
                   "footer": {
                   "type": "box",
                   "layout": "horizontal",
                   "contents": [
                                       {
                                       "type": "button",
                                       "style": "secondary",
                                       "color": "#FFFFFF",
                                       "height": "sm",
                                       "gravity": "center",
                                       "flex": 1,
                                       "action": {
                                       "type": "uri",
                                       "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                       "uri": "http://nav.cx/11S41K2",
                                        }
                                        },
                                        {
                                       "type": "spacer",
                                       "size": "sm",
                                    }
                                 ],
                               "flex": 0
                            }
                        }
                    }
                    sendflex(to, data)
                    achink.sendContact(to, c)
                elif msg.text.lower().startswith("yt"):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "styles": {
                                            "header": {
                                                "backgroundColor": "#FF0000"
                                            },
                                            "body": {
                                               "backgroundColor": "#DAA520",
                                               "separator": True,
                                               "separatorColor": "#000000"
                                            },
                                            "footer": {
                                                "backgroundColor": "#FF0000",
                                                "separator": True,
                                               "separatorColor": "#EE1289"
                                           }
                                        },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                               {
                                               "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#0000CD",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "YOUTUBE MEDIA",
                                                        "uri": "https://line.me/ti/p/~" + achink.profile.userid
                                                }
                                            }]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/ti/p/~" + achink.profile.userid
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    "url": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),
                                                 #   "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "sm",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#EE1289"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "Title",
                                                    "color": "#0000CD",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#FFFFFF",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#0000CD",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Page",
                                                        "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#0000CD",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#0000CD",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "type": "flex",
                                        "altText": "Youtube",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                    }
                                    sendTemplate(to, data)
                if text.lower() == "bc info":
                    sa="this is how to use broadcast"
                    sa+="\n-Announcement message / ID line"
                    sa+="\n-example> <"
                    sa+="\n-bc/aboutme.."
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == "fireword info":
                    sa = "How to use firewords> <"
                    sa += "\n-setfireword: reply"
                    sa += "\nexample"
                    sa += "\n- your set :why am i"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == "stag":
                    sa = "Cara menggunakan rusa jantan"
                    sa += "\n@user rusa [nomor] @ user"
                    sa += "\nContoh"
                    sa += "\nstag 1 @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u266f0d1211f905b2ca386024d9d4e165"}}
                    sendTemplate(to,data)
                if text.lower() == "Mantra":
                    sa = "Cara menggunakan ejaan"
                    sa += "\n- stags [pesan] @ user"
                    sa += "\nContoh"
                    sa += "\n- set bocah ngapaya @user "
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u266f0d1211f905b2ca386024d9d4e165"}}
                    sendTemplate(to,data)
                if text.lower() == ".set" or text.lower() == "set":
                    sas = "𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒"
                    if settings["autoAdd"] == True: sa = "\n• ☑️ Autoadd「ON」"
                    else:sa = "\n• ❎ Autoadd「OFF」"
                    if settings["autoblock"] == True: sa += "\n• ☑️ AutoBlock「ON」"
                    else:sa += "\n• ❎ AutoBlock「OFF」"
                    if sets["autoCancel"]["on"] == True: sa +="\n•️ ☑️ Autocancel: " + str(sets["autoCancel"]["members"])
                    else:sa += "\n• ❎ Autocancel「OFF」"
                    if tagadd["tags"] == True: sa += "\n•️ ☑️ Autorespon「ON」"
                    else:sa += "\n• ❎ Autorespon「OFF」"
                    if tagadd["tagss"] == True: sa += "\n• ☑️ Autorespon2「ON」"
                    else:sa += "\n• ❎ Autorespon2「OFF」"
                    if sets["tagsticker"] == True: sa += "\n•️ ☑️ Autoresponsticker「ON」"
                    else:sa += "\n• ❎ Autoresponsticker「OFF」"
                    if settings["autolike"] == True: sa += "\n• ☑️ Autolike「ON」"
                    else:sa += "\n• ❎ Autolike「OFF」"
                    if settings["com"] == True: sa += "\n• ☑️ Com「ON」"
                    else:sa += "\n• ❎ Com「OFF」"
                    if settings["Welcome"] == True: sa += "\n• ☑️ Welcome「ON」"
                    else:sa += "\n• ❎ Welcame「OFF」"
                    if settings["Wc"] == True: sa += "\n• ☑️ Welcome2 「ON」"
                    else:sa += "\n•️ ❎ Welcome2「OFF」"
                    if settings["wcsti2"] == True: sa += "\n• ☑️ Welcomesticker 「ON」"
                    else:sa += "\n• ❎ Welcomesticker「OFF」"
                    if settings["Leave"] == True: sa += "\n• ☑️ Responleave 「ON」"
                    else:sa += "\n• ❎ Responleave「OFF」"
                    if settings["lv"] == True: sa += "\n• ☑️ Autoadd「ON」"
                    else:sa += "\n• ❎ Autoadd「OFF」"
                    if settings["unsendMessage"] == True: sa += "\n• ☑️ Unsend「ON」"
                    else:sa += "\n•️ ❎ Unsend「OFF」"
                    if settings["Sticker"] == True: sa += "\n• ☑️  Sticker 「ON」"
                    else:sa += "\n• ❎ Sticker「OFF」"
                    if sets["Sticker"] == True: sa += "\n• ☑️ Setsticker「ON」"
                    else:sa += "\n• ❎ Setsticker「OFF」"
                    data = {
                            "type": "flex",
                                    "altText": "SET BOT",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#9400D3"
                                        },
                                        "body": {
                                        "backgroundColor": "#2F4F4F"
                                        },
                                        "footer": {
                                          "backgroundColor": "#9400D3"
                                        }
                                        },
                "type": "bubble",
                "header": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                                   {
                                   "type": "button",
                                   "style": "secondary",
                                   "color": "#FFFFFF",
                                   "height": "sm",
                                   "gravity": "center",
                                   "flex": 1,
                                   "action": {
                                                  "type": "uri",
                                                  "label": "SET BOT",
                                                  "uri": "http://nav.cx/11S41K2"
                                                 }
                                              },
                                           ]
                                        },
                            "hero": {
                            "type": "image",
                            "url": "https://drive.google.com/uc?export=download&id=1-5RUY4pS_OASV42FXtkGLFIViTL6NHEo",
                    #        "url": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),
                            "size": "full",
                        #    "aspectRatio": "1:1",
                        #    "aspectMode": "fit",
                          "aspectRatio": "16:9",
                          "aspectMode": "cover",
                           "action": {
                                          "type": "uri",
                                          "uri": "http://nav.cx/11S41K2"
                                        }
                                     },
                        "body": {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "md",
                        "contents": [
                                           {
                                            "type": "box",
                                            "layout": "vertical",
                                            "flex": 1,
                                            "contents": [
                                                               {
                                                                "text":"{}".format(str(sa)),
                                                                "size": "sm",
                                                                "margin": "none",
                                                                "color": "#FFFFFF",
                                                                "wrap": True,
                                                                "weight": "regular",
                                                                "type": "text"
                                                                }
                                                             ]
                                                         }
                                                     ]
                                                 },
                                  "footer": {
                                  "type": "box",
                                  "layout": "horizontal",
                                  "contents": [
                                                     {
                                                      "type": "button",
                                                      "style": "secondary",
                                                      "color": "#FFFFFF",
                                                      "height": "sm",
                                                      "gravity": "center",
                                                      "flex": 1,
                                                      "action": {
                                                                      "type": "uri",
                                                                      "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                                                      "uri": "http://nav.cx/11S41K2",
                                                                      }
                                                                  },
                                                              {
                                                         "type": "spacer",
                                                      "size": "sm",
                                                 }
                                            ],
                                       "flex": 0
                                   }
                               }
                            }
                    sendflex(to, data)
                elif cmd == "vvirus":
                       helpMessage2 = infomeme()
                       achink.sendMessage(msg.to, str(helpMessage2))
                elif cmd == "steal":
                            ret = "  • Pict [@]\n"
                            ret += "  • Cover [@]\n"
                            ret += "  • Profile [@]\n"
                            ret += "  • Video [@]\n"
                            ret += "  • Name [@]\n"
                            ret += "  • Bio [@]\n"
                            ret += "  • Contact [@]\n"
                            ret += "  • Clone [@]\n"
                            ret += "  • Unclone\n"
                            ret += "  • Mid [@]"
                            hello = "{}".format(str(ret))
                            data = {
                                    "type": "flex",
                                    "altText": "STEAL",
                                        "contents": {
                                        "styles": {
                                        "body": {
                                        "backgroundColor": "#800000"
                                        },
                                        "footer": {
                                          "backgroundColor": "#DAA520"
                                        }
                                        },
                                            "type": "bubble",
                                                "hero": {
                                                    "type": "image",
                                                    "url": "https://raw.githubusercontent.com/achinkmaulana/png/master/1552388441041.jpg",
                                                    "size": "full",
                                                    "aspectRatio": "1:1",
                                                    "aspectMode": "fit",
                                                },
                                            "body": {
                                            "contents": [
                                              {
                                                "contents": [
                                                  {
                                                    "text": "[ SET STEAL ]",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#00BFFF",
                                                    "wrap": True,
                                                    "weight": "bold",
                                                    "type": "text"
                                                  }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#FFFFFF"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "contents": [
                                                      {
                                                        "text":"{}".format(str(ret)),
                                                        "size": "sm",
                                                        "margin": "none",
                                                        "color": "#00FF00",
                                                        "wrap": True,
                                                        "weight": "regular",
                                                        "type": "text"
                                                      }
                                                    ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                                  }
                                                ],          
                                                "type": "box",
                                                "layout": "vertical"
                                              }
                                            ],
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "vertical"
                                        },
                                        "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                                    "uri": "http://nav.cx/11S41K2",
                                                }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                            sendflex(to, data)
                elif cmd == "spam":
                         #   ret = "    [ Type Spamming ]\n\n"
                            ret = " ★ Spam Text\n"
                            ret += " ★ Spam 1 [1][enter|text]\n"
                            ret += " ★ Spam Gift\n"
                            ret += " ★ Spam 2 [1][@|]\n"
                            ret += " ★ Spam Contact\n"
                            ret += " ★ Spam 3 [1][@]\n"
                            ret += " ★ Spam Mention\n"
                            ret += " ★ Spam 4 [1][@]"
                            hello = "{}".format(str(ret))
                            data = {
                                        "type": "flex",
                                        "altText": "Message",
                                        "contents": {
                                        "type": "bubble", 
                                        "hero": {
                                        "type": "image",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover",
                                        "url": "https://raw.githubusercontent.com/achinkmaulana/png/master/1552388441041.jpg",
                                        "size": "full",
                                        "margin": "xxl"
                                    #    "type": "bubble",
                                    #    "styles": {
                                     #       "body": {
                                         #   "backgroundColor": '#000000'
                          #      },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Type Spaming",
                                        "color": "#000000",
                                        "align": "center",
                                        "weight": "bold",
                                        "size": "xxl"
                                         },
                                        {
                                          "type": "separator",
                                          "color": "#000000"
                                         },
                                         {
                                                "type": "text",
                                                "text": "{}".format(str(ret)),
                                                "wrap": True,
                                                "color": "#000000",
                                                "gravity": "center",
                                                "size": "md"
                                                },
                                                {
                                                "type": "separator",
                                                 "color": "#000000"
                                                },
                                            ]
                                       },
                                  }
                             }
                            sendTemplate(to, data)
                elif cmd == "feature":
                            ret = "  ◼️     Image [text]\n"
                            ret += "  ◼️     Drawwindow [text]\n"
                            ret += "  ◼️     Drawlight [text]\n"
                            ret += "  ◼️     Drawsoupletters [text]\n"
                            ret += "  ◼️     Drawcookies [text]\n"
                            ret += "  ◼️     Themes [query]\n"
                            ret += "  ◼️     Stickers [query]\n"
                            ret += "  ◼️     Goimage2 [text]\n"
                            ret += "  ◼️     Instagram2 [text]\n"
                            ret += "  ◼️     Devianart [text]\n"
                            ret += "  ◼️     Food2 [text]\n"
                            ret += "  ◼️     Calc [num]\n"
                            ret += "  ◼️     Urban [query]\n"
                            ret += "  ◼️     Randomname\n"
                            ret += "  ◼️     Anitoki\n"
                            ret += "  ◼️     Cinema xx1\n"
                            ret += "  ◼️     Bitcoin\n"
                            ret += "  ◼️     Creepypasta\n"
                            ret += "  ◼️     Kaskus [query]\n"
                            ret += "  ◼️     Arti-NAME [NAME]\n"
                            ret += "  ◼️     Cosplay [name]\n"
                            ret += "  ◼️     Viloid [name]\n"
                            ret += "  ◼️     Zodiac [query]\n"
                            ret += "  ◼️     Zalgo [name]\n"
                            ret += "  ◼️     Webtoon\n"
                            ret += "  ◼️     Youtubemp4 [URL]\n"
                            ret += "  ◼️     Youtubemp3 [URL]\n"
                            ret += "  ◼️     Youtubelink [text]\n"
                            ret += "  ◼️     Fileytmp3 [URL]\n"
                            ret += "  ◼️     Video [query]\n"
                            ret += "  ◼️     Fileytmp4 [URL]\n"
                            ret += "  ◼️     Google [text]\n"
                            ret += "  ◼️     Wikipedia [text]\n"
                            ret += "  ◼️     Topnews\n"
                            ret += "  ◼️     Tvschedule\n"
                            ret += "  ◼️     Doujinnews\n"
                            ret += "  ◼️     Quran\n"
                            ret += "  ◼️     Githubprofile [username]\n"
                            ret += "  ◼️     Githubfollowing [username]\n"
                            ret += "  ◼️     Githubfollowers [username]\n"
                            ret += "  ◼️     Githubrepo [username]\n"
                            ret += "  ◼️     Githuzip [name|name]\n"
                            ret += "  ◼️     Fmylife\n"
                            ret += "  ◼️     Single\n"
                            ret += "  ◼️     Motivate"
                            hello = "{}".format(str(ret))
                            data = {
                            "type": "flex",
                                    "altText": "type bc",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#000000"
                                        },
                                        "body": {
                                        "backgroundColor": "#DCDCDC"
                                        },
                                        "footer": {
                                          "backgroundColor": "#000000"
                                        }
                                        },
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "SEARCH GOOGLE",
                                    "uri": "http://nav.cx/11S41K2"
      }
      },
    ]
  },
#  "hero": {
 #   "type": "image",
  #  "url": "https://raw.githubusercontent.com/achinkmaulana/png/master/google_PNG19636.png",
   # "size": "full",
    #"aspectRatio": "1:1",
 #   "aspectMode": "fit",
  #  "aspectRatio": "20:13",
   # "aspectMode": "cover",
#    "action": {
 #     "type": "uri",
  #    "uri": "http://nav.cx/11S41K2"
   # }
  #},
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "contents": [
          {
            "type": "image",
           # "type": "image",
                                                    "url": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),
                                                 #   "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    #"aspectMode": "cover",
                                                  #  "gravity": "bottom",
                                                    "size": "lg",
                                               #     "aspectRatio": "1:1",
          #  "aspectMode": "cover",
           # "aspectRatio": "4:3",
         #   "size": "sm",
            "gravity": "bottom"
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#0000CD"
                                            }, {
       #   }
    #    ]
     # },
    #  {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
                                                    "text":"{}".format(str(ret)),
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "MODE DESTOP",
                                    "uri": "http://nav.cx/11S41K2",
       # "type": "button",
        #"action": {
         # "type": "uri",
          #"label": "KELUARGA",
        #  "uri": "http://nav.cx/11S41K2",
        }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                            sendflex(to, data)
                
                elif cmd.startswith("flex "):
                            sep = text.split(" ")
                            pesan = text.replace(sep[0] + " ","")
                            data = {
                                "type": "flex",
                                "altText": "flex",
                                "contents": {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(pesan),
                                                "wrap": True,
                                                "align": "start",
                                                "gravity": "center",
                                                "size": "sm"
                                            },
                                        ]
                                    }
                                }
                            }
                            sendTemplate(to, data)
                
                elif cmd == ".typebc":
                           # ret = "Type: Broadcast\n\n"
                            ret = "  • Gbroadcast\n"
                            ret += "  • Fbroadcast\n"
                            ret += "  • Allbroadcast\n"
                            ret += "  • Groupcastvoice\n"
                            ret += "  • Friendcastvoice"
                            hello = "{}".format(str(ret))
                            cu = achink.getProfileCoverURL(achinkMID)
                            image = str(cu)
                            data = {
                            "type": "flex",
                                    "altText": "type bc",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#0000CD"
                                        },
                                        "body": {
                                        "backgroundColor": "#000000"
                                        },
                                        "footer": {
                                          "backgroundColor": "#0000CD"
                                        }
                                        },
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "BROADCAST",
                                    "uri": "http://nav.cx/11S41K2"
      }
      },
    ]
  },
#  "hero": {
#    "type": "image",
 #   "url": "https://files.boteater.net/jpg-kji9di06.jpg",
  #  "size": "full",
#    "aspectRatio": "1:1",
 #   "aspectMode": "fit",
  #  "aspectRatio": "20:13",
   # "aspectMode": "cover",
 #   "action": {
  #    "type": "uri",
   #   "uri": "http://nav.cx/11S41K2"
 #   }
  #},
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "contents": [
          {
            "type": "image",
           # "type": "image",
                                                    "url": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),
                                                 #   "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    #"aspectMode": "cover",
                                                  #  "gravity": "bottom",
                                                    "size": "lg",
                                               #     "aspectRatio": "1:1",
          #  "aspectMode": "cover",
           # "aspectRatio": "4:3",
         #   "size": "sm",
            "gravity": "bottom"
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#FFFFFF"
                                            }, {
       #   }
    #    ]
     # },
    #  {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
                                                    "text":"{}".format(str(ret)),
                                                    "color": "#FFFFFF",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                    "uri": "http://nav.cx/11S41K2",
       # "type": "button",
        #"action": {
         # "type": "uri",
          #"label": "KELUARGA",
        #  "uri": "http://nav.cx/11S41K2",
        }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                            sendflex(to, data)
                
                
                elif cmd.startswith("song "):
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                            data = r.text
                            data = json.loads(data)
                            b = data
                            c = str(b["title"])
                            d = str(b["singer"])
                            e = str(b["url"])
                            g = str(b["image"])
                            hasil = "Singer: "+str(d)
                            hasil += "\nTITLE : "+str(c)
                            data = {
                            "type": "flex",
                                    "altText": "MENU HELP",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#0000CD"
                                        },
                                        "body": {
                                        "backgroundColor": "#000000"
                                        },
                                        "footer": {
                                          "backgroundColor": "#0000CD"
                                        }
                                        },
                                        "type": "bubble",
                                        "header": {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                                           {
                                                            "type": "button",
                                                            "style": "secondary",
                                                            "color": "#FFFFFF",
                                                            "height": "sm",
                                                            "gravity": "center",
                                                            "flex": 1,
                                                            "action": {
                                                            "type": "uri",
                                                            "label": "SONG SEARCH",
                                                            "uri": "http://nav.cx/11S41K2"
                                                            }
                                                          },
                                                       ]
                                                   },
                                                   "body": {
                                                   "type": "box",
                                                   "layout": "horizontal",
                                                   "spacing": "md",
                                          "contents": [
                                          {
                                          "type": "box",
                                          "layout": "vertical",
                                          "flex": 0,
                                   "contents": [
                                   {
                                    "type": "image",
                                    "url": g,
                                    "gravity": "bottom"
                                    }
                                  ]
                               }, 
                            {
                             "type": "separator",
                             "color": "#FFFFFF"
                              }, 
                             {
                             "type": "box",
                             "layout": "vertical",
                             "flex": 2,
                      "contents": [
                      {
                       "type": "text",
                       "text": hasil,
                       "color": "#FFFFFF",
                       "size": "sm",
                       "weight": "bold",
                      "flex": 3,
                      "wrap": True,
                     "gravity": "top"
                    }
                  ]
               }
            ]
         },
        "footer": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                                           {
                                             "type": "button",
                                             "style": "secondary",
                                             "color": "#FFFFFF",
                                             "height": "sm",
                                             "gravity": "center",
                                             "flex": 1,
                                             "action": {
                                             "type": "uri",
                                             "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                             "uri": "http://nav.cx/11S41K2",
                                            }
                                          },
                                        {
                                           "type": "spacer",
                                           "size": "sm",
                                         }
                                       ],
                                    "flex": 0
                                   }
                                }
                            }
                            sendTemplate(to, data)
                            achink.sendAudioWithURL(to,e)
                            achink.sendMessage(to, "error\n" + str(error))
                elif cmd.startswith("broadcast "):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            groups = achink.getGroupIdsJoined()
                            for gr in groups:
                            	data = {
                            "type": "flex",
                                    "altText": " info",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#0000CD"
                                        },
                                        "body": {
                                        "backgroundColor": "#000000"
                                        },
                                        "footer": {
                                          "backgroundColor": "#0000CD"
                                        }
                                        },
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "BROADCAST",
                                    "uri": "http://nav.cx/11S41K2"
      }
      },
    ]
  },
#  "hero": {
#    "type": "image",
 #   "url": "https://files.boteater.net/jpg-kji9di06.jpg",
  #  "size": "full",
#    "aspectRatio": "1:1",
 #   "aspectMode": "fit",
  #  "aspectRatio": "20:13",
   # "aspectMode": "cover",
 #   "action": {
  #    "type": "uri",
   #   "uri": "http://nav.cx/11S41K2"
 #   }
  #},
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "contents": [
          {
            "type": "image",
           # "type": "image",
                                                    "url": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),
                                                 #   "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    #"aspectMode": "cover",
                                                  #  "gravity": "bottom",
                                                    "size": "lg",
                                               #     "aspectRatio": "1:1",
          #  "aspectMode": "cover",
           # "aspectRatio": "4:3",
         #   "size": "sm",
            "gravity": "bottom"
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#FFFFFF"
                                            }, {
       #   }
    #    ]
     # },
    #  {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
                                                    "text": "{}".format(text),
                                                    "color": "#FFFFFF",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                    "uri": "http://nav.cx/11S41K2",
       # "type": "button",
        #"action": {
         # "type": "uri",
          #"label": "KELUARGA",
        #  "uri": "http://nav.cx/11S41K2",
        }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                            bcTemplate(gr, data)
                elif cmd == "reject" and sender == achinkMID:
                            if msg.toType == 2:
                                group = achink.getGroup(to)
                                if group.invitee is None or group.invitee == []:
                                    achink.sendMessage(to, "There is no refinement")
                                else:
                                    invitee = [contact.mid for contact in group.invitee]
                                    for inv in invitee:
                                        achink.cancelGroupInvitation(to, [inv])
                                        time.sleep(1)
                                    achink.sendMessage(to, "Succes canceled 「 {} 」user".format(str(len(invitee))))
                elif cmd == "cleanthis":
                            if msg.toType == 2:
                                group = achink.getGroup(to)
                                gMembers = [contact.mid for contact in group.members]
                                for i in gMembers:
                                    time.sleep(0.008)
                                    achink.kickoutFromGroup(to,[i])
                                achink.sendMessage(to,"Just Some Casual Cleasing")
                            else:
                                achink.sendMessage(to,"failed >_<")
                elif cmd == "memelist":
                            f = open('memeGen.txt','r')
                            lines = f.readlines()
                            panjang = len(lines)
                            lists = ""
                            for a in lines:
                                lists += str(a)
                            achink.sendMessage(to,"Template List :\n%s" %(lists))
                elif cmd.startswith('.set1 autolike comment ') and sender == achinkMID:
                            name = removeCmd(".set1 autolike comment",text)
                            wait["autoLike"]['comment'] = str(name)
                            achink.sendMessage(to,"「 AutoLike 」\nAutoLike message has been set to:\n" + wait["autoLike"]['comment'])
                elif cmd == "clearchat" and sender == achinkMID:
                            achink.removeAllMessages(op.param2)
                            achink.generateReplyMessage(msg.id)
                            achink.sendReplyMessage(msg.id, to, "Chat di bersihkan")

                elif cmd.startswith("bguru "):
                    separate = text.split(" ")
                    id = text.replace(separate[0] + " ","")
                    cond = id.split("|")
                    search = str(cond[0])
                    gifnya = ["{}".format(search)]
                    data = {
                        "type": "template",
                        "altText": "{} sent a sticker.".format(achink.getProfile().displayName),
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "full",
                                     "action": {
                                         "type": "uri",
                                          "uri": "http://nav.cx/11S41K2"
                                     }
                                }
                            ]
                        }
                    }                    
                    achink.unsendMessage(msg.id)
                    sendTemplate(to, data)                                        
                    time.sleep(1)
                    
                elif cmd.startswith("bsticker "):
                        separate = text.split(" ")
                        id = text.replace(separate[0] + " ","")
                        cond = id.split("|")
                        search = str(cond[0])
                        data = {
                            "type": "template",
                            "altText": "BIG STICKER",
                            "baseSize": {
                                "height": 1040,
                                "width": 1040
                            },
                            "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png".format(search),
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                            }
                        }
                        sendTemplate(to, data)
                        
                elif cmd == "randomtiktok":
                            contact = achink.getContact(sender)
                            data = {
                                "type": "video",
                                "originalContentUrl": "https://rest.farzain.com/api/tiktok.php?apikey=fn",
                                "previewImageUrl": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                }
                            sendTemplate(to, data)
                
                elif cmd.startswith("pic "):
                                query = removeCmd("food", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []                                	
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1562242036-RW04okm?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "I'm hungry",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif cmd == "media":
                            ret = "◽ song [ TITLE ]\n"
                            ret += "◽ Smule [ id ]\n"
                            ret += "◽ Yt [ TITLE ]\n"
                            ret += "◽ Youtube [ TITLE ]\n"
                            ret += "◽ Playstore [ NAME app ]\n"
                            ret += "◽ Image [ NAME ]\n"
                            ret += "◽ pic [ NAME ]\n"
                            ret += "◽ Memelist\n"
                            ret += "◽ Randomtiktok\n"
                            ret += "◽ Random\n"
                            ret += "◽ Food [ TITLE ]\n"
                            data = {
                            "type": "flex",
                                    "altText": "MEDIA",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#9400D3"
                                        },
                                        "body": {
                                        "backgroundColor": "#2F4F4F"
                                        },
                                        "footer": {
                                          "backgroundColor": "#9400D3"
                                        }
                                        },
                "type": "bubble",
                "header": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                                   {
                                   "type": "button",
                                   "style": "secondary",
                                   "color": "#FFFFFF",
                                   "height": "sm",
                                   "gravity": "center",
                                   "flex": 1,
                                   "action": {
                                                  "type": "uri",
                                                  "label": "MENU HELP",
                                                  "uri": "http://nav.cx/11S41K2"
                                                 }
                                              },
                                           ]
                                        },
                            "hero": {
                            "type": "image",
                            "url": "https://drive.google.com/uc?export=download&id=1-5RUY4pS_OASV42FXtkGLFIViTL6NHEo",
                    #        "url": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),
                            "size": "full",
                        #    "aspectRatio": "1:1",
                        #    "aspectMode": "fit",
                          "aspectRatio": "16:9",
                          "aspectMode": "cover",
                           "action": {
                                          "type": "uri",
                                          "uri": "http://nav.cx/11S41K2"
                                        }
                                     },
                        "body": {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "md",
                        "contents": [
                                           {
                                            "type": "box",
                                            "layout": "vertical",
                                            "flex": 1,
                                            "contents": [
                                                               {
                                                                "text":"{}".format(str(ret)),
                                                                "size": "sm",
                                                                "margin": "none",
                                                                "color": "#FFFFFF",
                                                                "wrap": True,
                                                                "weight": "regular",
                                                                "type": "text"
                                                                }
                                                             ]
                                                         }
                                                     ]
                                                 },
                                  "footer": {
                                  "type": "box",
                                  "layout": "horizontal",
                                  "contents": [
                                                     {
                                                      "type": "button",
                                                      "style": "secondary",
                                                      "color": "#FFFFFF",
                                                      "height": "sm",
                                                      "gravity": "center",
                                                      "flex": 1,
                                                      "action": {
                                                                      "type": "uri",
                                                                      "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                                                      "uri": "http://nav.cx/11S41K2",
                                                                      }
                                                                  },
                                                              {
                                                         "type": "spacer",
                                                      "size": "sm",
                                                 }
                                            ],
                                       "flex": 0
                                   }
                               }
                            }
                            sendflex(to, data)
                elif cmd == "kick":
                            ret = "◽ Kick [ @ ]\n"
                            ret += "◽ cleanthjs\n"
                            ret += "◽ Nuke\n"
                            ret += "◽ Bypass\n"
                            ret += "◽ Cancelall"
                            data = {
                            "type": "flex",
                                    "altText": "MENU KICK",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#9400D3"
                                        },
                                        "body": {
                                        "backgroundColor": "#2F4F4F"
                                        },
                                        "footer": {
                                          "backgroundColor": "#9400D3"
                                        }
                                        },
                "type": "bubble",
                "header": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                                   {
                                   "type": "button",
                                   "style": "secondary",
                                   "color": "#FFFFFF",
                                   "height": "sm",
                                   "gravity": "center",
                                   "flex": 1,
                                   "action": {
                                                  "type": "uri",
                                                  "label": "KICK COMMAND",
                                                  "uri": "http://nav.cx/11S41K2"
                                                 }
                                              },
                                           ]
                                        },
                            "hero": {
                            "type": "image",
                            "url": "https://drive.google.com/uc?export=download&id=1-5RUY4pS_OASV42FXtkGLFIViTL6NHEo",
                    #        "url": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),
                            "size": "full",
                        #    "aspectRatio": "1:1",
                        #    "aspectMode": "fit",
                          "aspectRatio": "16:9",
                          "aspectMode": "cover",
                           "action": {
                                          "type": "uri",
                                          "uri": "http://nav.cx/11S41K2"
                                        }
                                     },
                        "body": {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "md",
                        "contents": [
                                           {
                                            "type": "box",
                                            "layout": "vertical",
                                            "flex": 1,
                                            "contents": [
                                                               {
                                                                "text":"{}".format(str(ret)),
                                                                "size": "sm",
                                                                "margin": "none",
                                                                "color": "#FFFFFF",
                                                                "wrap": True,
                                                                "weight": "regular",
                                                                "type": "text"
                                                                }
                                                             ]
                                                         }
                                                     ]
                                                 },
                                  "footer": {
                                  "type": "box",
                                  "layout": "horizontal",
                                  "contents": [
                                                     {
                                                      "type": "button",
                                                      "style": "secondary",
                                                      "color": "#FFFFFF",
                                                      "height": "sm",
                                                      "gravity": "center",
                                                      "flex": 1,
                                                      "action": {
                                                                      "type": "uri",
                                                                      "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                                                      "uri": "http://nav.cx/11S41K2",
                                                                      }
                                                                  },
                                                              {
                                                         "type": "spacer",
                                                      "size": "sm",
                                                 }
                                            ],
                                       "flex": 0
                                   }
                               }
                            }
                            sendflex(to, data)
                elif cmd == "settings":
                            ret = "◽ Autojoin on/off\n"
                            ret += "◽ Autoblock on/off\n"
                            ret += "◽ Autolike on/off\n"
                            ret += "◽ Stealtag on/off\n"
                            ret += "◽ Autocomment on/off\n"
                            ret += "◽ Autojointicket on/off\n"
                            ret += "◽ Responkick on/off\n"
                            ret += "◽ Chatbot on/off\n"
                            ret += "◽ Unsend on/off\n"
                            ret += "◽ Prokick on/off\n"
                            ret += "◽ Procancel on/off\n"
                            ret += "◽ Proinvite on/off\n"
                            ret += "◽ Proqr on/off\n"
                            ret += "◽ Allpro on/off\n"
                            ret += "◽ NAME [ text ]\n"
                            ret += "◽ Bio [ text ]\n"
                            ret += "◽ Autocancel on/off"
                            data = {
                            "type": "flex",
                                    "altText": "SETTINGS",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#9400D3"
                                        },
                                        "body": {
                                        "backgroundColor": "#2F4F4F"
                                        },
                                        "footer": {
                                          "backgroundColor": "#9400D3"
                                        }
                                        },
                "type": "bubble",
                "header": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                                   {
                                   "type": "button",
                                   "style": "secondary",
                                   "color": "#FFFFFF",
                                   "height": "sm",
                                   "gravity": "center",
                                   "flex": 1,
                                   "action": {
                                                  "type": "uri",
                                                  "label": "KICK COMMAND",
                                                  "uri": "http://nav.cx/11S41K2"
                                                 }
                                              },
                                           ]
                                        },
                            "hero": {
                            "type": "image",
                            "url": "https://drive.google.com/uc?export=download&id=1-5RUY4pS_OASV42FXtkGLFIViTL6NHEo",
                    #        "url": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),
                            "size": "full",
                        #    "aspectRatio": "1:1",
                        #    "aspectMode": "fit",
                          "aspectRatio": "16:9",
                          "aspectMode": "cover",
                           "action": {
                                          "type": "uri",
                                          "uri": "http://nav.cx/11S41K2"
                                        }
                                     },
                        "body": {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "md",
                        "contents": [
                                           {
                                            "type": "box",
                                            "layout": "vertical",
                                            "flex": 1,
                                            "contents": [
                                                               {
                                                                "text":"{}".format(str(ret)),
                                                                "size": "sm",
                                                                "margin": "none",
                                                                "color": "#FFFFFF",
                                                                "wrap": True,
                                                                "weight": "regular",
                                                                "type": "text"
                                                                }
                                                             ]
                                                         }
                                                     ]
                                                 },
                                  "footer": {
                                  "type": "box",
                                  "layout": "horizontal",
                                  "contents": [
                                                     {
                                                      "type": "button",
                                                      "style": "secondary",
                                                      "color": "#FFFFFF",
                                                      "height": "sm",
                                                      "gravity": "center",
                                                      "flex": 1,
                                                      "action": {
                                                                      "type": "uri",
                                                                      "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                                                      "uri": "http://nav.cx/11S41K2",
                                                                      }
                                                                  },
                                                              {
                                                         "type": "spacer",
                                                      "size": "sm",
                                                 }
                                            ],
                                       "flex": 0
                                   }
                               }
                            }
                            sendflex(to, data)
                elif cmd == "self":
                            ret = "◽ Me\n"
                            ret += "◽ About\n"
                            ret += "◽ Sp\n"
                            ret += "◽ Tag\n"
                            ret += "◽ Grouplist\n"
                            ret += "◽ Reject\n"
                            ret += "◽ clearchat\n"
                            ret += "◽ memberlist\n"
                            ret += "◽ Blocklist\n"
                            ret += "◽ Block [ @ ]\n"
                            ret += "◽ Pic [ @ ]\n"
                            ret += "◽ Info [ @ ]\n"
                            ret += "◽ Clone [ @ ]\n"
                            ret += "◽ Unclone\n"
                            ret += "◽ curl\n"
                            ret += "◽ ourl\n"
                            ret += "◽ Bc [ text ]\n"
                            ret += "◽ lurk on/off\n"
                            ret += "◽ Gc/Gcreator\n"
                            ret += "◽ Ginfo\n"
                            ret += "◽ Footer [ text ]\n"
                            ret += "◽ Flex [ text ]\n"
                            ret += "◽ kickall\n"
                            ret += "◽ Au [  virus ]\n"
                            ret += "◽ downloadyt [ youtube link ]\n"
                            ret += "◽ spam gift [ amount] [ @ ]\n"
                            ret += "◽ Spam 1 [ amount ] [ @ ]\n"
                            ret += "◽ Spam 2 [ amount ] [ @ ]\n"
                            ret += "◽ Spam 3 [ amount ] [ @ ]\n"
                            ret += "◽ Spam 4 [ amount ] [ @ ]\n"
                            ret += "◽ grouplist"
                            data = {
                            "type": "flex",
                                    "altText": "MENU HELP",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#9400D3"
                                        },
                                        "body": {
                                        "backgroundColor": "#2F4F4F"
                                        },
                                        "footer": {
                                          "backgroundColor": "#9400D3"
                                        }
                                        },
                "type": "bubble",
                "header": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                                   {
                                   "type": "button",
                                   "style": "secondary",
                                   "color": "#FFFFFF",
                                   "height": "sm",
                                   "gravity": "center",
                                   "flex": 1,
                                   "action": {
                                                  "type": "uri",
                                                  "label": "MENU HELP",
                                                  "uri": "http://nav.cx/11S41K2"
                                                 }
                                              },
                                           ]
                                        },
                            "hero": {
                            "type": "image",
                            "url": "https://drive.google.com/uc?export=download&id=1-5RUY4pS_OASV42FXtkGLFIViTL6NHEo",
                    #        "url": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),
                            "size": "full",
                        #    "aspectRatio": "1:1",
                        #    "aspectMode": "fit",
                          "aspectRatio": "16:9",
                          "aspectMode": "cover",
                           "action": {
                                          "type": "uri",
                                          "uri": "http://nav.cx/11S41K2"
                                        }
                                     },
                        "body": {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "md",
                        "contents": [
                                           {
                                            "type": "box",
                                            "layout": "vertical",
                                            "flex": 1,
                                            "contents": [
                                                               {
                                                                "text":"{}".format(str(ret)),
                                                                "size": "sm",
                                                                "margin": "none",
                                                                "color": "#FFFFFF",
                                                                "wrap": True,
                                                                "weight": "regular",
                                                                "type": "text"
                                                                }
                                                             ]
                                                         }
                                                     ]
                                                 },
                                  "footer": {
                                  "type": "box",
                                  "layout": "horizontal",
                                  "contents": [
                                                     {
                                                      "type": "button",
                                                      "style": "secondary",
                                                      "color": "#FFFFFF",
                                                      "height": "sm",
                                                      "gravity": "center",
                                                      "flex": 1,
                                                      "action": {
                                                                      "type": "uri",
                                                                      "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                                                      "uri": "http://nav.cx/11S41K2",
                                                                      }
                                                                  },
                                                              {
                                                         "type": "spacer",
                                                      "size": "sm",
                                                 }
                                            ],
                                       "flex": 0
                                   }
                               }
                            }
                            sendflex(to, data)
                elif cmd == "help":
                            ret = "◼️ Self\n"
                            ret += "◼️ Media\n"
                            ret += "◼️ Group\n"
                            ret += "◼️ Set\n"
                            ret += "◼️ Blacklist\n"
                            ret += "◼️ Kick\n"
                            ret += "◼️ Profile\n"
                            ret += "◼️ Settings"
                            data = {
                            "type": "flex",
                                    "altText": "HELP MENU",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#9400D3"
                                        },
                                        "body": {
                                        "backgroundColor": "#2F4F4F"
                                        },
                                        "footer": {
                                          "backgroundColor": "#9400D3"
                                        }
                                        },
                "type": "bubble",
                "header": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                                   {
                                   "type": "button",
                                   "style": "secondary",
                                   "color": "#FFFFFF",
                                   "height": "sm",
                                   "gravity": "center",
                                   "flex": 1,
                                   "action": {
                                                  "type": "uri",
                                                  "label": "MENU HELP",
                                                  "uri": "http://nav.cx/11S41K2"
                                                 }
                                              },
                                           ]
                                        },
                            "hero": {
                            "type": "image",
                            "url": "https://drive.google.com/uc?export=download&id=1-5RUY4pS_OASV42FXtkGLFIViTL6NHEo",
                    #        "url": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),
                            "size": "full",
                        #    "aspectRatio": "1:1",
                        #    "aspectMode": "fit",
                          "aspectRatio": "16:9",
                          "aspectMode": "cover",
                           "action": {
                                          "type": "uri",
                                          "uri": "http://nav.cx/11S41K2"
                                        }
                                     },
                        "body": {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "md",
                        "contents": [
                                           {
                                            "type": "box",
                                            "layout": "vertical",
                                            "flex": 1,
                                            "contents": [
                                                               {
                                                                "text":"{}".format(str(ret)),
                                                                "size": "sm",
                                                                "margin": "none",
                                                                "color": "#FFFFFF",
                                                                "wrap": True,
                                                                "weight": "regular",
                                                                "type": "text"
                                                                }
                                                             ]
                                                         }
                                                     ]
                                                 },
                                  "footer": {
                                  "type": "box",
                                  "layout": "horizontal",
                                  "contents": [
                                                     {
                                                      "type": "button",
                                                      "style": "secondary",
                                                      "color": "#FFFFFF",
                                                      "height": "sm",
                                                      "gravity": "center",
                                                      "flex": 1,
                                                      "action": {
                                                                      "type": "uri",
                                                                      "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                                                      "uri": "http://nav.cx/11S41K2",
                                                                      }
                                                                  },
                                                              {
                                                         "type": "spacer",
                                                      "size": "sm",
                                                 }
                                            ],
                                       "flex": 0
                                   }
                               }
                            }
                            sendflex(to, data)
                
                if cmd.startswith("youtube "):
                            a = achink.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+achink.adityasplittext(cmd,'s')+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
                            if a["items"] != []:
                                no = 0
                                ret_ = []
                                for music in a["items"]:
                                    no += 1
                                    ret_.append({"type": "bubble","header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Youtube","weight": "bold","color": "#9b0606","size": "sm"}]},"hero": {"type": "image","url": 'https://i.ytimg.com/vi/{}/hqdefault.jpg'.format(music['id']['videoId']),"size": "full","aspectRatio": "20:13","aspectMode": "cover","action": {"type": "uri","uri": 'https://www.youtube.com/watch?v=' +music['id']['videoId']}},"body": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Title","color": "#9b0606","size": "sm","flex": 1},{"type": "text","text": "{}".format(music['snippet']['title']),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]},"footer": {"type": "box","layout": "horizontal","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Official","uri": 'https://www.youtube.com/watch?v=' +music['id']['videoId']}},{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Mp4","uri": "{}youtube%20video%20https://www.youtube.com/watch?v={}".format(wait['ttt'],music['id']['videoId'])}},{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Mp3","uri": "{}youtube%20audio%20https://www.youtube.com/watch?v={}".format(wait['ttt'],music['id']['videoId'])}},],}})
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {"messages": [{"type": "flex","altText": "Youtube.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                                    sendCarousel(to,data)
                            else:
                                achink.sendMessage(to,"Type: Search Youtube Video\nStatus: "+str(self.adityasplittext(msg.text,'s'))+" not found")
                if text.lower() == "me":
                    cover = achink.getProfileCoverURL(achink.profile.mid)
                    pp = achink.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = achink.getProfile().displayName
                    status = achink.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={"type":"flex","altText":"{} sendFlex".format(name),"contents":{"type":"bubble",'styles': {"body":{"backgroundColor":"#0000CD"}},"hero":{"type":"image","url":cover,"size":"full","aspectRatio":"20:13","aspectMode":"cover"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":" "},{"type":"image","url":profile,"size":"lg"},{"type":"text","text":" "},{"type":"text","text":name,"size":"xl","weight":"bold","color":s,"align":"center"},{"type":"text","text":" "},{"type":"text","text":status,"align":"center","size":"xs","color":s,"wrap":True},{"type":"text","text":" "},{"type":"button","style":"primary","color":"#669999","action":{"type":"uri","label":"ADD ME","uri":"http://nav.cx/11S41K2"}}]}}}
                    sendTemplate(to, data)
                if text.lower() == "me2":
                    contact = achink.getContact(sender)
                    sendTemplate(to,{"type":"flex","altText": "𝙂𝙐𝙍𝙐𝘽𝙊𝙏𝙎","contents":{"type":"bubble","footer":{"type":"box","layout":"horizontal","contents":[{"color":"#FF69B4","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://app/1636169025-yQ7bGMVA?type=profile"},"type":"text","text":"𝙂𝙐𝙍𝙐𝘽𝙊𝙏𝙎","align":"center","weight":"bold"},{"type":"separator","color":"#FF69B4"},{"color":"#FF69B4","size":"xs","wrap":True,"action":{"type":"uri","uri":"http://nav.cx/11S41K2"},"type":"text","text":"Chat_Me","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#FFD2E6"},"body":{"backgroundColor":"#ffffff"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#FF69B4"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://drive.google.com/uc?export=download&id=1-5RUY4pS_OASV42FXtkGLFIViTL6NHEo"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://raw.githubusercontent.com/achinkmaulana/png/master/YT-Logo.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://media.giphy.com/media/qqWB4u3mrTlrG/giphy.gif"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://i.pinimg.com/originals/a6/94/ec/a694ec9773292abec803f07befd73e74.gif"},{"type":"separator","color":"#FF69B4"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#FF69B4"},{"type":"box","contents":[{"type":"separator","color":"#FF69B4"},{"color":"#413877","size":"md","wrap":True,"type":"text","text":"Guru bots","weight":"bold"},{"type":"separator","color":"#FF69B4"},{"color":"#413877","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#FF69B4"},{"color":"#FF69B4","size":"xs","wrap":True,"type":"text","text":"Status Profile:","weight":"bold"},{"type":"text","text":"{}".format(contact.statusMessage),"size":"xxs","wrap":True,"color":"#422002"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"},"hero":{"aspectMode":"cover","margin":"xxl","aspectRatio":"1:1","size":"full","type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)}}})
                elif text.lower() == "me3":
                            s = temp["te"]
                            a = temp["t"]
                            contact = achink.getContact(achinkMID)
                            cover = achink.getProfileCoverURL(achinkMID)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                    },
                                    "body": {
                                       "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "weight": "bold",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1
                                            },
                                            {
                                                "type": "text",
                                                "text": "𝐌𝐘 𝐏𝐑𝐎𝐅𝐈𝐋𝐄 𝐏𝐈𝐂",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                       ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+achinkMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "NAME AND DP",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://nav.cx/11S41K2"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(cover),
                                        "size": "full",
                                        "aspectRatio":"20:13",
                                        "aspectMode":"cover"
                                  },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+achinkMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "𝐂𝐨𝐯𝐞𝐫 𝐩𝐢𝐜",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://nav.cx/11S41K2"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "profile pic",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "color": s,
                                                "size": "md"
                                            },
                                            {
                                                "type": "text",
                                                "text": "𝐍𝐀𝐌𝐄",
                                                "align": "center",
                                                "color": a,
                                                "size": "sm",
                                            },
                                            {
                                                "type": "text",
                                                "text": "MY BIO",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.statusMessage),
                                                "align": "center",
                                                "color": s,
                                                "wrap": True,
                                                "size": "md"
                                           },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+achinkMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "ME",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://nav.cx/11S41K2"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(contact.displayName),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                elif cmd == "a":
                        	_session = requests.session()
                        	n1 = LiffChatContext(to)
                        	n2 = LiffContext(chat=n1)
                        	view = LiffViewRequest('1562242036-RW04okm', n2)
                        	token = achink.liff.issueLiffView(view)
                        	url = 'https://api.line.me/message/v3/share'
                        	headers = {
                        		'Content-Type': 'application/json',
                        		'Authorization': 'Bearer %s' % token.accessToken
                        	}
                        	jsonData = {
                        		"to": to,
                        		"messages": [
                        			{
                        				"type": "template",
                        				"altText": "LINE",
                        				"template": {
                        					"type": "carousel",
                        					"actions": [],
                        					"columns": [
                                                {
                                                	"title": "Creatore",
                                                	"text": "Info creator",
                                                	"actions": [
                                                		{
                                                			"type": "uri",
                                                			"label": "ADD CREATOR",
                                                			"uri": "http://nav.cx/11S41K2"
                                                		}
                                                	]
                                                },
                                                {
                                                	"title": "My Youtube",
                                                	"text": "Info youtube creator",
                                                	"actions": [
                                                		{
                                                			"type": "uri",
                                                			"label": "Youtube",
                                                			"uri": "https://m.youtube.com/WOBProduction"
                                                		}
                                                	]                                                		
                                                },
                                                {
                                                	"title": "Game",
                                                	"text": "Game",
                                                	"actions": [
                                                		{
                                                			"type": "uri",
                                                			"label": "Game",
                                                			"uri": "line://ch/1526709289"
                                                		}
                                                	]                                                		
                                                },
                                                {                                                    
                                                	"title": " Group Event",
                                                	"text": " Group Event",
                                                	"actions": [
                                                		{
                                                			"type": "uri",
                                                			"label": " Group Event",
                                                			"uri": "line://ch/1506931000"                                                            
                                                		}                                                		
                                                	]
                                                }
                        					]
                        				}
                        			}
                        		]
                        	}
                        	data = json.dumps(jsonData)
                        	sendPost = _session.post(url, data=data, headers=headers)
                elif text.lower().startswith("smule "):
                            separate = text.split(" ")
                            id = text.replace(separate[0] + " ","")
                            cond = id.split("|")
                            search = str(cond[0])
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("https://smule.com/{}/performances/json".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    ret_ = "LIST RECORD"
                                    no = 0 + 1
                                    for smule in data["list"]:
                                        ret_ += "\n" + str(no)+"• "+str(smule["title"])
                                        no += 1
                                    ret_ += "\n"
                                    #true = True
                                    profile = "https://initiate.alphacoders.com/queue_files/1082167.jpg"
                                    chatme = "http://nav.cx/11S41K2"
                                    print('Search Smule')
                                    true = True
                                    data = {
                            "type": "flex",
                                    "altText": "SMULE MEDIA",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#0000CD"
                                        },
                                        "body": {
                                        "backgroundColor": "#000000"
                                        },
                                        "footer": {
                                          "backgroundColor": "#0000CD"
                                        }
                                        },
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "SMULE MEDIA",
                                    "uri": "http://nav.cx/11S41K2"
      }
      },
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRjNLa6n5F__PpSjk-O-QWtToEP7MdgJ75lcP-bUwjHUaw9Q0QG",
    "size": "full",
    "aspectRatio": "16:9",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://nav.cx/11S41K2"
    }
  },
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 1,
        "contents": [
          {
            "text": ret_ ,
            "size": "sm",
            "margin": "none",
            "color": "#FFFFFF",
            "wrap": True,
            "weight": "regular",
            "type": "text"
            }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                    "uri": "http://nav.cx/11S41K2",
                                    }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                                    sendflex(to, data)

                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["list"]):
                                        smule = data["list"][num - 1]
                                        r = web.get("https://smule.com/{}/performances/json".format(urllib.parse.quote(search)))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["list"] != []:
                                            am = "◽Detail Record Smule"
                                            am += "\n◽ SINGER: "+str(smule["owner"]["handle"])
                                            am += "\n◽ TITLE: "+str(smule["title"])
                                            am += "\n◽ BIO: "+str(smule["message"])
                                            am += "\n◽ PLAYS: "+str(smule["stats"]["total_listens"])
                                            am += "\n◽ LIKES: "+str(smule["stats"]["total_loves"])
                                            am += "\n◽ COMMENTS: "+str(smule["stats"]["total_comments"])
                                            am += "\n◽Audio and Video editing"
                                            hasil = "◽Detail Record\n\n"+str(am)
                                            dl = str(smule["cover_url"])
                                        #    image = str(smule["cover_url"])
                                            chatme = "http://nav.cx/11S41K2"
                                            true = True
                                            data = {
                            "type": "flex",
                                    "altText": "smule record",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#0000CD"
                                        },
                                        "body": {
                                        "backgroundColor": "#000000"
                                        },
                                        "footer": {
                                          "backgroundColor": "#0000CD"
                                        }
                                        },
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "SMULE SEARCH RESULTS",
                                    "uri": "http://nav.cx/11S41K2"
      }
      },
    ]
  },
  "hero": {
  "type": "image",
    "url": dl,
#    "url":"https://raw.githubusercontent.com/achinkmaulana/png/master/1553688604757.gif",
  #  "url":"https://obs.line-scdn.net/{".format(achink.getContact(achinkMID).pictureStatus),
 #   "url": "https://files.boteater.net/jpg-q_vxahyn.jpg",
    "size": "full",
    "aspectRatio": "1:1",
    "aspectMode": "fit",
#    "aspectRatio": "20:13",
  #  "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://nav.cx/11S41K2"
    }
  },
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 1,
        "contents": [
          {
            "text": hasil,
            "size": "sm",
            "margin": "none",
            "color": "#FFFFFF",
            "wrap": True,
            "weight": "regular",
            "type": "text"
            }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                    "uri": "http://nav.cx/11S41K2",
                                    }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                                            sendflex(to, data)
                                            key = smule["key"]
                                            qx = "https://www.smule.com/p/" + str(key)
                                            r = requests.get("https://api.eater.pw/smule?url={}".format(qx))
                                            data = r.text
                                            data = json.loads(data)
                                            achink.sendAudioWithURL(to, str(data["result"][0]["video"]))
                                            achink.sendVideoWithURL(to, str(data["result"][0]["video"]))
                
                elif text.lower() == 'myinfo' or text.lower() == "about":
                    try:
                        arr = []
                        owner = "ua1d9f1d9bc6a371266c0a3f0887921da"
                        creator = achink.getContact(owner)
                        contact = achink.getContact(achinkMID)
                        grouplist = achink.getGroupIdsJoined()
                        contactlist = achink.getAllContactIds()
                        blockedlist = achink.getBlockedContactIds()
                        IdsInvit = achink.getGroupIdsInvited()
                        times = time.time() - Start
                        runtime = timeChange(times)
                        ret_ = "\n◾ NAME               : {}".format(contact.displayName)
                        ret_ += "\n◾ Total Groups : {}".format(str(len(grouplist)))
                        ret_ += "\n◾ friends             : {}".format(str(len(contactlist)))
                        ret_ += "\n◾ blocked            : {}".format(str(len(blockedlist)))
                        ret_ += "\n◾️ group pending : {}".format(str(len(IdsInvit)))
                        ret_ += "\n◾ bot rtime          :{}".format(str(runtime))
                        ret_ += "\n◾ Creator.            : {}".format(str(creator.displayName))
                        feds = "{}".format(str(ret_))
                        data = {
                            "type": "flex",
                                    "altText": "iAmGuru",
                                        "contents": {
                                        "styles": {
                                        "header": {
                                        "backgroundColor":"#0000CD"
                                        },
                                        "body": {
                                        "backgroundColor": "#000000"
                                        },
                                        "footer": {
                                          "backgroundColor": "#0000CD"
                                        }
                                        },
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "MENU HELP",
                                    "uri": "http://nav.cx/11S41K2"
      }
      },
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),
 #   "url": "https://files.boteater.net/jpg-q_vxahyn.jpg",
    "size": "full",
    "aspectRatio": "1:1",
    "aspectMode": "fit",
 #   "aspectRatio": "20:13",
  #  "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://nav.cx/11S41K2"
    }
  },
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 1,
        "contents": [
          {
            "text":"{}".format(str(ret_)),
            "size": "sm",
            "margin": "none",
            "color": "#FFFFFF",
            "wrap": True,
            "weight": "regular",
            "type": "text"
            }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
      "type": "button",
                                "style": "secondary",
                                "color": "#FFFFFF",
                                "height": "sm",
                                "gravity": "center",
                                "flex": 1,
                                "action": {
                                    "type": "uri",
                                    "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                    "uri": "http://nav.cx/11S41K2",
                                    }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                        sendflex(to, data)
                        achink.sendContact(msg.to, creator.mid)
                    except Exception as e:
                        achink.sendMessage(msg.to, str(e))
                elif text.lower() == 'memberlist':
                    if msg.toType == 2:
                        group = achink.getGroup(to)
                        ret_ = "╰☆☆ 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐋𝐈𝐒𝐓 ☆☆╮\n"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n\nTotal {} members".format(str(len(group.members)))
                        data = {
                            "type": "flex",
                            "altText": "Member list",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                        "backgroundColor": '#000000'
                                    },
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": ret_,
                                            "color": "#00FF00",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                },
                            }
                        }
                                    
                        sendTemplate(to, data)
                elif text.lower() == 'grouplist':
                        groups = achink.groups
                        ret_ = " ╰☆☆ 𝐆𝐑𝐎𝐔𝐏𝐋𝐈𝐒𝐓 ☆☆╮\n"
                        no = 0 + 1
                        for gid in groups:
                            group = achink.getGroup(gid)
                            ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n\n TOTLE {} GROUPS".format(str(len(groups)))
                        data = {
                            "type": "flex",
                            "altText": "Group list",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                         "backgroundColor": '#ffffff'
                                    },
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type":"text",
                                            "text": ret_,
                                            "color": "#ee1298",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                        {
                                         "type": "separator",
                                         "margin":"md"
                                         },
                                         {
                                           "type": "text",
                                            "text": "           ✳️◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦✳️",
                                            "color": "#0000CD",
                                            "wrap": True,
                                            "size": "md"
                                         },
                                    ]
                                },
                            }
                        }
                        sendTemplate(to, data)
                elif text.lower() == ".restart" or text.lower() == ".reboot":
                    gifnya = ["https://codemyui.com/wp-content/uploads/2016/08/circular-water-fill-loading-animation.gif"]
                    data = {
                        "type": "template",
                        "altText": "Reset",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "full",
                                     "action": {
                                         "type": "uri",
                                          "uri": "http://nav.cx/11S41K2"
                                     }
                                }
                            ]
                        }
                    }
                    sendTemplate(to, data)
                    time.sleep(1)
                    ga = "RESTARTING"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(ga)),
                        "sentBy": {
                             "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                             "iconUrl": "https://raw.githubusercontent.com/achinkmaulana/png/master/1552389695781.jpg",
                             "uri": "http://nav.cx/11S41K2"
                        }
                    }
                    sendTemplate(to, data)
                    restartBot()
                
                elif text.lower() == 'ginfo':
                    group = achink.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ACCOUNT DELETED"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "CLOSE"
                        gTicket = "CANNOT DISPLAY QR LKMK"
                    else:
                        gQr = "OPEN"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(achink.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "▁  ▄  ▆  █ 𝐆𝐑𝐎𝐔𝐏 𝐈𝐍𝐅𝐎 █  ▆  ▄  ▁\n____________________________"
                    ret_ += "\n🔹 NAME.      : {}".format(str(group.name))
                    ret_ += "\n🔹 GID            : {}".format(group.id)
                    ret_ += "\n🔹 FOUNDER : {}".format(str(gCreator))
                    ret_ += "\n🔹 Members  : {}".format(str(len(group.members)))
                    ret_ += "\n🔹 Pending     : {}".format(gPending)
                    ret_ += "\n🔹 QR               : {}".format(gQr)
                    ret_ += "\n🔹 QR LINK      : {}".format(gTicket)
                    ret_ +="\n____________________________"
                    ret_ += "\n✳️◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦✳️"
                    data = {
                        "type": "flex",
                        "altText": "info group",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                               #     {
                                     #   "type": "image",
                                      #  "url": path, 
                                    #    "size": "xl"
                                  #  },
                                    {
                                        "type": "text",
                                        "text": ret_,
                                        "color": "#FFFFFF",
                                        "wrap": True,
                                        "size": "md",
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == ".runtime" or text.lower() == ".runtime":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    pp = achink.getProfile().pictureStatus
                    run = "★RUN TIME★\n"
                    run += runtime
                    data = {
                        "type": "flex",
                        "altText": "{}".format(run),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                 },
                            },
                            "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(pp),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                    },
                                     "body": {
                                     "type": "box",
                                     "layout": "vertical",
                                     "contents": [
                                    {
                                    "type": "separator",
                                     "color": "#00FF00"
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(run),
                                        "wrap": True,
                                        "color": "#FFFFFF",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "xl"
                                    },
                                    {
                                     "type": "separator",
                                     "color": "#00FF00"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == ".gantippgroup":
                    if msg.toType == 2:
                        if to not in sets["changeGroupPicture"]:
                            sets["changeGroupPicture"].append(to)
                        achink.sendMessage(to, "send pic")
                elif text.lower() == "tag" or text.lower() == "tagall":
                    if msg._from in achinkMID:
                        group = achink.getGroup(msg.to)
                        NAME = [contact.mid for contact in group.members]
                        nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, jml = [], [], [], [], [], [], [], [], [], len(NAME)
                        if jml <= 20:
                          mentionMembers(msg.to, NAME)
                        if jml > 20 and jml < 40:
                          for i in range (0, 19):
                              nm1 += [NAME[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, len(NAME)):
                              nm2 += [NAME[j]]
                          mentionMembers(msg.to, nm2)
                        if jml > 40 and jml < 60:
                          for i in range (0, 19):
                              nm1 += [NAME[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [NAME[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, len(NAME)):
                              nm3 += [NAME[k]]
                          mentionMembers(msg.to, nm3)
                        if jml > 60 and jml < 80:
                          for i in range (0, 19):
                              nm1 += [NAME[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [NAME[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [NAME[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, len(NAME)):
                              nm4 += [NAME[l]]
                          mentionMembers(msg.to, nm4)
                        if jml > 80 and jml < 100:
                          for i in range (0, 19):
                              nm1 += [NAME[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [NAME[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [NAME[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [NAME[l]]
                          mentionMembers(msg.to, nm4)
                          for m in range (80, len(NAME)):
                              nm5 += [NAME[m]]
                          mentionMembers(msg.to, nm5)
                        if jml > 100 and jml < 120:
                          for i in range (0, 19):
                              nm1 += [NAME[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [NAME[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [NAME[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [NAME[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [NAME[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, len(NAME)):
                              nm6 += [NAME[o]]
                          mentionMembers(msg.to, nm6)
                        if jml > 120 and jml < 140:
                          for i in range (0, 19):
                              nm1 += [NAME[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [NAME[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [NAME[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [NAME[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [NAME[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [NAME[o]]
                          mentionMembers(msg.to, nm6)
                          for v in range (120, len(NAME)):
                              nm7 += [NAME[v]]
                          mentionMembers(msg.to, nm7)
                        if jml > 140 and jml < 160:
                          for i in range (0, 19):
                               nm1 += [NAME[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [NAME[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [NAME[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [NAME[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [NAME[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [NAME[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [NAME[q]]
                          mentionMembers(msg.to, nm7)
                          for r in range (140, len(NAME)):
                              nm8 += [NAME[r]]
                          mentionMembers(msg.to, nm8)
                        if jml > 160 and jml < 180:
                          for i in range (0, 19):
                              nm1 += [NAME[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [NAME[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [NAME[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [NAME[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [NAME[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [NAME[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [NAME[q]]
                          mentionMembers(msg.to, nm7)
                          for z in range (140, 159):
                              nm8 += [NAME[z]]
                          mentionMembers(msg.to, nm8)
                          for f in range (160, len(NAME)):
                              nm9 += [NAME[f]]
                          mentionMembers(msg.to, nm9)
                elif cmd.startswith('spam 1 '):
                            try:
                                msg.text = achink.mycmd(msg.text,wait)
                                j = int(msg.text.split(' ')[2])
                                a = [achink.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                                h = [achink.sendMessage(to,b) for b in a];achink.sendMessage(to, '「 Spam 」\nTarget has been spammed with {} amount of messages♪'.format(j))
                            except:pass
                elif cmd.startswith('spam gift '):
                            if msg.toType == 0:
                                msg.text = achink.mycmd(msg.text,wait)
                                j = int(msg.text.split(' ')[2])
                                a = [achink.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                                b = [achink.giftmessage(to) for b in a];achink.sendMessage(to, '「 Spam 」\nTarget has been spammed with {} amount of messages♪'.format(j))
                            else:
                                j = int(msg.text.split(' ')[2])
                                a = [achink.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    NAME = [key1]
                                    b = [achink.giftmessage(key1) for b in a];achink.sendMention(to, '「 Spam 」\n@GuruTagshas been spammed with {} amount of gift♪'.format(j),'',[key1])
                elif cmd.startswith('spam 3 '):
                            msg.text = achink.mycmd(msg.text,wait)
                            j = int(msg.text.split(' ')[2])
                            a = [achink.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                            try:group = achink.getGroup(to);NAME = [contact.mid for contact in group.members];b = [achink.sendContact(to,random.choice(NAME)) for b in a]
                            except:NAME = [to,to];b = [achink.sendContact(to,random.choice(NAME)) for b in a]
                elif cmd.startswith('spam 4 '):
                            j = int(msg.text.split(' ')[2])
                            lontong = cmd
                            msg.text = achink.mycmd(msg.text,wait)
                            a = settings['keyCommand'].title()
                            if settings['setKey'] == False:a = ''
                            anu = [achink.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                NAME = [key1]
                                if cmd.startswith(a+" "):gss = 7 + len(a)+1
                                else:gss = 7 + len(a)
                                msg.contentMetadata = {'AGENT_LINK': 'line://ti/p/~{}'.format(achink.getProfile().userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + achink.getProfile().picturePath,'AGENT_NAME': ' 「 SPAM MENTION 」','MENTION': str('{"MENTIONEES":' + json.dumps([{'S':str(int(key['S'])-gss-len(msg.text.split(' ')[2])-1+13), 'E':str(int(key['E'])-gss-len(msg.text.split(' ')[2])-1+13), 'M':key['M']} for key in eval(msg.contentMetadata["MENTION"])["MENTIONEES"]]) + '}')}
                                msg.text = lontong[gss+1+len(msg.text.split(' ')[2]):].replace(lontong[gss+1+len(msg.text.split(' ')[2]):],' 「 Mention 」\n{}'.format(lontong[gss+1+len(msg.text.split(' ')[2]):]))
                                b = [achink.sendMessages(msg) for b in anu]
                elif msg.text.lower().startswith("image "):
                                query = removeCmd("image", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("https://api.boteater.co/googleimg?search={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                        if 'http://' in fn["img"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["img"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "GURUBOTS",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(fn["img"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Google_Image",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("playstore "):
                                query = removeCmd("playstore", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/playstore.php?id={}&apikey=KJaOT94NCD1bP1veQoJ7uXc9M".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data != []:
                                    ret_ = []
                                    for music in data:
                                        if 'http://' in music["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(music["icon"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Download",
                                                        "uri": "{}".format(str(music["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Searching App",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif cmd.startswith("xvideos "):
                            query = removeCmd(text, setKey)
                            achink.sendMessage(to, 'sedang mencari.......')
                            achink.unsendMessage(msg.id)
                            cond = query.split("+")
                            search = str(cond[0])
                            result = requests.get("https://api.eater.pw/xvideos?page={}".format(str(search)))
                            data=json.loads(result.text)['result']
                            ayudha = []
                            for byudha in data:
                               sendflex(to,{"type": "video","originalContentUrl": byudha['dl'],"previewImageUrl": byudha['img'],})
                            achink.sendMessage(to, 'silahkan toton sampe crot....')
                elif cmd == 'xxxvideo new':
                            achink.sendMessage(to, 'sedang mencari......')
                            r = requests.get("https://api.eater.pw/xvideos?page=1")
                            data=json.loads(r.text)['result']
                            ayudha = []
                            for byudha in data:
                               sendflex(to,{"type": "video","originalContentUrl": byudha['dl'],"previewImageUrl": byudha['img'],})
                            achink.sendMessage(to, 'silahkan toton sampe crot')
                elif cmd == 'xxxvideo on':
                            achink.sendMessage(to, 'sedang mencari....')
                            angka = random.randint(1, 200)
                            r = requests.get("https://api.eater.pw/xvideos?page={}".format(angka))
                            data=json.loads(r.text)['result']
                            ayudha = []
                            for byudha in data:
                               sendflex(to,{"type": "video","originalContentUrl": byudha['dl'],"previewImageUrl": byudha['img'],})
                            achink.sendMessage(to, 'silahkan toton sampe croot')
                elif msg.text.lower().startswith("text "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=ee1289,70&chf=bg,s,ff99cc"
                    achink.sendImageWithURL(msg.to, urlnya)
                elif text.lower() == 'clearban' or text.lower() == "cban":
                      apalo["Talkblacklist"] = []
                      achink.sendMessage(to, "ban cleard")
                elif text.lower() == "cancelall" or text.lower() == "cancel" and sender == achinkMID:
                            if msg.toType == 2:
                                group = achink.getGroup(to)
                                if group.invitee is None or group.invitee == []:
                                    achink.sendMessage(to, "Nothing")
                                else:
                                    invitee = [contact.mid for contact in group.invitee]
                                    for inv in invitee:
                                        achink.cancelGroupInvitation(to, [inv])
                                    achink.sendMessage(to, "{} invitation cancelled".format(str(len(invitee))))
                elif text.lower() == "blist":
                    if msg._from in achinkMID:
                        if apalo["Talkblacklist"] == []:
                            achink.sendMessage(to, "empty")
                        else:
                            for bl in apalo["Talkblacklist"]:
                                achink.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                
                elif msg.text.lower() == ".colors":
                            c="https://i.pinimg.com/originals/d0/9c/8a/d09c8ad110eb44532825df454085a376.jpg"
                            p="https://i.pinimg.com/originals/7c/d3/aa/7cd3aa57150f8f6f18711ff22c9f6d4a.jpg"
                            m="ᴇxᴀᴍᴘʟᴇ 𝟷:-\n ᴛᴏ ᴄʜᴀɴɢᴇ ᴄᴏʟᴏʀ ᴛʏᴘᴇ:- \nᴄᴏʟᴏʀ: #ᴄᴏʟᴏʀᴄᴏᴅᴇ. \n\nᴇxᴀᴍᴘʟᴇ 𝟸:--\n ᴛᴏ ᴄʜᴀɴɢᴇ ᴄᴏʟᴏʀ ᴛᴀɢ ᴛʏᴘᴇ:-\n ᴄᴏʟᴏʀ𝟸: #ᴄᴏᴅᴇᴄᴏʟᴏʀ'"
                            achink.sendImageWithURL(to,c)
                            achink.sendImageWithURL(to,p)
                            achink.sendMessage(to,m)
                elif msg.text.lower().startswith("setblok "):
                            text_ = removeCmd("setblok ", text)
                            try:
                                tagadd["b"] = text_
                                achink.sendMessage(to,"「 Set blok otomatis 」\nApakah : " + text_)
                            except:
                                achink.sendMessage(to,"Sudah")
#=========================================================
#                  [ Command On/Off ]
#=========================================================
                if text.lower() == ".autolike on":
                    settings["autolike"] = True
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐧"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".autolike off":
                    settings["autolike"] = False
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐟𝐟"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".autoblock on":
                  if msg._from in admin:
                      settings["autoblock"] = True
                      am = "sukses mengaktifkan auto block"
                      data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                      sendTemplate(to,data)
                  else:
                      am = "auto block sudah aktif"
                      data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                      sendTemplate(to,data)
                if text.lower() == ".autoblock off":
                  if msg._from in admin:
                      settings["autoblock"] = False
                      am = "sukses menonaktifkan auto block"
                      data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                      sendTemplate(to,data)
                  else:
                      achink.sendMessage(msg.to,"auto block sudah tidak aktif")
                if text.lower() == ".autocoment on":
                    settings["com"] = True
                    am = "AUTO COMMENT NOW ON"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".autocoment off":
                    settings["com"] = False
                    am = "AUTO COMMENT NOW OFF"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "𝐀𝐌𝐛𝐨𝐭𝐥??𝐧𝐞", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".welcome on":
                    settings["Welcome"] = True
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐧"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".welcome off":
                    settings["Welcome"] = False
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐟𝐟"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".wc2 on":
                    settings["Wc"] = True
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐧 "
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".wc2 off":
                    settings["Wc"] = False
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐟𝐟"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".autoleave on":
                    settings["Leave"] = True
                    am = "AUTOLEAVE NOW ON"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".autoleave off":
                    settings["Leave"] = False
                    am = "AUTOLEAVE NOW OFF"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".unsend on":
                    settings["unsendMessage"] = True
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐧 "
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".unsend off":
                    settings["unsendMessage"] = False
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐟𝐟"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".jointicket on":
                    sets["autoJoinTicket"] = True
                    am = "now on"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".jointicket off":
                    sets["autoJoinTicket"] = False
                    am = "now off"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".responleave on":
                    settings["lv"] = True
                    am ="𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐧"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".responleave off":
                    settings["lv"] = False
                    am ="𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐟𝐟"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".wcsticker2 on":
                    settings["wcsti2"] = True
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐧 "
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".wcsticker2 off":
                    settings["wcsti2"] = False
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐟𝐟"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿??𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".respontagtikel on":
                    sets["tagsticker"] = True
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐧"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".respontagtikel off":
                    sets["tagsticker"] = False
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐟𝐟"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".sticker1 on":
                    settings["Sticker"] = True
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐧"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".sticker1 off":
                    settings["Sticker"] = False
                    am = "𝐓𝐮𝐫𝐧𝐞𝐝 𝐨𝐟𝐟"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".sticker2 on":
                    sets["Sticker"] = True
                    am = "berhasil mengaktifkan stiker 2"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔??𝐔𝐁??𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                if text.lower() == ".sticker2 off":
                    sets["Sticker"] = False
                    am = "berhasil menonaktifkan stiker di 2"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
                elif text.lower()== ".addstickertag":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "tag"
                    am = "Kirim stickernya"
                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "𝐀??𝐛𝐨𝐭𝐥𝐢𝐧𝐞", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                    sendTemplate(to,data)
#==================================================================================================
                elif cmd.startswith("add sticker1 ") and sender == achinkMID:
                    load()
                    name = removeCmd("add sticker1", text)
                    name = name.lower()
                    if name not in stickers1:
                       nissa["addTikel2"]["status"] = True
                       nissa["addTikel2"]["name"] = name.lower()
                       stickers1[name.lower()] = {}
                       f = codecs.open('sticker1.json','w','utf-8')
                       json.dump(stickers1, f, sort_keys=True, indent=4, ensure_ascii=False)
                       achink.sendMessage(to, "Send stickers to save as {} ".format(name.lower()))
                    else:
                       achink.sendMessage(to, "Stickers {} already in list.".format(name.lower()))
                elif cmd.startswith("del sticker1 ") and sender == achinkMID:
                    name = removeCmd("del sticker1", text)
                    name = name.lower()
                    if name in stickers1:
                        del stickers1[name.lower()]
                        f = codecs.open('sticker1.json','w','utf-8')
                        json.dump(stickers2, f, sort_keys=True, indent=4, ensure_ascii=False)
                        achink.sendMessage(to, "Success delete stickers {} ".format(name.lower()))
                    else:
                        achink.sendMessage(to, "Stickers {} not found in list.".format(name.lower()))
                elif cmd.startswith("add sticker2 ") and sender == achinkMID:
                    load()
                    name = removeCmd("add sticker2", text)
                    name = name.lower()
                    if name not in stickers2:
                        anyun["addTikel"]["status"] = True
                        anyun["addTikel"]["name"] = name.lower()
                        stickers2[name.lower()] = {}
                        f = codecs.open('sticker2.json','w','utf-8')
                        json.dump(stickers2, f, sort_keys=True, indent=4, ensure_ascii=False)
                        achink.sendMessage(to, "Send stickers to save as {} ".format(name.lower()))
                    else:
                        achink.sendMessage(to, "Stickers {} already in list.".format(name.lower()))
                elif cmd.startswith("del sticker2 ") and sender == achinkMID:
                     name = removeCmd("del sticker2", text)
                     name = name.lower()
                     if name in stickers2:
                         del stickers2[name.lower()]
                         f = codecs.open('sticker2.json','w','utf-8')
                         json.dump(stickers2, f, sort_keys=True, indent=4, ensure_ascii=False)
                         achink.sendMessage(to, "Success delete stickers {} ".format(name.lower()))
                     else:
                         achink.sendMessage(to, "Stickers {} not found in list.".format(name.lower())) 
                elif cmd.startswith("add sticker ") and sender == achinkMID:
                    load()
                    name = removeCmd("add sticker", text)
                    name = name.lower()
                    if name not in stickers:
                       settings["addSticker"]["status"] = True
                       settings["addSticker"]["name"] = str(name.lower())
                       stickers[str(name.lower())] = {}
                       f = codecs.open('sticker.json','w','utf-8')
                       json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                       achink.sendMessage(to, "Type: Stickers\n • Detail: Add sticker\n • Status: Send sticker..")
                    else:
                       achink.sendMessage(to, "Type: Stickers\n • Detail: Add sticker\n • Status: Failed, Sticker name already in list..")
                elif cmd.startswith("del sticker ") and sender == achinkMID:
                    load()
                    name = removeCmd("del sticker", text)
                    name = name.lower()
                    if name in stickers:
                       del stickers[str(name.lower())]
                       f = codecs.open('sticker.json','w','utf-8')
                       json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                       achink.sendMessage(to, "Type: Sticker\n • Detail: Delete sticker\n • Status: Succes delete Sticker {}".format(str(name.lower())))
                    else:
                       achink.sendMessage(to, "Type: Sticker\n • Detail: Delete sticker\n • Status: Failed, Sticker name not in list")
                elif cmd.startswith("changesticker ") and sender == achinkMID:
                    load()
                    name = removeCmd("changesticker", text)
                    name = name.lower()
                    if name in stickers:
                       settings["addSticker"]["status"] = True
                       settings["addSticker"]["name"] = str(name.lower())
                       stickers[str(name.lower())] = ""
                       f = codecs.open('sticker.json','w','utf-8')
                       json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                       achink.sendMessage(to, "Type: Stickers\n • Detail: Change sticker\n • Status: Send sticker..")
                    else:
                       achink.sendMessage(to, "Type: Stickers\n • Detail: Change sticker\n • Status: Failed, Sticker not in list..")
                elif cmd == "list sticker2":
                    load()
                    ret_ = "「 Sticker List 」\n"
                    for sticker in stickers2:
                        ret_ += "\n" + sticker.title()
                    ret_ += "\n\nTotal {} Stickers".format(str(len(stickers2)))
                    achink.generateReplyMessage(msg.id)
                    achink.sendReplyMessage(msg.id, to, ret_)
                elif cmd == "list sticker1":
                    load()
                    ret_ = "「 Sticker List 」\n"
                    for sticker in stickers1:
                        ret_ += "\n" + sticker.title()
                    ret_ += "\n\nTotal {} Stickers".format(str(len(stickers1)))
                    achink.generateReplyMessage(msg.id)
                    achink.sendReplyMessage(msg.id, to, ret_)
                elif cmd == "list sticker":
                    load()
                    ret_ = "「 Sticker List 」\n"
                    for sticker in stickers:
                        ret_ += "\n" + sticker.title()
                    ret_ += "\n\nTotal {} Stickers".format(str(len(stickers)))
                    achink.generateReplyMessage(msg.id)
                    achink.sendReplyMessage(msg.id, to, ret_)
                elif cmd.startswith("sendsticker ") and sender == achinkMID:
                    load()
                    text = removeCmd("sendsticker", text)
                    cond = text.split(" ")
                    jml = int(cond[0])
                    stickername = text.replace(cond[0] + " ","").lower()
                    if stickername in stickers:
                        sid = stickers[stickername]["STKID"]
                        spkg = stickers[stickername]["STKPKGID"]
                        sver = stickers[stickername]["STKVER"]
                    else:
                       return
                    for x in range(jml):
                        sendStickers(to, sver, spkg, sid)
 #=========================================
                elif cmd.startswith("ogroup "):
                    text = removeCmd("ogroup", text)
                    sep = text.split(" ")
                    name = text.replace(sep[0] + " ", text)
                    achink.createGroup(name, [achinkMID])
                    gids = achink.getGroupIdsByName(name)
                    for gid in gids:
                	    try:
                		    x = achink.getGroup(gid)
                		    x.preventedJoinByTicket = False
                		    achink.updateGroup(x)
                	    except Exception as e:
                		    achink.sendMessage(to, str(e))
                    achink.sendMessage(to, "GROUP CREATED {}\n\nQR : http://line.me/R/ti/g/{}".format(str(name), str(achink.reissueGroupTicket(x.id))))
                elif cmd.startswith("kick ") and sender == achinkMID:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"] [0] ["M"]
                    for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                    for target in targets:
                       try:
                           achink.kickoutFromGroup(to,[target])
                       except Exception as e:
                           achink.sendMessage(to, str(e))
                elif cmd.startswith("clone "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        clone = ast.literal_eval(msg.contentMetadata['MENTION'])
                        clones = clone['MENTIONEES']
                        target = []
                        for clone in clones:
                            if clone["M"] not in target:
                               target.append(clone["M"])
                        for she in target:
                            BackupProfile = achink.getContact(sender)
                            Save1 = "http://dl.profile.line-cdn.net/{}".format(BackupProfile.pictureStatus);Save2 = "{}".format(BackupProfile.displayName);ProfileMe["PictureMe"] = Save1;ProfileMe["NameMe"] = Save2
                            contact = achink.getContact(she);ClonerV2(she)
                            sendMention(to, contact.mid, "「 Clone Profile 」\n", "\nStatus : Success");achink.sendContact(to, str(BackupProfile.mid));achink.sendContact(to, str(contact.mid))
                elif cmd == "unclone":
                    try:
                         achinkProfile = achink.getProfile()
                         achinkName = achink.getProfile()
                         achinkProfile.statusMessage = str(ProfileMe["myProfile"]["statusMessage"])
                         achinkProfile.pictureStatus = str(ProfileMe["myProfile"]["pictureStatus"])
                         achinkName.displayName = ProfileMe["NameMe"]
                         achink.updateProfile(clientName)
                         path = achink.downloadFileURL(ProfileMe["PictureMe"])
                         achink.updateProfilePicture(path)
                         coverId = str(ProfileMe["myProfile"]["coverId"])
                         achink.updateProfileCoverById(coverId)
                         BackupProfile = achink.getContact(sender)
                         sendMention(to, BackupProfile.mid, "Success");achink.sendContact(to, str(BackupProfile.mid))
                    except Exception as error:
                         achink.sendMessage(to, "Failed to Backup")
                elif cmd.startswith("pic "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                               lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + achink.getContact(ls).pictureStatus
                            achink.generateReplyMessage(msg.id)
                            achink.sendReplyImageWithURL(msg.id, to, str(path))
                elif cmd.startswith("cover "):
                    if achink != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                   lists.append(mention["M"])
                            for ls in lists:
                                path = achink.getProfileCoverURL(ls)
                                path = str(path)
                                achink.generateReplyMessage(msg.id)
                                achink.sendReplyImageWithURL(msg.id, to, str(path))
                elif cmd.startswith("info "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                               lists.append(mention["M"])
                        for ls in lists:
                            contact = achink.getContact(ls)
                            cu = achink.getProfileCoverURL(ls)
                            path = str(cu)
                            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            achink.sendMessage(msg.to,"—(••÷[ 𝐍𝐀𝐌𝐄 ]÷••)—\n" + contact.displayName + "\n—(••÷[ 𝐌𝐈𝐃 ]÷••)— :\n" + contact.mid + "\n\n—(••÷[ 𝐁𝐈𝐎 ]÷••)— :\n" + contact.statusMessage)
                            achink.sendImageWithURL(msg.to,image)
                            achink.sendImageWithURL(msg.to,path)
                elif cmd == "autojoin on":
                    if settings['autoJoin'] == True:
                        msgs=" 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐨𝐧 "
                    else:
                        msgs=" 𝐀𝐔𝐓𝐎𝐉𝐎𝐈𝐍 𝐓𝐔𝐑𝐍𝐄𝐃 𝐎𝐍 "
                        settings['autoJoin']=True
                    achink.sendMessage(msg.to, msgs)
                elif cmd == "autojoin off":
                    if settings['autoJoin'] == False:
                        msgs="𝐀𝐥??𝐞𝐚𝐝𝐲 𝐨𝐟𝐟"
                    else:
                        msgs="𝐀𝐔𝐓𝐎𝐉𝐎𝐈𝐍 𝐓𝐔𝐑𝐍𝐄𝐃 𝐎𝐅𝐅"
                        settings['autoJoin']=False
                    achink.sendMessage(msg.to, msgs)
                elif cmd == "addsidertikel" and sender == achinkMID:
                     settings["messageSticker"]["addStatus"] = True
                     settings["messageSticker"]["addName"] = "readerSticker"
                     achink.sendMessage(to, "please send a sticker.")
                elif cmd == "delsidertikel" and sender == achinkMID:
                     settings["messageSticker"]["listSticker"]["readerSticker"]["status"] = False
                     achink.sendMessage(to, "succes delete a sticker.")
                elif cmd.startswith("setsider ") and sender == achinkMID:
                     text_ = removeCmd("getreader msg set", text)
                     try:
                         settings["readerPesan"] = text_
                         achink.sendMessage(to," 「 Get Reader 」\nChanged to : " + text_)
                     except:
                         achink.sendMessage(to," 「Get Reader 」\nFailed to replace message")
                elif cmd == "lurk on" and sender == achinkMID:
                    settings["getReader"][receiver] = []
                    #settings['getReader'][receiver]['status'] = True
                    achink.sendMessage(to, "Getreader set to on.")
                elif cmd == "lurk off" and sender == achinkMID:
                    if receiver in settings["getReader"]:
                       del settings["getReader"][receiver]
                       #settings['getReader'][receiver]['status'] = False
                       achink.sendMessage(to, "Getreader set to off.")
                elif cmd == "stealtag on":
                    if temptag["stealtag"] == True:
                        msgs=" 「 Steal Tag 」\nSteal Tag already Enable♪"
                    else:
                        msgs=" 「 Steal Tag 」\nSteal Tag set to Enable♪"
                        temptag["stealtag"] = True
                    achink.sendMessage(to, msgs)
                elif cmd == "stealtag off":
                    if temptag["stealtag"] == False:
                        msgs=" 「 Steal Tag 」\nSteal Tag already DISABLED♪"
                    else:
                        msgs=" 「 Steal Tag 」\nSteal Tag set to DISABLED♪"
                        temptag["stealtag"] = False
                    achink.sendMessage(to, msgs)
                elif cmd == ".leave":
                    if msg.toType == 2:
                       group = achink.getGroup(to)
                       achink.sendMessage(to, "GOOD BYE  "+str(group.name))
                       achink.leaveGroup(to)
                elif cmd == "nuke":
                    if msg.toType == 2:
                        group = achink.getGroup(to)
                        gMembers = [contact.mid for contact in group.members]
                        for i in gMembers:
                            time.sleep(0.008)
                            achink.kickoutFromGroup(to,[i])
                        achink.sendMessage(to,"Just Some Casual Cleaning")
                    else:
                        achink.sendMessage(to,"failed >_<")
                elif cmd == "blocklist" and sender == achinkMID:
                    blockedlist = achink.getBlockedContactIds()
                    kontak = achink.getContacts(blockedlist)
                    num=1
                    msgs="◦•●◉✿ 𝐁𝐋𝐎𝐂𝐊𝐋𝐈𝐒𝐓 ✿◉●•◦\n"
                    for ids in kontak:
                        msgs+="\n%i. %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n\nTotal Blocked : %i" % len(kontak)
                    msgs+= "\nBlockInfo「 number 」"
                    msgs+= "\nConBlock"
                    msgs+= "\nBlockfriend [@]"
                    msgs+= "\nBlockmid [mid]"
                    msgs+= "\nUnblockmid [mid]"
                    hello = "{}".format(str(msgs))
                    data = {
                                "type": "text",
                                "text": "{}".format(str(msgs)),
                                "sentBy": {
                                "label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦",
                                "iconUrl": "https://drive.google.com/uc?export=download&id=1-5RUY4pS_OASV42FXtkGLFIViTL6NHEo",
                                "uri": "http://nav.cx/11S41K2"
                            }
                      }
                    sendTemplate(to, data)
#======•=======================================
#                      [ CHANGE PP VIDIO URL ]
#==================================-===========
                elif msg.text.lower().startswith("downoadyt"):
                            link = removeCmd("cvpurl", text)
                            contact = achink.getContact(sender)
                            achink.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = achink.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            changeVideoAndPictureProfile(pict, vids)
                           # achink.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Succes")
                            am = "• Status: Succes"
                            data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "◦◉✿𝐆𝐔𝐑𝐔𝐁𝐎𝐓𝐒✿◉◦", "iconUrl": "https://obs.line-scdn.net/{}".format(achink.getContact(achinkMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                            sendTemplate(to,data)
                            os.remove("TeamAnuBot.mp4")
                elif cmd.startswith('unsend '):
                            achink.unsendMessage(msg.id)
                            j = int(msg.text.split(' ')[1])
                            a = [achink.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                            if len(msg.text.split(' ')) == 2:
                                h = wait['Unsend'][msg.to]['B']
                                n = len(wait['Unsend'][msg.to]['B'])
                                for b in h[:j]:
                                    try:
                                        achink.unsendMessage(b)
                                        wait['Unsend'][msg.to]['B'].remove(b)
                                    except:pass
                                t = len(wait['Unsend'][msg.to]['B'])
  #                              client.generateReplyMessage(msg.id)
  #                              client.sendReplyMessage(msg.id, to," 「 Unsend 」\nUnsend {} message".format((n-t)))
                            if len(msg.text.split(' ')) >= 3:h = [achink.unsendMessage(achink.sendMessage(to,achink.adityasplittext(msg.text,'s')).id) for b in a]
            elif msg.contentType == 1:
                if sets["pict"] == True:
                    path = achink.downloadObjectMsg(msg_id)
                    sets["pict"] = False
                    sets["listpict"] = str(path)
                    achink.sendMessage(to, "Done...")
            elif msg.contentType == 1:
                if sets["changePictureProfile"] == True:
                    path = achink.downloadObjectMsg(msg_id)
                    sets["changePictureProfile"] = False
                    achink.updateProfilePicture(path)
                    achink.sendMessage(to, "Done")
                if msg.toType == 2:
                    if to in sets["changeGroupPicture"]:
                        path = achink.downloadObjectMsg(msg_id)
                        sets["changeGroupPicture"].remove(to)
                        achink.updateGroupPicture(to, path)
                        achink.sendMessage(to, "Done")
                                
#=================================================================================
#=================================================================================
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != achink.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                
                if msg.contentType == 0 and sender not in achinkMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if sets["tagsticker"] == True:
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if achinkMID in mention["M"]:
                                      msg = sets["messageSticker"]["listSticker"]["tag"]
                                      if msg != None:
                                          contact = achink.getContact(achinkMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+' kirim stickers','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
                                      else:
                                          contact = achink.getContact(achinkMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+'SEND stickers','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            achink.sendMessage(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        achink.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
                        
                if msg.contentType == 7:
                    if anyun["addTikel"]["status"] == True:
                        stickers2[anyun["addTikel"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers2[anyun["addTikel"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        stickers2[anyun["addTikel"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        f = codecs.open('sticker2.json','w','utf-8')
                        json.dump(stickers2, f, sort_keys=True, indent=4, ensure_ascii=False)
                        achink.sendMessage(to, "Success add sticker {}".format(str(anyun["addTikel"]["name"])))
                        anyun["addTikel"]["status"] = False
                        anyun["addTikel"]["name"] = ""
                if msg.contentType == 7:
                    if nissa["addTikel2"]["status"] == True:
                        stickers1[nissa["addTikel2"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        f = codecs.open('sticker1.json','w','utf-8')
                        json.dump(stickers1, f, sort_keys=True, indent=4, ensure_ascii=False)
                        achink.sendMessage(to, "Success add sticker {}".format(str(nissa["addTikel2"]["name"])))
                        nissa["addTikel2"]["status"] = False
                        nissa["addTikel2"]["name"] = ""      
#====================================================================
                if msg.contentType == 0:
                    if "/ti/g/" in text.lower():
                    	if sets["autoJoinTicket"] == True:
                      #  if settings["autoJoin"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = achink.findGroupByTicket(ticket_id)
                                if len(group.members) >= wait["Members"]:
                                    achink.acceptGroupInvitationByTicket(group.id,ticket_id)
                                else:
                                    achink.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    achink.leaveGroup(group.id)
                    if text in tes["Message"]:
                        mentions(to,tes["Message"][msg.text],[sender])                          
#                      if text.lower() in tes2["Message2"]:
#                        client.generateReplyMessage(msg.id)
#                          client.sendReplyMessage(msg.id, to, "{}".format(tes2["Message2"][msg.text]))
                    if text.lower() in tes2["Message2"]:
                        data = {
                            "type": "flex",
                            "altText": "flex",
                            "contents": {
                                "type": "bubble",
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "{}".format(tes2["Message2"][text]),
                                            "wrap": True,
                                            "align": "start",
                                            "gravity": "center",
                                            "size": "sm"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
                for image in images:
                    if text.lower() == image:
                        achink.generateReplyMessage(msg.id)
                        achink.sendReplyImage(msg.id, to, images[image])

                for sticker in stickers:
                    if text.lower() == sticker:
                        sid = stickers[sticker]["STKID"]
                        spkg = stickers[sticker]["STKPKGID"]
                        sver = stickers[sticker]["STKVER"]
                        try:
                            sendSticker(to, msg._from, sver, spkg, sid)
                        except Exception as e:
                            sendSticker2(to, msg._from, sver, spkg, sid)

                for sticker in stickers2:
                    try:
                        if text.lower() == sticker:
                            sid = stickers2[sticker]["STKID"]
                            spkg = stickers2[sticker]["STKPKGID"]
                            sver = stickers2[sticker]["STKVER"]
                            a = achink.shop.getProduct(packageID=int(spkg), language='ID', country='ID')
                            if a.hasAnimation == True:data = {"type": "template","altText": "{} sent a sticker.".format(achink.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "http://nav.cx/11S41K2"}}]}}
                            else:data = {"type": "template","altText": "{} sent a sticker.".format(achink.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/android/sticker@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}]}}
                            sendTemplate(to,data)
                    except Exception as e:
                        print(e)

                for sticker in stickers1:
                    if text.lower() == sticker:
                        sid = stickers1[sticker]["STKID"]
                        data = {
                            "type": "template",
                            "altText": "Love you GURU",
                            "baseSize": {
                                "height": 1040,
                                "width": 1040
                            },
                            "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png".format(sid),
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                            }
                        }
                        sendTemplate(to, data)
#========================================================================
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            achink.sendMessage(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        achink.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
#=======================================
#          Mode publick
#=======================================
                    
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != achink.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "!respon":
                    achink.sendMessage(to,"i Am Active!!!! ")
            if "/ti/g/" in msg.text.lower():
                        if sets["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = achink.findGroupByTicket(ticket_id)
                                achink.acceptGroupInvitationByTicket(group.id,ticket_id)
                                achink.sendMessage(group.id,str(tagadd["m"]))
                                achink.sendMessage(to, "Joined %s " % str(group.name))
            elif msg.contentType == 7:
                if settings['Sticker']:
                    if 'STKOPT' in msg.contentMetadata:
                        contact = achimk.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' kirim sticker','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        contact = achink.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+'kirim sticker','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)    
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != achinkMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"location":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = achink.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = achink.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = achink.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = achink.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
        if op.type == 65:
            if op.param1 not in chatbot["botMute"]:
                if settings["unsendMessage"] == True:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        ah = time.time()
                        ikkeh = achink.getContact(msg_dict[msg_id]["from"])
                        if "text" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                            del msg_dict[msg_id]
                        else:
                            if "image" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nImage :\nBelow"
                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                achink.sendImage(at, msg_dict[msg_id]["image"])
                                del msg_dict[msg_id]
                            else:
                                if "video" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nVideo :\nBelow"
                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                    achink.sendVideo(at, msg_dict[msg_id]["video"])
                                    del msg_dict[msg_id]
                                else:
                                    if "audio" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nAudio :\nBelow"
                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                        achink.sendAudio(at, msg_dict[msg_id]["audio"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "sticker" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nSticker :\nBelow"
                                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                            achink.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "mid" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nContact :\nBelow"
                                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                achink.sendContact(at, msg_dict[msg_id]["mid"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "location" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nLocation :\nBelow"
                                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                    achink.sendLocation(at, msg_dict[msg_id]["location"])
                                                    del msg_dict[msg_id]
                                                else:
                                                    if "file" in msg_dict[msg_id]:
                                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                        waktumsg = format_timespan(waktumsg)
                                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                        rat_ += "\nFile :\nBelow"
                                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                        achink.sendFile(at, msg_dict[msg_id]["file"])
                                                        del msg_dict[msg_id]
                else:
                    print ("[ ERROR ] Terjadi Error Karena Tidak Ada Data Chat Tersebut~")
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            NOTIFIED_READ_MESSAGE(op)
    except Exception as error:
        logError(error)

#==============================================================================#

        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

def run():
    while True:
        try:
            ops = achinkPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(achinkBot(op))
                   achinkPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
    run()
