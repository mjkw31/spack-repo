# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeVviniferaUrgiIggp8x(RPackage):
	"""Full reference nuclear genome sequences for Vitis vinifera subsp. vinifera PN40024 (IGGP version 8X)

	Full reference nuclear genome sequences for Vitis vinifera subsp. vinifera PN40024 (derived from Pinot Noir and close to homozygosity after 6-9 rounds of selfing) as assembled by the IGGP (version 8X) and available at the URGI (INRA). More details in Jaillon et al (Nature, 2007).
	"""
	
	bioc = "BSgenome.Vvinifera.URGI.IGGP8X" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Vvinifera.URGI.IGGP8X_0.1.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Vvinifera.URGI.IGGP8X/BSgenome.Vvinifera.URGI.IGGP8X_0.1.tar.gz"]

	version("0.1", md5="fccaf60e5c9352b9c454f7a8ecac2a20")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation