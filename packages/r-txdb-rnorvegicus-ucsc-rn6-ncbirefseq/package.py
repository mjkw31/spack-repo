# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbRnorvegicusUcscRn6Ncbirefseq(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Rnorvegicus.UCSC.rn6.ncbiRefSeq" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Rnorvegicus.UCSC.rn6.ncbiRefSeq_3.12.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Rnorvegicus.UCSC.rn6.ncbiRefSeq/TxDb.Rnorvegicus.UCSC.rn6.ncbiRefSeq_3.12.0.tar.gz"]

	version("3.12.0", md5="6660ee000fbc956541728c6dadf1fca7")

	depends_on("r-genomicfeatures@1.41.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation