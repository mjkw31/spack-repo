# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLittler(RPackage):
	"""R at the Command-Line via 'r'

	A scripting and command-line front-end
 is provided by 'r' (aka 'littler') as a lightweight binary wrapper around
 the GNU R language and environment for statistical computing and graphics.
 While R can be used in batch mode, the r binary adds full support for
 both 'shebang'-style scripting (i.e. using a  hash-mark-exclamation-path
 expression as the first line in scripts) as well as command-line use in
 standard Unix pipelines. In other words, r provides the R language without
 the environment.
	"""
	
	homepage = "https://github.com/eddelbuettel/littler"
	cran = "littler"

	version("0.3.19", md5="d0d7480bc3c1014069d00d1162b61cc0")



