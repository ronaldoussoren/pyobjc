import distutils.command.build

class build(distutils.command.build.build):

	def has_swig_interfaces(self):
		return 1

	def should_build_togl( self ):
		"""Determine whether to build togl shared library"""
		# XXX do something intelligent here!
		return 1

	sub_commands = [
		('build_w', has_swig_interfaces),
		('config', None),
	] + distutils.command.build.build.sub_commands + [
		('build_togl', should_build_togl),
	]

