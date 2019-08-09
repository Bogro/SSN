import os
import sys
import time
import logging


class Logger(object):

    def __init__(self):
        self.message = ""
        self.file = 0
        self.now = time.strftime('%Y-%m-%d')
        try:
            if os.access('var', os.F_OK):
                self.creat_log_folder()
            else:
                os.mkdir('var')
                self.creat_log_folder()
        except:
            print('Error execution')

    def log(self, message):
        """
        Default message logger
        :param message:
        """
        self.message = message
        
        file = f'var/logs/logger-{self.now}.log'
        self.__open_file__(file)
        self.__write_message__()

    def info(self, message):
        """
        Message logger info in folder info
        :param message:
        """
        self.message = message
        if self.creat_log_folder('info'):
            file = f'var/logs/info/{self.now}.log'
            self.__open_file__(file)
            self.__write_message__()
        else:
            print('ERROR')

    def success(self, message):
        """
        Message logger success in success folder
        :param message:
        """
        self.message = message
        if self.creat_log_folder('success'):
            file = f'var/logs/success/{self.now}.log'
            self.__open_file__(file)
            self.__write_message__()
        else:
            print('ERROR')

    def warning(self, message):
        """
        Message logger warning in warning folder
        :param message:
        """
        self.message = message
        if self.creat_log_folder('warning'):
            file = f'var/logs/warning/{self.now}.log'
            self.__open_file__(file)
            self.__write_message__()
        else:
            print('ERROR')

    def danger(self, message):
        """
        Message logger danger in danger folder
        :param message:
        """
        self.message = message

        if self.creat_log_folder('danger'):
            file = f'var/logs/danger/{self.now}.log'
            self.__open_file__(file)
            self.__write_message__()
        else:
            print('ERROR')

    def __open_file__(self, file):
        """
        Open file methode
        :param file:
        """
        try:
            self.file = open(file, "a")
        except FileNotFoundError:
            self.file = open(file, "a")

    def __write_message__(self):
        """
        Write message method
        """
        try:
            self.file.write(f"\n{self.message}")
        except:
            print('Error write log')
        finally:
            self.file.close()

    def creat_log_folder(self, type=''):
        """
        Treatment for the created folder of a logger
        :param type:
        :return:
        """
        try:
            if len(type) <= 0:
                os.makedirs('var/logs')
                return True
            else:
                try:
                    dir_list = os.listdir('var/logs')
                    length = len(dir_list)
                    if length == 0:
                        try:
                            os.makedirs(f'var/logs/{type}')
                            return True
                        except:
                            return False
                    else:
                        for i in range(length):
                            if dir_list[i] == type:
                                return True
                            else:
                                try:
                                    os.makedirs(f'var/logs/{type}')
                                    return True
                                except:
                                    return False
                except NotADirectoryError:
                    return False
        except FileExistsError:
            print('exist')

