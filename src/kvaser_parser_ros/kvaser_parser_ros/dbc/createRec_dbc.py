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
		name='VehicleXb',
		id=151,
		dlc=8,
		signals=[
			Signal(
				name='time',
				size=(0, 32),           # (startbit, length)
				scaling=(1, 0),
				limits=(0, 1e+30),
				unit="s",
			),
			Signal(
				name='Xb',
				size=(32, 32),
				scaling=(1, 0),
				limits=(-1e+30, 1e+30),
				unit="m",
			),
		]),
	Message(
		name='VehicleYb',
		id=152,
		dlc=8,
		signals=[
			Signal(
				name='time',
				size=(0, 32),
				scaling=(1, 0),
				limits=(0, 1e+30),
				unit="s",
			),
			Signal(
				name='Yb',
				size=(32, 32),
				scaling=(1, 0),
				limits=(-1e+30, 1e+30),
				unit="m",
			),
			# EnumSignal(
			# 	name='Gear',
			# 	size=(0, 3),
			# 	scaling=(1, 0),
			# 	limits=(0, 5),
			# 	unit="",
			# 	enums={
			# 		'Idle': 0,
			# 		'Gear_1': 1,
			# 		'Gear_2': 2,
			# 		'Gear_3': 3,
			# 		'Gear_4': 4,
			# 		'Gear_5': 5,
			# 	},
			# ),
		]),
		Message(
		name='VehicleYaw',
		id=153,
		dlc=8,
		signals=[
			Signal(
				name='time',
				size=(0, 32),           # (startbit, length)
				scaling=(1, 0),
				limits=(0, 1e+30),
				unit="s",
			),
			Signal(
				name='Yaw',
				size=(32, 32),
				scaling=(1, 0),
				limits=(-1e+30, 1e+30),
				unit="rad",
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
	parser.add_argument('--filename', default='./dbc/vehicle_example.dbc', help=(
		"The filename to save the database to."))
	parser.add_argument('-n', '--name', default='vehicle_example', help=(
		"The name of the database (not the filename, the internal name."))
	args = parser.parse_args()

	create_database(args.name, args.filename)


# 官网： https://www.kvaser.cn/developer-blog/python-can/
# from canlib import kvadblib

# # 生成一个数据库
# db = kvadblib .Dbc(name='VehicleState')

# # 加上报文
# message = db.new_message(name='VehicleXb',
# 			 id=151,
# 			 dlc=8)

# message.new_signal(
#        name='time' ,
#        size=kvadblib.ValueSize(startbit=0, length=32) ,
#        scaling=kvadblib . ValueScaling( factor=1, offset=0) ,
#        limits=kvadblib . ValueLimits(min=0, max=1e+30) ,
#        unit='s',
#        comment='time of the vehicle state Xb.' )

# message.new_signal(
#        name='Xb' ,
#        size=kvadblib.ValueSize(startbit=32, length=32) ,
#        scaling=kvadblib . ValueScaling( factor=1, offset=0) ,
#        limits=kvadblib . ValueLimits(min=-1e+30, max=1e+30) ,
#        unit='m',
#        comment='vehicle state Xb.' )

# db. write_file ('VehicleState.dbc')
# db. close()

# """
# 输出DBC文件，检测是否可读
# """
# import textwrap
# from canlib import kvadblib

# with kvadblib.Dbc(filename='vehicle_example.dbc') as db:
#     print(db)
#     for message in db:
#         print('\n{}'.format(message))
#         for signal in message:
#             print(textwrap.fill('{}'.format(signal), 80))
