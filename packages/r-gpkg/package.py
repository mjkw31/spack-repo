# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpkg(RPackage):
	"""Utilities for the Open Geospatial Consortium 'GeoPackage' Format

	Build Open Geospatial Consortium 'GeoPackage' files (<https://www.geopackage.org/>). 'GDAL' utilities for reading and writing spatial data are provided by the 'terra' package. Additional 'GeoPackage' and 'SQLite' features for attributes and tabular data are implemented with the 'RSQLite' package.
	"""
	
	homepage = "https://humus.rocks/gpkg/"
	cran = "gpkg" 

	version("0.0.7", md5="69117ee9ab2d38ea5e8ef53fc251f57d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
