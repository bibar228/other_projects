import requests
from bs4 import BeautifulSoup


url_our = ["https://perm.istudio-shop.ru/catalog/iPhone/iPhone-12/Apple-iPhone-12-64Gb-White-18e5a501.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-12/Apple-iPhone-12-128Gb-White-18e5a4fa.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-13/Apple-iPhone-13-128Gb-Starlight-1aae83b6.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-13/Apple-iPhone-13-256Gb-Starlight-1aae83bb.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14/Apple-iPhone-14-128Gb-Starlight-17452c1b.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14/Apple-iPhone-14-256Gb-Blue-20779f9c.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14-Plus/Apple-iPhone-14-Plus-128Gb-Starlight-7a5c8d9b.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14-Plus/Apple-iPhone-14-Plus-256Gb-Starlight-9362bb60.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14-Plus/Apple-iPhone-14-Plus-512Gb-Starlight-ac87649e.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14-Pro/Apple-iPhone-14-Pro-128Gb-Gold-bd87dbb4.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14-Pro/Apple-iPhone-14-Pro-256Gb-Gold-e6aebd37.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14-Pro/Apple-iPhone-14-Pro-512Gb-Gold-ff3f72df.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14-Pro/Apple-iPhone-14-Pro-1TB-Gold-d5f14175.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14-Pro-Max/Apple-iPhone-14-Pro-Max-128Gb-Gold-55a67f54.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14-Pro-Max/Apple-iPhone-14-Pro-Max-256Gb-Gold-b838bb0f.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14-Pro-Max/Apple-iPhone-14-Pro-Max-512Gb-Gold-ccb8b823.html",
           "https://perm.istudio-shop.ru/catalog/iPhone/iPhone-14-Pro-Max/Apple-iPhone-14-Pro-Max-1TB-Gold-a3b42912.html",
           "https://perm.istudio-shop.ru/catalog/Apple-Watch/Series-SE/Apple-Watch-Series-SE-40mm-Space-Gray-Aluminum-Case-with-Black-Sport-Band-535e1259.html",
           "https://perm.istudio-shop.ru/catalog/Apple-Watch/Series-SE/Apple-Watch-Series-SE-44mm-Space-Gray-Aluminum-Case-with-Black-Sport-Band-535e125a.html",
           "https://perm.istudio-shop.ru/catalog/Apple-Watch/Series-SE-2/Apple-Watch-Series-SE-2-40mm-Midnight-Aluminum-Case-with-Midnight-Sand-Sport-Band-cbd4c5b1.html",
           "https://perm.istudio-shop.ru/catalog/Apple-Watch/Series-SE-2/Apple-Watch-Series-SE-2-44mm-Midnight-Aluminum-Case-with-Midnight-Sand-Sport-Band-dc0494b3.html",
           "https://perm.istudio-shop.ru/catalog/Apple-Watch/Series-Ultra/Apple-Watch-Series-Ultra-49mm-Titanium-Case-with-Yellow-Trail-Loop-SM-5d5c2483.html",
           "https://perm.istudio-shop.ru/catalog/Apple-Watch/Series-8/Apple-Watch-Series-8-41mm-Midnight-Aluminum-Case-Midnight-Sport-Band-83d6182d.html",
           "https://perm.istudio-shop.ru/catalog/Apple-Watch/Series-8/Apple-Watch-Series-8-45mm-Midnight-Aluminum-Case-Midnight-Sport-Band-068435cf.html",
           "https://perm.istudio-shop.ru/catalog/naushnikiBluetooth-garnitury/Apple/besprovodnye-naushniki-Apple-AirPods-2-41dccd2d.html",
           "https://perm.istudio-shop.ru/catalog/naushnikiBluetooth-garnitury/Apple/besprovodnye-naushniki-Apple-AirPods-3-81f146cf.html",
           "https://perm.istudio-shop.ru/catalog/naushnikiBluetooth-garnitury/Apple/besprovodnye-naushniki-Apple-AirPods-Pro-2021-MagSafe-740370c6.html",
           "https://perm.istudio-shop.ru/catalog/naushnikiBluetooth-garnitury/Apple/besprovodnye-naushniki-Apple-AirPods-Pro-2-MagSafe-7785c8b2.html",
           "https://perm.istudio-shop.ru/catalog/naushnikiBluetooth-garnitury/Apple/besprovodnye-naushniki-Apple-AirPods-Max-Silver-8c13626a.html"
        ]


