import requests ,random
from requests import get,post

discord= "https://discord.com/api/webhooks/1049998270891569243/tyQfvFsOn6YwMQlxroUuj9qwuXYvkV4bzwgR9uvwcUNYztV_adAZrAAKtdX1NoRJHenp"
#my accounts for instagram @014931500 / @Jpno 
num= int(input("Enter The number of usernames ? :"))

while True:
    chars="qw_ertyuiopa.123456789.0sdfghjkl_z.xc_vbn_mqwer.t_yuiopasd0123466.559856_fghjkl.zxcvbnmqwert000.yuio_pasdf.ghjklzxc.vbnmqw.ertyuiopasd_fghj.klzx.cvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890.";user=""
    for user in range(1):
        user=""
        for item in range(num):
            user+=random.choice(chars)	

        url= "https://www.youtube.com/@"+user 
        userhead={
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,ar;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        re = requests.get(url , headers=userhead)
        if re.status_code==404:
            print("This user av now "+user)
            data = {}
            gif = f"https://skinmc.net/en/achievement/8/Done+/This+{user}+Available"
            data["embeds"] = [{ "description" : f"**User Youtube **","thumbnail" : {"url": f"https://skinmc.net/en/achievement/8/Done+/This+{user}+Available"},"footer" : {"text": f'\t\t By: Muath '}}]
            post(discord, json=data)
        else:print("Not Good "+user)
