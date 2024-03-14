from turtle import onclick, onrelease
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDRectangleFlatButton,MDIconButton,MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import MDList,OneLineListItem
from kivy.uix.widget import Widget
from helpers import Text_Copied,copo,drop,pickup
from kivy.uix.scrollview import ScrollView
from kivy.core.clipboard import Clipboard 
from kivy.uix.boxlayout import BoxLayout
import requests
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
import requests
true=True
false=False
null=None

from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

class CabX(MDApp):

    def build(self):
        self.screen = Screen()
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.primary_palette = "Red"
        btn_pickup= MDRectangleFlatButton(text="Confirm PickUp",pos_hint={"center_x": 0.6, "center_y": 0.8},on_release=self.send_pickup,)
        btn_drop= MDRectangleFlatButton(text="Confirm Drop",pos_hint={"center_x": 0.6, "center_y": 0.7},on_release=self.send_drop,)
        #btn_search= MDRectangleFlatButton(text="Search",pos_hint={"center_x": 0.34, "center_y": 0.6},on_release=self.send_text,)
        dark_icon = MDFloatingActionButton(icon='theme-light-dark',pos_hint={"center_x": 0.91, "center_y": 0.9},on_release=self.switch_theme_style,)
        btn_search = MDRectangleFlatIconButton(text="Search",icon='map-search',pos_hint={"center_x": 0.34, "center_y": 0.6},on_release=self.send_text,)
        self.theme_cls.theme_style ="Light"
        self.pickup= Builder.load_string(pickup)
        self.drop= Builder.load_string(drop)
        self.d={}

        self.copso=Builder.load_file(r"C:\Users\91889\Desktop\pythonprogs\TRCLIP\PyCab\copi.kv")
        self.ola_font=Builder.load_file(r"C:\Users\91889\Desktop\pythonprogs\TRCLIP\PyCab\olafont.kv")
        self.scroll = ScrollView(size_hint=(0.7, 0.5),pos_hint={"center_x": 0.4, "center_y": 0.2},)
        self.list_view=MDList()
        item1=OneLineListItem(text='Locations :')
        self.list_view.add_widget(item1)
        self.scroll.add_widget(self.list_view)
        self.screen.add_widget(self.scroll)
        self.screen.add_widget(dark_icon)
        self.screen.add_widget(self.drop)
        self.screen.add_widget(self.pickup)
        self.screen.add_widget(btn_pickup)
        self.screen.add_widget(btn_drop)
        self.screen.add_widget(btn_search)
        return self.screen



    def send_pickup(self,obj):
        q=str(self.pickup.text).replace(" ","+")
        headers = {'Authorization': 'prj_live_pk_45ceb9fa92e11e8a388d29aa275d66c2ebb0de44',}
        query=q
        scroll = ScrollView(size_hint=(0.7, 0.5),pos_hint={"center_x": 0.4, "center_y": 0.2},)
        response = requests.get('https://api.radar.io/v1/search/autocomplete?query={}'.format(query), headers=headers)
        byte_str=eval(str(response.content)[2:-1])
        loc_list=(byte_str["addresses"])
        for i in range(len(loc_list)):
            t=""
            try:
                country=(loc_list[i]["country"])
            except:
                country=''
            try:
                city=(loc_list[i]["city"])
            except:
                city=''
            try:
                dist=(loc_list[i]["neighborhood"])
            except:
                dist=''
            try:
                pincode=(loc_list[i]["postalCode"])
            except:
                pincode=''
            try:
                place=(loc_list[i]["placeLabel"])
            except:
                place=''
            try:
                state=(loc_list[i]["state"])
            except:
                state=''
            t+=place+" "+dist+" "+city+" "+state+" "+pincode+" "+country
            a=(t.strip().replace("   "," ").replace("  "," "))
            p=(loc_list[i]["geometry"]["coordinates"])
            self.d[a]=p
            self.pickup.text=a
            item1=OneLineListItem(text=self.pickup.text,on_release=self.print_item)
            self.list_view.add_widget(item1)
            
    def print_item(self, instance):
        d=self.d
        self.pickup.text=instance.text
        self.scroll.clear_widgets()
        self.list_view.clear_widgets()
        item1=OneLineListItem(text='Locations :')
        self.list_view.add_widget(item1,-1)
        self.scroll.add_widget(self.list_view)
    

    def send_uber(self,a,b):
        # pickup_latitude=17.490261803102022

        # pickup_longitude=78.45205482398886

        # drop_latitude=17.527562140261793

        # drop_longitude =78.4228482393393
        pickup_latitude=a[1]

        pickup_longitude=a[0]

        drop_latitude=b[1]

        drop_longitude =b[0]



        cookies = {
        'usl_rollout_id': '57ea89c1-56ef-40a9-81ea-24c319588f95',
        'marketing_vistor_id': '912fdfbc-637b-4bab-a6af-845e1eac3311',
        'udi-id': 'vFBoEPTmjmnxYBWwPC0NR+MhZ38FElyQMj/qMXP9FtWdijnDwpX4f9X6PUziMpbiVKr3ndNmW2LsdJZ/kDicDbKynaNuzHmlmwf9l5QKhET3HPZy2gb3K6YLtFmvp0QhxfYKOlKFxbAs28oCk6vEmiDIz0WueWht7IshSGyHYOMZlqY7tr4pQ9TIdFLn8yI+vVbg8r15u+3LRrhx6AATcA==tzW0PnEsBcPlg5baLUC2lw==MJMBUsW+FMdHx+q5K82gbe2dPA+I6oXuWCDlbdH1fVo=',
        'segmentCookie': 'b',
        'CONSENTMGR': 'c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1687366483109%7Cconsent:true',
        '_cc': 'AVyrNIhPlEvBIsKAeS3r5KFB',
        '_cid_cc': 'AVyrNIhPlEvBIsKAeS3r5KFB',
        '_gcl_au': '1.1.1454870100.1687366484',
        'udi-fingerprint': '3revIHv8WQqRppkimPlisycHCjdfUalEg+7vS/bC6miPGSdoVZUIZUzL9kwL8hT8bUDbHl40gLcpCr913wsE/A==n4SQQuqAftVOENPOfDfQ9DYkIuCJfqZ9N1Bp+LvWHJ8=',
        'utag_geo_code': 'US',
        '_gid': 'GA1.2.1912184767.1694577554',
        'x-uber-analytics-session-id': '552ecca6-c6de-44d4-ae13-5e9fe790346b',
        'sid': 'QA.CAESEDcZjXM68EGWtRcIPQCvm7QYt4GjqQYiATEqJDk2Yzk1ZDBlLTAzYTctNGE1OC1hNDZkLWEyNTNjNDU3NTNiMTJAFJUGDttdcPNExADs-4BfYEBG2IbUGwOXkusch1fpwCaQ08ezeldVsjfxH3-jbOsg94cyZdl2WEx7SZY1x42mLjoBMUIIdWJlci5jb20.zlQ6rc1OfiSEwNwQXV82Gob60J4FIRyGyLbh2rjVdO4',
        'isWebLogin': 'true',
        'csid': '1.1697169591700.bCUo7pbFAVBU2HMgtM712+yB/2oMQbY0vbNWBRQRHVA=',
        '_ua': '{"session_id":"52261075-b26a-494b-9129-cd5ebbeb051e","session_time_ms":1694577591980}',
        'mp_adec770be288b16d9008c964acfba5c2_mixpanel': '%7B%22distinct_id%22%3A%20%2296c95d0e-03a7-4a58-a46d-a253c45753b1%22%2C%22%24device_id%22%3A%20%22188dee13c5764e-0637bc0530d20b-26031d51-144000-188dee13c58179a%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fauth.uber.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22auth.uber.com%22%2C%22%24user_id%22%3A%20%2296c95d0e-03a7-4a58-a46d-a253c45753b1%22%2C%22%24search_engine%22%3A%20%22google%22%7D',
        'utag_main': 'v_id:0188dee13c73000f73b82c5b8da70506f002a06700978$_sn:4$_se:4$_ss:0$_st:1694579392835$segment:b$optimizely_segment:b$ses_id:1694577553087%3Bexp-session$_pn:2%3Bexp-session',
        '_ga': 'GA1.2.2080569943.1687366484',
        'jwt-session': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InNlc3Npb25fdHlwZSI6ImRlc2t0b3Bfc2Vzc2lvbiIsInRlbmFuY3kiOiJ1YmVyL3Byb2R1Y3Rpb24ifSwiaWF0IjoxNjk0NTc3NTkxLCJleHAiOjE2OTQ2NjM5OTF9.CNvUUd4Hda82LJM7oLDZxxNg9cCaz-_3w8gM1LuDsdI',
        'udi-fingerprint': '95nwYctcMeegXjj9sr1HQiWND9fLG6A4fyWYdK4dDD64kkyMs1TH6t8v/kY+CWbu+u9scbyR2Ii4K6YB2gVP0w==50BZm1jGSD67mVoRYgJUvYJSscCcnyURFJ+BjtZ18xo=',
        '_ga_XTGQLY6KPT': 'GS1.1.1694577553.5.1.1694577646.0.0.0',
        }

        headers = {
        'authority': 'm.uber.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': 'usl_rollout_id=57ea89c1-56ef-40a9-81ea-24c319588f95; marketing_vistor_id=912fdfbc-637b-4bab-a6af-845e1eac3311; udi-id=vFBoEPTmjmnxYBWwPC0NR+MhZ38FElyQMj/qMXP9FtWdijnDwpX4f9X6PUziMpbiVKr3ndNmW2LsdJZ/kDicDbKynaNuzHmlmwf9l5QKhET3HPZy2gb3K6YLtFmvp0QhxfYKOlKFxbAs28oCk6vEmiDIz0WueWht7IshSGyHYOMZlqY7tr4pQ9TIdFLn8yI+vVbg8r15u+3LRrhx6AATcA==tzW0PnEsBcPlg5baLUC2lw==MJMBUsW+FMdHx+q5K82gbe2dPA+I6oXuWCDlbdH1fVo=; segmentCookie=b; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1687366483109%7Cconsent:true; _cc=AVyrNIhPlEvBIsKAeS3r5KFB; _cid_cc=AVyrNIhPlEvBIsKAeS3r5KFB; _gcl_au=1.1.1454870100.1687366484; udi-fingerprint=3revIHv8WQqRppkimPlisycHCjdfUalEg+7vS/bC6miPGSdoVZUIZUzL9kwL8hT8bUDbHl40gLcpCr913wsE/A==n4SQQuqAftVOENPOfDfQ9DYkIuCJfqZ9N1Bp+LvWHJ8=; utag_geo_code=US; _gid=GA1.2.1912184767.1694577554; x-uber-analytics-session-id=552ecca6-c6de-44d4-ae13-5e9fe790346b; sid=QA.CAESEDcZjXM68EGWtRcIPQCvm7QYt4GjqQYiATEqJDk2Yzk1ZDBlLTAzYTctNGE1OC1hNDZkLWEyNTNjNDU3NTNiMTJAFJUGDttdcPNExADs-4BfYEBG2IbUGwOXkusch1fpwCaQ08ezeldVsjfxH3-jbOsg94cyZdl2WEx7SZY1x42mLjoBMUIIdWJlci5jb20.zlQ6rc1OfiSEwNwQXV82Gob60J4FIRyGyLbh2rjVdO4; isWebLogin=true; csid=1.1697169591700.bCUo7pbFAVBU2HMgtM712+yB/2oMQbY0vbNWBRQRHVA=; _ua={"session_id":"52261075-b26a-494b-9129-cd5ebbeb051e","session_time_ms":1694577591980}; mp_adec770be288b16d9008c964acfba5c2_mixpanel=%7B%22distinct_id%22%3A%20%2296c95d0e-03a7-4a58-a46d-a253c45753b1%22%2C%22%24device_id%22%3A%20%22188dee13c5764e-0637bc0530d20b-26031d51-144000-188dee13c58179a%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fauth.uber.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22auth.uber.com%22%2C%22%24user_id%22%3A%20%2296c95d0e-03a7-4a58-a46d-a253c45753b1%22%2C%22%24search_engine%22%3A%20%22google%22%7D; utag_main=v_id:0188dee13c73000f73b82c5b8da70506f002a06700978$_sn:4$_se:4$_ss:0$_st:1694579392835$segment:b$optimizely_segment:b$ses_id:1694577553087%3Bexp-session$_pn:2%3Bexp-session; _ga=GA1.2.2080569943.1687366484; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InNlc3Npb25fdHlwZSI6ImRlc2t0b3Bfc2Vzc2lvbiIsInRlbmFuY3kiOiJ1YmVyL3Byb2R1Y3Rpb24ifSwiaWF0IjoxNjk0NTc3NTkxLCJleHAiOjE2OTQ2NjM5OTF9.CNvUUd4Hda82LJM7oLDZxxNg9cCaz-_3w8gM1LuDsdI; udi-fingerprint=95nwYctcMeegXjj9sr1HQiWND9fLG6A4fyWYdK4dDD64kkyMs1TH6t8v/kY+CWbu+u9scbyR2Ii4K6YB2gVP0w==50BZm1jGSD67mVoRYgJUvYJSscCcnyURFJ+BjtZ18xo=; _ga_XTGQLY6KPT=GS1.1.1694577553.5.1.1694577646.0.0.0',
        'origin': 'https://m.uber.com',
        'pragma': 'no-cache',
        'referer': 'https://m.uber.com/looking?drop%5B0%5D=%7B%22latitude%22%3A17.4899275%2C%22longitude%22%3A78.45259%2C%22addressLine1%22%3A%22Ridge%20Towers%22%2C%22addressLine2%22%3A%2248-243%2F2%20Bus%20Stop%20near%20Ganesh%20Nagar%2C%20Surya%20Nagar%2C%20Quthbullapur%2C%20Hyderabad%2C%20Telangana%22%2C%22id%22%3A%22ChIJxeviAEKQyzsR5Y5i8WeWWAI%22%2C%22provider%22%3A%22google_places%22%2C%22index%22%3A0%7D&pickup=%7B%22latitude%22%3A17.5161534%2C%22longitude%22%3A78.4496168%2C%22addressLine1%22%3A%22Chinthal%22%2C%22addressLine2%22%3A%22Hyderabad%2C%20Telangana%22%2C%22id%22%3A%22ChIJ29GrmWyQyzsRfrMbkpZLAFQ%22%2C%22provider%22%3A%22google_places%22%2C%22index%22%3A0%7D',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-csrf-token': 'x',
        'x-uber-rv-session-type': 'desktop_session',
        'x-uber-wa-info': 'UTXTIJNNNLPNJIRRDHMKHFHM',
        }

        json_data = {
            'operationName': 'Products',
            'variables': {
                'includeClassificationFilters': True,
                'includeRecommended': False,
                'destinations': [
                    {
                        'latitude': drop_latitude,
                        'longitude': drop_longitude,
                    },
                ],
                'pickup': {
                    'latitude': pickup_latitude,
                    'longitude': pickup_longitude,
                },
            },
            'query': 'query Products($destinations: [InputCoordinate!]!, $includeClassificationFilters: Boolean = false, $includeRecommended: Boolean = false, $pickup: InputCoordinate!, $pickupFormattedTime: String, $profileType: String, $targetProductType: EnumRVWebCommonTargetProductType) {\n  products(\n    destinations: $destinations\n    includeClassificationFilters: $includeClassificationFilters\n    includeRecommended: $includeRecommended\n    pickup: $pickup\n    pickupFormattedTime: $pickupFormattedTime\n    profileType: $profileType\n    targetProductType: $targetProductType\n  ) {\n    ...ProductsFragment\n    __typename\n  }\n}\n\nfragment ProductsFragment on RVWebCommonProductsResponse {\n  classificationFilters {\n    ...ClassificationFiltersFragment\n    __typename\n  }\n  defaultVVID\n  productsUnavailableMessage\n  renderRankingInformation\n  tiers {\n    ...TierFragment\n    __typename\n  }\n  __typename\n}\n\nfragment BadgesFragment on RVWebCommonProductBadge {\n  color\n  text\n  __typename\n}\n\nfragment ClassificationFiltersFragment on RVWebCommonClassificationFilters {\n  filters {\n    ...ClassificationFilterFragment\n    __typename\n  }\n  hiddenVVIDs\n  standardProductVVID\n  __typename\n}\n\nfragment ClassificationFilterFragment on RVWebCommonClassificationFilter {\n  currencyCode\n  displayText\n  fareDifference\n  icon\n  vvid\n  __typename\n}\n\nfragment TierFragment on RVWebCommonProductTier {\n  products {\n    ...ProductFragment\n    __typename\n  }\n  title\n  __typename\n}\n\nfragment ProductFragment on RVWebCommonProduct {\n  badges {\n    ...BadgesFragment\n    __typename\n  }\n  capacity\n  cityID\n  currencyCode\n  description\n  detailedDescription\n  discountPrimary\n  displayName\n  estimatedTripTime\n  etaStringShort\n  fare\n  hasPromo\n  hasRidePass\n  id\n  is3p\n  isAvailable\n  legalConsent {\n    ...ProductLegalConsentFragment\n    __typename\n  }\n  meta\n  preAdjustmentValue\n  productImageUrl\n  productUuid\n  reserveEnabled\n  __typename\n}\n\nfragment ProductLegalConsentFragment on RVWebCommonProductLegalConsent {\n  header\n  image {\n    url\n    width\n    __typename\n  }\n  description\n  enabled\n  ctaUrl\n  ctaDisplayString\n  buttonLabel\n  showOnce\n  __typename\n}\n',
        }

        response = requests.post('https://m.uber.com/graphql', cookies=cookies, headers=headers, json=json_data)
        a=str(response.content)
        p="{"+(str(response.content)[a.find("products")-1:a.find("title")-3])+"}"
        j=""
        d=[]
        uber_all_cost,uber_all=[],[]
        uber_costss={}
        list_uber=["Moto","UberAuto","UberGo","Go Sedan","Premier","UberXL"]
        for i in p:
            if i!="\\":
                j+=i
        aa=(j.split("xe2x82xb9")[1:])
        bb=(j.split('displayName":"')[1:])
        for i in bb:
            uber_all.append(i.split('"')[0])
        for i in aa:
            uber_all_cost.append(float(i.split('"')[0]))
        uber_all_cost.sort()
        for i in range(len(list_uber)):
            uber_costss[list_uber[i]]=str(uber_all_cost[i])
        print(uber_costss)
        uber_costs={}
        list_uber=["Moto","UberAuto","UberGo","Go Sedan","Premier","UberXL"]
        list_uberr=list_uber[::-1]
        for i in list_uberr:
            if i not in uber_costss:
                uber_costs[i]="Not available"
            else:
                uber_costs[i]=str(uber_costss[i])
        b=0
        c=0
        
        self.screen.add_widget(self.copso)
        for i in uber_costs:
            t=''
            
            t+=(i+" -> "+uber_costs[i])
            
            
            b+=5
            c+=0.075
            self.screen.add_widget(
                MDLabel(
                    text=t,
                    pos=(10,b),
                    pos_hint ={'center_x':.6, 'center_y':c},
                    theme_text_color="Error",
                )
            )


    def send_ola(self,a,b):
        pickup_latitude=a[1]
        pickup_longitude=a[0]
        drop_latitude=b[1]
        drop_longitude =b[0]
        cookies = {
        '_ga_7QP5L1NN0B': 'GS1.1.1694574256.2.0.1694574256.60.0.0',
        '_gid': 'GA1.2.1694680844.1694574257',
        'OSRN_v1': 'bizCzSEp8TQXj7DnXHP5Cv7p',
        '_csrf': 'yXcce7Q4wmkOZhr3zOHK24ub',
        'XSRF-TOKEN': '4UHj71MZ-UGJ8uPzwBYMU4KZnLc87MmeZkZY',
        '_ga_FR59878HTR': 'GS1.2.1694574307.1.0.1694574307.60.0.0',
        '_gcl_au': '1.1.1029015434.1694574307',
        '_ga': 'GA1.2.1072462973.1691301149',
        '_ga_EKVXJMSBW2': 'GS1.2.1694574344.1.0.1694574344.60.0.0',
        'wasc': 'web-11c0e22f-81b1-42b6-b40c-3c2c2c789d26__AQECAHgfxP3kLfatAqX5D3Wm8Q4cwpCiqFMlbQIth8I9m4HyQQAAANswgdgGCSqGSIb3DQEHBqCByjCBxwIBADCBwQYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAwARKe3iyKHOL4fQusCARCAgZPZUzVxw5W4U9B8gpwo75t7DkeorRYavfesvgfnB4ICFjZEdtzSHMNjQZLzzm%2Fxu03EuZuRp1HFfr9bDyRXuqVY%2F%2F2De0Do421mFNBBBfgTi8EZ010RXneed3g6KmrfHg%2B6DPqx5Gcr%2BRRemZX61wJvIhMl0GnHj21zJE1uIUdLz4yXqSqmgx6f9BNoEoHXZAprkKg%3D',
        '_ga_2TR8WHTK1X': 'GS1.1.1694574307.1.1.1694574517.60.0.0',
        }

        headers = {
        'authority': 'book.olacabs.com',
        'accept': 'application/json',
        'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,te;q=0.6',
        'content-type': 'application/json',
        # 'cookie': '_ga_7QP5L1NN0B=GS1.1.1694574256.2.0.1694574256.60.0.0; _gid=GA1.2.1694680844.1694574257; OSRN_v1=bizCzSEp8TQXj7DnXHP5Cv7p; _csrf=yXcce7Q4wmkOZhr3zOHK24ub; XSRF-TOKEN=4UHj71MZ-UGJ8uPzwBYMU4KZnLc87MmeZkZY; _ga_FR59878HTR=GS1.2.1694574307.1.0.1694574307.60.0.0; _gcl_au=1.1.1029015434.1694574307; _ga=GA1.2.1072462973.1691301149; _ga_EKVXJMSBW2=GS1.2.1694574344.1.0.1694574344.60.0.0; wasc=web-11c0e22f-81b1-42b6-b40c-3c2c2c789d26__AQECAHgfxP3kLfatAqX5D3Wm8Q4cwpCiqFMlbQIth8I9m4HyQQAAANswgdgGCSqGSIb3DQEHBqCByjCBxwIBADCBwQYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAwARKe3iyKHOL4fQusCARCAgZPZUzVxw5W4U9B8gpwo75t7DkeorRYavfesvgfnB4ICFjZEdtzSHMNjQZLzzm%2Fxu03EuZuRp1HFfr9bDyRXuqVY%2F%2F2De0Do421mFNBBBfgTi8EZ010RXneed3g6KmrfHg%2B6DPqx5Gcr%2BRRemZX61wJvIhMl0GnHj21zJE1uIUdLz4yXqSqmgx6f9BNoEoHXZAprkKg%3D; _ga_2TR8WHTK1X=GS1.1.1694574307.1.1.1694574517.60.0.0',
        'referer': 'https://book.olacabs.com/?serviceType=p2p&utm_source=widget_on_olacabs&drop_lat=17.52987&drop_lng=78.42366&drop_name=Tatva%20Global%20School%2C%20Hyderabad%20(Best%20And%20Top%20CBSE%20School%20In%20Kukatpally%20Hyderabad%20Telangana%20India%20%3A%20Tatva%20Global%20School)%20Tatva%20Global%20High%20School%20Rd%20Sri%20Balaji%20Layout%20Gajularamaram%20Hyderabad%20Telangana%20500055%20India&lat=17.587514732147113&lng=78.41293892322165&pickup_name=HCQ7%2B44V%2C%20Gandi%20Maisamma%2C%20Domara%20Pocham%20Pally%2C%20Hyderabad&pickup=',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-fingerprint-id': '68764164',
        'x-requested-with': 'XMLHttpRequest',
    }
        params = {
            'pickupLat': str(pickup_latitude),
            'pickupLng': str(pickup_longitude),
            'pickupMode': 'NOW',
            'leadSource': 'desktop_website',
            'dropLat': str(drop_latitude),
            'dropLng': str(drop_longitude),
            'silent': 'false',
        }
        t=''
        response = requests.get('https://book.olacabs.com/data-api/category-fare/p2p', params=params, cookies=cookies, headers=headers)
        self.screen.add_widget(self.ola_font)
        b=0
        c=0
        try:
            null="null"
            print("pas1")
            ola_str=str(response.content)[2:-1]
            ola_eval=eval(ola_str)
            print("pas1")
            print(ola_eval)
            ola_cabs=ola_eval["data"]["p2p"]["categories"]
            print(ola_cabs)
            ola_lstss=['bike','auto','mini','prime','suv']
            ola_lstsss=ola_lstss[::-1]
            b+=5
            c+=0.075
            self.screen.add_widget(
                MDLabel(
                    text=" ",
                    pos=(10,b),
                    pos_hint ={'center_x':.9, 'center_y':c},
                    theme_text_color="Error",
                )
            )
            for  i in ola_lstsss:
                try:
                    print(i)
                    t="Ola {} -> ".format(i.title())+str(ola_cabs[i]["price"]).replace("\xe2\x82\xb9","Rs.")
                    b+=5
                    c+=0.075
                    self.screen.add_widget(
                        MDLabel(
                            text=t,
                            pos=(10,b),
                            pos_hint ={'center_x':.9, 'center_y':c},
                            theme_text_color="Error",
                        )
                    )
                except:
                    t="Ola {} -> ".format(i.title())+"Not available"
                    b+=5
                    c+=0.075
                    self.screen.add_widget(
                        MDLabel(
                            text=t,
                            pos=(10,b),
                            pos_hint ={'center_x':.9, 'center_y':c},
                            theme_text_color="Error",
                        )
                    )
                    
        except Exception as e:
            print("errror",e)
            b+=5
            c+=0.075
            self.screen.add_widget(
                MDLabel(
                    text=" ",
                    pos=(10,b),
                    pos_hint ={'center_x':.9, 'center_y':c},
                    theme_text_color="Error",
                )
            )


    def send_text(self,obj):
        d=self.d
        a="a"
        b="b"
        a=d[self.pickup.text]
        b=(d[self.drop.text])
        print(d[self.pickup.text],self.pickup.text)
        print(d[self.drop.text],self.drop.text)
        self.scroll.clear_widgets()
        self.list_view.clear_widgets()
        self.send_uber(a,b)
        self.send_ola(a,b)
        
        

    def send_drop(self,obj):
        headers = {'Authorization': 'prj_live_pk_45ceb9fa92e11e8a388d29aa275d66c2ebb0de44',}
        q=str(self.drop.text).replace(" ","+")
        scroll = ScrollView(size_hint=(0.7, 0.5),pos_hint={"center_x": 0.4, "center_y": 0.2},)
        response = requests.get('https://api.radar.io/v1/search/autocomplete?query={}'.format(q), headers=headers)
        byte_str=eval(str(response.content)[2:-1])
        loc_list=(byte_str["addresses"])
        for i in range(len(loc_list)):
            t=""
            try:
                country=(loc_list[i]["country"])
            except:
                country=''
            try:
                city=(loc_list[i]["city"])
            except:
                city=''
            try:
                dist=(loc_list[i]["neighborhood"])
            except:
                dist=''
            try:
                pincode=(loc_list[i]["postalCode"])
            except:
                pincode=''
            try:
                place=(loc_list[i]["placeLabel"])
            except:
                place=''
            try:
                state=(loc_list[i]["state"])
            except:
                state=''
            t+=place+" "+dist+" "+city+" "+state+" "+pincode+" "+country
            a=(t.strip().replace("   "," ").replace("  "," "))
            p=(loc_list[i]["geometry"]["coordinates"])
            self.d[a]=p
            self.drop.text=(t.strip().replace("   "," ").replace("  "," "))
            item1=OneLineListItem(text=self.drop.text,on_release=self.print_drop)
            self.list_view.add_widget(item1)
    
        
    def print_drop(self, instance):
        d=self.d
        self.drop.text=instance.text
        self.scroll.clear_widgets()
        self.scroll = ScrollView(size_hint=(0.7, 0.5),pos_hint={"center_x": 0.4, "center_y": 0.2},)
        self.list_view=MDList()
        item1=OneLineListItem(text='Locations :')
        self.list_view.add_widget(item1,-1)
        self.scroll.add_widget(self.list_view)


    def switch_theme_style(self,obj):
        self.theme_cls.primary_palette = (
            "Red" if self.theme_cls.primary_palette == "Blue" else "Blue"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )


CabX().run()
    


