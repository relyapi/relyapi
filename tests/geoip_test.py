"""
https://github.com/P3TERX/GeoLite.mmdb?tab=readme-ov-file
https://github.com/Loyalsoldier/geoip/blob/release/GeoLite2-Country-CSV.zip
https://github.com/Loyalsoldier/geoip
"""
import geoip2.database

reader = geoip2.database.Reader(r'GeoLite2-City.mmdb')

response = reader.city('91.103.120.55')  # 输入 IP

country = response.country.name  # 国家
region = response.subdivisions.most_specific.name  # 省/州
city = response.city.name  # 城市

print(f"{country} - {region} - {city}")

reader.close()
