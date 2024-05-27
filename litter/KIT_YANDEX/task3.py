import sys
from typing import List


class LogMobileDistinguisher:
    def __init__(self, desktop_file_name, mobile_file_name):
        self.desktop = self.read_file(desktop_file_name)
        self.mobile = self.read_file(mobile_file_name)
        self.process_log()

    @staticmethod
    def read_file(file_name: str) -> List[str]:
        with open(file_name, 'r') as fi:
            result = []
            for line in fi.readlines():
                result.append(line.strip())
            return result

    def get_line_client(self, line_ua: str) -> str:
        result = 'unknown'


        if line_ua in self.desktop:
            result = 'desktop'
            return result
        if line_ua in self.mobile:
            result = 'mobile'
            return result
        return result

    @staticmethod
    def get_line_fields(line: str):
        result = ' '.join(list(line.split())[8:])[1:-1]
        return result

    def process_log(self):
        for line in gets_arr:
            field = self.get_line_fields(line)
            client = self.get_line_client(field)
            print(client + ' ' + line.strip())


if __name__ == '__main__':
    with open("gets.txt", "r") as gets:
        gets_arr = gets.readlines()
    LogMobileDistinguisher('d.txt', 'm.txt')
