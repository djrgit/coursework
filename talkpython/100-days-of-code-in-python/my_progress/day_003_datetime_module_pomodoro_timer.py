#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import datetime
from datetime import timedelta


def system_sound():
	print('\a')
	time.sleep(0.25)


class Timespan(object):

	def set_timespan(self, minutes):
		"""Set the amount of time to pass, in minutes."""
		self.timespan = minutes

	def get_timespan(self):
		"""View the current timespan setting."""
		return self.timespan

	def start_timer(self):
		"""Records the current time when called."""
		self.start = datetime.now()
		return self.start

	def determine_stop_time(self):
		"""Determines the stop time of the timespan."""
		#self.stop_time = self.start + timedelta(minutes=self.timespan)
		self.stop_time = self.start_timer() + timedelta(minutes=self.get_timespan())
		return self.stop_time

	def alert_start(self, num_alerts=1):
		self.num_alerts = num_alerts
		self.start_timer()
		self.determine_stop_time()
		for i in range(self.num_alerts):
			system_sound()


'''
class Task(object):

	def set_task(self, task):
		"""Set the task to make progress towards."""
		self.task = task

	def get_task(self):
		"""View the current task to be accomplished."""
		return self.task
'''


class Focus(Timespan):  # add Task parent class later?

	def __init__(self, num_alerts=3):
		self.focus_alerts = num_alerts
		print('Initializing a period of focus...')

	def focus_start(self):
		self.set_timespan(self.focus)
		print("ENTERING a {}-minute FOCUS period...".format(self.get_timespan()))
		self.alert_start(self.focus_alerts)

	def focus_stop(self):
		print("LEAVING a {}-minute FOCUS period...".format(self.get_timespan()))


class Break(Timespan):

	def __init__(self, num_alerts):
		self.break_alerts = num_alerts
		super().__init__()

	def break_start(self):
		self.set_timespan(self._break)
		print("ENTERING a {}-minute BREAK period...".format(self.get_timespan()))
		self.alert_start(self.break_alerts)

	def break_stop(self):
		print("LEAVING a {}-minute break period...".format(self.get_timespan()))


class ShortBreak(Break):

	def __init__(self, num_alerts=2):
		print('Initializing a short break window...')
		super().__init__(num_alerts)
	

class ExtendedBreak(Break):
	
	def __init__(self, num_alerts=4):
		print('Initializing an extended break...')
		super().__init__(num_alerts)


class Pomodoro(ShortBreak, Focus):

	def __init__(self, focus=25, _sbreak=5, count=1):
		self.focus = focus
		self._break = _sbreak
		self.cycles = count
		super().__init__()

	def pomodoro_start(self):
		while self.cycles > 0:
			self.focus_start()
			while datetime.now() < self.stop_time:
				pass
			self.focus_stop()
			self.break_start()
			while datetime.now() < self.stop_time:
				pass
			self.break_stop()
			self.cycles -= 1


class WorkdayPomodoros(Pomodoro, ExtendedBreak):

	def __init__(self, focus=25, _sbreak=5, _lbreak=30, count=16):
		super().__init__()
		self.focus = focus
		self._break = _sbreak
		self._sbreak = _sbreak
		self._lbreak = _lbreak
		self.cycles = count
		self.decrement = 4
		
	def workday_start(self):

		if self.cycles % self.decrement == 0:
			self.count = self.cycles
			self.cycles = self.decrement
		else:
			raise Exception

		while self.count > 0:
			self.pomodoro_start()
			self.count -= self.decrement

			self._break = self._lbreak
			self.break_start()
			while datetime.now() < self.stop_time:
				pass
			self.break_stop()
			
			self._break = self._sbreak
			self.cycles = self.decrement


if __name__ == "__main__":
	today = datetime.today()
	year = today.year
	month = today.month
	day = today.day
	hour = 7
	minute = 27
	start = datetime(year, month, day, hour, minute)
	while datetime.now() < start:
		pass
	work = WorkdayPomodoros()
	work.workday_start()