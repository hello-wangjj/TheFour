#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import time
__author__ = 'wangjj'
__mtime__ = '20161107下午 8:20'
urls = [
    'http://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html'.format(
        str(i)) for i in range(
            0,
            1050,
        30)]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    'Cookie': 'TAUnique=%1%enc%3AyR1sPrT%2FsXJHdDcT4uJMZ8K4IS%2FWp1M2BaJOHlavovjmhWnEwXwJZw%3D%3D; TASSK=enc%3AdBS8tGnNC9cgOcCiUJwauZp9a80EHw%2BmSoTEXLzOkZRrJDAposbINnoY9P4SpuJ%2B; __gads=ID=8815d1dbc07a166f:T=1471100510:S=ALNI_MZyLE5HGgmf_HLiVy_G8E7spkfwfg; bdshare_firstime=1471100456457; TACds=B.1.14858.2.2016-09-18; ServerPool=R; CommercePopunder=SuppressAll*1478516196238; ki_u=8ef56502-3344-3d32-1363-458a; ki_s=167327%3A4.0.0.1.2; TAPD=tripadvisor.cn; TAAuth2=%1%3%3A82869428bc16627d6a2ec42084235d65%3AAIFmRO22xBS8WadcjOgEn1Yfsm8UMeaGvx6Q6KfhQhBUM3Sd2AZI1Aa239NYQrSNJboy6oaVfuZtECGXltOGuxyWygZwkpMlXHF2J8DBWBkxbW7vuYzWMi1Pkc%2FVpPo7F2iDtEEuiOxJyvn9WFL0E9eu1t4Ey6g2MybSUiH4nusk8%2FGlVrHYqJV6f%2FEcBRbQ48qrqfx%2BIaYv27ndVs%2BgTchwuaDpet0gBM1Ks1j0%2FvCJ; _smt_uid=58206241.57a75a94; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.28953_312l105127_312l143361_312l60763_312*RS.1; CM=%1%HanaPersist%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C3%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C11%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7C2016sticksess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7C2016stickpers%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttractions-g60763-Activities-oa1020-New_York_City_New_York.html; ki_t=1471100397903%3B1478516181961%3B1478535220310%3B3%3B48; ki_r=; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1476157037,1478516181; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1478535220; TASession=%1%V2ID.F61643EC119610686BF1BDD472A13335*SQ.179*LP.%2FFanyi*PR.39776%7C*LS.Saves*GR.43*TCPAR.67*TBR.26*EXEX.91*ABTR.7*PPRP.66*PHTB.69*FS.92*CPU.24*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.85340371A1005E252A667BFB47DA6D79*LF.zhCN*FA.1*DF.0*IR.3*OD.en_US*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.60763; TAUD=LA-1478516183395-1*LG-62918626-2.1.F.*LD-62918627-.....; roybatty=TNI1625!AGZBtOe49brQkSv8%2BjHvmXVnCj6KCNuln%2FpC29AN4PKTL%2BZOcBiuO%2FwUxloooPaJNu96bEbLgSryg%2FexyrXZHFCA%2FR28HhlO3M77R3uOaoGLTPUuBNpSGAxu0z4DIvQ3MvM9T7C%2Fb76x%2BZ16gKdZ7yw%2F0ofDgoZp5LQCXNy7KhOX%2C1; NPID='
}
# url_save = 'http://www.tripadvisor.cn/Saves#534715'
# 收藏夹的内容通过ajax返回
url_ajax = 'http://www.tripadvisor.cn/ModuleAjax?'


def get_attractions(url, data=None):
    wb_data = requests.get(url)
    time.sleep(4)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.property_title > a')
    images = soup.select('img[width="160"]')
    cates = soup.select(
        'div.element_wrap > div.wrap.al_border.attraction_element > div.p13n_reasoning_v2')
    if data is None:
        for title, image, cate in zip(titles, images, cates):
            data = {
                'title': title.get_text(),
                'image': image.get('src'),
                'cate': list(cate.stripped_strings)
            }
            print(data)


def get_favs(url, data=None):
    body = {
        'actions': '[{"name":"FETCH","resource":"modules.saves.model.SingleTripView","params":{"folderId":"534715"},"id":"clientaction31"}]',
        'authenticator': 'DEFAULT',
        'context': '{"Errors":[{"$t":"modules.common.model.Errors","$i":""}],"features":[{"gamification_badge_collection":{"enabled":true}}],"Saves_Strings":[{"$t":"modules.saves.model.Strings","$i":""}],"LoggedInMember":[{"$t":"modules.common.model.LoggedInMember","$i":""}],"Saves_AllTripsView":[{"$t":"modules.saves.collection.AllTripsView","$i":""}],"Saves_SingleTripView":[{"$t":"modules.saves.model.SingleTripView","$i":""}],"Member":[{"$t":"modules.common.model.Member","$i":"memberId:k52EsvKglkM="}],"MemberCenter_ContributionView":[{"$t":"modules.membercenter.model.ContributionView","$i":"memberId:k52EsvKglkM="}]}',
        'token': 'TNI1625!AGZBtOe49brQkSv8+jHvmXVnCj6KCNuln/pC29AN4PKTL+ZOcBiuO/wUxloooPaJNu96bEbLgSryg/exyrXZHFCA/R28HhlO3M77R3uOaoGLTPUuBNpSGAxu0z4DIvQ3MvM9T7C/b76x+Z16gKdZ7yw/0ofDgoZp5LQCXNy7KhOX',
        'version': '5'
    }
    post_data = requests.post(
        url,
        headers=headers,
        data=body)
    print(post_data.status_code)
    json_str = json.loads(post_data.text)
    if data is None:
        keys = json_str['store']['modules.common.entity.JSONAddress'].keys()
        addresses = json_str['store']['modules.common.entity.JSONAddress']
        images = json_str['store'][
            'modules.unimplemented.entity.AccommodationSizedThumbnail']
        descs = json_str['store']['modules.common.entity.JSONAttraction']
        for i in keys:
            data = {
                'name': descs[i]['name'],
                'description': descs[i]['description'],
                'images': 'http:' + images[i]['url'],
                'address': str(addresses[i].get('line4')) + str(addresses[i].get('line3')) + str(
                    addresses[i].get('line2')) + str(addresses[i].get('line1')),
                'type': descs[i]['types'],
                'category': descs[i]['category']
            }
            print(data)
for url in urls:
    get_attractions(url)
