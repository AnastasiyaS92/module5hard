from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def log_in(self, login: str, password: str):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def add(self, *args):
        for film in args:
            if film not in self.videos:
                self.videos.append(film)

    def get_videos(self, word):
        list_film = []
        for video in self.videos:
            if word.upper() in video.title.upper():
                list_film.append(video.title)
        return list_film

    def watch_video(self, film):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео.')
            return

        for element in self.videos:
            if element.title == film:
                if element.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу!')
                    return

                for i in range(element.duration):
                    print(f'{i + 1}', end=' ')
                    sleep(1)
                    element.time_now += 1
                element.time_now = 0
                print('Конец видео.')
                sleep(2)


if __name__ == '__main__':
    ur = UrTube()
    v1: Video = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
