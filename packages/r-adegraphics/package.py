# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdegraphics(RPackage):
	"""An S4 Lattice-Based Package for the Representation of Multivariate Data.

	Graphical functionalities for the representation of multivariate data.  It
	is a complete re-implementation of the functions available in the 'ade4'
	package."""

	cran = "adegraphics"

	version("1.0-21", md5="cf27cc7a367ff5bfe485dcedf21cf75e")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-ade4@1.7.13:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-sp@1.1.1:", type=("build", "run"))