url_ipointperm = ["https://ipointperm.ru/product/apple-iphone-12-64gb-chernyy",
    "https://ipointperm.ru/product/apple-iphone-12-128gb-chernyy",
    "https://ipointperm.ru/product/iphone-13-128gb-black",
    "https://ipointperm.ru/product/apple-iphone-13-256gb-tyomnaya-noch",
    "https://ipointperm.ru/product/apple-iphone-14-128gb-midnight",
    "https://ipointperm.ru/product/apple-iphone-14-256gb-midnight",
    "https://ipointperm.ru/product/apple-iphone-14-plus-128gb-midnight",
    "https://ipointperm.ru/product/apple-iphone-14-plus-256gb-midnight",
    "https://ipointperm.ru/product/apple-iphone-14-plus-512gb-midnight",
    "https://ipointperm.ru/product/apple-iphone-14-pro-128gb-deep-blue",
    "https://ipointperm.ru/product/apple-iphone-14-pro-256gb-deep-blue",
    "https://ipointperm.ru/product/apple-iphone-14-pro-512gb-deep-blue",
    "https://ipointperm.ru/product/apple-iphone-14-pro-1tb-deep-purple",
    "https://ipointperm.ru/product/apple-iphone-14-pro-max-128gb-deep-purple",
    "https://ipointperm.ru/product/apple-iphone-14-pro-max-256gb-deep-purple",
    "https://ipointperm.ru/product/apple-iphone-14-pro-max-512gb-deep-purple",
    "https://ipointperm.ru/product/apple-iphone-14-pro-max-1tb-deep-purple",
    "",
    "",
    "https://ipointperm.ru/product/apple-watch-se-40mm-2022-midnight",
    "https://ipointperm.ru/product/apple-watch-se-44mm-2022-midnight",
    "https://ipointperm.ru/product/apple-watch-ultra-49mm-titanium-case",
    "https://ipointperm.ru/product/apple-watch-8-41mm-midnight",
    "https://ipointperm.ru/product/apple-watch-8-45mm-midnight",
    "https://ipointperm.ru/product/apple-airpods-2-2",
    "https://ipointperm.ru/product/apple-airpods-3",
    "https://ipointperm.ru/product/apple-airpods-pro",
    "https://ipointperm.ru/product/apple-airpods-pro-2nd-generation-2022",
    "https://ipointperm.ru/product/airpods-max"]


url_appleword = ["https://aw-store.ru/catalog/iphone/iphone_12_12_mini/85725/",
                  "https://aw-store.ru/catalog/iphone/iphone_12_12_mini/85730/",
                  "https://aw-store.ru/catalog/iphone/iphone_13_13_mini/86107/",
                 "https://aw-store.ru/catalog/iphone/iphone_13_13_mini/86112/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_14_plus/86364/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_14_plus/86369/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_14_plus/86379/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_14_plus/86384/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_14_plus/86389/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_pro_14_pro_max/86393/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_pro_14_pro_max/86397/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_pro_14_pro_max/86401/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_pro_14_pro_max/86405/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_pro_14_pro_max/86409/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_pro_14_pro_max/86413/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_pro_14_pro_max/86417/",
                 "https://aw-store.ru/catalog/iphone/iphone_14_pro_14_pro_max/86421/",
                 "",
                 "",
                 "https://aw-store.ru/catalog/watch/watch_se_2022/86439/",
                 "https://aw-store.ru/catalog/watch/watch_se_2022/86442/",
                 "https://aw-store.ru/catalog/watch/watch_ultra/86457/",
                 "https://aw-store.ru/catalog/watch/watch_series_8/86446/",
                 "https://aw-store.ru/catalog/watch/watch_series_8/86450/",
                 "https://aw-store.ru/catalog/portativnaya_tekhnika/naushniki/78200/",
                 "https://aw-store.ru/catalog/portativnaya_tekhnika/naushniki/86215/",
                 "https://aw-store.ru/catalog/portativnaya_tekhnika/naushniki/78201/",
                 "https://aw-store.ru/catalog/portativnaya_tekhnika/naushniki/86424/",
                 "https://aw-store.ru/catalog/portativnaya_tekhnika/naushniki/85835/"]


