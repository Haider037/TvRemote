from remoteGui import *


class Television(QMainWindow, Ui_TvRemote):
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        This program initializes all the necessary
        variables
        """
        super().__init__()
        self.setupUi(self)
        self.powerButton.clicked.connect(lambda: self.power())
        self.muteButton.clicked.connect(lambda: self.mute())
        self.volumeDown.clicked.connect(lambda: self.volume_down())
        self.volumeUp.clicked.connect(lambda: self.volume_up())
        self.channelDown.clicked.connect(lambda: self.channel_down())
        self.channelUp.clicked.connect(lambda: self.channel_up())
        self.__status: bool = False
        self.__mute: bool = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> bool:
        """
        This program checks the status of the TV and then changes it to the opposite status.
        :return: boolean
        """

        if not self.__status:
            self.__status = True
            self.muteLabel.setVisible(self.__mute)
            self.channelImage.setVisible(True)
            self.channelImage.setVisible(True)
            self.volumeBar.setVisible(True)
        else:
            self.__status = False
            self.muteLabel.setVisible(False)
            self.channelImage.setVisible(False)

        return self.__status

    def mute(self) -> bool:
        """
        This program checks the status of the TV, if on it will check if the TV is on mute or not, and change it to
        the opposite state.
        :return: boolean
        """

        if self.__status:
            if not self.__mute:
                self.__mute = True
                self.muteLabel.setVisible(True)
                self.volumeBar.setVisible(False)
            else:
                self.__mute = False
                self.muteLabel.setVisible(False)
                self.volumeBar.setVisible(True)

            return self.__mute

    def channel_up(self) -> None:
        """
        This program checks if the TV is on, if so it will increase the channel by one and display it. If at max it will go to first.
        :return: None
        """

        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
                if self.__channel == 3:
                    self.displayImage(self.channelImage, "MBC3.png")
                elif self.__channel == 1:
                    self.displayImage(self.channelImage, "BeinSports.png")
                elif self.__channel == 2:
                    self.displayImage(self.channelImage, "CNN.png")
            else:
                self.__channel = Television.MIN_CHANNEL
                self.displayImage(self.channelImage, "BBC.png")

    def channel_down(self) -> None:
        """
        This program checks if the TV is on, if so it will decrease the channel by one and display the channel. If at min it will go to highest.
        :return: None
        """

        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
                if self.__channel == 0:
                    self.displayImage(self.channelImage, "BBC.png")
                elif self.__channel == 1:
                    self.displayImage(self.channelImage, "BeinSports.png")
                elif self.__channel == 2:
                    self.displayImage(self.channelImage, "CNN.png")
            else:
                self.__channel = Television.MAX_CHANNEL
                self.displayImage(self.channelImage, "MBC3.png")

    def volume_up(self) -> None:
        """
        This program checks if the TV is on, if so it will increase the volume by one. If at max it will go to stay.
        :return: None
        """

        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__mute = False
                self.__volume += 1
                self.volumeBar.setValue(self.__volume)
            else:
                self.__mute = False
                self.__volume = Television.MAX_VOLUME
                self.volumeBar.setValue(self.__volume)
            self.muteLabel.setVisible(self.__mute)

    def volume_down(self) -> None:
        """
         This program checks if the TV is on, if so it will decrease the volume by one. If at min it will go to stay.
        :return: integer
        """

        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__mute = False
                self.__volume -= 1
                self.volumeBar.setValue(self.__volume)
            else:
                self.__mute = False
                self.__volume = Television.MIN_VOLUME
                self.volumeBar.setValue(self.__volume)
            self.muteLabel.setVisible(self.__mute)

    def __str__(self) -> str:
        """
         This program prints the current status of the TV, mute, and volume.
        :return: string of the status of all three parameters
        """

        if self.__mute:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
