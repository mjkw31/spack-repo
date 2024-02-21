# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnix(RPackage):
	"""POSIX System Utilities

	Bindings to system utilities found in most Unix systems such as
	POSIX functions which are not part of the Standard C Library.
	"""
	
	homepage = "https://jeroen.r-universe.dev/unix"
	cran = "unix"

	version("1.5.6", md5="ea966ea9fb4f59ef99cb6cfa09432fa7")



