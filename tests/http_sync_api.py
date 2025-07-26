import time

import httpx
from charset_normalizer import from_bytes

from tranport import ForwardingTransport

client = httpx.Client(transport=ForwardingTransport())
# client = httpx.Client()

# "https://httpbin.org/get"
# url = 'https://h5api.m.taobao.com/h5/mtop.taobao.pcdetail.data.get/1.0/?jsv=2.7.5&appKey=12574478&t=1753253502724&sign=8d3ef6c50bc7b8e5ab6d26245923a7c3&api=mtop.taobao.pcdetail.data.get&v=1.0&isSec=0&ecode=0&timeout=10000&ttid=2022%40taobao_litepc_9.17.0&AntiFlood=true&AntiCreep=true&dataType=json&valueType=string&type=json&data=%7B%22id%22%3A%22920151030898%22%2C%22detail_v%22%3A%223.3.2%22%2C%22exParams%22%3A%22%7B%5C%22id%5C%22%3A%5C%22920151030898%5C%22%2C%5C%22pvid%5C%22%3A%5C%221ca2c056-933f-43bb-ab10-c20fe888f4b2%5C%22%2C%5C%22scm%5C%22%3A%5C%221007.40986.420852.520371%5C%22%2C%5C%22skuId%5C%22%3A%5C%225965041306559%5C%22%2C%5C%22spm%5C%22%3A%5C%22a21bo.jianhua%2Fa.201876.d1.5af92a89DbvnMC%5C%22%2C%5C%22utparam%5C%22%3A%5C%22%7B%5C%5C%5C%22abid%5C%5C%5C%22%3A%5C%5C%5C%22520371%5C%5C%5C%22%2C%5C%5C%5C%22item_ctr%5C%5C%5C%22%3A0%2C%5C%5C%5C%22x_object_type%5C%5C%5C%22%3A%5C%5C%5C%22item%5C%5C%5C%22%2C%5C%5C%5C%22pc_pvid%5C%5C%5C%22%3A%5C%5C%5C%221ca2c056-933f-43bb-ab10-c20fe888f4b2%5C%5C%5C%22%2C%5C%5C%5C%22item_cvr%5C%5C%5C%22%3A0%2C%5C%5C%5C%22mix_group%5C%5C%5C%22%3A%5C%5C%5C%22%5C%5C%5C%22%2C%5C%5C%5C%22pc_scene%5C%5C%5C%22%3A%5C%5C%5C%2220001%5C%5C%5C%22%2C%5C%5C%5C%22item_ecpm%5C%5C%5C%22%3A0%2C%5C%5C%5C%22aplus_abtest%5C%5C%5C%22%3A%5C%5C%5C%22d0f6f2453320cd2e232fa957203ab976%5C%5C%5C%22%2C%5C%5C%5C%22tpp_buckets%5C%5C%5C%22%3A%5C%5C%5C%2230986%23420852%23module%5C%5C%5C%22%2C%5C%5C%5C%22x_object_id%5C%5C%5C%22%3A920151030898%2C%5C%5C%5C%22ab_info%5C%5C%5C%22%3A%5C%5C%5C%2230986%23420852%23-1%23%5C%5C%5C%22%7D%5C%22%2C%5C%22xxc%5C%22%3A%5C%22home_recommend%5C%22%2C%5C%22queryParams%5C%22%3A%5C%22id%3D920151030898%26ltk2%3D17532534875665q3kkttoe73w8llli4zufb%26pvid%3D1ca2c056-933f-43bb-ab10-c20fe888f4b2%26scm%3D1007.40986.420852.520371%26skuId%3D5965041306559%26spm%3Da21bo.jianhua%252Fa.201876.d1.5af92a89DbvnMC%26utparam%3D%257B%2522abid%2522%253A%2522520371%2522%252C%2522item_ctr%2522%253A0%252C%2522x_object_type%2522%253A%2522item%2522%252C%2522pc_pvid%2522%253A%25221ca2c056-933f-43bb-ab10-c20fe888f4b2%2522%252C%2522item_cvr%2522%253A0%252C%2522mix_group%2522%253A%2522%2522%252C%2522pc_scene%2522%253A%252220001%2522%252C%2522item_ecpm%2522%253A0%252C%2522aplus_abtest%2522%253A%2522d0f6f2453320cd2e232fa957203ab976%2522%252C%2522tpp_buckets%2522%253A%252230986%2523420852%2523module%2522%252C%2522x_object_id%2522%253A920151030898%252C%2522ab_info%2522%253A%252230986%2523420852%2523-1%2523%2522%257D%26xxc%3Dhome_recommend%5C%22%2C%5C%22domain%5C%22%3A%5C%22https%3A%2F%2Fitem.taobao.com%5C%22%2C%5C%22path_name%5C%22%3A%5C%22%2Fitem.htm%5C%22%2C%5C%22pcSource%5C%22%3A%5C%22pcTaobaoMain%5C%22%2C%5C%22appKey%5C%22%3A%5C%223q2%2B7wX9z8JkLmN1oP5QrStUvWxYzA0B%5C%22%2C%5C%22refId%5C%22%3A%5C%22OQLAXmC4wfP0IakLEpSUmju3UcFSOfCMe1183XEZ6KI%3D%5C%22%2C%5C%22nonce%5C%22%3A%5C%22fui4Y5l6gb2FCEKCsU3%2F8QvyLEyC24NuxlShO5YNUCo%3D%5C%22%2C%5C%22feTraceId%5C%22%3A%5C%22e0c89dce-3ff2-4803-bc8c-7d07a0dfa220%5C%22%7D%22%7D'
headers = {
    # 'bx-umidtoken': 'T2gA7hdNyYEDlQNqHL5qBBLTO0gnaw4WFkpy_fBEFlMhde4kLg_6AA1TCfe6M2-ZRR8=',
    # 'x-pipu2': "h%7Bdufj%7Cvljommtc%7Dv%2C(8%2C8%2F)0%3E!%3A%26'9%3A%606%2B%2F%2Fg*1%3B%3A3%2B%3D%3C*g*1%3B%3A3%2B%3D%3C*g*1%3B%3A3%2B%3D%3C*go%7Bo%7B",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://item.taobao.com",
    "referer": "https://item.taobao.com",
    "cookie": 'thw=cn; wk_cookie2=19f87593975a3f9bd7b260a1fe92ce8f; wk_unb=UoTUOqkyuVGCXA%3D%3D; aui=1580993065; cookie2=125d44a46272791eaca7fca31a273a71; t=7d19e9bcd1bed6fb395e5de8c45df1a8; _tb_token_=71b1feebe5b63; sgcookie=E100UJeih4P9%2F9CO406ZMYbow8YaHdbfuSSX3ulinUQeZogBMdt5B%2FsLIaOTQaKFLnJF6yAIyDZCmbQR%2BQZDc3KX8EFUKwKMIrjCobQ0L5Psg7EMqJqXYflqDwHyHSfRelc5SL7qvFFIYWKyIlYJp8e9BA%3D%3D; tracknick=; xlly_s=1; mtop_partitioned_detect=1; _m_h5_tk=d669faa1bbf906fc5d71fa21b7f1e8b5_1753256638922; _m_h5_tk_enc=6d236082ebb8a84a9391a4149939b4ae; sca=289541c2; bxuab=0; isg=BHh4lepuZFtoWoggSu8cnp2mSSYK4dxrgA7eBLLp2rNozRm3WvFg-ozlgcX9m5RD; tfstk=gX6-Zfa6Lr4l8hWJmgPmxj9csxE0SSjPDaSsKeYoOZQArG1kZMTHpwQdJUAQzLXdkaj1ZQjCKH6pUtfoKU4ypM_MpP4gIRjP4LJQSPjv2Z59dHwHRSA72fig2P4gI-VScpU8Sw23xwwvYEtSFpG7DmT2x49BPBgjGhTXdpMWAmiXjhMSdp_CcoKele9BNwObDHlr20LnVeHdwg-13lo9VvMCH3d7igTjdnWv2QL1VtkIdf-JwFsWlzgkOjRfYBBEYvdhV17efag7JeWAcT115rckP1Kdj6Q_xb-D9TJvRTwZXE6RvtdPi4GWXLLJ1TO_plI6OsBvETaE_ijvPCpciSzktLQR_FR7gr7dDUbCeIg8oefGmTOA5rDA8BCCEK67lRIrROXOSv0MWHc7DohETQt4LZheVvptCUxvSocmTXRD0nLgDohETQt2DFq0nXlein5..',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}

