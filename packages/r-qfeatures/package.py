# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQfeatures(RPackage):
	"""Quantitative features for mass spectrometry data

	The QFeatures infrastructure enables the management and processing of quantitative features for high-throughput mass spectrometry assays. It provides a familiar Bioconductor user experience to manages quantitative data across different assay levels (such as peptide spectrum matches, peptides and proteins) in a coherent and tractable format.
	"""
	
	homepage = "https://github.com/RforMassSpectrometry/QFeatures"
	bioc = "QFeatures" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/QFeatures_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/QFeatures/QFeatures_1.12.0.tar.gz"]

	version("1.12.0", md5="6833061a024bb9783b7d9a85bc282a88")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-protgenerics@1.27.1:", type=("build", "run"))
	depends_on("r-annotationfilter", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mscoreutils@1.7.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
