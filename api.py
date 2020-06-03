import sys
import argparse

from Options.options import GetFriendsOption, GetAlbumsOption


def show_friends(arguments): GetFriendsOption.print_friends(GetFriendsOption.get_friends(arguments.user_id))


def show_albums(arguments): GetAlbumsOption.print_albums(GetAlbumsOption.get_albums(arguments.owner_id))


def get_parser():
    parser_ = argparse.ArgumentParser(description='Программа для простейшего взаимодействия с api.vk.com',
                                      epilog='Автор: Шимаев Дмитрий КН203')
    subparsers = parser_.add_subparsers()

    # region get_friend
    parser_get_friends = subparsers.add_parser('friends', help='Возвращает список друзей указанного пользователя')
    parser_get_friends.add_argument('-id', '--user_id', type=int, help='id пользователя')
    parser_get_friends.set_defaults(function=show_friends)
    # endregion

    # region get_albums
    parser_get_albums = subparsers.add_parser('albums', help='Возвращает список альбомов указанного пользователя')
    parser_get_albums.add_argument('-id', '--owner_id', type=int, help='id пользователя')
    parser_get_albums.set_defaults(function=show_albums)
    # endregion

    return parser_


if __name__ == '__main__':
    parser = get_parser()
    if len(sys.argv) == 1:
        parser.parse_args(['-h']).function()
    else:
        args = parser.parse_args()
        args.function(args)