body = {
    "jsv": "2.7.5",
    "appKey": "12574478",
    "t": "1753266490635",
    "sign": "a1926a06b852e0e4467e9fd3db3a4b94",
    "api": "mtop.taobao.pcdetail.data.get",
    "v": "1.0",
    "isSec": "0",
    "ecode": "0",
    "timeout": "10000",
    "ttid": "2022@taobao_litepc_9.17.0",
    "AntiFlood": "true",
    "AntiCreep": "true",
    "dataType": "json",
    "valueType": "string",
    "type": "json",
    "data": {"id": "914207844760", "detail_v": "3.3.2",
             "exParams": "{\"id\":\"914207844760\",\"pvid\":\"ea5ff2f2-b3fa-409a-a0e1-97065611df52\",\"scm\":\"1007.40986.420852.520372\",\"skuId\":\"5038612183860\",\"spm\":\"a21bo.jianhua/a.201876.d13.5af92a89CG15f1\",\"utparam\":\"{\\\"abid\\\":\\\"520372\\\",\\\"item_ctr\\\":0,\\\"x_object_type\\\":\\\"item\\\",\\\"pc_pvid\\\":\\\"ea5ff2f2-b3fa-409a-a0e1-97065611df52\\\",\\\"item_cvr\\\":0,\\\"mix_group\\\":\\\"\\\",\\\"pc_scene\\\":\\\"20001\\\",\\\"item_ecpm\\\":0,\\\"aplus_abtest\\\":\\\"cb98573c80be78070270b13b66228028\\\",\\\"tpp_buckets\\\":\\\"30986#420852#module\\\",\\\"x_object_id\\\":677811311950,\\\"ab_info\\\":\\\"30986#420852#-1#\\\"}\",\"xxc\":\"home_recommend\",\"queryParams\":\"id=677811311950&ltk2=1753266480249a6wq1tn94ypmp5s0a6usqq&pvid=ea5ff2f2-b3fa-409a-a0e1-97065611df52&scm=1007.40986.420852.520372&skuId=5038612183860&spm=a21bo.jianhua%2Fa.201876.d13.5af92a89CG15f1&utparam=%7B%22abid%22%3A%22520372%22%2C%22item_ctr%22%3A0%2C%22x_object_type%22%3A%22item%22%2C%22pc_pvid%22%3A%22ea5ff2f2-b3fa-409a-a0e1-97065611df52%22%2C%22item_cvr%22%3A0%2C%22mix_group%22%3A%22%22%2C%22pc_scene%22%3A%2220001%22%2C%22item_ecpm%22%3A0%2C%22aplus_abtest%22%3A%22cb98573c80be78070270b13b66228028%22%2C%22tpp_buckets%22%3A%2230986%23420852%23module%22%2C%22x_object_id%22%3A677811311950%2C%22ab_info%22%3A%2230986%23420852%23-1%23%22%7D&xxc=home_recommend\",\"domain\":\"https://item.taobao.com\",\"path_name\":\"/item.htm\",\"pcSource\":\"pcTaobaoMain\",\"appKey\":\"3q2+7wX9z8JkLmN1oP5QrStUvWxYzA0B\",\"refId\":\"qpwf1ia3TROBr4pZeesSCnEuwmNBRqZmi73VCLc/9ac=\",\"nonce\":\"Qyb3y3WsGXsF7HK8wMFVtSz0yqIjkyfkmpeGBpV6CE4=\",\"feTraceId\":\"2cc93268-c36d-469a-82e8-5d95cfed039a\"}"}
}

url = 'https://h5api.m.taobao.com/h5/mtop.taobao.pcdetail.data.get/1.0/'
start = time.time()
resp = client.get(url=url, params=body, headers=headers)
end = time.time()
print(resp.text)
print(end - start)

# detected = from_bytes(resp.content).best()
# decoded_text = detected.text if detected else resp.content.decode('utf-8', errors='replace')


print(client.get(url='https://www.taobao.com').text)
