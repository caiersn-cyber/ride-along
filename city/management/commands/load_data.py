from django.core.management.base import BaseCommand
from city.models import City, County


class Command(BaseCommand):
    help = 'Load Cities and Counties'

    def handle(self, *args, **kwargs):
        if City.objects.count() > 0:
            City.objects.all().delete()
        if County.objects.count() > 0:
            County.objects.all().delete()

        cities = [
            {
                'name': '贵阳市',
                'latitude': 26.6499922,
                'longitude': 106.6246178
            },

            {
                'name': '六盘水市',
                'latitude': 26.5963778,
                'longitude': 104.8279652,
            },

            {
                'name': '遵义市',
                'latitude': 27.7237996,
                'longitude': 106.9191408,
            },

            {
                'name': '安顺市',
                'latitude': 26.254911,
                'longitude': 105.9437773,
            },

            {
                'name': '毕节市',
                'latitude': 27.2150032,
                'longitude': 105.215166,
            },

            {
                'name': '铜仁市',
                'latitude': 27.952938,
                'longitude': 108.584018,
            },

            {
                'name': '黔西南布依族苗族自治州',
                'latitude': 25.0925381,
                'longitude': 104.9019205,
            },

            {
                'name': '黔东南苗族侗族自治州',
                'latitude': 26.5870883,
                'longitude': 107.978748,
            },

            {
                'name': '黔南布依族苗族自治州',
                'latitude': 26.257011,
                'longitude': 107.5180339,
            }

        ]

        # if not City.objects.count():
        for city in cities:
            name = city['name']
            latitude = city['latitude']
            longitude = city['longitude']
            City.objects.create(name=name, latitude=latitude, longitude=longitude)

        # 贵阳
        guiyang = City.objects.get(name='贵阳市')

        guiyang_county = [
            {
                'name': '乌当区',
                'latitude': 26.6336497,
                'longitude': 106.7493435,
            },

            {
                'name': '南明区',
                'latitude': 26.5722545,
                'longitude': 106.7050549,
            },

            {
                'name': '云岩区',
                'latitude': 26.6079969,
                'longitude': 106.7205994,
            },

            {
                'name': '花溪区',
                'latitude': 26.438812,
                'longitude': 106.657623,
            },

            {
                'name': '白云区',
                'latitude': 26.6824352,
                'longitude': 106.6178509,
            },

            {
                'name': '观山湖区',
                'latitude': 26.6196131,
                'longitude': 106.595038,
            },

            {
                'name': '清镇市',
                'latitude': 26.5585041,
                'longitude': 106.4668752,
            },

            {
                'name': '开阳县',
                'latitude': 27.060922,
                'longitude': 106.9655857,
            },

            {
                'name': '息烽县',
                'latitude': 27.0995612,
                'longitude': 106.7316896,
            },

            {
                'name': '修文县',
                'latitude': 26.8424454,
                'longitude': 106.5886106,
            },
        ]

        for county in guiyang_county:
            name = county['name']
            latitude = county['latitude']
            longitude = county['longitude']
            County.objects.create(name=name, latitude=latitude, longitude=longitude, city=guiyang)

        liupanshui = City.objects.get(name='六盘水市')

        liupanshui_county = [
            {
                'name': '钟山区',
                'latitude': 26.594502849999998,
                'longitude': 104.85042917396679,
            },

            {
                'name': '水城区',
                'latitude': 26.5511613,
                'longitude': 104.9551167,
            },

            {
                'name': '盘州市',
                'latitude': 25.8678,
                'longitude': 104.6031,
            },

            {
                'name': '六枝特区',
                'latitude': 26.306247,
                'longitude': 105.323507,
            },
        ]

        for county in liupanshui_county:
            name = county['name']
            latitude = county['latitude']
            longitude = county['longitude']
            County.objects.create(name=name, latitude=latitude, longitude=longitude, city=liupanshui)

        zunyi = City.objects.get(name='遵义市')

        zunyi_county = [
            {
                'name': '汇川区',
                'latitude': 27.7538411,
                'longitude': 106.9318421,
            },

            {
                'name': '红花岗区',
                'latitude': 27.6677199,
                'longitude': 106.9443526,
            },

            {
                'name': '播州区',
                'latitude': 27.5396316,
                'longitude': 106.8214413,
            },

            {
                'name': '赤水市',
                'latitude': 28.5914382,
                'longitude': 105.6956747,
            },

            {
                'name': '仁怀市',
                'latitude': 27.8065324,
                'longitude': 106.4099199,
            },

            {
                'name': '桐梓县',
                'latitude': 28.3704847,
                'longitude': 105.9260324,
            },

            {
                'name': '绥阳县',
                'latitude': 28.0663854,
                'longitude': 107.2722459,
            },

            {
                'name': '正安县',
                'latitude': 28.556647,
                'longitude': 107.449628,
            },

            {
                'name': '凤冈县',
                'latitude': 27.932802,
                'longitude': 107.779757,
            },

            {
                'name': '湄潭县',
                'latitude': 27.7379405,
                'longitude': 107.5068323,
            },

            {
                'name': '余庆县',
                'latitude': 27.400864,
                'longitude': 107.664416,
            },

            {
                'name': '习水县',
                'latitude': 28.3161993,
                'longitude': 106.2157148,
            },

            {
                'name': '道真仡佬族苗族自治县',
                'latitude': 28.8695065,
                'longitude': 107.6069394,
            },

            {
                'name': '务川仡佬族苗族自治县',
                'latitude': 28.5663348,
                'longitude': 107.8957142,
            },
        ]

        for county in zunyi_county:
            name = county['name']
            latitude = county['latitude']
            longitude = county['longitude']
            County.objects.create(name=name, latitude=latitude, longitude=longitude, city=zunyi)

        anshun = City.objects.get(name='安顺市')

        anshun_county = [
            {
                'name': '西秀区',
                'latitude': 26.1841025,
                'longitude': 106.0620503,
            },

            {
                'name': '平坝区',
                'latitude': 26.4171781,
                'longitude': 106.2547525,
            },

            {
                'name': '普定县',
                'latitude': 26.3768929,
                'longitude': 105.7338679,
            },

            {
                'name': '镇宁布依族苗族自治县',
                'latitude': 25.9137457,
                'longitude': 105.8203997,
            },

            {
                'name': '关岭布依族苗族自治县',
                'latitude': 25.9481991,
                'longitude': 105.6319533,
            },

            {
                'name': '紫云苗族布依族自治县',
                'latitude': 25.7546983,
                'longitude': 106.0815923,
            },

        ]

        for county in anshun_county:
            name = county['name']
            latitude = county['latitude']
            longitude = county['longitude']
            County.objects.create(name=name, latitude=latitude, longitude=longitude, city=anshun)

        bijie = City.objects.get(name='毕节市')

        bijie_county = [
            {
                'name': '七星关区',
                'latitude': 27.2858633,
                'longitude': 105.2865997,
            },

            {
                'name': '黔西市',
                'latitude': 27.0123382,
                'longitude': 106.0285636,
            },

            {
                'name': '大方县',
                'latitude': 27.1495528,
                'longitude': 105.6003223,
            },

            {
                'name': '金沙县',
                'latitude': 27.4586013,
                'longitude': 106.2721365,
            },

            {
                'name': '织金县',
                'latitude': 26.6414506,
                'longitude': 105.7933078,
            },

            {
                'name': '纳雍县',
                'latitude': 26.7763735,
                'longitude': 105.3776485,
            },

            {
                'name': '赫章县',
                'latitude': 27.192859,
                'longitude': 104.630354,
            },

            {
                'name': '威宁彝族回族苗族自治县',
                'latitude': 27.0349,
                'longitude': 104.067332,
            },

        ]

        for county in bijie_county:
            name = county['name']
            latitude = county['latitude']
            longitude = county['longitude']
            County.objects.create(name=name, latitude=latitude, longitude=longitude, city=bijie)

        tongren = City.objects.get(name='铜仁市')

        tongren_county = [
            {
                'name': '碧江区',
                'latitude': 27.7347312,
                'longitude': 109.1852081,
            },

            {
                'name': '万山区',
                'latitude': 27.6948488,
                'longitude': 109.1765603,
            },

            {
                'name': '江口县',
                'latitude': 27.7026661,
                'longitude': 108.8351361,
            },

            {
                'name': '石阡县',
                'latitude': 27.7347312,
                'longitude': 109.1852081,
            },

            {
                'name': '思南县',
                'latitude': 27.9443973,
                'longitude': 108.2499676,
            },

            {
                'name': '德江县',
                'latitude': 28.2664303,
                'longitude': 108.1114695,
            },

            {
                'name': '玉屏侗族自治县',
                'latitude': 27.335178,
                'longitude': 109.01254,
            },

            {
                'name': '印江土家族苗族自治县',
                'latitude': 27.9966567,
                'longitude': 108.4056876,
            },

            {
                'name': '沿河土家族自治县',
                'latitude': 28.65428575,
                'longitude': 108.25430598992476,
            },

            {
                'name': '松桃苗族自治县',
                'latitude': 27.8864411,
                'longitude': 109.2770033,
            },
        ]

        for county in tongren_county:
            name = county['name']
            latitude = county['latitude']
            longitude = county['longitude']
            County.objects.create(name=name, latitude=latitude, longitude=longitude, city=tongren)

        qianxinan = City.objects.get(name='黔西南布依族苗族自治州')

        qianxinan_county = [
            {
                'name': '兴义市',
                'latitude': 25.0947613,
                'longitude': 104.8935472,
            },

            {
                'name': '兴仁市',
                'latitude': 25.50503,
                'longitude': 105.19988,
            },

            {
                'name': '普安县',
                'latitude': 25.7602213,
                'longitude': 104.9855973,
            },

            {
                'name': '晴隆县',
                'latitude': 25.4549,
                'longitude': 105.6417,
            },

            {
                'name': '望谟县',
                'latitude': 25.1693666,
                'longitude': 106.0875769,
            },

            {
                'name': '册亨县',
                'latitude': 24.96433,
                'longitude': 105.7943,
            },

            {
                'name': '安龙县',
                'latitude': 25.2109136,
                'longitude': 105.3149496,
            },

        ]

        for county in qianxinan_county:
            name = county['name']
            latitude = county['latitude']
            longitude = county['longitude']
            County.objects.create(name=name, latitude=latitude, longitude=longitude, city=qianxinan)

        qiandongnan = City.objects.get(name='黔东南苗族侗族自治州')

        qiandongnan_county = [
            {
                'name': '凯里市',
                'latitude': 26.5710542,
                'longitude': 107.9769525,
            },

            {
                'name': '黄平县',
                'latitude': 26.953575,
                'longitude': 107.845834,
            },

            {
                'name': '施秉县',
                'latitude': 27.0850121,
                'longitude': 108.1114495,
            },

            {
                'name': '三穗县',
                'latitude': 26.9607344,
                'longitude': 108.751655,
            },

            {
                'name': '镇远县',
                'latitude': 27.134993,
                'longitude': 108.45421,
            },

            {
                'name': '岑巩县',
                'latitude': 27.35551,
                'longitude': 108.69193,
            },

            {
                'name': '天柱县',
                'latitude': 26.9130012,
                'longitude': 109.2034226,
            },

            {
                'name': '锦屏县',
                'latitude': 26.6774641,
                'longitude': 109.1938575,
            },

            {
                'name': '剑河县',
                'latitude': 26.6739142,
                'longitude': 108.6856216,
            },

            {
                'name': '台江县',
                'latitude': 26.609506,
                'longitude': 108.318147,
            },

            {
                'name': '黎平县',
                'latitude': 26.2361643,
                'longitude': 109.1309824,
            },

            {
                'name': '榕江县',
                'latitude': 25.9356793,
                'longitude': 108.5175229,
            },

            {
                'name': '从江县',
                'latitude': 25.7569141,
                'longitude': 108.9036051,
            },

            {
                'name': '雷山县',
                'latitude': 26.3825439,
                'longitude': 108.0753069,
            },

            {
                'name': '麻江县',
                'latitude': 26.460601,
                'longitude': 107.643667,
            },

            {
                'name': '丹寨县',
                'latitude': 26.244187,
                'longitude': 107.895155,
            },

        ]

        for county in qiandongnan_county:
            name = county['name']
            latitude = county['latitude']
            longitude = county['longitude']
            County.objects.create(name=name, latitude=latitude, longitude=longitude, city=qiandongnan)

        qiannan = City.objects.get(name='黔南布依族苗族自治州')

        qiannan_county = [
            {
                'name': '都匀市',
                'latitude': 26.1908679,
                'longitude': 107.4526239,
            },

            {
                'name': '福泉市',
                'latitude': 26.8068033,
                'longitude': 107.4565621,
            },

            {
                'name': '荔波县',
                'latitude': 25.4084427,
                'longitude': 107.8785657,
            },

            {
                'name': '贵定县',
                'latitude': 26.39759,
                'longitude': 107.187411,
            },

            {
                'name': '瓮安县',
                'latitude': 27.14594,
                'longitude': 107.406364,
            },

            {
                'name': '独山县',
                'latitude': 25.726227,
                'longitude': 107.567303,
            },

            {
                'name': '平塘县',
                'latitude': 25.801017,
                'longitude': 107.209266,
            },

            {
                'name': '罗甸县',
                'latitude': 25.483333,
                'longitude': 106.65,
            },

            {
                'name': '长顺县',
                'latitude': 26.0005466,
                'longitude': 106.4273045,
            },

            {
                'name': '龙里县',
                'latitude': 26.516296,
                'longitude': 106.954644,
            },

            {
                'name': '惠水县',
                'latitude': 26.0196756,
                'longitude': 106.7430503,
            },

            {
                'name': '三都水族自治县',
                'latitude': 25.9884537,
                'longitude': 107.8704841,
            },
        ]

        for county in qiannan_county:
            name = county['name']
            latitude = county['latitude']
            longitude = county['longitude']
            County.objects.create(name=name, latitude=latitude, longitude=longitude, city=qiannan)







