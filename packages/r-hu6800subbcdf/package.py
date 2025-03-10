# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu6800subbcdf(RPackage):
	"""hu6800subbcdf

	A package containing an environment representing the Hu6800subB.CDF file.
	"""
	
	bioc = "hu6800subbcdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hu6800subbcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hu6800subbcdf/hu6800subbcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="529aad5e4e73594c8cb66274d7e4adc5")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation