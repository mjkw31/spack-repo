# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBarley1cdf(RPackage):
	"""barley1cdf

	A package containing an environment representing the Barley1.CDF file.
	"""
	
	bioc = "barley1cdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/barley1cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/barley1cdf/barley1cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="16a2ca83f550518756d9fa3273672157")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation