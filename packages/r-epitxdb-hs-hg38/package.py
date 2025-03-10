# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpitxdbHsHg38(RPackage):
	"""Annotation package for EpiTxDb objects

	Exposes an annotation databases generated from several sources by exposing these as EpiTxDb object. Generated for Homo sapiens/hg38.
	"""
	
	homepage = "https://github.com/FelixErnst/EpiTxDb.Hs.hg38"
	bioc = "EpiTxDb.Hs.hg38" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/EpiTxDb.Hs.hg38_0.99.7.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/EpiTxDb.Hs.hg38/EpiTxDb.Hs.hg38_0.99.7.tar.gz"]

	version("0.99.7", md5="e30af95f285788a9777a8207a8ef73a9", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/EpiTxDb.Hs.hg38_0.99.7.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-epitxdb", type=("build", "run"))

	# annotation