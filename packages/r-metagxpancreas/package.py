# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetagxpancreas(RPackage):
	"""Transcriptomic Pancreatic Cancer Datasets

	A collection of pancreatic Cancer transcriptomic datasets that are part of the MetaGxData package compendium. This package contains multiple pancreas cancer datasets that have been downloaded from various resources and turned into SummarizedExperiment objects. The details of how the authors normalized the data can be found in the experiment data section of the objects. Additionally, the location the data was obtained from can be found in the url variables of the experiment data portion of each SE.
	"""
	
	bioc = "MetaGxPancreas" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/MetaGxPancreas_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/MetaGxPancreas/MetaGxPancreas_1.22.0.tar.gz"]

	version("1.22.0", md5="0c1764dc18a9a180b2121649c98a26a1")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

	# experiment