url_gadjetmarket = [[requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][0]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][0]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][3]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][6]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][9]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][12]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][15]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][1]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][1]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][4]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][7]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][10]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][13]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/210886170.json").json()["products"][0]["variants"][16]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][0]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][0]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][3]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][6]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][9]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][12]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][15]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][1]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][1]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][4]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][7]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][10]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][13]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/262173327.json").json()["products"][0]["variants"][16]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322414212.json").json()["products"][0]["variants"][0]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322414212.json").json()["products"][0]["variants"][0]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322414212.json").json()["products"][0]["variants"][3]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322414212.json").json()["products"][0]["variants"][6]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322414212.json").json()["products"][0]["variants"][9]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322414212.json").json()["products"][0]["variants"][12]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322414212.json").json()["products"][0]["variants"][1]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322414212.json").json()["products"][0]["variants"][1]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322414212.json").json()["products"][0]["variants"][4]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322414212.json").json()["products"][0]["variants"][7]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322414212.json").json()["products"][0]["variants"][10]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322414212.json").json()["products"][0]["variants"][13]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][0]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][0]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][3]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][6]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][9]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][12]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][1]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][1]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][4]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][7]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][10]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][13]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][2]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][2]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][5]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][8]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][11]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322447580.json").json()["products"][0]["variants"][14]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][0]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][0]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][4]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][8]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][12]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][1]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][1]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][5]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][9]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][13]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][2]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][2]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][6]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][10]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][14]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][3]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][3]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][7]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][11]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322476487.json").json()["products"][0]["variants"][15]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][0]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][0]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][4]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][8]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][12]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][1]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][1]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][5]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][9]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][13]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][2]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][2]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][6]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][10]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][14]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][3]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][3]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][7]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][11]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322486371.json").json()["products"][0]["variants"][15]["available"]] else False],
                    [""],
                    [""],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/327568958.json").json()["products"][0]["variants"][0]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/327568958.json").json()["products"][0]["variants"][0]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/327568958.json").json()["products"][0]["variants"][2]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/327568958.json").json()["products"][0]["variants"][4]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/327568958.json").json()["products"][0]["variants"][1]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/327568958.json").json()["products"][0]["variants"][1]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/327568958.json").json()["products"][0]["variants"][3]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/327568958.json").json()["products"][0]["variants"][5]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322824594.json").json()["products"][0]["variants"][0]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322824594.json").json()["products"][0]["variants"][0]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322824594.json").json()["products"][0]["variants"][1]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322824594.json").json()["products"][0]["variants"][2]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322824594.json").json()["products"][0]["variants"][3]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322824594.json").json()["products"][0]["variants"][4]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322824594.json").json()["products"][0]["variants"][5]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322824594.json").json()["products"][0]["variants"][6]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322824594.json").json()["products"][0]["variants"][7]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322824594.json").json()["products"][0]["variants"][8]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322546339.json").json()["products"][0]["variants"][0]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322546339.json").json()["products"][0]["variants"][0]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322546339.json").json()["products"][0]["variants"][2]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322546339.json").json()["products"][0]["variants"][4]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322546339.json").json()["products"][0]["variants"][6]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322546339.json").json()["products"][0]["variants"][1]["price"], True if True in [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322546339.json").json()["products"][0]["variants"][1]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322546339.json").json()["products"][0]["variants"][3]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322546339.json").json()["products"][0]["variants"][5]["available"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/322546339.json").json()["products"][0]["variants"][7]["available"]] else False],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/135447626.json").json()["products"][0]["variants"][0]["price"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/135447626.json").json()["products"][0]["variants"][0]["available"]],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/342929373.json").json()["products"][0]["variants"][0]["price"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/342929373.json").json()["products"][0]["variants"][0]["available"]],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/275796995.json").json()["products"][0]["variants"][0]["price"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/275796995.json").json()["products"][0]["variants"][0]["available"]],
                    [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/323228328.json").json()["products"][0]["variants"][0]["price"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/323228328.json").json()["products"][0]["variants"][0]["available"]],
                    [""]]


