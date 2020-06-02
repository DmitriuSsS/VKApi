import requests


access_token = '43f280d943f280d943f280d92c4380e039443f243f280d91d2420341a6e2edfb7ef4683'
version = '5.107'


class GetFriendsOption:
    @staticmethod
    def get_friends(user_id: int) -> list:
        offset = 0
        count = 100
        friends = []
        while True:
            response = requests.get('https://api.vk.com/method/friends.get',
                                    params={
                                        'access_token': access_token,
                                        'v': version,
                                        'user_id': user_id,
                                        'fields': 'domain',
                                        'count': count,
                                        'offset': offset
                                    })
            next_friends = response.json()
            friends += map(lambda friend:
                           {'id': friend['id'], 'first_name': friend['first_name'], 'last_name': friend['last_name']},
                           next_friends['response']['items'])

            if len(next_friends) < count:
                break

        return friends

    @staticmethod
    def print_friends(friends: list):
        if not friends:
            print("У данного пользователя нет друзей :(")
        else:
            print("Друзья этого пользователя:")
            for friend in friends:
                print(f'> ID: {friend["id"]}, Имя: {friend["first_name"]}, Фамилия: {friend["last_name"]}')


class GetAlbumsOption:
    @staticmethod
    def get_albums(owner_id: int) -> list:
        response = requests.get('https://api.vk.com/method/photos.getAlbums',
                                params={
                                    'access_token': access_token,
                                    'v': version,
                                    'owner_id': owner_id,
                                    'fields': 'domain'
                                })

        return list(
            map(lambda album: {'id': album['id'], 'title': album['title'], 'description': album['description']},
                response.json()['response']['items'])
        )

    @staticmethod
    def print_albums(albums: list):
        if not albums:
            print("У данного пользователя нет альбомов")
        else:
            print("Альбомы данного пользователя")
            for album in albums:
                line = f'ID: {album["id"]}, Название: {album["title"]}'
                if album["description"]:
                    line += f'Описание: {album["description"]}'
                print(line)
