# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYe6100subdcdf(RPackage):
	"""ye6100subdcdf

	A package containing an environment representing the Ye6100subD.CDF file.
	"""
	
	bioc = "ye6100subdcdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ye6100subdcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ye6100subdcdf/ye6100subdcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="521b501ddbcdc680c3d27b5b201029b1")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation