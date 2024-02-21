# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnu34cdf(RPackage):
	"""rnu34cdf

	A package containing an environment representing the RN_U34.CDF file.
	"""
	
	bioc = "rnu34cdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/rnu34cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/rnu34cdf/rnu34cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="0f2564fc6ac89de4d779faf253f23ce3")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation