# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbCelegansUcscCe11Ensgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Celegans.UCSC.ce11.ensGene" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Celegans.UCSC.ce11.ensGene_3.15.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Celegans.UCSC.ce11.ensGene/TxDb.Celegans.UCSC.ce11.ensGene_3.15.0.tar.gz"]

	version("3.15.0", md5="1b4d61d06ac8acb27e57d1fafc5b79ce")

	depends_on("r-genomicfeatures@1.47.13:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation