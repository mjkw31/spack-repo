# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLwgeom(RPackage):
	"""Bindings to Selected 'liblwgeom' Functions for Simple Features.

	Access to selected functions found in 'liblwgeom'
	<https://github.com/postgis/postgis/tree/master/liblwgeom>, the
	light-weight geometry library used by 'PostGIS' <https://postgis.net/>."""

	cran = "lwgeom"

	version("0.2-13", md5="9bf0d8b96f4e19f2a042d50cb66d7989")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-sf@0.6.0:", type=("build", "run"))
	depends_on("geos@3.5.0:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))
	depends_on("sqlite@3:", type=("build", "link", "run"))
