# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmmcopy(RPackage):
	"""Copy number prediction with correction for GC and mappability bias for HTS data

	Corrects GC and mappability biases for readcounts (i.e. coverage) in non-overlapping windows of fixed length for single whole genome samples, yielding a rough estimate of copy number for furthur analysis.  Designed for rapid correction of high coverage whole genome tumour and normal samples.
	"""
	
	bioc = "HMMcopy" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/HMMcopy_1.44.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/HMMcopy/HMMcopy_1.44.0.tar.gz"]

	version("1.44.0", md5="4785371e1642cd191330693396010a6e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
