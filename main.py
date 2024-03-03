import flet as ft
import json
import requests

index = 3

def main(page: ft.Page):

    def setIndexZero(e):
        global index
        index = 0
    
    def setIndexThree(e):
        global index
        index = 3

    def play_music(e):
        # アクセストークンを取得する
        headers = {
            'Authorization': 'Basic ZDMxNGNhZjdhODIwNDlmZWIwYzgwYzZiOTIzZGNkODA6YzUxOTU3ZmNiYWVhNDAwMDhlYjRkOGJhYzgwMzQwYmU=',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'grant_type': 'refresh_token',
            'refresh_token': 'AQDgisALHNFTFI2N1Rlj9_x1XgJdt6sB3wQXHDsvJtgBObpRvAD4O5bx1RjCIeBzA3T4wLSuoFyNyL0fsAvC3aBioPZxyfx8N7bwT6rn4J51V5crgBLdkWQdqfBwhBbd5HA',
        }

        response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

        access_token = json.loads(response.text)["access_token"]

        # APIを叩く
        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
        }

        json_data = {
            'context_uri': 'spotify:playlist:6OJHpbVGr7JigmFEU9xq0O',
            'offset': {
                'position': index,
            },
            'position_ms': 0,
        }

        response = requests.put('https://api.spotify.com/v1/me/player/play?device_id=4bb8a462453c69392da0985c0084e61c96dadbc7', headers=headers, json=json_data)

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.ElevatedButton("祝日天国", on_click=play_music, on_hover=setIndexZero),
        ft.ElevatedButton("ビームが撃てたらいいのに", on_click=play_music, on_hover=setIndexThree),
    )

ft.app(target=main)