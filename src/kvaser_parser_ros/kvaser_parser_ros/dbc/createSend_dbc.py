"""
# https://blog.csdn.net/ShakalakaPHD/article/details/115770026
# author:Hurricane
# date:  2021/4/16
# File : CAN_Create_Database.py 
# E-mail:hurri_cane@qq.com

"""

import argparse
from collections import namedtuple

from canlib import kvadblib

Message = namedtuple('Message', 'name id dlc signals')
Signal = namedtuple('Signal', 'name size scaling limits unit')
EnumSignal = namedtuple('EnumSignal', 'name size scaling limits unit enums')

_messages = [
		Message(
		name='Steering',
		id=100,
		dlc=8,
		signals=[
			Signal(
				name='Sttime',
				size=(0, 32),           # (startbit, length)
				scaling=(1, 0),
				limits=(0, 1e+30),
				unit="s",
			),
			Signal(
				name='StAngle',
				size=(32, 32),
				scaling=(1, 0),
				limits=(-1e+30, 1e+30),
				unit="deg",
			),
		]),
		Message(
		name='Speed',
		id=101,
		dlc=8,
		signals=[
			Signal(
				name='Sptime',
				size=(0, 32),
				scaling=(1, 0),
				limits=(0, 1e+30),
				unit="s",
			),
			Signal(
				name='VehicleVx',
				size=(32, 32),
				scaling=(1, 0),
				limits=(-1e+30, 1e+30),
				unit="km/h",
			),
		]),
]


def create_database(name, filename):
	db = kvadblib.Dbc(name=name)

	for _msg in _messages:
		message = db.new_message(
			name=_msg.name,
			id=_msg.id,
			dlc=_msg.dlc,
		)

		for _sig in _msg.signals:
			if isinstance(_sig, EnumSignal):
				_type = kvadblib.SignalType.ENUM_UNSIGNED
				_enums = _sig.enums
			else:
				# _type = kvadblib.SignalType.UNSIGNED  
				_type = kvadblib.SignalType.FLOAT 
				_enums = {}
			message.new_signal(
				name=_sig.name,
				type=_type,
				byte_order=kvadblib.SignalByteOrder.INTEL,
				# mode=kvadblib.SignalMultiplexMode.MUX_INDEPENDENT,
				mode=kvadblib.SignalMultiplexMode.SIGNAL,
				size=kvadblib.ValueSize(*_sig.size),
				scaling=kvadblib.ValueScaling(*_sig.scaling),
				limits=kvadblib.ValueLimits(*_sig.limits),
				unit=_sig.unit,
				enums=_enums,
			)

	db.write_file(filename)
	db.close()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description="Create a database from scratch.")
	parser.add_argument('--filename', default='./dbc/send_data.dbc', help=(
		"The filename to save the database to."))
	parser.add_argument('-n', '--name', default='send_data', help=(
		"The name of the database (not the filename, the internal name."))
	args = parser.parse_args()

	create_database(args.name, args.filename)