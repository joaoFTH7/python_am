import subprocess
import socket
import cx_Freeze

executables = [cx_Freeze.Executable("client-win.py")]
cx_Freeze.setup(
	name = "Executavel",
	options = {"build_exe":{"packages":["subprocess","socket"]}},
	executables = executables
)