# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromdraw(RPackage):
	"""chromDraw is a R package for drawing the schemes of karyotypes in the linear and circular fashion.

	ChromDraw is a R package for drawing the schemes of karyotype(s) in the linear and circular fashion. It is possible to visualized cytogenetic marsk on the chromosomes. This tool has own input data format. Input data can be imported from the GenomicRanges data structure. This package can visualized the data in the BED file format. Here is requirement on to the first nine fields of the BED format. Output files format are *.eps and *.svg.
	"""
	
	homepage = "www.plantcytogenomics.org/chromDraw"
	bioc = "chromDraw"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/chromDraw_2.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/chromDraw/chromDraw_2.32.0.tar.gz"]

	version("2.32.0", md5="a2cb0f03cdde9853f68662b1783a2edb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-genomicranges@1.17.46:", type=("build", "run"))
