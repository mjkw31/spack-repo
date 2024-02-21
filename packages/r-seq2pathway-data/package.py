# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeq2pathwayData(RPackage):
	"""data set for R package seq2pathway

	Supporting data for the seq2patheway package. Includes modified gene sets from MsigDB and org.Hs.eg.db; gene locus definitions from GENCODE project.
	"""
	
	bioc = "seq2pathway.data" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/seq2pathway.data_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/seq2pathway.data/seq2pathway.data_1.34.0.tar.gz"]

	version("1.34.0", md5="b0035ff986391159c1329eac9fb96661")

	depends_on("r@3.6.2:", type=("build", "run"))

	# experiment