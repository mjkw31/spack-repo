# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomewidesnp6crlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for fast genotyping Affymetrix GenomeWideSnp_6 arrays using the 'crlmm' package.
	"""
	
	bioc = "genomewidesnp6Crlmm" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/genomewidesnp6Crlmm_1.0.7.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/genomewidesnp6Crlmm/genomewidesnp6Crlmm_1.0.7.tar.gz"]

	version("1.0.7", md5="13dd5aef3d814524896f2f3013beb78b")


	# annotation