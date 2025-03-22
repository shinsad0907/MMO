# link https://anotepad.com/notes/gnb2q4wb
import requests
from time import sleep

re = requests.get('https://anotepad.com/notes/gnb2q4wb').text
key = (re.split('<div class="plaintext ">')[1].split('</div>')[0])
if key == 'open':
    import re
    from time import sleep
    class spamcmt():
        def __init__(self,cookie,uge) -> None:
            ck = f'{cookie}'
            us = f'{uge}'
            try:
                self.cookies = {
                    'sb': ck.split('sb=')[1].split(';')[0],
                    'datr':ck.split('datr=')[1].split(';')[0] ,
                    'c_user': ck.split('c_user=')[1].split(';')[0],
                    'xs': ck.split('xs=')[1].split(';')[0],
                    'fr': ck.split('fr=')[1].split(';')[0],
                    'presence': ck.split('presence=')[1].split(';')[0],
                    
                }
            except:
                self.cookies = {
                    'sb': ck.split('sb=')[1].split(';')[0],
                    'datr':ck.split('datr=')[1].split(';')[0] ,
                    'c_user': ck.split('c_user=')[1].split(';')[0],
                    'xs': ck.split('xs=')[1].split(';')[0],
                    'fr': ck.split('fr=')[1].split(';')[0],
                    
                }
            self.headers = {
                'authority': 'mbasic.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'cache-control': 'no-cache',
                # 'cookie': 'sb=ghGyZMQNd-t6C2gxm9HaLy-K; datr=06z5ZKQ_PD93TumELUma7cKL; c_user=61553593387589; m_page_voice=61553593387589; wd=1920x953; xs=26%3AxiRE_Mj5FTTHXw%3A2%3A1702093751%3A-1%3A3840%3A%3AAcXgp1cnQnA_P0BM0gKajywPOSKux8f9lBXZkvPJLbNV; fr=1F8xDEivHDXIRkOGa.AWV3ZyPVlx1mv7TVdNvZW1k28PM.BlrnSJ.QI.AAA.0.0.BlrnSO.AWVA8j9XCWw; presence=C%7B%22t3%22%3A%5B%7B%22o%22%3A0%2C%22i%22%3A%22u.100084875303481%22%7D%5D%2C%22utc3%22%3A1705931980995%2C%22v%22%3A1%7D',
                'dpr': '1',
                'pragma': 'no-cache',
                'referer': 'https://mbasic.facebook.com/groups/?category=membership&ref_component=mbasic_home_header&ref_page=%2Fwap%2Fprofile_tribe.php&refid=18&paipv=0&eav=AfYJ6S5zcXGn5g1V7l6Vi5yawN-eek0udvObJuP5HH424cC-UOXTCLarroH1kSpcYZc',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.225", "Google Chrome";v="120.0.6099.225"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"10.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': f'{us}',
                'viewport-width': '958',
            }
            self.get_cookies = {
                'cf_clearance': 'LInT285MT09ex.W7etumJ3MhBKe0vREdILKMvGNoErc-1703686542-0-2-30d11ca0.cde8bdff.e0249095-150.0.0',
            }

            self.get_headers = {
                'authority': 'id.traodoisub.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'cf_clearance=LInT285MT09ex.W7etumJ3MhBKe0vREdILKMvGNoErc-1703686542-0-2-30d11ca0.cde8bdff.e0249095-150.0.0',
                'origin': 'https://id.traodoisub.com',
                'pragma': 'no-cache',
                'referer': 'https://id.traodoisub.com/',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': f'{us}',
                'x-requested-with': 'XMLHttpRequest',
            }
        def main(self):
            self.gr = []
            self.namegr = []
            print('[1] Spam Bài Viết Cố Định')
            print('[2] Spam Groups Cố Định')
            print('[3] Spam Groups Ngẫu Nhiên')
            self.chosse_cn =int(input('Chọn Chức Năng: '))
            def groups():
                response = requests.get(
                    # 'https://mbasic.facebook.com/groups/httpswww.hcm789.comid14029408/',
                    'https://mbasic.facebook.com/groups/',
                    # params=params,
                    cookies=self.cookies,
                    headers=self.headers,
                ).text
                for i in response.split():  
                    match = re.search(r'href="https://mbasic.facebook.com/groups/([^"]+)"', i)
                    thong_tin_page = re.search(r'href="https://mbasic.facebook.com/groups/([^"]+)"', i)
                    if match:
                        url = match.group(1)
                        
                        # print(response_json)
                        # print(url['id']);sleep(3)
                        self.gr.append(url)
                for i in self.gr:

                    response = requests.get(f'https://mbasic.facebook.com/groups/{i}', cookies=self.cookies, headers=self.headers).text
                    self.namegr.append(response.split('<title>')[1].split('</title>')[0])
                # print(self.gr)
                stt=0
                if len(self.gr) == 0:
                    print('khong co gr')
                    exit()
                for i in self.namegr:
                    print(f'[{stt}] chon gr de lay tst: {i}')
                    stt = stt + 1
                print('------------------------------------------')
                self.choose = (input('choose: '))
                
                print('------------------------------------------')
            if self.chosse_cn == 3:
                groups()
            if self.chosse_cn == 2:
                self.linkgrcc = input('Link Groups: ')
            if self.chosse_cn == 1:
                self.linktst = input('Link Bài Viết: ')
                data = {
                        'link': f'{self.linktst}',
                    }

                response = requests.post('https://id.traodoisub.com/api.php', cookies=self.get_cookies, headers=self.get_headers, data=data)
                response_json = response.json()
                self.getid = response_json['id']
            self.sp = input('nhap noi dung can spam: ')
            self.dung = int(input('baonhieu cmt thi dung tool: '))
            self.delay = int(input('delay tool: '))
            def tst():
                self.id= []
                self.loads = []
                # print(self.gr)
                
                if self.chosse_cn == 2:
                    data = {
                        'link': f'{self.linkgrcc}',
                    }

                    response = requests.post('https://id.traodoisub.com/api.php', cookies=self.get_cookies, headers=self.get_headers, data=data)
                    response_json = response.json()
                    self.getid = response_json['id']
                    if len(self.loads) > 0:
                        response = requests.get(
                                f'https://mbasic.facebook.com/groups/{self.loads[i]}',
                                # 'https://mbasic.facebook.com/groups/?seemore&refid=27&paipv=0&eav=AfZG2N2g7_tgWqlx8Yo8R6Z6l5UyShi0R6LmN_krbQap0Hte1NbRIoY1Xlmepl3bbv4',
                                # params=params,    
                                cookies=self.cookies,
                                headers=self.headers,
                            ).text
                        self.loads.pop(0)
                    else:
                        response = requests.get(
                            f'https://mbasic.facebook.com/groups/{self.getid}',
                            # 'https://mbasic.facebook.com/groups/?seemore&refid=27&paipv=0&eav=AfZG2N2g7_tgWqlx8Yo8R6Z6l5UyShi0R6LmN_krbQap0Hte1NbRIoY1Xlmepl3bbv4',
                            # params=params,    
                            cookies=self.cookies,
                            headers=self.headers,
                        ).text
                    # print(response)
                    for i in response.split():
                    # if i[stt].split('id="')[1].split('"><a')[0][0:4] == 'like':
                    
                    #     # print(url)
                    # # if 'Xem thêm bài viết' in i: href="/groups/6298669586831641
                    #     self.loads.append(url)
                        match = re.search(r'id="like_([^"]+)"', i)
                        if match:
                            url = match.group(1)
                            # print('id bài viết trên nhóm mới gần nhất là: '+url)
                            self.id.append(url)
                    match = re.search(r'bacr=([^"]+)"', i)
                    if match:
                        url = match.group(1)
                        self.loads.append(url)
                if self.chosse_cn == 3:
                    for i in range(len(self.choose.split())):
                        if len(self.loads) > len(self.choose.split()) - 1:

                        # lay uid tst va link xem them
                            response = requests.get(
                                f'https://mbasic.facebook.com/groups/{self.loads[i]}',
                                # 'https://mbasic.facebook.com/groups/?seemore&refid=27&paipv=0&eav=AfZG2N2g7_tgWqlx8Yo8R6Z6l5UyShi0R6LmN_krbQap0Hte1NbRIoY1Xlmepl3bbv4',
                                # params=params,    
                                cookies=self.cookies,
                                headers=self.headers,
                            ).text
                            self.loads.pop(0)
                        else:
                       
                        
                            response = requests.get(
                                f'https://mbasic.facebook.com/groups/{self.gr[int(self.choose.split()[i])]}',
                                # 'https://mbasic.facebook.com/groups/?seemore&refid=27&paipv=0&eav=AfZG2N2g7_tgWqlx8Yo8R6Z6l5UyShi0R6LmN_krbQap0Hte1NbRIoY1Xlmepl3bbv4',
                                # params=params,
                                cookies=self.cookies,
                                headers=self.headers,
                            ).text
                    for i in response.split():
                    # if i[stt].split('id="')[1].split('"><a')[0][0:4] == 'like':
                    
                    #     # print(url)
                    # # if 'Xem thêm bài viết' in i: href="/groups/6298669586831641
                    #     self.loads.append(url)
                        match = re.search(r'id="like_([^"]+)"', i)
                        if match:
                            url = match.group(1)
                            # print('id bài viết trên nhóm mới gần nhất là: '+url)
                            self.id.append(url)
                        match = re.search(r'bacr=([^"]+)"', i)
                        if match:
                            url = match.group(1)
                            self.loads.append(url)
                print('------------------------------------------')
                print(f'success {len(self.id)} link bai viet')
                print('------------------------------------------')
                
            # tst()
            self.stt = 0
            

            def cmt():
             
                if self.chosse_cn == 1:
                    id = self.getid
                    r = requests.get(f'https://mbasic.facebook.com/{id}', cookies=self.cookies, headers=self.headers).url
                    accest = requests.get(r, cookies=self.cookies, headers=self.headers).text
                    nodecmt = 'https://mbasic.facebook.com/a/comment.php?fs='+accest.split('/a/comment.php?fs=')[1].split('"')[0].replace("amp;", '')
                    fb_dtsg = accest.split('name="fb_dtsg" value="')[1].split('"')[0]
                    jazoest = accest.split('name="jazoest" value="')[1].split('"')[0]
                    data = {
                        'fb_dtsg': fb_dtsg,
                        'jazoest': jazoest,
                        'comment_text': f'{self.sp}',
                    }
                    requests.post(nodecmt, data=data,cookies=self.cookies, headers=self.headers)
                    print(f'{self.stt} done {id}')
                    self.stt = self.stt + 1
                    sleep(self.delay)
                    
                    
                try:
                    tst()
                    
                    r = requests.get(f'https://mbasic.facebook.com/{self.id[0]}', cookies=self.cookies, headers=self.headers).url
                    accest = requests.get(r, cookies=self.cookies, headers=self.headers).text
                    nodecmt = 'https://mbasic.facebook.com/a/comment.php?fs='+accest.split('/a/comment.php?fs=')[1].split('"')[0].replace("amp;", '')
                    fb_dtsg = accest.split('name="fb_dtsg" value="')[1].split('"')[0]
                    jazoest = accest.split('name="jazoest" value="')[1].split('"')[0]
                    data = {
                        'fb_dtsg': fb_dtsg,
                        'jazoest': jazoest,
                        'comment_text': f'{self.sp}',
                    }
                    requests.post(nodecmt, data=data,cookies=self.cookies, headers=self.headers)
                    
                    print(f'{self.stt} done {self.id[0]}')
                    self.stt = self.stt + 1
                    sleep(self.delay)
                    self.id.pop(0)
                        
                        
                except:
                    print('lỗi bài viết')
            if self.chosse_cn == 1:
                for i in range(self.dung):
                    cmt()
            else:
                for i in range(self.dung):
                    try:
                        cmt()
                    except:
                        cmt()
    spamcmt(input('Input Cookie: '),input('input user-agent: ')).main()
else:
    print('tool da dong')