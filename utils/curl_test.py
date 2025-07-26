import curl_cffi

"""
https://github.com/FlareSolverr/FlareSolverr
"""
r = curl_cffi.get("https://freedium.cfd/https://medium.com/the-riff/ozzy-osbourne-legacy-of-a-madman-264a0a6c30c5",
                  impersonate="chrome")

# r = requests.get("https://freedium.cfd/https://medium.com/the-riff/ozzy-osbourne-legacy-of-a-madman-264a0a6c30c5",
#                  impersonate="chrome")
print(r.text)