url_connect = [[requests.get("http://www.connectperm.ru/products_by_id/234913234.json").json()["products"][0]["variants"][0]["price"], requests.get("http://www.connectperm.ru/products_by_id/234913234.json").json()["products"][0]["variants"][0]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/234913234.json").json()["products"][0]["variants"][2]["price"], requests.get("http://www.connectperm.ru/products_by_id/234913234.json").json()["products"][0]["variants"][2]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/263251221.json").json()["products"][0]["variants"][0]["price"], requests.get("http://www.connectperm.ru/products_by_id/263251221.json").json()["products"][0]["variants"][0]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/263251221.json").json()["products"][0]["variants"][2]["price"], requests.get("http://www.connectperm.ru/products_by_id/263251221.json").json()["products"][0]["variants"][2]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325481032.json").json()["products"][0]["variants"][0]["price"], requests.get("http://www.connectperm.ru/products_by_id/325481032.json").json()["products"][0]["variants"][0]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325481032.json").json()["products"][0]["variants"][2]["price"], requests.get("http://www.connectperm.ru/products_by_id/325481032.json").json()["products"][0]["variants"][2]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325494328.json").json()["products"][0]["variants"][0]["price"], requests.get("http://www.connectperm.ru/products_by_id/325494328.json").json()["products"][0]["variants"][0]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325494328.json").json()["products"][0]["variants"][1]["price"], requests.get("http://www.connectperm.ru/products_by_id/325494328.json").json()["products"][0]["variants"][1]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325494328.json").json()["products"][0]["variants"][2]["price"], requests.get("http://www.connectperm.ru/products_by_id/325494328.json").json()["products"][0]["variants"][2]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325570569.json").json()["products"][0]["variants"][0]["price"], requests.get("http://www.connectperm.ru/products_by_id/325570569.json").json()["products"][0]["variants"][0]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325570569.json").json()["products"][0]["variants"][1]["price"], requests.get("http://www.connectperm.ru/products_by_id/325570569.json").json()["products"][0]["variants"][1]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325570569.json").json()["products"][0]["variants"][2]["price"], requests.get("http://www.connectperm.ru/products_by_id/325570569.json").json()["products"][0]["variants"][2]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325570569.json").json()["products"][0]["variants"][3]["price"], requests.get("http://www.connectperm.ru/products_by_id/325570569.json").json()["products"][0]["variants"][3]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325574035.json").json()["products"][0]["variants"][0]["price"], requests.get("http://www.connectperm.ru/products_by_id/325574035.json").json()["products"][0]["variants"][0]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325574035.json").json()["products"][0]["variants"][1]["price"], requests.get("http://www.connectperm.ru/products_by_id/325574035.json").json()["products"][0]["variants"][1]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325574035.json").json()["products"][0]["variants"][2]["price"], requests.get("http://www.connectperm.ru/products_by_id/325574035.json").json()["products"][0]["variants"][2]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325574035.json").json()["products"][0]["variants"][3]["price"], requests.get("http://www.connectperm.ru/products_by_id/325574035.json").json()["products"][0]["variants"][3]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325574035.json").json()["products"][0]["variants"][3]["price"], requests.get("http://www.connectperm.ru/products_by_id/325574035.json").json()["products"][0]["variants"][3]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/325574035.json").json()["products"][0]["variants"][3]["price"], requests.get("http://www.connectperm.ru/products_by_id/325574035.json").json()["products"][0]["variants"][3]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/209023763.json").json()["products"][0]["variants"][0]["price"], requests.get("http://www.connectperm.ru/products_by_id/209023763.json").json()["products"][0]["variants"][0]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/209023763.json").json()["products"][0]["variants"][3]["price"], requests.get("http://www.connectperm.ru/products_by_id/209023763.json").json()["products"][0]["variants"][3]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/327995952.json").json()["products"][0]["variants"][0]["price"], requests.get("http://www.connectperm.ru/products_by_id/327995952.json").json()["products"][0]["variants"][0]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/327995952.json").json()["products"][0]["variants"][3]["price"], requests.get("http://www.connectperm.ru/products_by_id/327995952.json").json()["products"][0]["variants"][3]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/328002996.json").json()["products"][0]["variants"][0]["price"], requests.get("http://www.connectperm.ru/products_by_id/328002996.json").json()["products"][0]["variants"][0]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/182446926.json").json()["products"][0]["variants"][0]["price"], requests.get("http://www.connectperm.ru/products_by_id/182446926.json").json()["products"][0]["variants"][0]["available"]],
               [requests.get("http://www.connectperm.ru/products_by_id/274052920,182446926.json").json()["products"][0]["variants"][0]["price"], requests.get("http://www.connectperm.ru/products_by_id/274052920,182446926.json").json()["products"][0]["variants"][0]["available"]],
               [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/275796995.json").json()["products"][0]["variants"][0]["price"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/275796995.json").json()["products"][0]["variants"][0]["available"]],
               [requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/323228328.json").json()["products"][0]["variants"][0]["price"], requests.get("https://www.xn--80aahffbe8aqxkjdvf.xn--p1ai/products_by_id/323228328.json").json()["products"][0]["variants"][0]["available"]],
               [""]]

dict_products = {"0": ["Наименование товара", "Наши цены", "iPointperm", "AppleWord", "Гаджетмаркетпро", "Connect"]}


"""ФОРМИРОВАНИЕ ЗАГОЛОВКОВ ТАБЛИЦЫ"""
#with open("pars/tablica.csv", "w", encoding="UTF-8", newline='') as file:
    #writer = csv.writer(file)
    #writer.writerow(("Наименование товара", "Наши цены", "ipointperm", "AppleWord Perm", "Гаджетмаркетпро", "connect"))


"""ФОРМИРОВАНИЕ СЛОВАРЯ С НАШИМИ ЦЕНАМИ"""

for i in range(0, len(url_our)):
    if len(url_our[i]) > 0:
        src = requests.get(url_our[i]).text
        soup_price = BeautifulSoup(src, "lxml").find(class_="cen bk_price")
        soup_name = BeautifulSoup(src, "lxml").find(itemprop="name").text

        dict_products[str(i+1)] = [soup_name, soup_price.text.replace('\xa0руб', '').replace(' ', '')]


"""ЗАПИСЬ В СЛОВАРЬ ДАННЫХ ИПОИНПЕРМЬ"""

for d in range(len(url_ipointperm)):
    if len(url_ipointperm[d]) > 0:
        src = requests.get(url_ipointperm[d]).text
        soup_price = BeautifulSoup(src, "lxml").find(class_="price js-product-price")

        dict_products[str(d+1)] += [soup_price.text.replace('\xa0руб', '').replace(' ', '')]
    else:
        dict_products[str(d+1)] += [""]


"""ЗАПИСЬ В СЛОВАРЬ ДАННЫХ АППЛЕВОРД"""

for d in range(len(url_appleword)):
    if len(url_appleword[d]) > 0:
        src = requests.get(url_appleword[d]).text
        soup_price = BeautifulSoup(src, "lxml").find(class_="price_value")

        dict_products[str(d+1)] += [soup_price.text.replace('\xa0руб', '').replace(' ', '')]
    else:
        dict_products[str(d+1)] += [""]


"""ЗАПИСЬ В СЛОВАРЬ ДАННЫХ ГАДЖЕТМАРКЕТ"""

for d in range(len(url_gadjetmarket)):
    if len(url_gadjetmarket[d]) > 1:
        if url_gadjetmarket[d][1] == False:
            dict_products[str(d+1)] += [f"{url_gadjetmarket[d][0][:-2]} (Нет в наличии)"]
        else:
            dict_products[str(d+1)] += [url_gadjetmarket[d][0][:-2]]
    else:
        dict_products[str(d+1)] += [""]


"""ЗАПИСЬ В СЛОВАРЬ ДАННЫХ КОННЕКТ"""

for d in range(len(url_connect)):
    if len(url_connect[d]) > 1:
        if url_connect[d][1] == False:
            dict_products[str(d+1)] += [f"{url_connect[d][0][:-2]} (Нет в наличии)"]
        else:
            dict_products[str(d+1)] += [url_connect[d][0][:-2]]
    else:
        dict_products[str(d+1)] += [""]










