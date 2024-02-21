# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbCfamiliarisUcscCanfam4Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Cfamiliaris.UCSC.canFam4.refGene" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Cfamiliaris.UCSC.canFam4.refGene_3.14.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Cfamiliaris.UCSC.canFam4.refGene/TxDb.Cfamiliaris.UCSC.canFam4.refGene_3.14.0.tar.gz"]

	version("3.14.0", md5="0b47072fa79cf8e99f8563002a0998cb")

	depends_on("r-genomicfeatures@1.45.2:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation