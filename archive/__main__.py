from tap import tapify
import subprocess

def main(day: int):
	"""
	Archive that will run thorugh specified day
	"""
	output = subprocess.run(f"cd archive/day_{day}; python run.py", shell=True, capture_output=True)
	if output.returncode:
		print(output.stderr.decode())
	else:
		print(output.stdout.decode())
 
if __name__ == "__main__":
	tapify(main)