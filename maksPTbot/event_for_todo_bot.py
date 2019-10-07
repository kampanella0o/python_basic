from datetime import datetime, date, time

class Event:


    def __init__(self, task_name, date, time, status=" - TO DO", date_time=None):
        self.__task_name = task_name
        self.__date = datetime.strptime(date, '%d.%m.%Y').date()
        self.__time = datetime.strptime(time,'%H.%M').time()
        self.__status = status
        self.__date_time = date_time

    @property
    def task_name(self):
        return self.__task_name

    @task_name.setter
    def task_name(self, task_name):
        self.__task_name = task_name

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = datetime.strptime(date, '%d.%m.%Y').date()

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time = datetime.strptime(time,'%H.%M').time()

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def date_time(self):
        self.__date_time = datetime.combine(self.__date, self.__time)
        return self.__date_time

    def __str__(self):
        # return self.__task_name + ', ' + \
        #        str(self.__date.strftime("%d.%m.%Y")) + \
        #        " at " + str(self.__time.strftime("%H.%M")) + self.__status
        return '%s, %s at %s%s' % (self.__task_name, str(self.__date.strftime("%d.%m.%Y")), \
                str(self.__time.strftime("%H.%M")), self.__status)
