"""Modification of bdist_wininst to include numeric version in filename
"""
import sys, os, string, struct
from distutils.command.bdist_wininst import bdist_wininst

if hasattr( bdist_wininst, 'get_installer_filename' ):
	# Python 2.4a2 and beyond...
	BdistWinInstaller = bdist_wininst
else:
	class BdistWinInstaller(bdist_wininst):
		"""Version of bdist_wininst with customization point for filename

		This class should operate identically to the built-in
		class for Python 2.3 and below, it exists solely to
		provide the customization point which exists in
		Python 2.4a2 and beyond
		"""
		def get_installer_filename(self, fullname ):
			"""Calculate the final installer filename"""
			if self.target_version:
				return os.path.join(
					self.dist_dir,
					"%s.win32-py%s.exe" % (
						fullname,
						self.target_version
					)
				)
			else:
				return os.path.join(
					self.dist_dir,
					"%s.win32.exe" % fullname
				)
		def create_exe (self, arcname, fullname, bitmap=None):
			"""Do the actual creation of the executable file

			The base command, unfortunately, does not break down
			this command into sub-commands, so this method is
			almost entirely a duplication of the base-class method,
			with the only noticeable difference being the
			call to get_installer_filename(...) instead of
			calculating the filename inline.
			"""
			import struct

			self.mkpath(self.dist_dir)

			cfgdata = self.get_inidata()
			installer_name = self.get_installer_filename(
				fullname,
			)
			self.announce("creating %s" % installer_name)

			if bitmap:
				bitmapdata = open(bitmap, "rb").read()
				bitmaplen = len(bitmapdata)
			else:
				bitmaplen = 0

			file = open(installer_name, "wb")
			file.write(self.get_exe_bytes())
			if bitmap:
				file.write(bitmapdata)

			file.write(cfgdata)
			header = struct.pack("<iii",
								 0x1234567A,       # tag
								 len(cfgdata),     # length
								 bitmaplen,        # number of bytes in bitmap
								 )
			file.write(header)
			file.write(open(arcname, "rb").read())

class NumericWinInstaller(BdistWinInstaller):
	"""Version of BdistWininst which includes Numpy version in name"""
	def get_installer_filename(self, fullname ):
		"""Calculate the final installer filename"""
		try:
			import Numeric
			numeric_version = 'numpy%s'%( string.split(Numeric.__version__, '.')[0], )
		except ImportError:
			numeric_version = 'nonum'
		if self.target_version:
			return os.path.join(
				self.dist_dir,
				"%s.py%s-%s.exe" % (
					fullname,
					self.target_version,
					numeric_version,
				)
			)
		else:
			return os.path.join(
				self.dist_dir,
				"%s.%s.exe" %(
					fullname,
					numeric_version,
				)
			)

