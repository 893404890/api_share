from API.baseapi import BaseApi
class LoginApi(BaseApi):
    def login(self,username,pwd,captcha):
        headers = {'Content-Type': 'application/json'}
        r=self.request('post',url='/rest/login',json={
  "accountName": username,
  "password": pwd,
  "captcha": captcha},
                     headers=headers
                     )
        return r