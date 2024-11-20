class NADataHandling:
    def __init__(self):
        self.study = [
            "https://v39.moodle.uniduna.hu/my/",
            "https://nappw.dfad.duf.hu/hallgato_ng/login",
            "ms-teams.exe"
        ]
        self.personalProjects = [
            "D:\Program Files\Microsoft Visual Studio\\2022\Community\Common7\IDE\\devenv.exe",
            "https://github.com/login",
            "https://www.youtube.com/@GameDeveloperTraining",
            "https://www.youtube.com/@sebastiankamph"
        ]
        self.ownTime =[
            "https://www.youtube.com/",
            "https://discord.com/channels/@me",
            "D:\Steam\\Steam.exe"
        ]

    def NAgetStudy(self):
        return self.study

    def NAgetProjects(self):
        return self.personalProjects

    def NAgetOwnTime(self):
        return self.ownTime
