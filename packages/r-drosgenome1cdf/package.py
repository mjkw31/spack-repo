# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrosgenome1cdf(RPackage):
	"""drosgenome1cdf

	A package containing an environment representing the DrosGenome1.CDF file.
	"""
	
	bioc = "drosgenome1cdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/drosgenome1cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/drosgenome1cdf/drosgenome1cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="e12983f2148c10ef1faa50f810b6eee3")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation