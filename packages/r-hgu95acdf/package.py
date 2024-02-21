# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95acdf(RPackage):
	"""hgu95acdf

	A package containing an environment representing the HG_U95A.CDF file.
	"""
	
	bioc = "hgu95acdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hgu95acdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hgu95acdf/hgu95acdf_2.18.0.tar.gz"]

	version("2.18.0", md5="afc999d77b1532154d45911ad15a5897")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation